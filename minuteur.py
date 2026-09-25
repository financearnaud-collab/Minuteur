import streamlit as st
import streamlit.components.v1 as components
from datetime import date, timedelta

st.set_page_config(page_title="Mon Minuteur", page_icon="⏳")
st.title("⏳ Départ de Lionel")
st.subheader("Vivement le 30 octobre 2026 à 16h15")

# Code HTML et JavaScript pour l'affichage dynamique
code_html_js = """
<div id="minuteur" style="text-align: center; font-size: 50px; font-weight: bold; color: #1f77b4; background-color: #f0f2f6; padding: 30px; border-radius: 15px; font-family: sans-serif; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);">
    Chargement...
</div>

<script>
    const dateCible = new Date("2026-10-30T16:15:00").getTime();

    const intervalle = setInterval(function() {
        const maintenant = new Date().getTime();
        const difference = dateCible - maintenant;

        if (difference <= 0) {
            clearInterval(intervalle);
            document.getElementById("minuteur").innerHTML = "⏰ Temps écoulé !";
            return;
        }

        const jours = Math.floor(difference / (1000 * 60 * 60 * 24));
        let heures = Math.floor((difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        let minutes = Math.floor((difference % (1000 * 60)) / (1000 * 60));
        let secondes = Math.floor((difference % (1000 * 60)) / 1000);

        heures = heures < 10 ? "0" + heures : heures;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        secondes = secondes < 10 ? "0" + secondes : secondes;

        document.getElementById("minuteur").innerHTML = jours + " Jours <br>" + heures + " : " + minutes + " : " + secondes;
    }, 1000);
</script>
"""

# Utilisation de components.html pour autoriser l'exécution du JavaScript
components.html(code_html_js, height=200)


# --- Calcul des jours ouvrés / travaillés ---
def calculer_jours_ouvres(debut: date, fin: date) -> int:
    jours_ouvres = 0
    actuel = debut
    while actuel < fin:
        if actuel.weekday() < 5:  # Du lundi (0) au vendredi (4)
            jours_ouvres += 1
        actuel += timedelta(days=1)
    return jours_ouvres


aujourdhui = date.today()
date_cible = date(2026, 10, 30)

if aujourdhui < date_cible:
    nb_jours_ouvres = calculer_jours_ouvres(aujourdhui, date_cible)
    st.metric(
        label="💼 Jours travaillés restants (lundi au vendredi)",
        value=f"{nb_jours_ouvres} jours",
        help="Nombre de jours ouvrés hors week-ends entre aujourd'hui et la date cible."
    )
else:
    st.info("La date cible est atteinte ou dépassée !")