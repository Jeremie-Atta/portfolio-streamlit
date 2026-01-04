import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="Portfolio | Data Analyst",
    page_icon="📊",
    layout="wide",
)

# --- Header ---
col1, col2 = st.columns([1, 3], vertical_alignment="center")

with col1:
    img_path = Path("jeremie_copie.jpg")
    if img_path.exists():
        st.image(str(img_path), width=160)
    else:
        st.info("Ajoute une photo : jeremie_copie.jpg")

with col2:
    st.title("Atta Jérémie KOUAME")
    st.caption("Ingénieur Statisticien – Économiste | Data Analyst & Business Analyst (Junior)")
    st.write(
        "J’utilise l’analyse de données, les statistiques et les KPI "
        "pour soutenir la prise de décision business et économique."
    )

st.divider()

# --- Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller à", ["Accueil", "À propos", "Projets", "Compétences", "CV", "Contact"])

# ---------------- PAGES ----------------
if page == "Accueil":
    st.subheader("Bienvenue 👋")

    st.write(
        "Bienvenue sur mon portfolio.\n\n"
        "Je suis **Ingénieur Statisticien–Économiste**, spécialisé en analyse de données et "
        "aide à la décision.\n\n"
        "Ce site présente mon parcours, mes projets et les compétences que je développe "
        "en tant que **Data Analyst & Business Analyst**."
    )

    st.markdown("### Ce que vous trouverez ici")
    st.markdown(
        "- 📊 Des projets concrets d’analyse de données, de reporting et de KPI\n"
        "- 🧠 Mes compétences techniques et analytiques\n"
        "- 📄 Mon CV et mes informations de contact"
    )

elif page == "À propos":
    st.subheader("À propos")
    st.write(
        "Ingénieur Statisticien–Économiste de formation, je me spécialise dans l’analyse de données, "
        "la modélisation statistique et l’aide à la décision.\n\n"
        "Mon parcours m’a permis de développer des compétences solides en statistiques appliquées, "
        "analyse exploratoire et visualisation de données, avec une attention particulière portée "
        "à la compréhension des enjeux business.\n\n"
        "J’aime structurer des problématiques métiers, construire des indicateurs de performance "
        "et transformer les résultats en recommandations claires et exploitables.\n\n"
        "Je recherche actuellement une opportunité en Data Analyst ou Business Analyst, "
        "afin de continuer à développer mes compétences tout en apportant une réelle valeur ajoutée "
        "aux équipes métiers."
    )

elif page == "Projets":
    st.subheader("Projets")

    with st.expander("📌 Projet 1 — Prédiction de la rétention d’abonnés fibre (Machine Learning)"):
        st.markdown("""
**Contexte :** Dans un marché télécom concurrentiel, la rétention des abonnés est un enjeu stratégique.  
**Objectif :** identifier les clients à risque de suspension ou de résiliation afin de proposer des actions de rétention ciblées.  

**Données :** données clients anonymisées (usage, ancienneté, incidents, statut).  
**Outils :** Python (Pandas, NumPy, Scikit-learn), Streamlit.  
**Méthodes :** nettoyage, EDA, feature engineering, modélisation de classification, évaluation des performances.
""")

        st.markdown("### Résultats & insights")
        st.markdown("""
- Identification des abonnés à risque de churn  
- Variables clés : ancienneté, usage, incidents techniques  
- Modèle utile pour cibler des actions de rétention
""")

        st.markdown("### Impact business")
        st.markdown("""
- Réduction potentielle du taux de churn  
- Meilleure allocation des actions commerciales  
- Amélioration de la valeur client
""")

    with st.expander("📌 Projet 2 — Déterminants de la pauvreté des exploitants agricoles (UEMOA, 2021)"):
        st.markdown("""
**Contexte :** La pauvreté rurale demeure un enjeu majeur en zone UEMOA.  
**Objectif :** analyser les facteurs associés à la pauvreté des exploitants agricoles afin d’éclairer la décision publique.

**Données :** données socio-économiques 2021 (ménages/exploitants) : caractéristiques du ménage, éducation, accès aux services, conditions de production, etc.  
**Outils :** Stata (modélisation économétrique), préparation/structuration des bases.  
**Méthodes :** nettoyage, analyse descriptive, estimation économétrique, interprétation, recommandations.
""")

        st.markdown("### Contribution")
        st.markdown("""
- Construction, nettoyage et structuration de bases de données socio-économiques  
- Modélisation économétrique appliquée au développement rural  
- Rédaction et synthèse de résultats pour appuyer l’aide à la décision
""")

        st.markdown("### Résultats (à détailler dans la version finale)")
        st.markdown("""
- Identification de facteurs associés à la pauvreté (ex. éducation, accès aux services, caractéristiques de l’exploitation)  
- Recommandations orientées politiques publiques : ciblage des actions, renforcement des capacités, amélioration de l’accès aux services
""")

    with st.expander("📌 Projet 3 — Gestion et optimisation d’un portefeuille actions / obligations"):
        st.markdown("""
**Contexte :** La gestion de portefeuille vise à optimiser la performance financière tout en maîtrisant le risque.  
**Objectif :** construire une stratégie d’allocation actions / obligations maximisant la performance ajustée au risque.

**Données :** rendements d’actions et d’obligations, taux d’intérêt, indicateurs de marché.  
**Outils :** Excel avancé (modélisation, reporting), finance quantitative.  
**Méthodes :** analyse rendement/risque, allocation d’actifs, sensibilité aux taux, optimisation, reporting.
""")

        st.markdown("### Résultats & insights")
        st.markdown("""
- Amélioration du couple rendement / risque  
- Sensibilité différenciée du portefeuille aux variations de marché  
- Arbitrage actions / obligations selon le contexte macro-financier
""")

        st.markdown("### Recommandations")
        st.markdown("""
- Ajustement de l’allocation selon le profil de risque  
- Stratégies de couverture face aux variations de taux  
- Suivi régulier via des indicateurs de performance
""")

    with st.expander("📌 Projet 4 — Analyse de la satisfaction du restaurant de l’ENSEA"):
        st.markdown("""
**Contexte :** La satisfaction des usagers est un indicateur clé de la qualité de service.  
**Objectif :** mesurer la satisfaction des étudiants et identifier les axes d’amélioration prioritaires.

**Données :** enquête auprès des étudiants (qualité des repas, prix, hygiène, temps d’attente, accueil).  
**Outils :** Python / R, statistiques multivariées, visualisation de données.  
**Méthodes :** construction d’indicateurs, ACP, alpha de Cronbach, interprétation.
""")

        st.markdown("### Résultats & insights")
        st.markdown("""
- Construction d’un indicateur global de satisfaction fiable  
- Identification des dimensions clés de la satisfaction  
- Mise en évidence des facteurs d’amélioration prioritaires
""")

        st.markdown("### Recommandations")
        st.markdown("""
- Amélioration de la qualité perçue des repas  
- Réduction du temps d’attente  
- Renforcement de l’accueil et de l’organisation du service
""")


elif page == "Compétences":
    st.subheader("Compétences")

    st.markdown("### 📊 Data & Statistiques")
    st.markdown("""
- Analyse exploratoire des données (EDA)  
- Statistiques descriptives et inférentielles  
- Régression, classification, clustering  
- Séries temporelles  
- Analyse factorielle (ACP), fiabilité (alpha de Cronbach)
""")

    st.markdown("### 🤖 Machine Learning")
    st.markdown("""
- Préparation et nettoyage des données  
- Feature engineering  
- Modèles de classification (churn / rétention)  
- Évaluation des performances des modèles
""")

    st.markdown("### 🧠 Économétrie & Politiques publiques")
    st.markdown("""
- Modélisation économétrique appliquée  
- Analyse des déterminants socio-économiques  
- Interprétation des résultats et recommandations
""")

    st.markdown("### 💼 Business & Finance")
    st.markdown("""
- Analyse de KPI et reporting  
- Aide à la décision  
- Gestion et optimisation de portefeuille  
- Analyse du risque et sensibilité aux taux
""")

    st.markdown("### 🛠️ Outils & technologies")
    st.markdown("""
- **Langages :** Python, R, SQL  
- **Data & ML :** Pandas, NumPy, Scikit-learn  
- **BI & Dataviz :** Power BI, Tableau, Excel avancé  
- **Stats & éco :** Stata, SPSS, EViews  
- **Autres :** VS Code, Git (bases)
""")


elif page == "CV":
    st.subheader("📄 Curriculum Vitae")

    st.write(
        "Vous pouvez consulter ou télécharger mon CV ci-dessous."
    )

    with open("CV_ISE_KOUAME_ATTA.pdf", "rb") as file:
        st.download_button(
            label="⬇️ Télécharger mon CV (PDF)",
            data=file,
            file_name="CCV_ISE_KOUAME_ATTA.pdf",
            mime="application/pdf"
        )


elif page == "Contact":
    st.subheader("📬 Contact")

    st.write("N’hésitez pas à me contacter pour toute opportunité, collaboration ou échange professionnel.")

    st.markdown("### 📧 Email")
    st.markdown("[attajeremiek@gmail.com](mailto:attajeremiek@gmail.com)")

    st.markdown("### 📱 Téléphone")
    st.markdown(
        "- [+225 07 79 01 08 72](tel:+2250779010872)\n"
        "- [+225 01 72 66 68 99](tel:+2250172666899)\n"
        "- [+225 07 89 25 29 67](tel:+2250789252967)"
    )

    st.markdown("### 📍 Localisation")
    st.write("Abidjan, Côte d’Ivoire")

    st.markdown("### 💼 LinkedIn")
    st.markdown("[atta-jérémie-kouame](https://www.linkedin.com)")

