import streamlit as st
from pymongo import MongoClient
from streamlit_extras.switch_page_button import switch_page

# Conexão com o MongoDB Atlas
client = MongoClient(
    "mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/"
)
db = client["gestao_escola"]
collection_grades = db["grades"]

# Título da página
st.title("Listagem de Notas por Aluno")

# Botão para voltar ao lobby
returnlobby = st.text("Deseja voltar ao lobby?")
if st.button("Voltar ao lobby"):
    switch_page("lobby page")

# Obter a lista de alunos
students = collection_grades.distinct("aluno")
selected_student = st.selectbox("Selecione um aluno", students)

# Consultar as notas do aluno selecionado
grades = collection_grades.find({"aluno": selected_student})

if grades:
    st.write(f"Notas do aluno {selected_student}:")
    for grade in grades:
        st.write(f"- Matéria: {grade['materia']}, Nota: {grade['nota']}")
else:
    st.write("Nenhuma nota encontrada para este aluno.")
