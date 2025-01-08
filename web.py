import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(
    page_title="Application Streamlit Exemple",
    page_icon="📊",
    layout="wide",
)

# Titre de l'application
st.title("Application Interactive avec Streamlit 🎉")

# Section 1 : Charger et afficher des données
st.header("1. Charger et Afficher des Données")
uploaded_file = st.file_uploader("Chargez un fichier CSV :", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :")
    st.dataframe(data)

    # Afficher des statistiques descriptives
    st.subheader("Statistiques descriptives")
    st.write(data.describe())

# Section 2 : Visualisation
st.header("2. Visualisation des Données")
if uploaded_file is not None:
    colonne = st.selectbox("Sélectionnez une colonne numérique pour visualisation :", data.select_dtypes(include="number").columns)
    if colonne:
        fig, ax = plt.subplots()
        data[colonne].hist(ax=ax, bins=20, color="skyblue", edgecolor="black")
        ax.set_title(f"Distribution de {colonne}")
        ax.set_xlabel(colonne)
        ax.set_ylabel("Fréquence")
        st.pyplot(fig)

# Section 3 : Calcul Interactif
st.header("3. Analyse Personnalisée")
if uploaded_file is not None:
    filtre_valeur = st.slider(f"Filtrer les valeurs de la colonne '{colonne}' :", min_value=float(data[colonne].min()), max_value=float(data[colonne].max()))
    data_filtre = data[data[colonne] >= filtre_valeur]
    st.write(f"Données après filtration sur '{colonne} ≥ {filtre_valeur}' :")
    st.dataframe(data_filtre)

    # Export des données filtrées
    st.download_button(
        label="Télécharger les données filtrées",
        data=data_filtre.to_csv(index=False),
        file_name="donnees_filtrees.csv",
        mime="text/csv",
    )

# Section 4 : À propos
st.sidebar.title("À propos")
st.sidebar.info("Ceci est une application Streamlit de démonstration. Créée avec ❤️ et Python.")