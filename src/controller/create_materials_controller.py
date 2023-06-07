from pymongo import MongoClient
from datetime import datetime
from .create_materials_view import show_create_materials_page, show_success_message, show_warning_message

# Conexão com o MongoDB Atlas
client = MongoClient("mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
db = client["gestao_escola"]
collection_materials = db["materials"]
collection_subjects = db["subjects"]

def get_subject_names():
    subjects = collection_subjects.find({}, {"name": 1})
    subject_names = [subject["name"] for subject in subjects]
    return subject_names

def create_material(content_name, selected_subject, date, description):
    if content_name:
        content_data = {
            "content_name": content_name,
            "subject": selected_subject,
            "date": date.strftime("%d-%m-%Y"),
            "description": description,
        }
        collection_materials.insert_one(content_data)
        show_success_message()
    else:
        show_warning_message()
