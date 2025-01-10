import streamlit as st
import re

# Fonction pour vérifier si l'email est valide
def is_valid_email(email):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(regex, email) is not None

# Fonction pour masquer les éléments par défaut de Streamlit
def hide_streamlit_style():
    hide_style = """
    <style>
    /* Cacher le menu hamburger en haut à droite */
    #MainMenu {visibility: hidden;}
    /* Cacher le footer "Made with Streamlit" */
    footer {visibility: hidden;}
    /* Cacher le bandeau de paramètres */
    header {visibility: hidden;}
    /* Centrer le conteneur verticalement */
    .stApp {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    /* Styles pour les boutons ronds */
    .circle-button {
        display: inline-block;
        width: 150px;
        height: 150px;
        line-height: 150px;
        border-radius: 50%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        font-size: 16px;
        text-decoration: none;
        margin: 10px;
        cursor: pointer;
    }
    .circle-button:hover {
        background-color: #45a049;
    }
    </style>
    """
    st.markdown(hide_style, unsafe_allow_html=True)

# Fonction pour la page de connexion
def login_page():
    st.title("Bienvenue")
    st.subheader("Veuillez entrer votre adresse email pour vous connecter")

    email = st.text_input("Adresse Email")

    if st.button("Se Connecter"):
        if email and is_valid_email(email):
            st.session_state['authenticated'] = True
            st.session_state['user_email'] = email
            st.success(f"Connexion réussie avec l'adresse {email}!")
        else:
            st.error("Veuillez entrer une adresse email valide.")

# Fonction pour la page principale avec les boutons ronds
def main_menu():
    st.title("Tableau de Bord Principal")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Besoin client", key="besoin_client"):
            st.session_state['page'] = 'besoin_client'

    with col2:
        if st.button("Proposition consultant", key="proposition_consultant"):
            st.session_state['page'] = 'proposition_consultant'

    with col3:
        if st.button("Liste des profils", key="liste_profils"):
            st.session_state['page'] = 'liste_profils'

# Fonction pour la page "Besoin client"
def page_besoin_client():
    st.title("Besoin Client")
    st.write("Contenu spécifique au module Besoin Client.")
    if st.button("Retour au menu principal"):
        st.session_state['page'] = 'main_menu'

# Fonction pour la page "Proposition consultant"
def page_proposition_consultant():
    st.title("Proposition Consultant")
    st.write("Contenu spécifique au module Proposition Consultant.")
    if st.button("Retour au menu principal"):
        st.session_state['page'] = 'main_menu'

# Fonction pour la page "Liste des profils"
def page_liste_profils():
    st.title("Liste des Profils")
    st.write("Contenu spécifique au module Liste des Profils.")
    if st.button("Retour au menu principal"):
        st.session_state['page'] = 'main_menu'

# Fonction principale
def main():
    # Configuration de la page (doit être la première commande)
    st.set_page_config(
        page_title="Application Multi-Modules",
        page_icon="🔒",
        layout="wide",
    )

    # Appliquer le style pour masquer les éléments indésirables
    hide_streamlit_style()

    # Initialiser les variables de session si elles n'existent pas
    if 'authenticated' not in st.session_state:
        st.session_state['authenticated'] = False
    if 'page' not in st.session_state:
        st.session_state['page'] = 'login'

    # Navigation entre les pages
    if not st.session_state['authenticated']:
        login_page()
    else:
        if st.session_state['page'] == 'main_menu':
            main_menu()
        elif st.session_state['page'] == 'besoin_client':
            page_besoin_client()
        elif st.session_state['page'] == 'proposition_consultant':
            page_proposition_consultant()
        elif st.session_state['page'] == 'liste_profils':
            page_liste_profils()
        else:
            main_menu()

# Exécuter l'application
if __name__ == "__main__":
    main()
