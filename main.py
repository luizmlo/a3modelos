import streamlit as st
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page


# Conexão com o MongoDB Atlas
client = MongoClient(
    "mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["gestao_escola"]
collection = db["users"]

# Título da página
st.title("Bem vindo ao sistema de gestão escolar!")
st.text("Faça login ou crie uma conta para continuar.")

# Escolha entre login e criar conta
login_or_create = st.selectbox(
    "Escolha uma opção:", ("Login", "Criar Conta"))

# Entrada do usuário e senha
username = st.text_input("Usuário")
password = st.text_input("Senha", type="password")

# Botão de login ou criar conta
if login_or_create == "Login":
    if st.button("Login"):
        # Verifica se o usuário e senha estão corretos
        user_data = collection.find_one(
            {"username": username, "password": password})
        if user_data:
            st.success("Login realizado com sucesso!")
            switch_page("lobby page")

        else:
            st.error("Usuário ou senha inválidos.")
else:
    if st.button("Criar Conta"):
        # Verifica se o usuário já existe
        user_data = collection.find_one({"username": username})
        if user_data:
            st.error(
                "Usuário já existe. Por favor, escolha outro nome de usuário.")
        else:
            # Insere novo usuário no banco de dados
            new_user = {"username": username, "password": password}
            collection.insert_one(new_user)
            st.success("Conta criada com sucesso!")
            # Função para obter a hora atual


def get_current_hour():
    # Lógica para obter o horário atual
    # ...
    return 12  # Simulando a hora atual

# Função para determinar a saudação com base na hora


def get_greeting(hour):
    if 6 <= hour < 12:
        return "Bom dia"
    elif 12 <= hour < 18:
        return "Boa tarde"
    else:
        return "Boa noite"
