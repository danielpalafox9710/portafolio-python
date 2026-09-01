import pandas as pd
import numpy as np
import holidays

#Definimos variable de vales basura
VALES_SUBCATEGORIAS_BASURA = {'Activar', 'Transferencia', 'Modificar', 'Extravio'}

#Variable devoluciones basura
DEVOLUCIONES_SUBCATEGORIAS_BASURA = {'Fuera de tiempo'}

#Variable para tickets basura de cambio de precio de menos de 15 mins
PRECIO_UMBRAL_BASURA_MINUTOS = 15

# Comentario de cierre basura
PATRON_CIERRE_VACIO = (
    r'^(listo|atendido|cerrado|resuelto|solucionado|ok|gracias|hecho|'
    r'finalizado|completado)[\s\.\!\,]*$'
)


# ----------------- Función para combinar fecha y hora -----------------
def combinar_fecha_hora(fecha_serie, hora_serie):

    fecha_norm = pd.to_datetime(fecha_serie).dt.normalize()

    if pd.api.types.is_timedelta64_dtype(hora_serie):
        hora_delta = hora_serie
    else:
        hora_str = hora_serie.astype(str).str.extract(r'(\d{1,2}:\d{2}:\d{2})')[0]
        hora_delta = pd.to_timedelta(hora_str, errors='coerce')

    return fecha_norm + hora_delta


# ---------- Función para calcular el SLA considerando días hábiles y feriados ----------
def calcular_sla(apertura, cierre, feriados):
    if pd.isnull(apertura) or pd.isnull(cierre) or apertura > cierre:
        return np.nan

    tiempo_total = pd.Timedelta(0)
    dia_actual = apertura.floor('D')
    dia_fin = cierre.floor('D')

    while dia_actual <= dia_fin:
        # excluimos días festivos
        if dia_actual.date() in feriados:
            dia_actual += pd.Timedelta(days=1)
            continue

        # Días y hrs de trabajo
        dia_semana = dia_actual.weekday()
        if dia_semana <= 5:  # Lunes a sabado
            inicio_operativo = dia_actual + pd.Timedelta(hours=8)
            fin_operativo = dia_actual + pd.Timedelta(hours=20)
        else:
            inicio_operativo = dia_actual + pd.Timedelta(hours=10)
            fin_operativo = dia_actual + pd.Timedelta(hours=17)

        inicio_calculo = max(apertura, inicio_operativo) if dia_actual == apertura.floor('D') else inicio_operativo
        fin_calculo = min(cierre, fin_operativo) if dia_actual == dia_fin else fin_operativo

        if inicio_calculo < fin_calculo:
            tiempo_total += (fin_calculo - inicio_calculo)

        dia_actual += pd.Timedelta(days=1)

    return tiempo_total.total_seconds() / 3600  # Convertir a horas

# ---------------------------------------------------------------------

# Procesamiento de limpieza de tickets basura y análisis de SLA ------------------

def procesar_tickets(archivo_excel):
    df = pd.read_excel(archivo_excel)

    # El export a veces trae una columna fantasma sin nombre (encabezado
    # vacío/espacio en blanco); la descartamos para no arrastrar ruido.
    columnas_validas = [c for c in df.columns if str(c).strip() != '']
    df = df[columnas_validas]

    df['Apertura_DT'] = combinar_fecha_hora(df['FechaCreacion'], df['HoraCreacion'])
    df['Cierre_DT'] = combinar_fecha_hora(df['FechaCierre'], df['HoraCierre'])

    # El SLA real se calcula primero porque la regla de "Precio básico"
    # depende de cuánto tardó el ticket en horario laboral.
    feriados = holidays.Mexico(years=range(2025, 2031))
    df['SLA_Horas'] = df.apply(
        lambda fila: calcular_sla(fila['Apertura_DT'], fila['Cierre_DT'], feriados), axis=1
    )

    # Limpieza de comentarios.
    df['Comentarios'] = df['Comentarios'].fillna('')
    df['Comentarios_Norm'] = df['Comentarios'].astype(str).str.lower().str.strip()
    df['Ultimo_Comentario'] = df['Comentarios_Norm'].str.split(';').str[-1].str.strip()
    df['Ultimo_Comentario_Texto'] = df['Ultimo_Comentario'].str.split(':', n=1).str[-1].str.strip()

    # --- Reglas de "ticket basura" (no cuentan para el rendimiento del gestor) ---
    es_no_cerrado = ~df['Estatus'].isin(['CERRADO'])
    es_cierre_vacio = df['Ultimo_Comentario_Texto'].str.match(PATRON_CIERRE_VACIO, na=False)
    es_vale_tramite = (df['Categoria'] == 'Vales') & df['SubCategoria'].isin(VALES_SUBCATEGORIAS_BASURA)
    es_llave_devolucion = (df['Categoria'] == 'Devoluciones') & df['SubCategoria'].isin(DEVOLUCIONES_SUBCATEGORIAS_BASURA)
    es_precio_basico = (df['Categoria'] == 'Precio') & (df['SLA_Horas'] < PRECIO_UMBRAL_BASURA_MINUTOS / 60)

    df['Es_Basura'] = es_no_cerrado | es_cierre_vacio | es_vale_tramite | es_llave_devolucion | es_precio_basico

    # Motivo de exclusión
    df['Motivo_Basura'] = np.select(
        [es_no_cerrado, es_vale_tramite, es_llave_devolucion, es_precio_basico, es_cierre_vacio],
        ['No cerrado', 'Trámite de vale', 'Llave de devolución', 'Cambio de precio básico', 'Cierre sin contenido'],
        default=''
    )

    df['Categoria_Real'] = df['Categoria']

    return df

# --------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) > 1:
        ruta_prueba = sys.argv[1]

        if os.path.exists(ruta_prueba):
            print(f"Iniciando procesamiento ETL de prueba para: {ruta_prueba}")
            try:
                df_resultado = procesar_tickets(ruta_prueba)
                print(f"\nTotal tickets: {len(df_resultado)}")
                print(f"Válidos: {(~df_resultado['Es_Basura']).sum()}  |  "
                      f"Basura: {df_resultado['Es_Basura'].sum()}")
                print("\n--- Motivo_Basura ---")
                print(df_resultado.loc[df_resultado['Es_Basura'], 'Motivo_Basura'].value_counts())
                columnas_validacion = ['TicketId', 'Categoria', 'SubCategoria', 'Es_Basura', 'Motivo_Basura', 'SLA_Horas']
                print("\n--- Resultados de SLA (Últimos 5 tickets) ---")
                print(df_resultado[columnas_validacion].tail(5))
            except Exception as e:
                print(f"Error crítico durante el procesamiento: {e}")
        else:
            print("Error: El archivo proporcionado no existe en la ruta.")
    else:
        print("Módulo ETL compilado correctamente.")
        print("Para probar localmente ejecuta: python etl_engine.py <ruta_del_archivo.xlsx>")