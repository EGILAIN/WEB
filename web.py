import streamlit as st
import re

# Fonction pour vérifier si l'email est valide
def is_valid_email(email):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(regex, email) is not None

# Fonction pour masquer les éléments par défaut de Streamlit et ajuster les marges
def hide_streamlit_style():
    hide_style = """
    <style>
    /* Cacher le menu hamburger en haut à droite */
    #MainMenu {visibility: hidden;}
    /* Cacher le footer "Made with Streamlit" */
    footer {visibility: hidden;}
    /* Cacher le bandeau de paramètres */
    header {visibility: hidden;}

    /* Ajuster les sections */
    .section {
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
        margin-top: 0px; /* Supprime les marges au-dessus */
    }

    /* Ajuster les colonnes pour éviter les marges inutiles */
    .stVerticalBlock > div {
        padding-top: 0px !important;
        margin-top: 0px !important;
    }

    /* Styliser les en-têtes des sections */
    .section-header {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #4CAF50;
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
            st.experimental_rerun()
        else:
            st.error("Veuillez entrer une adresse email valide.")

# Fonction principale
def main():
    st.set_page_config(page_title="Proposition Consultant", page_icon="🔒", layout="wide")
    hide_streamlit_style()

    # Exemple de formulaire
    st.title("Proposition Consultant")
    st.write("Veuillez remplir les informations suivantes :")

    with st.form("proposition_consultant_form"):
        # Création de quatre colonnes
        col1, col2, col3, col4 = st.columns(4)

        # Colonne Responsable
        with col1:
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("<div class='section-header'>Responsable</div>", unsafe_allow_html=True)
            st.selectbox("Associé", ["CHS", "YLD", "JCA", "JBH", "Autres"], key="associe")
            st.selectbox("Siège", ["Kleber", "Rochefort", "Montesson"], key="siege")
            st.selectbox("Source", ["Réseau social", "Bouche à oreille", "Relation client"], key="source")
            st.markdown("</div>", unsafe_allow_html=True)

        # Colonne Candidat
        with col2:
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("<div class='section-header'>Candidat</div>", unsafe_allow_html=True)
            st.text_input("Nom", key="nom")
            st.text_input("Prénom", key="prenom")
            st.text_input("Adresse mail", key="email")
            st.text_input("Téléphone", key="telephone")
            st.markdown("</div>", unsafe_allow_html=True)

        # Colonne Poste
        with col3:
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("<div class='section-header'>Poste</div>", unsafe_allow_html=True)
            st.selectbox(
                "Métier",
                ["Comptabilité générale", "Comptabilité analytique", "Comptabilité auxiliaire",
                 "Audit comptable", "Audit IT", "Contrôle de gestion", "Fiscalité", 
                 "Analyste data", "Ingénieur data", "Manager data", "Ressource humaine", "Consolidation"],
                key="metier"
            )
            st.number_input("Expérience (années)", min_value=0, step=1, key="experience")
            st.number_input("Taux (%)", min_value=0, max_value=100, step=1, key="taux")
            st.text_input("Localisation Poste", key="localisation")
            st.markdown("</div>", unsafe_allow_html=True)

        # Colonne Compétences
        with col4:
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("<div class='section-header'>Compétences</div>", unsafe_allow_html=True)
            st.multiselect("Compétences générales", ["Informatique", "Comptabilité", "Finance", "Droit", "Relationnel"], key="competences_generales")
            st.multiselect("Compétences techniques", ["Exemple 1", "Exemple 2"], key="competences_techniques")
            st.multiselect("Compétences linguistiques", ["Anglais", "Français", "Espagnol", "Russe", "Arabe", "Chinois"], key="competences_linguistiques")
            st.markdown("</div>", unsafe_allow_html=True)

        # Bouton de soumission
        st.form_submit_button("Soumettre Proposition")

if __name__ == "__main__":
    # Initialiser les variables de session
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["user_email"] = ""

    # Si l'utilisateur est authentifié, afficher le formulaire principal
    if st.session_state["authenticated"]:
        main()
    else:
        # Afficher la page de connexion
        login_page()
