import streamlit as st
from PIL import Image
import os

# Configuration de la page
st.set_page_config(
    page_title="Galerie d'Images IA",
    page_icon="🖼️",
    layout="wide",
)

# Titre de la page
st.title("🌟 Galerie d'Images Générées par Intelligence Artificielle 🌟")

# Introduction
st.markdown("""
Bienvenue sur cette vitrine interactive ! Ici, vous pouvez explorer des créations uniques générées par intelligence artificielle. 
Chaque image est une œuvre d'art créée avec des algorithmes avancés. Profitez de la galerie ci-dessous et téléchargez vos images préférées.
""")

# Section Galerie
st.header("🎨 Galerie d'Images")
col1, col2, col3 = st.columns(3)

# Charger les images du dossier
chemin_images = "images"
fichiers_images = [f for f in os.listdir(chemin_images) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Affichage des images
if fichiers_images:
    for index, fichier in enumerate(fichiers_images):
        image = Image.open(os.path.join(chemin_images, fichier))
        with [col1, col2, col3][index % 3]:  # Affiche les images en colonnes
            st.image(image, use_column_width=True)
            st.caption(fichier)
            st.download_button(
                label="📥 Télécharger",
                data=open(os.path.join(chemin_images, fichier), "rb").read(),
                file_name=fichier,
                mime="image/png"
            )
else:
    st.write("Aucune image disponible dans la galerie. Ajoutez des images dans le dossier `images` pour les afficher ici.")

# Section Génération d'Images (Optionnel)
st.header("🤖 Générer une Nouvelle Image")
st.markdown("""
Vous voulez générer une nouvelle image ? Cliquez sur le bouton ci-dessous pour utiliser un modèle d'intelligence artificielle 
et ajouter votre création à la galerie.
""")

if st.button("Générer une Image"):
    from utils.generer_images import generer_image_ia  # Fonction personnalisée
    nouvelle_image = generer_image_ia(chemin_images)
    st.success(f"L'image `{nouvelle_image}` a été générée avec succès et ajoutée à la galerie !")

# Pied de page
st.sidebar.title("À propos")
st.sidebar.info("Ce site est un exemple de vitrine d'images IA créée avec Streamlit. Contactez-nous pour plus d'informations.")
