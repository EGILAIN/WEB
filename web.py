import streamlit as st

def main():
    # **1. Configuration de la page** (DOIT être la première commande Streamlit)
    st.set_page_config(
        page_title="Page d'Accueil",
        page_icon="🔒",
        layout="centered",
    )

    # **2. Masquer le menu hamburger et le footer de Streamlit**
    hide_streamlit_style = """
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
                /* Personnaliser le conteneur */
                .container {
                    text-align: center;
                }
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # **3. Conteneur central pour le formulaire de connexion**
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

if __name__ == "__main__":
    main()
