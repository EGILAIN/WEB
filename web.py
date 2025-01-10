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

# Fonction pour la page principale avec le bandeau de navigation
def main_app():
    # Création du bandeau de navigation à gauche
    st.sidebar.title("Navigation")
    navigation = st.sidebar.radio("Aller à", ("Besoin client", "Proposition consultant", "Liste des profils", "Déconnexion"))

    # Affichage du contenu en fonction de la sélection
    if navigation == "Besoin client":
        page_besoin_client()
    elif navigation == "Proposition consultant":
        page_proposition_consultant()
    elif navigation == "Liste des profils":
        page_liste_profils()
    elif navigation == "Déconnexion":
        st.session_state['authenticated'] = False
        st.session_state['page'] = 'login'
        st.experimental_rerun()

# Fonction pour la page "Besoin client"
def page_besoin_client():
    st.title("Besoin Client")
    st.write("Contenu spécifique au module **Besoin Client**.")
    # Ajoutez ici les fonctionnalités spécifiques à ce module

# Fonction pour la page "Proposition consultant"
def page_proposition_consultant():
    st.title("Proposition Consultant")
    st.write("Contenu spécifique au module **Proposition Consultant**.")
    # Ajoutez ici les fonctionnalités spécifiques à ce module

# Fonction pour la page "Liste des profils"
def page_liste_profils():
    st.title("Liste des Profils")
    st.write("Contenu spécifique au module **Liste des Profils**.")
    # Ajoutez ici les fonctionnalités spécifiques à ce module

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
    if 'user_email' not in st.session_state:
        st.session_state['user_email'] = ''

    # Navigation entre les pages
    if not st.session_state['authenticated']:
        login_page()
    else:
        main_app()

# Exécuter l'application
if __name__ == "__main__":
    main()
