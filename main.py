import streamlit as st
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page

# Conexão com o MongoDB Atlas
client = MongoClient("mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["a3modelos"]
collection = db["escola"]

# Título da página
st.title("Sistema de Gestão Escolar - Login de Professores")

# Entrada do usuário e senha
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

# Botão de login
if st.button("Login"):
    # Verifica as credenciais do professor no banco de dados
    users_data = collection.find_one({"username": username, "password": password})
    if users_data:
        st.success("Login realizado com sucesso!")
        switch_page("lobby_page")
    else:
        st.error("Usuário ou senha incorretos!")
