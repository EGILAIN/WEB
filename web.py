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
    /* Ajouter un fond légèrement gris pour le conteneur principal */
    .stApp {
        background-color: #f0f2f6;
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
        st.session_state['user_email'] = ''
        st.experimental_rerun()

# Fonction pour la page "Besoin client"
def page_besoin_client():
    st.title("Besoin Client")
    st.write("Contenu spécifique au module **Besoin Client**.")
    # Ajoutez ici les fonctionnalités spécifiques à ce module

# Fonction pour la page "Proposition consultant"
def page_proposition_consultant():
    st.title("Proposition Consultant")
    st.write("Veuillez remplir les informations suivantes :")

    with st.form("proposition_consultant_form"):
        # Création de quatre colonnes
        col1, col2, col3, col4 = st.columns(4)

        # Colonne Responsable
        with col1:
            st.header("Responsable")
            responsable_associe = st.text_input("Associé", key="associe")
            responsable_localisation = st.text_input("Localisation Responsable", key="localisation_responsable")
            responsable_source = st.text_input("Source", key="source")
            responsable_origine = st.text_input("Origine", key="origine")

        # Colonne Candidat
        with col2:
            st.header("Candidat")
            candidat_nom = st.text_input("Nom", key="nom")
            candidat_prenom = st.text_input("Prénom", key="prenom")
            candidat_email = st.text_input("Adresse mail", key="adresse_mail")
            candidat_telephone = st.text_input("Téléphone", key="telephone")

        # Colonne Poste
        with col3:
            st.header("Poste")
            poste_metier = st.text_input("Métier", key="metier")
            poste_experience = st.number_input("Expérience (années)", min_value=0, step=1, key="experience")
            poste_taux = st.number_input("Taux (%)", min_value=0, max_value=100, step=1, key="taux")
            poste_localisation = st.text_input("Localisation Poste", key="localisation_poste")

        # Colonne Compétences
        with col4:
            st.header("Compétences")
            competence_metier = st.text_area("Compétences métier", key="competences_metier")
            competence_generales = st.text_area("Compétences générales", key="competences_generales")
            competence_techniques = st.text_area("Compétences techniques", key="competences_techniques")
            competence_linguistiques = st.text_area("Compétences linguistiques", key="competences_linguistiques")

        # Bouton de soumission
        submitted = st.form_submit_button("Soumettre Proposition")

        if submitted:
            # Validation simple des champs requis
            if not (responsable_associe and candidat_nom and poste_metier):
                st.error("Veuillez remplir les champs obligatoires (Associé, Nom, Métier).")
            else:
                # Traitement des données du formulaire
                proposition_data = {
                    "Responsable": {
                        "Associé": responsable_associe,
                        "Localisation": responsable_localisation,
                        "Source": responsable_source,
                        "Origine": responsable_origine
                    },
                    "Candidat": {
                        "Nom": candidat_nom,
                        "Prénom": candidat_prenom,
                        "Adresse mail": candidat_email,
                        "Téléphone": candidat_telephone
                    },
                    "Poste": {
                        "Métier": poste_metier,
                        "Expérience": poste_experience,
                        "Taux": poste_taux,
                        "Localisation": poste_localisation
                    },
                    "Compétences": {
                        "Compétences métier": competence_metier,
                        "Compétences générales": competence_generales,
                        "Compétences techniques": competence_techniques,
                        "Compétences linguistiques": competence_linguistiques
                    }
                }

                # Ici, vous pouvez ajouter la logique pour enregistrer les données, par exemple dans une base de données ou un fichier
                st.success("Proposition Consultant soumise avec succès !")
                st.json(proposition_data)  # Affiche les données soumises pour vérification

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
