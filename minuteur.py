import base64
from datetime import date, timedelta
import streamlit as st
import streamlit.components.v1 as components


# Fonction pour encoder l'image locale en base64
def charger_image_locale(chemin_image):
    with open(chemin_image, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


st.set_page_config(page_title="Mon Minuteur", page_icon="⏳")

# --- IMAGE DE FOND PERSONNELLE ---
# Indique le nom de ton fichier image (JPG, PNG, WEBP)
nom_fichier_photo = "ma_photo.jpg"

try:
    img_b64 = charger_image_locale(nom_fichier_photo)
    url_image_fond = f"data:image/jpeg;base64,{img_b64}"
except FileNotFoundError:
    # Image de secours si ton fichier n'est pas trouvé
    url_image_fond = "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1920&q=80"

st.markdown(
    f"""
    <style>
    /* Image de fond avec assombrissement noir à 65% */
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)), url("{url_image_fond}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* Titres en blanc avec ombre */
    h1, h2, h3 {{
        color: #FFFFFF !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8) !important;
    }}

    /* Encadrement metric en rose pâle */
    [data-testid="stMetric"] {{
        background-color: rgba(255, 228, 230, 0.92);
        padding: 15px 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
    }}
    [data-testid="stMetricLabel"] p {{
        color: #881337 !important;
        font-weight: 600 !important;
    }}
    [data-testid="stMetricValue"] div {{
        color: #4c0519 !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)