import streamlit as st
import re

# Fonction pour vérifier si l'email est valide
def is_valid_email(email):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(regex, email) is not None

# Fonction pour masquer les éléments par défaut de Streamlit et ajouter des bordures autour des sections
def hide_streamlit_style():
    hide_style = """
    <style>
    /* Cacher le menu hamburger en haut à droite */
    #MainMenu {visibility: hidden;}
    /* Cacher le footer "Made with Streamlit" */
    footer {visibility: hidden;}
    /* Cacher le bandeau de paramètres */
    header {visibility: hidden;}
    
    /* Styles pour les sections avec bordure */
    .section {
        border: 1px solid #ccc;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
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

# Fonction pour la page principale avec le bandeau de navigation
def main_app():
    # Création du bandeau de navigation à gauche
    st.sidebar.title("Navigation")
    navigation = st.sidebar.radio("Aller à", ("Besoin client", "Proposition consultant", "Liste des profils", "Suivi d'activité", "Déconnexion"))

    # Affichage du contenu en fonction de la sélection
    if navigation == "Besoin client":
        page_besoin_client()
    elif navigation == "Proposition consultant":
        page_proposition_consultant()
    elif navigation == "Liste des profils":
        page_liste_profils()
    elif navigation == "Suivi d'activité":
        page_suivi_activite()
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
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("<div class='section-header'>Responsable</div>", unsafe_allow_html=True)
            responsable_associe = st.selectbox(
                "Associé",
                options=["CHS", "YLD", "JCA", "JBH", "Autres"],
                key="associe"
            )
            responsable_siege = st.selectbox(
                "Siège",
                options=["Kleber", "Rochefort", "Montesson"],
                key="siege"
            )
            responsable_source = st.selectbox(
                "Source",
                options=["Réseau social", "Bouche à oreille", "Relation client"],
                key="source"
            )
            # Origine supprimé
            st.markdown("</div>", unsafe_allow_html=True)

        # Colonne Candidat
        with col2:
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("<div class='section-header'>Candidat</div>", unsafe_allow_html=True)
            candidat_nom = st.text_input("Nom", key="nom")
            candidat_prenom = st.text_input("Prénom", key="prenom")
            candidat_email = st.text_input("Adresse mail", key="adresse_mail")
            candidat_telephone = st.text_input("Téléphone", key="telephone")
            st.markdown("</div>", unsafe_allow_html=True)

        # Colonne Poste
        with col3:
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("<div class='section-header'>Poste</div>", unsafe_allow_html=True)
            poste_metier = st.selectbox(
                "Métier",
                options=[
                    "Comptabilité générale", "Comptabilité analytique", "Comptabilité auxiliaire",
                    "Audit comptable", "Audit IT", "Contrôle de gestion", "Fiscalité",
                    "Analyste data", "Ingénieur data", "Manager data", "Ressource humaine", "Consolidation"
                ],
                key="metier"
            )
            poste_experience = st.number_input("Expérience (années)", min_value=0, step=1, key="experience")
            poste_taux = st.number_input("Taux (%)", min_value=0, max_value=100, step=1, key="taux")
            poste_localisation = st.text_input("Localisation Poste", key="localisation_poste")
            st.markdown("</div>", unsafe_allow_html=True)

        # Colonne Compétences
        with col4:
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.markdown("<div class='section-header'>Compétences</div>", unsafe_allow_html=True)
            competence_generales = st.multiselect(
                "Compétences générales",
                options=["Informatique", "Comptabilité", "Finance", "Droit", "Système d'information", "Relationnel"],
                key="competences_generales"
            )
            competence_techniques = st.multiselect(
                "Compétences techniques",
                options=["Exemple 1", "Exemple 2"],  # Liste à venir
                key="competences_techniques"
            )
            competence_linguistiques = st.multiselect(
                "Compétences linguistiques",
                options=["Anglais", "Français", "Espagnol", "Russe", "Arabe", "Chinois"],
                key="competences_linguistiques"
            )
            st.markdown("</div>", unsafe_allow_html=True)

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
                        "Siège": responsable_siege,
                        "Source": responsable_source
                        # "Origine" supprimé
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
                        "Compétences générales": competence_generales,
                        "Compétences techniques": competence_techniques,
                        "Compétences linguistiques": competence_linguistiques
                    }
                }

                # Initialiser la liste des propositions si elle n'existe pas
                if 'proposals' not in st.session_state:
                    st.session_state['proposals'] = []

                # Ajouter la nouvelle proposition à la liste
                st.session_state['proposals'].append(proposition_data)

                # Récapitulatif numéroté des propositions
                st.success("Proposition Consultant soumise avec succès !")
                st.markdown("### Récapitulatif des Propositions")
                for idx, proposal in enumerate(st.session_state['proposals'], 1):
                    st.markdown(f"**{idx}. Responsable :** {proposal['Responsable']['Associé']}")
                    st.markdown(f"- **Siège :** {proposal['Responsable']['Siège']}")
                    st.markdown(f"- **Source :** {proposal['Responsable']['Source']}")
                    st.markdown(f"**Candidat :** {proposal['Candidat']['Nom']} {proposal['Candidat']['Prénom']}")
                    st.markdown(f"- **Adresse mail :** {proposal['Candidat']['Adresse mail']}")
                    st.markdown(f"- **Téléphone :** {proposal['Candidat']['Téléphone']}")
                    st.markdown(f"**Poste :** {proposal['Poste']['Métier']}")
                    st.markdown(f"- **Expérience :** {proposal['Poste']['Expérience']} ans")
                    st.markdown(f"- **Taux :** {proposal['Poste']['Taux']}%")
                    st.markdown(f"- **Localisation :** {proposal['Poste']['Localisation']}")
                    st.markdown(f"**Compétences Générales :** {', '.join(proposal['Compétences']['Compétences générales'])}")
                    st.markdown(f"**Compétences Techniques :** {', '.join(proposal['Compétences']['Compétences techniques'])}")
                    st.markdown(f"**Compétences Linguistiques :** {', '.join(proposal['Compétences']['Compétences linguistiques'])}")
                    st.markdown("---")

    # Fonction pour la page "Liste des profils"
    def page_liste_profils():
        st.title("Liste des Profils")
        st.write("Contenu spécifique au module **Liste des Profils**.")
        # Ajoutez ici les fonctionnalités spécifiques à ce module

    # Fonction pour la page "Suivi d'activité"
    def page_suivi_activite():
        st.title("Suivi d'Activité")
        st.write("Voici la liste des propositions soumises :")

        if 'proposals' not in st.session_state or not st.session_state['proposals']:
            st.info("Aucune proposition n'a été soumise pour le moment.")
        else:
            for idx, proposal in enumerate(st.session_state['proposals'], 1):
                st.markdown(f"### Proposition {idx}")
                st.markdown(f"**Responsable :** {proposal['Responsable']['Associé']}")
                st.markdown(f"- **Siège :** {proposal['Responsable']['Siège']}")
                st.markdown(f"- **Source :** {proposal['Responsable']['Source']}")
                st.markdown(f"**Candidat :** {proposal['Candidat']['Nom']} {proposal['Candidat']['Prénom']}")
                st.markdown(f"- **Adresse mail :** {proposal['Candidat']['Adresse mail']}")
                st.markdown(f"- **Téléphone :** {proposal['Candidat']['Téléphone']}")
                st.markdown(f"**Poste :** {proposal['Poste']['Métier']}")
                st.markdown(f"- **Expérience :** {proposal['Poste']['Expérience']} ans")
                st.markdown(f"- **Taux :** {proposal['Poste']['Taux']}%")
                st.markdown(f"- **Localisation :** {proposal['Poste']['Localisation']}")
                st.markdown(f"**Compétences Générales :** {', '.join(proposal['Compétences']['Compétences générales'])}")
                st.markdown(f"**Compétences Techniques :** {', '.join(proposal['Compétences']['Compétences techniques'])}")
                st.markdown(f"**Compétences Linguistiques :** {', '.join(proposal['Compétences']['Compétences linguistiques'])}")
                st.markdown("---")

    # Fonction principale
    def main():
        # Configuration de la page (doit être la première commande)
        st.set_page_config(
            page_title="Application Multi-Modules",
            page_icon="🔒",
            layout="wide",
        )

        # Appliquer le style pour masquer les éléments indésirables et ajouter des bordures
        hide_streamlit_style()

        # Initialiser les variables de session si elles n'existent pas
        if 'authenticated' not in st.session_state:
            st.session_state['authenticated'] = False
        if 'user_email' not in st.session_state:
            st.session_state['user_email'] = ''
        if 'proposals' not in st.session_state:
            st.session_state['proposals'] = []

        # Navigation entre les pages
        if not st.session_state['authenticated']:
            login_page()
        else:
            main_app()

    # Exécuter l'application
    if __name__ == "__main__":
        main()
