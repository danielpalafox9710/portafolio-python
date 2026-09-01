import streamlit as st
import pandas as pd
import plotly.express as px
from etl_engine import procesar_tickets
from pathlib import Path
directorio_base=Path(__file__).parent

logocklass=directorio_base / "assets" / "LogoCklass.png"

st.set_page_config(
    page_title="Dashboard SLA | Mesa de Ayuda",
    page_icon=str(logocklass),
    layout="wide"
)

def cargar_y_procesar_dtos(archivo_subido):
    return procesar_tickets(archivo_subido)
#Color del fondo
fondo_color = """
<style>
.stApp {
    background-color: #2D3139;
}
</style>
"""
st.markdown(fondo_color, unsafe_allow_html=True)
##################################################
portada =directorio_base / "assets" / "cklass_portada.jpg"
st.image(str(portada), width=400)
st.title("Análisis de SLA - Mesa de Ayuda")
st.markdown("Sube el reporte en formato Excel (.xlsx)")
archivo = st.file_uploader("Selecciona el reporte de tickets", type=["xlsx"])
#Quitar la sangría del paddy
ajuste_espaciado = """
<style>
    /* Acerca el bloque de contenido a la barra superior */
    .block-container {
        padding-top: 4rem !important; 
    }
    
    /* Reduce el espacio específico entre la imagen y el título st.title */
    h1 {
        padding-top: 0rem !important;
        margin-top: 0rem !important;
    }
</style>
"""
st.markdown(ajuste_espaciado, unsafe_allow_html=True)

if archivo is not None:
    df_completo = cargar_y_procesar_dtos(archivo)
    st.success("¡Datos procesados con éxito!")
    
    #--------------------------------------------------------- Filtro para separar tickets basura con tickets reales"
    df_valido = df_completo[df_completo['Es_Basura'] == False].copy()
    df_basura = df_completo[df_completo['Es_Basura'] == True].copy()
    
#--------------------------------------------------------- Creamos pestañas para separar la interfaz
    tab_dashboard, tab_auditoria = st.tabs(["📊 Dashboard Principal", "🗑️ Auditoría de Basura"])
    
    # Dashboard general
    with tab_dashboard:
        st.markdown("### Resumen Operativo Global")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Tickets Recibidos", len(df_completo))
        col2.metric("Tickets Válidos", len(df_valido))
        col3.metric("Basura Operativa Filtrada", len(df_basura))
        col4.metric("SLA Global Promedio (Hrs)", round(df_valido['SLA_Horas'].mean(), 2))

        st.divider()

        # Gráfico 1: Tickets por Gestor
        st.markdown("#### 1. Tickets Válidos por Gestor")
        df_gestores = df_valido['Gestor'].value_counts().reset_index()
        df_gestores.columns = ['Gestor', 'Cantidad']
        fig_gestores = px.bar(df_gestores, x='Gestor', y='Cantidad', text='Cantidad', color='Cantidad', color_continuous_scale='Blues')
        st.plotly_chart(fig_gestores, use_container_width=True)


        #Grafico SLA por categoría
        st.markdown("2. SLA Promedio por Categoría")

        df_sla_cat = df_valido.groupby('Categoria_Real')['SLA_Horas'].mean().reset_index()

        fig_sla = px.bar(
             df_sla_cat, 
            x='Categoria_Real', 
             y='SLA_Horas', 
             title="SLA Real Promedio (Hrs)"
        )
        st.plotly_chart(fig_sla, use_container_width=True)
        #Grafico Volumen por categoría
        st.markdown("3. Volumen por Categoría")
        df_categorias = df_valido['Categoria_Real'].value_counts().reset_index()
        df_categorias.columns = ['Categoria_Real', 'Cantidad']

        fig_dona = px.pie(
            df_categorias, 
            values='Cantidad', 
            names='Categoria_Real', 
            hole=0.4, 
            title="Distribución de Incidentes"
        )
        st.plotly_chart(fig_dona, use_container_width=True)

        # Gráfico 2 y 3:

        st.divider()

        #SLA por gestor
        st.markdown("#### Desglose de SLA por Gestor y Categoría")
        
        df_sla_gestor_cat = df_valido.groupby(['Gestor', 'Categoria_Real'])['SLA_Horas'].mean().reset_index()
        
       #Lista de gestores
        lista_gestores = df_sla_gestor_cat['Gestor'].unique()
        
        if len(lista_gestores) > 0:
            # Crea una pestaña por cada gestor
            tabs_gestores = st.tabs(lista_gestores.tolist())
            
            for i, tab_g in enumerate(tabs_gestores):
                gestor_actual = lista_gestores[i]
                with tab_g:
                    # Filtramos solo los datos del gestor actual
                    df_g = df_sla_gestor_cat[df_sla_gestor_cat['Gestor'] == gestor_actual].copy()
                    df_g['SLA_Horas'] = df_g['SLA_Horas'].round(2)
                    
                    # Renombramos para presentación y mostramos la tabla
                    df_g = df_g.rename(columns={'Categoria_Real': 'Categoría', 'SLA_Horas': 'SLA Promedio (Hrs)'})
                    
                    st.dataframe(df_g[['Categoría', 'SLA Promedio (Hrs)']], use_container_width=True, hide_index=True)

        st.divider()
        #TICKETS POR SUCURSAL Y CATEGORÍA
        st.markdown("#### Desglose de Tickets por Sucursal")
        
        #Contamos cantidad
        df_sucursal_cat = df_valido.groupby(['Sucursal', 'Categoria_Real']).size().reset_index(name='Total Tickets')
        
        lista_sucursales = df_sucursal_cat['Sucursal'].sort_values().unique()
        
        if len(lista_sucursales) > 0:
            #Uso de Selectbox para evitar el colapso visual de las pestañas
            sucursal_seleccionada = st.selectbox(
                "Selecciona una Sucursal para auditar su carga:", 
                lista_sucursales
            )
            
            
            df_s = df_sucursal_cat[df_sucursal_cat['Sucursal'] == sucursal_seleccionada].copy()
            
            #Ordenamos los tickets
            df_s = df_s.sort_values(by='Total Tickets', ascending=False)
            df_s = df_s.rename(columns={'Categoria_Real': 'Categoría'})
            
            st.dataframe(df_s[['Categoría', 'Total Tickets']], use_container_width=True, hide_index=True)

    #---------------------------Top sucursales por ticket
    st.divider()

       
    st.markdown("Top 3 Sucursales Críticas por Categoría")
        
        # Contar tickets cruzando Categoría y Sucursal
    df_cat_suc = df_valido.groupby(['Categoria_Real', 'Sucursal']).size().reset_index(name='Total Tickets')
        
        # 2. Ordenamiento
    df_cat_suc = df_cat_suc.sort_values(by=['Categoria_Real', 'Total Tickets'], ascending=[True, False])
        
    df_top3_cat = df_cat_suc.groupby('Categoria_Real').head(5)
        
    lista_categorias = df_top3_cat['Categoria_Real'].unique()
        
    if len(lista_categorias) > 0:
        categoria_seleccionada = st.selectbox(
                "Selecciona una Categoría para auditar sus 5 sucursales con mayor volumen:", 
                lista_categorias
         )
            
        df_vista_top3 = df_top3_cat[df_top3_cat['Categoria_Real'] == categoria_seleccionada].copy()
            
        df_vista_top3 = df_vista_top3[['Sucursal', 'Total Tickets']]
            
        st.dataframe(df_vista_top3, use_container_width=True, hide_index=True)



    #Tickets basura
    with tab_auditoria:
        st.markdown("### Tickets Descartados del Análisis de Rendimiento")
        st.info("Estos tickets fueron marcados como 'Basura' por el motor ETL según las reglas de negocio (ej. trámites de vales, cierres vacíos, etc.).")
        
        if not df_basura.empty:
            # Extraemos estrictamente las columnas correspondientes
            columnas_basura = ['TicketId', 'Titulo', 'Categoria', 'SubCategoria', 'Gestor', 'Motivo_Basura']
            df_basura_vista = df_basura[columnas_basura].copy()
            
            # Renombrar para interfaz
            df_basura_vista = df_basura_vista.rename(columns={
                'TicketId': 'Número de Ticket',
                'Titulo': 'Título',
                'Categoria': 'Categoría',
                'Motivo_Basura': 'Regla de Exclusión'
            })
            
            st.dataframe(df_basura_vista, use_container_width=True, hide_index=True)
            
            # Boton para descargar la basura
            csv_basura = df_basura_vista.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Descargar Reporte de Basura (CSV)",
                data=csv_basura,
                file_name="tickets_basura_audit.csv",
                mime="text/csv",
            )
        else:
            st.success("No se encontraron tickets basura en este archivo.")