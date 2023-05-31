import streamlit as st
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page


# Database utilizada com a collection "professors" para cadastro de professores
client = MongoClient(
    "mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["gestao_escola"]
collection = db["professors"]

# Título da página
st.title("Cadastro de Professor")
returnlobby = st.text("Deseja voltar ao lobby?")
if st.button("Voltar ao lobby"):
    switch_page("lobby page")


# Campos do formulário de cadastro de professor
name = st.text_input("Nome do Professor")
department = st.text_input("Departamento do Professor")

if st.button("Cadastrar"):
    # Realizar a operação de cadastro do professor
    if name and department:
        professor = {
            "name": name,
            "department": department
        }
        collection.insert_one(professor)
        st.success("Professor cadastrado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")
