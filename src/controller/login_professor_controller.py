from pymongo import MongoClient
from .login_professor_view import show_login_page, show_login_success_message, show_login_error_message

def login(username, password):
    client = MongoClient("mongodb+srv://eduardojaworiwski:EPNybNtTQ7kP5wqo@cluster0.jb76ewp.mongodb.net/")
    db = client["gestao_escola"]
    collection = db["users"]
    
    if username.isdigit():
        professor = collection.find_one({"username": int(username), "password": password})
        if professor:
            show_login_success_message()
            return True
    show_login_error_message()
    return False
