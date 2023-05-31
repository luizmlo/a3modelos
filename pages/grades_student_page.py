from datetime import datetime
import streamlit as st
from pymongo import MongoClient
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
st.title("Cadastro de Notas por Aluno")
returnlobby = st.text("Deseja voltar ao lobby?")
if st.button("Voltar ao lobby"):
    switch_page("lobby page")


# Campos do formulário de cadastro de nota
name = st.text_input("Nome do Aluno")
registration = st.text_input("Matrícula do Aluno")

# Obter sugestões para o campo "Matéria"
subject_suggestions = subject_collection.distinct("name")
subject = st.selectbox("Matéria", subject_suggestions)

# Entrada da nota da prova
nota = st.number_input("Nota da Prova", step=0.1)

if st.button("Cadastrar"):
    # Realizar a operação de cadastro da nota
    if name and registration and subject and nota:
        nota_aluno = {
            "name": name,
            "registration": registration,
            "subject": subject,
            "nota": nota,
            "date": datetime.now(),
        }
        attendance_collection.insert_one(nota_aluno)
        st.success("Nota cadastrada com sucesso!")
    else:
        st.error("Por favor, preencha todos os campos.")
