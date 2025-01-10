import streamlit as st

# Masquer le menu hamburger et le footer de Streamlit
hide_streamlit_style = """
            <style>
            /* Cacher le menu hamburger en haut à droite */
            #MainMenu {visibility: hidden;}
            /* Cacher le footer "Made with Streamlit" */
            footer {visibility: hidden;}
            /* Cacher le bandeau de paramètres */
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Configuration de la page
st.set_page_config(
    page_title="Page d'Accueil",
    page_icon="🔑",
    layout="centered",
)

# Conteneur central pour le formulaire de connexion
with st.container():
    st.title("Bienvenue")
    st.subheader("Veuillez entrer votre adresse email pour vous connecter")

    # Champ de saisie pour l'email
    email = st.text_input("Adresse Email", type="email")

    # Bouton de soumission
    if st.button("Se Connecter"):
        if email:
            # Ici, vous pouvez ajouter la logique de vérification de l'email
            st.success(f"Connexion réussie avec l'adresse {email}!")
        else:
            st.error("Veuillez entrer une adresse email valide.")
