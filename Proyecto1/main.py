import streamlit as st
from loader import reader
from shuntingYard import *
from Node import *
from AFN import *
from AFD import *

st.set_page_config(page_title="Proyecto 1", page_icon="🧠")
st.title('Proyecto 1 Analizador Lexico')

# Expresiones precargadas
predefined_expressions = reader('/Laboratorios_Teoria_Computacion-/Proyecto1/file_read.txt')

if 'expression_input' not in st.session_state:
    st.session_state.expression_input = ''

if st.button('ε'):
    st.session_state.expression_input += 'ε'

col1, col2 = st.columns([2, 2])
with col1:
    selected_expression = st.selectbox('Usar una expresión guardada', [''] + predefined_expressions)
with col2:
    expression_input = st.text_input('Ingresa la expresión manualmente', st.session_state.expression_input)

# Guardar la expresión ingresada en el estado de sesión
st.session_state.expression_input = expression_input

expression = expression_input if expression_input else selected_expression

# Cadena para evaluar
if 'chain_w' not in st.session_state:
    st.session_state.chain_w = ''

st.session_state.chain_w = st.text_input('Ingresa la cadena w para evaluar', st.session_state.chain_w)



# Evaluar cadena
if st.button('Evaluar cadena en AFD Y AFN'):
    expression = expression or ''
    regex = expression
    postfix, _ = infixToPostfix(regex)
    root = build_tree(postfix)
    afn = buildAFN(root)
    afd = subset_Algoritm(afn)
    afd.minimizumAFD()
    AFN_value = afn.acept_Chain(st.session_state.chain_w)
    AFD_value = afd.acept_Chain(st.session_state.chain_w)

    if AFN_value:
        st.success("La cadena w es aceptada por el autómata AFN")
    else:
        st.error("La cadena w no es aceptada por el autómata AFN")

    if AFD_value:
        st.success("La cadena w es aceptada por el autómata AFD")
    else:
        st.error("La cadena w no es aceptada por el autómata AFD")

# Generar AFD, AFN
if st.button('Generar AFD, AFN'):
    expression = expression or ''
    try:
        regex = expression
        postfix, _ = infixToPostfix(regex)
        root = build_tree(postfix)
        draw_tree_graphviz(root)
        st.text('Arbol sintactico generado')
        st.image("\Laboratorios_Teoria_Computacion-\Proyecto1\\binary_tree_image.png", width=300)
        afn = buildAFN(root)
        afn.graphicAFN()
        st.text('AFN de la expresión')
        st.image("\Laboratorios_Teoria_Computacion-\Proyecto1\AFN_automata.png", width=800)
        
        afd = subset_Algoritm(afn)
        afd.graphicAFD()
        afd.minimizumAFD()
        afd.graphicminimizumAFD()
        
        st.text('AFD de la expresión')
        st.image('\Laboratorios_Teoria_Computacion-\Proyecto1\AFD_automata.png')
        st.text('AFD minimizado de la expresión')
        st.image('\Laboratorios_Teoria_Computacion-\Proyecto1\AFD_automata_minimizum.png')
    except:
        st.error("No se pudo generar los automatas , verifique que su expresion sea correcta")