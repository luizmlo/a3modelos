import streamlit as st
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page


# Database utilizada com a collection "students" para cadastro de alunos
client = MongoClient(
    "mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["gestao_escola"]
collection = db["students"]

# Título da página
st.title("Cadastro de Aluno")
returnlobby = st.text("Deseja voltar ao lobby?")
if st.button("Voltar ao lobby"):
    switch_page("lobby page")

# Campos do formulário de cadastro de aluno
name = st.text_input("Nome do Aluno")
registration = st.text_input("Matrícula do Aluno")

if st.button("Cadastrar"):
    # Realizar a operação de cadastro do aluno
    if name and registration:
        student = {
            "name": name,
            "registration": registration
        }
        collection.insert_one(student)
        st.success("Aluno cadastrado com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")
