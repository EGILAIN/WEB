import streamlit as st

# Fonction pour cacher le menu et le footer de Streamlit
def hide_streamlit_style():
    hide_style = """
            <style>
            /* Cacher le menu hamburger en haut à droite */
            #MainMenu {visibility: hidden;}
            /* Cacher le footer "Made with Streamlit" */
            footer {visibility: hidden;}
            /* Cacher la barre de défilement à gauche (si présente) */
            /* Aucun élément par défaut à cacher ici */
            </style>
            """
    st.markdown(hide_style, unsafe_allow_html=True)

def main():
    # Appliquer le style pour masquer les éléments indésirables
    hide_streamlit_style()

    # Configurer la page pour utiliser tout l'espace disponible
    st.set_page_config(page_title="Page d'Accueil", page_icon="🔒", layout="centered")

    # Créer un conteneur central pour le formulaire de connexion
    with st.container():
        st.title("Bienvenue sur Mon Application")
        st.write("Veuillez vous connecter en entrant votre adresse email.")

        # Champ de saisie pour l'email
        email = st.text_input("Adresse Email", type="email")

        # Bouton de connexion
        if st.button("Se Connecter"):
            if email:
                # Ici, vous pouvez ajouter la logique de vérification de l'email
                st.success(f"Connexion réussie avec l'adresse {email}!")
            else:
                st.error("Veuillez entrer une adresse email valide.")

if __name__ == "__main__":
    main()
