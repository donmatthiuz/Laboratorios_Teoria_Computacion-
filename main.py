import streamlit as st
import yaml
from reader import Reader
from TM import TuringMachine
st.set_page_config(page_title="Simulador Maquina de Turing", page_icon="🧠")
st.title('Simulador de Maquina de Turing')
st.subheader('Instrucciones')
st.write("<p style='font-size:17px;'>Agregue el archivo de configuracion .yaml para evaluar la maquina de turing</span>", unsafe_allow_html=True)


with st.container():
    uploaded_file = st.file_uploader("Subir archivo de configuración", type=["yaml"])
    tipo_maquina = st.radio(
                "Seleccionar el tipo de Máquina de Turing",
                ("Reconocedora", "Alteradora")
            )
    if uploaded_file is not None:
        st.write("Archivo cargado exitosamente:")
        try:
            
            content = yaml.safe_load(uploaded_file)
            lector = Reader(content=content)
            maquina = TuringMachine(lector=lector)
            st.subheader('Digrama de la Maquina de Turing')
            maquina.generar_grafico()
            st.image('./graficas/maquina_turing.png')
            for c in lector.cadenas:
                result, historial, cinta = maquina.procesar(c)
                if tipo_maquina == "Reconocedora":
                    re= f"De la cadena \"{c}\" se llego al estado de: \"{result}\""
                    st.subheader('Resultado cadena')
                    if result == "rechazada":
                        st.error(re)
                    elif result == "aceptada":
                        st.success(re)
                elif tipo_maquina == "Alteradora":
                    re= f"De la cadena \"{c}\" se altero para: \"{cinta}\""
                    st.subheader('Resultado cadena')
                    if result == "aceptada":
                        st.success(re)
                pasos = ''
                pasos_show = ''
                for p in historial:
                    pasos += f'{p}<br>'
                    pasos_show += f'{p}\n'
                txt_content = f"CONFIGURACIONES MAQUINA DE TURING\nCadena: {c}\n\nEstado: {result}\nCinta: {cinta}\nConfiguraciones:\n" + pasos_show
                st.download_button(
                    label="Descargar archivo de configuraciones para esta cadena",
                    data=txt_content,
                    file_name=f"configuraciones_TM cadena:{c} .txt",  # Nombre del archivo .txt
                    mime="text/plain"  # MIME para archivos de texto
                )
                st.subheader('Configuraciones de la cinta')
                st.write(f"<span style='font-size:11px; font-style:italic;'>{pasos}</span>", unsafe_allow_html=True)
        
        except yaml.YAMLError as e:
            st.error(f"Error al leer el archivo YAML: {e}")
