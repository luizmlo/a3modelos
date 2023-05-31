import streamlit as st
from pymongo import MongoClient
from datetime import datetime

# Conexão com o MongoDB Atlas
client = MongoClient(
    "mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["gestao_escola"]
attendance_collection = db["attendance"]
subject_collection = db["subjects"]

# Título da página
st.title("Cadastro de Falta por Aluno")

# Campos do formulário de cadastro de falta
name = st.text_input("Nome do Aluno")
registration = st.text_input("Matrícula do Aluno")

# Obter sugestões para o campo "Matéria"
subject_suggestions = subject_collection.distinct("name")
subject = st.selectbox("Matéria", subject_suggestions)

professor = st.text_input("Professor", value="")
date = st.date_input("Data da Falta")

if st.button("Cadastrar"):
    # Realizar a operação de cadastro da falta
    if name and registration and subject and professor and date:
        attendance = {
            "name": name,
            "registration": registration,
            "subject": subject,
            "professor": professor,
            # Converter para datetime
            "date": datetime.combine(date, datetime.min.time())
        }
        attendance_collection.insert_one(attendance)
        st.success("Falta cadastrada com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")
