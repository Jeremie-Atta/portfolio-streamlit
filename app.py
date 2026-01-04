import streamlit as st
from pathlib import Path

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Portfolio | Atta Jérémie KOUAME",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------ STYLE (More premium + dynamic) ------------------
st.markdown("""
<style>
:root{
  --accent: #2563eb;      /* blue */
  --accent2:#10b981;      /* green */
  --ink: rgba(17, 24, 39, 0.92);
  --muted: rgba(17, 24, 39, 0.70);
  --stroke: rgba(148, 163, 184, 0.35);
  --glass: rgba(255, 255, 255, 0.72);
}

/* App background */
.stApp {
  background:
    radial-gradient(1200px 600px at 10% 10%, rgba(37,99,235,0.14), transparent 55%),
    radial-gradient(900px 500px at 85% 15%, rgba(16,185,129,0.14), transparent 55%),
    radial-gradient(1000px 650px at 50% 95%, rgba(99,102,241,0.10), transparent 55%),
    linear-gradient(180deg, rgba(248,250,252,1) 0%, rgba(255,255,255,1) 55%, rgba(248,250,252,1) 100%);
}

/* layout */
.block-container { padding-top: 2rem; padding-bottom: 3rem; max-width: 1120px; }

/* typography */
h1,h2,h3 { color: var(--ink); letter-spacing: -0.3px; }
p,li { color: var(--muted); }
.small { font-size: 0.96rem; color: var(--muted); line-height: 1.55; }

/* sidebar */
section[data-testid="stSidebar"]{
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(10px);
  border-right: 1px solid var(--stroke);
}
section[data-testid="stSidebar"] .stRadio label, 
section[data-testid="stSidebar"] p, 
section[data-testid="stSidebar"] span { color: var(--ink) !important; }

/* ✅ card (NOW COLORFUL) */
.card {
  padding: 1.15rem 1.25rem;
  border: 1px solid rgba(37,99,235,0.22);
  border-radius: 18px;

  /* ✅ background coloré (dégradé) */
  background: linear-gradient(
      135deg,
      rgba(37,99,235,0.14) 0%,
      rgba(16,185,129,0.12) 45%,
      rgba(99,102,241,0.10) 100%
  );

  backdrop-filter: blur(10px);
  box-shadow: 0 10px 30px rgba(2,6,23,0.08);
  transition: transform .16s ease, box-shadow .16s ease, border-color .16s ease;
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 18px 48px rgba(2,6,23,0.12);
  border-color: rgba(16,185,129,0.35);
}

/* badges */
.badge {
  display: inline-flex;
  align-items: center;
  padding: 0.28rem 0.65rem;
  margin-right: 0.4rem;
  margin-bottom: 0.4rem;
  border-radius: 999px;
  border: 1px solid rgba(37,99,235,0.22);
  font-size: 0.85rem;
  color: rgba(30,64,175,0.95);
  background: rgba(37,99,235,0.08);
}
.badge.green {
  border-color: rgba(16,185,129,0.24);
  color: rgba(4,120,87,0.95);
  background: rgba(16,185,129,0.09);
}
.badge.purple {
  border-color: rgba(99,102,241,0.22);
  color: rgba(67,56,202,0.95);
  background: rgba(99,102,241,0.10);
}

/* divider */
hr { margin: 1.2rem 0; border: none; border-top: 1px solid var(--stroke); }

/* buttons */
.stButton>button, .stDownloadButton>button {
  border-radius: 12px !important;
  padding: 0.62rem 0.9rem !important;
  border: 1px solid rgba(37,99,235,0.28) !important;
}
.stButton>button:hover, .stDownloadButton>button:hover {
  border-color: rgba(16,185,129,0.35) !important;
}

/* image rounding */
img { border-radius: 16px; }
</style>
""", unsafe_allow_html=True)

def badges(items, variant="blue"):
    cls = {"blue": "", "green": " green", "purple": " purple"}.get(variant, "")
    html = "".join([f'<span class="badge{cls}">{x}</span>' for x in items])
    st.markdown(html, unsafe_allow_html=True)

def card_open():
    st.markdown('<div class="card">', unsafe_allow_html=True)

def card_close():
    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.markdown("## ⚙️ Portfolio")
page = st.sidebar.radio("Navigation", ["Accueil", "À propos", "Projets", "Compétences", "CV", "Contact"])
st.sidebar.divider()
st.sidebar.caption("© Atta Jérémie KOUAME")

# ------------------ HEADER ------------------
colA, colB = st.columns([1, 3], vertical_alignment="center")

with colA:
    img_path = Path("jeremie_copie.jpg")
    if img_path.exists():
        st.image(str(img_path), width=170)
    else:
        st.info("Ajoute une photo : jeremie_copie.jpg")

with colB:
    card_open()
    st.markdown("## Atta Jérémie KOUAME")
    badges(["Ingénieur Statisticien–Économiste"], "purple")
    badges(["Data Analyst (Junior)", "Business Analyst (Junior)"], "green")
    st.markdown(
        '<div class="small">J’utilise l’analyse de données, les statistiques et les KPI pour soutenir la prise de décision business et économique.</div>',
        unsafe_allow_html=True
    )
    card_close()

st.divider()

# ------------------ PAGES ------------------
if page == "Accueil":
    st.subheader("Bienvenue 👋")

    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        card_open()
        st.markdown("**🎯 Objectif**")
        st.markdown('<div class="small">Présenter mon parcours, mes projets et ma valeur ajoutée orientée data & décision.</div>', unsafe_allow_html=True)
        card_close()
    with c2:
        card_open()
        st.markdown("**🧠 Ce que je fais**")
        st.markdown('<div class="small">Analyse, KPI, reporting, modélisation, visualisation et recommandations.</div>', unsafe_allow_html=True)
        card_close()
    with c3:
        card_open()
        st.markdown("**📍 Localisation**")
        st.markdown('<div class="small">Abidjan, Côte d’Ivoire</div>', unsafe_allow_html=True)
        card_close()

    st.markdown("### Aperçu")
    card_open()
    st.markdown(
        '<div class="small">'
        'Bienvenue sur mon portfolio.<br/><br/>'
        'Je suis <b>Ingénieur Statisticien–Économiste</b>, spécialisé en analyse de données et aide à la décision.<br/><br/>'
        'Ce site présente mon parcours, mes projets et les compétences que je développe en tant que <b>Data Analyst & Business Analyst</b>.'
        '</div>',
        unsafe_allow_html=True
    )
    card_close()

    st.markdown("### Accès rapide")
    q1, q2 = st.columns([2, 1], gap="large")
    with q1:
        card_open()
        st.markdown("**📌 Points clés**")
        st.markdown(
            "- 📊 Projets data, business & finance\n"
            "- 🧠 Méthode rigoureuse et orientée résultats\n"
            "- 📄 CV téléchargeable en un clic"
        )
        card_close()
    with q2:
        card_open()
        cv_path = Path("CV_ISE_KOUAME_ATTA.pdf")
        if cv_path.exists():
            with open(cv_path, "rb") as f:
                st.download_button(
                    "⬇️ Télécharger mon CV",
                    data=f,
                    file_name="CV_ISE_KOUAME_ATTA.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        else:
            st.error("CV introuvable")
        card_close()

elif page == "À propos":
    st.subheader("À propos")
    card_open()
    st.markdown(
        '<div class="small">'
        'Ingénieur Statisticien–Économiste de formation, je me spécialise dans l’analyse de données, la modélisation statistique et l’aide à la décision.<br/><br/>'
        'Mon parcours m’a permis de développer des compétences solides en statistiques appliquées, analyse exploratoire et visualisation de données, avec une attention particulière portée à la compréhension des enjeux business.<br/><br/>'
        'J’aime structurer des problématiques métiers, construire des indicateurs de performance et transformer les résultats en recommandations claires et exploitables.<br/><br/>'
        'Je recherche actuellement une opportunité en Data Analyst ou Business Analyst, afin de continuer à développer mes compétences tout en apportant une réelle valeur ajoutée aux équipes métiers.'
        '</div>',
        unsafe_allow_html=True
    )
    card_close()

elif page == "Projets":
    st.subheader("Projets")
    st.caption("Sélection de projets académiques et professionnels orientés data, business et finance.")

    left, right = st.columns(2, gap="large")

    with left:
        card_open()
        st.markdown("### 📌 Projet 1 — Prédiction de la rétention d’abonnés fibre (Machine Learning)")
        badges(["Python", "Pandas", "Scikit-learn"], "green")
        badges(["Classification", "EDA", "Business Impact"], "purple")
        st.markdown("**Contexte :** rétention = enjeu stratégique en télécom.")
        st.markdown("**Objectif :** identifier les clients à risque de suspension / résiliation pour cibler la rétention.")
        st.markdown("**Méthodes :** nettoyage, EDA, feature engineering, classification, évaluation.")
        st.markdown("**Résultat :** variables clés (ancienneté, usage, incidents) + recommandations actionnables.")
        card_close()

    with right:
        card_open()
        st.markdown("### 📌 Projet 2 — Déterminants de la pauvreté des exploitants agricoles (UEMOA, 2021)")
        badges(["Stata", "Économétrie"], "green")
        badges(["Data socio-éco", "Politiques publiques"], "purple")
        st.markdown("**Contexte :** enjeu majeur de pauvreté rurale en zone UEMOA.")
        st.markdown("**Objectif :** identifier les facteurs associés à la pauvreté pour éclairer la décision publique.")
        st.markdown("**Méthodes :** préparation des bases, descriptif, estimation économétrique, interprétation.")
        st.markdown("**Livrable :** synthèse des résultats + recommandations orientées action.")
        card_close()

    with left:
        card_open()
        st.markdown("### 📌 Projet 3 — Gestion et optimisation d’un portefeuille actions / obligations")
        badges(["Finance", "Risque"], "green")
        badges(["Allocation d’actifs", "Excel avancé"], "purple")
        st.markdown("**Objectif :** construire une allocation mixte optimisant la performance ajustée au risque.")
        st.markdown("**Méthodes :** analyse rendement/risque, sensibilité aux taux, optimisation, reporting.")
        st.markdown("**Résultat :** amélioration du couple rendement/risque + recommandations d’ajustement.")
        card_close()

    with right:
        card_open()
        st.markdown("### 📌 Projet 4 — Analyse de la satisfaction du restaurant de l’ENSEA (ACP)")
        badges(["Statistiques", "ACP"], "green")
        badges(["Alpha de Cronbach", "DataViz"], "purple")
        st.markdown("**Objectif :** mesurer la satisfaction et identifier les axes d’amélioration prioritaires.")
        st.markdown("**Méthodes :** indicateurs, ACP, fiabilité interne, visualisation, recommandations.")
        st.markdown("**Résultat :** indicateur global fiable + priorités d’amélioration.")
        card_close()

elif page == "Compétences":
    st.subheader("Compétences")

    c1, c2 = st.columns(2, gap="large")
    with c1:
        card_open()
        st.markdown("### 📊 Data & Statistiques")
        badges(["EDA", "Régression", "Séries temporelles", "ACP"], "green")
        st.markdown(
            "- Analyse exploratoire des données (EDA)\n"
            "- Statistiques descriptives et inférentielles\n"
            "- Régression, classification, clustering\n"
            "- Séries temporelles\n"
            "- ACP, fiabilité (alpha de Cronbach)"
        )
        card_close()

        card_open()
        st.markdown("### 🧠 Économétrie & Politiques publiques")
        badges(["Stata", "Modélisation", "Interprétation"], "purple")
        st.markdown(
            "- Modélisation économétrique appliquée\n"
            "- Analyse des déterminants socio-économiques\n"
            "- Interprétation des résultats et recommandations"
        )
        card_close()

    with c2:
        card_open()
        st.markdown("### 🤖 Machine Learning")
        badges(["Scikit-learn", "Classification", "Feature engineering"], "green")
        st.markdown(
            "- Préparation et nettoyage des données\n"
            "- Feature engineering\n"
            "- Modèles de classification (churn / rétention)\n"
            "- Évaluation des performances des modèles"
        )
        card_close()

        card_open()
        st.markdown("### 💼 Business & Finance")
        badges(["KPI", "Reporting", "Risque", "Allocation"], "purple")
        st.markdown(
            "- Analyse de KPI et reporting\n"
            "- Aide à la décision\n"
            "- Gestion et optimisation de portefeuille\n"
            "- Analyse du risque et sensibilité aux taux"
        )
        card_close()

    st.markdown("### 🛠️ Outils & technologies")
    card_open()
    badges(["Python", "R", "SQL", "Power BI", "Tableau", "Excel"], "green")
    st.markdown(
        "- **Langages :** Python, R, SQL\n"
        "- **Data & ML :** Pandas, NumPy, Scikit-learn\n"
        "- **BI & Dataviz :** Power BI, Tableau, Excel avancé\n"
        "- **Stats & éco :** Stata, SPSS, EViews\n"
        "- **Autres :** VS Code, Git (bases)"
    )
    card_close()

elif page == "CV":
    st.subheader("📄 Curriculum Vitae")

    c1, c2 = st.columns([2, 1], gap="large")
    with c1:
        card_open()
        st.markdown('<div class="small">Vous pouvez consulter ou télécharger mon CV ci-dessous.</div>', unsafe_allow_html=True)
        card_close()
    with c2:
        card_open()
        cv_path = Path("CV_ISE_KOUAME_ATTA.pdf")
        if cv_path.exists():
            with open(cv_path, "rb") as file:
                st.download_button(
                    label="⬇️ Télécharger mon CV (PDF)",
                    data=file,
                    file_name="CV_ISE_KOUAME_ATTA.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
        else:
            st.error("Fichier introuvable : CV_ISE_KOUAME_ATTA.pdf")
        card_close()

elif page == "Contact":
    st.subheader("📬 Contact")
    st.caption("Disponible pour opportunités, collaborations et échanges professionnels.")

    c1, c2 = st.columns(2, gap="large")

    with c1:
        card_open()
        st.markdown("### 📧 Email")
        st.markdown("[attajeremiek@gmail.com](mailto:attajeremiek@gmail.com)")
        st.markdown("### 📍 Localisation")
        st.markdown('<div class="small">Abidjan, Côte d’Ivoire</div>', unsafe_allow_html=True)
        card_close()

    with c2:
        card_open()
        st.markdown("### 📱 Téléphone")
        st.markdown(
            "- [+225 07 79 01 08 72](tel:+2250779010872)\n"
            "- [+225 01 72 66 68 99](tel:+2250172666899)\n"
            "- [+225 07 89 25 29 67](tel:+2250789252967)"
        )
        st.markdown("### 💼 LinkedIn")
        st.markdown("[atta-jérémie-kouame](https://www.linkedin.com)")
        card_close()
