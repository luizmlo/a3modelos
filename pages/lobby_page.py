import datetime
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pymongo import MongoClient

# import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Título da página
st.title("Lobby")

# Mensagem de boas-vindas
st.write("Bem-vindo ao lobby!")

st.write("O que você deseja fazer hoje?")
lobby_option = st.selectbox(
    "Escolha uma opção:",
    (
        "Selecione uma opção",
        "Cadastrar Aluno",
        "Cadastrar Matéria",
        "Cadastrar Professor",
        "Cadastrar Falta por Aluno",
        "Listar Faltas por Aluno",
        "Cadastrar Notas",
        "Listar notas por Aluno",
    ),
)

if lobby_option == "Cadastrar Aluno":
    switch_page("student page")

elif lobby_option == "Cadastrar Matéria":
    switch_page("subject page")

elif lobby_option == "Cadastrar Professor":
    switch_page("professor page")

elif lobby_option == "Cadastrar Falta por Aluno":
    switch_page("attendance page")

elif lobby_option == "Listar Faltas por Aluno":
    switch_page("list attendance student")

elif lobby_option == "Cadastrar Notas":
    switch_page("grades student page")
    
elif lobby_option == "Listar notas por Aluno":
    switch_page("list grades student")
