import streamlit as st
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page

# Conexão com o MongoDB Atlas
client = MongoClient(
    "mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/"
)
db = client["gestao_escola"]
collection = db["attendance"]

# Título da página
st.title("Listagem de Faltas por Aluno")
returnlobby = st.text("Deseja voltar ao lobby?")
if st.button("Voltar ao lobby"):
    switch_page("lobby page")

# Obter a lista de alunos
students = collection.distinct("name")
selected_student = st.selectbox("Selecione um aluno", students)

# Consultar as faltas do aluno selecionado
attendances = collection.find({"name": selected_student})

if attendances:
    st.write(f"Faltas do aluno {selected_student}:")
    for attendance in attendances:
        st.write(
            f"- Matéria: {attendance['subject']}, Professor: {attendance['professor']}, Data: {attendance['date']}"
        )
else:
    st.write("Nenhuma falta encontrada para este aluno.")
