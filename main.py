import streamlit as st
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page
import yaml


# Lendo as credenciais do arquivo credentials.txt
with open('credentials.txt') as file:
    lines = file.readlines()
    username = lines[1].strip()
    password = lines[2].strip()
    databaseM = lines [3].strip()
    database_url = lines[4].strip()
    

# Conexão com o MongoDB
client = MongoClient(f"mongodb+srv://{username}:{password}@{database_url}")
db = client[databaseM]
collection = db["users"]
# Título da página
st.title("Bem vindo ao sistema de gestão escolar!")
st.text("Faça login ou crie uma conta para continuar.")

# Escolha entre login e criar conta
login_or_create = st.selectbox("Escolha uma opção:", ("Login", "Criar Conta"))

# Entrada do usuário e senha
input_username = st.text_input("Usuário")
input_password = st.text_input("Senha", type="password")

# Botão de login ou criar conta
if login_or_create == "Login":
    if st.button("Login"):
        # Verifica se o usuário e senha estão corretos
        user_data = collection.find_one({"username": input_username, "password": input_password})
        if user_data:
            st.success("Login realizado com sucesso!")
            switch_page("lobby page")
        else:
            st.error("Usuário ou senha inválidos.")
else:
    if st.button("Criar Conta"):
        # Verifica se o usuário já existe
        existing_user = collection.count_documents({"username": input_username})
        if existing_user > 0:
            st.error("Usuário já existe. Por favor, escolha outro nome de usuário.")
        else:
            # Insere novo usuário no banco de dados
            new_user = {"username": input_username, "password": input_password}
            collection.insert_one(new_user)
            st.success("Conta criada com sucesso!")
