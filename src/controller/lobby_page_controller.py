from pymongo import MongoClient
import pandas as pd
import streamlit 
import streamlit as st
from .lobby_page_view import show_welcome_message, show_navbar, show_recent_contents

# Conexão com o MongoDB Atlas
client = MongoClient("mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["gestao_escola"]
collection = db["materials"]

def get_subjects():
    subjects = collection.distinct("subject")
    return subjects

def get_recent_contents(subject):
    pipeline = [
        {"$match": {"subject": subject}},
        {"$sort": {"date": -1}},
        {"$limit": 10},
    ]
    contents = list(collection.aggregate(pipeline))
    return contents

def show_recent_contents_table(contents):
    if contents:
        data = []
        subjects = []
        content_names = []
        descriptions = []
        for content in contents:
            data.append(content["date"])
            subjects.append(content["subject"])
            content_names.append(content["content_name"])
            descriptions.append(content["description"])
        dataframe = pd.DataFrame(
            {
                "Data": data,
                "Matéria": subjects,
                "Nome do Conteúdo": content_names,
                "Descrição": descriptions,
            }
        )
        streamlit.dataframe(dataframe)
    else:
        st.warning("Nenhum conteúdo encontrado para a matéria filtrada.")
