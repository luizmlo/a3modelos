import streamlit as st
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page

# Conexão com o MongoDB Atlas
client = MongoClient(
    "mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["gestao_escola"]
collection = db["users"]

# Título da página
st.title("Login de Professores")
st.header("Bem vindo ao sistema da SchoolTech!")
st.subheader("Por favor, faça login para continuar.")

# Entrada do nome de usuário e senha
username = st.text_input("Nome de Usuário")
password = st.text_input("Senha", type="password")

# Botão de login
if st.button("Login"):
    # Verifica se o professor existe no banco de dados
    professor = collection.find_one({"username": username, "password": password})
    if professor:
        st.success("Login realizado com sucesso!")
        switch_page("lobby page")
    else:
        st.error("Usuário ou senha incorretos!")
