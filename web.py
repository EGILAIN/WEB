import streamlit as st
import re

def is_valid_email(email):
    """Vérifie si l'email est valide à l'aide d'une expression régulière."""
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(regex, email) is not None

def main():
    st.set_page_config(
        page_title="Page d'Accueil",
        page_icon="🔒",
        layout="centered",
    )

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                .stApp {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .container {
                    text-align: center;
                }
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    with st.container():
        st.title("Bienvenue")
        st.subheader("Veuillez entrer votre adresse email pour vous connecter")

        # Champ de saisie pour l'email
        email = st.text_input("Adresse Email")

        # Validation en temps réel
        if email:
            if is_valid_email(email):
                st.success("Adresse email valide.")
            else:
                st.error("Adresse email invalide.")

        # Bouton de soumission
        if st.button("Se Connecter"):
            if email and is_valid_email(email):
                st.success(f"Connexion réussie avec l'adresse {email}!")
            else:
                st.error("Veuillez entrer une adresse email valide.")

if __name__ == "__main__":
    main()
