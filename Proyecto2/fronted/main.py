import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.Regex import Regex
from backend.CFG import CFG
from backend.Reader import *

st.set_page_config(page_title="Proyecto 2", page_icon="🧠")
st.title('Algoritmo CYK')

try:
    st.subheader('Instrucciones')
    st.write("<p style='font-size:17px;'>Modifique el archivo Files/files.txt y agregue su gramatica a evaluar recuerde agregar espacios entre tokens</span>", unsafe_allow_html=True)

except ValueError as e:
    st.error(f"Se produjo un error :  {e}")

if 'expression_input' not in st.session_state:
    st.session_state.expression_input = ''

expression_input = st.text_input('Ingresa una cadena w para validar', st.session_state.expression_input)


if st.button('Normalizar CFG y evaluar w'):
    try:
      rgt = Regex()
      rgt.load_filename('..\\Files\\file.txt')
      rgt.validateChains()
      cfg_ = CFG(rgt)
      red = Reader(cfg=cfg_)
      red.show_CFG_productions()      
      original = red.string_P.replace("\n", "<br>")
      cfg_.convert_to_Chumsky()
      red2 = Reader(cfg=cfg_)
      red2.show_CFG_productions()
      normalized = red2.string_P.replace("\n", "<br>")
      st.subheader('Gramatica Original')
      st.write(f"<span style='font-size:20px; font-style:italic;'>{original}</span>", unsafe_allow_html=True)
      st.subheader('Gramatica Normalizada')
      st.write(f"<span style='font-size:20px; font-style:italic;'>{normalized}</span>", unsafe_allow_html=True)
      st.subheader('Parse Tree')
      st.subheader('Pertenece o no ?')
    except ValueError as e:
        st.error(f"Se produjo un error :  {e}")


