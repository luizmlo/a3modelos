import streamlit as st
from pages.login_professor import login_professor_view, login_professor_controller
from user_controller import handle_user_selection

# Colapsa a barra lateral
st.set_page_config(initial_sidebar_state="collapsed")

def main():
    handle_user_selection()
    # Other controllers and view functions can be added here

if __name__ == "__main__":
    main()
