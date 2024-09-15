import streamlit as st
from loader import reader
from shuntingYard import *
from Node import *
from AFN import *
from AFD import *

st.set_page_config(page_title="Proyecto 1", page_icon="🧠")
st.title('Proyecto 1 Analizador Lexico')

#expresiones precargadas
predefined_expressions = reader('/Laboratorios_Teoria_Computacion-/Proyecto1/file_read.txt')

if 'expression_input' not in st.session_state:
    st.session_state.expression_input = ''

if st.button('ε'):
    st.session_state.expression_input += 'ε'

col1, col2 = st.columns([2,2])
with col1:
    selected_expression = st.selectbox('Usar una expresión guardada', [''] + predefined_expressions)
with col2:
    expression_input = st.text_input('Ingresa la expresión manualmente', st.session_state.expression_input)


st.session_state.expression_input = expression_input


expression = expression_input if expression_input else selected_expression


if st.button('Evaluar'):
    if expression:
        regex = expression
        postfix, _ = infixToPostfix(regex)
        root = build_tree(postfix)
        afn = buildAFN(root)
        afn.graphicAFN()
        st.text('AFN de la expresion')
        st.image("\Laboratorios_Teoria_Computacion-\Proyecto1\AFN_automata.png", width=800)
        afd = subset_Algoritm(afn)
        afd.minimizumAFD()
        afd.graphicAFD()
        st.text('AFD minimizado de la expresion')
        st.image('\Laboratorios_Teoria_Computacion-\Proyecto1\AFD_automata.png')