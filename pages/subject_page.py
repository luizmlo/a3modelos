import streamlit as st
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page

# Database utilizada com a collection "subjects" para cadastro de matérias
client = MongoClient("mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["gestao_escola"]
collection = db["subjects"]

# Título da página
st.title("Cadastro de Matéria")
returnlobby = st.text("Deseja voltar ao lobby?")
if st.button("Voltar ao lobby"):
    switch_page("lobby page")

# Campos do formulário de cadastro de matéria
name = st.text_input("Nome da Matéria")

if st.button("Cadastrar"):
    # Realizar a operação de cadastro da matéria
    if name:
        subject = {
            "name": name
        }
        collection.insert_one(subject)
        st.success("Matéria cadastrada com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")
