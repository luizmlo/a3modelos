import streamlit as st
from pymongo import MongoClient
from datetime import datetime
from streamlit_extras.switch_page_button import switch_page


# Conexão com o MongoDB Atlas
client = MongoClient(
    "mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/"
)
db = client["gestao_escola"]
attendance_collection = db["attendance"]
subject_collection = db["subjects"]
professor_collection = db["professors"]

# Título da página
st.title("Cadastro de Falta por Aluno")
returnlobby = st.text("Deseja voltar ao lobby?")
if st.button("Voltar ao lobby"):
    switch_page("lobby page")


# Campos do formulário de cadastro de falta
name = st.text_input("Nome do Aluno")
registration = st.text_input("Matrícula do Aluno")

# Obter sugestões para o campo "Matéria"
subject_suggestions = subject_collection.distinct("name")
subject = st.selectbox("Matéria", subject_suggestions)

# Obter sugestões para o campo "Professor"
professor_suggestions = professor_collection.distinct("name")
professor = st.selectbox("Professor", professor_suggestions)

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
            "date": datetime.combine(date, datetime.min.time()),
        }
        attendance_collection.insert_one(attendance)
        st.success("Falta cadastrada com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")
