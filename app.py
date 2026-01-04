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

/* TOP BAR */
.topbar{
  display:flex;
  align-items:center;
  justify-content:space-between;
  padding: 0.85rem 1rem;
  border: 1px solid rgba(37,99,235,0.20);
  border-radius: 16px;
  background: linear-gradient(135deg,
      rgba(37,99,235,0.12) 0%,
      rgba(16,185,129,0.10) 55%,
      rgba(99,102,241,0.10) 100%);
  box-shadow: 0 10px 30px rgba(2,6,23,0.06);
  margin-bottom: 1rem;
}
.topbar-left{ display:flex; gap:.6rem; align-items:center; }
.topbar-title{ font-weight:700; color: rgba(17,24,39,0.92); letter-spacing:-0.2px; }
.dot{
  width:10px; height:10px; border-radius:999px;
  background: rgba(16,185,129,0.95);
  box-shadow: 0 0 0 4px rgba(16,185,129,0.18);
}
.topbar-right{ display:flex; gap:.5rem; flex-wrap:wrap; justify-content:flex-end; }
.pill{
  display:inline-flex; align-items:center;
  padding: .28rem .65rem;
  border-radius: 999px;
  border: 1px solid rgba(148,163,184,0.35);
  background: rgba(255,255,255,0.55);
  color: rgba(17,24,39,0.75);
  font-size: .85rem;
}

/* FOOTER */
.footer{
  margin-top: 1.6rem;
  padding: 1rem 1rem;
  border-top: 1px solid rgba(148,163,184,0.35);
  display:flex;
  align-items:center;
  justify-content:space-between;
  color: rgba(17,24,39,0.65);
  font-size: 0.9rem;
}
.footer-links{ display:flex; gap:.5rem; align-items:center; flex-wrap:wrap; }
.footer a{
  color: rgba(37,99,235,0.85);
  text-decoration: none;
  font-weight: 600;
}
.footer a:hover{ text-decoration: underline; }

/* TIMELINE */
.timeline{
  position: relative;
  margin: 0.6rem 0 1.2rem 0;
  padding-left: 1.2rem;
}
.timeline:before{
  content:"";
  position:absolute;
  left: 6px;
  top: 6px;
  bottom: 6px;
  width: 2px;
  background: linear-gradient(180deg, rgba(37,99,235,0.55), rgba(16,185,129,0.55));
  border-radius: 999px;
}

.titem{
  position: relative;
  margin: 0.9rem 0;
  padding: 0.85rem 0.95rem 0.85rem 0.95rem;
  border: 1px solid rgba(37,99,235,0.18);
  border-radius: 16px;
  background: linear-gradient(135deg,
      rgba(37,99,235,0.10) 0%,
      rgba(16,185,129,0.08) 55%,
      rgba(99,102,241,0.08) 100%);
  box-shadow: 0 10px 24px rgba(2,6,23,0.06);
}

.tdot{
  position:absolute;
  left: -1.2rem;
  top: 1.05rem;
  width: 14px;
  height: 14px;
  border-radius: 999px;
  background: rgba(16,185,129,0.95);
  box-shadow: 0 0 0 5px rgba(16,185,129,0.18);
}

.tdate{
  font-size: 0.85rem;
  color: rgba(17,24,39,0.65);
  margin-bottom: 0.2rem;
}
.ttitle{
  font-weight: 800;
  color: rgba(17,24,39,0.92);
  margin-bottom: 0.2rem;
  letter-spacing: -0.2px;
}
.tmeta{
  font-size: 0.9rem;
  color: rgba(17,24,39,0.72);
  margin-bottom: 0.35rem;
}
.tdesc{
  font-size: 0.95rem;
  color: rgba(17,24,39,0.70);
  line-height: 1.55;
}


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
page = st.sidebar.radio("Navigation", ["Accueil", "À propos","Parcours", "Projets", "Compétences", "CV", "Contact"])
st.sidebar.divider()
st.sidebar.caption("© Atta Jérémie KOUAME")

# ------------------ TOP BAR ------------------
st.markdown("""
<div class="topbar">
  <div class="topbar-left">
    <span class="dot"></span>
    <span class="topbar-title">Portfolio</span>
  </div>
  <div class="topbar-right">
    <span class="pill">📍 Abidjan</span>
    <span class="pill">📊 Data Analyst • Business Analyst</span>
    <span class="pill">✅ Disponible</span>
  </div>
</div>
""", unsafe_allow_html=True)


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
    badges(["Data Analyst", "Business Analyst"], "green")
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
    

    # ================== PARCOURS PROFESSIONNEL ==================
elif page == "Parcours":
    st.subheader("📌 Parcours")

    # --------- TIMELINE SCOLAIRE ----------
    st.markdown("## 🎓 Parcours académique")
    card_open()
    st.markdown("""
    <div class="timeline">
      <div class="titem">
        <span class="tdot"></span>
        <div class="tdate">Année – Année</div>
        <div class="ttitle">Ingénieur Statisticien – Économiste</div>
        <div class="tmeta">ENSEA • Abidjan</div>
        <div class="tdesc">
          Statistiques appliquées, économétrie, data analysis, visualisation, méthodes quantitatives.
          Projets académiques orientés business, développement et finance.
        </div>
      </div>

      <div class="titem">
        <span class="tdot"></span>
        <div class="tdate">En continu</div>
        <div class="ttitle">Auto-formation Data & BI</div>
        <div class="tmeta">Python • Power BI • Tableau • SQL</div>
        <div class="tdesc">
          Approfondissement des compétences en data analytics, KPI, reporting, dashboards et machine learning.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    card_close()

    # --------- TIMELINE PRO ----------
    st.markdown("## 💼 Parcours professionnel")
    card_open()
    st.markdown("""
    <div class="timeline">
      <div class="titem">
        <span class="tdot"></span>
        <div class="tdate">Projet</div>
        <div class="ttitle">Data Analyst — Prédiction rétention / churn (Télécom)</div>
        <div class="tmeta">Python • ML • KPI</div>
        <div class="tdesc">
          Préparation des données, EDA, feature engineering, classification.
          Objectif : identifier les clients à risque et proposer des actions de rétention.
        </div>
      </div>

      <div class="titem">
        <span class="tdot"></span>
        <div class="tdate">Projet</div>
        <div class="ttitle">Économétrie — Déterminants de la pauvreté (UEMOA, 2021)</div>
        <div class="tmeta">Stata • Analyse socio-économique</div>
        <div class="tdesc">
          Structuration des bases, estimation économétrique, interprétation et recommandations
          pour appuyer la décision publique.
        </div>
      </div>

      <div class="titem">
        <span class="tdot"></span>
        <div class="tdate">Projet</div>
        <div class="ttitle">Finance — Optimisation portefeuille actions / obligations</div>
        <div class="tmeta">Excel avancé • Risk/Return</div>
        <div class="tdesc">
          Analyse rendement/risque, allocation d’actifs, sensibilité aux taux et reporting.
        </div>
      </div>

      <div class="titem">
        <span class="tdot"></span>
        <div class="tdate">Projet</div>
        <div class="ttitle">Statistiques — Satisfaction restaurant ENSEA (ACP)</div>
        <div class="tmeta">ACP • Alpha de Cronbach • DataViz</div>
        <div class="tdesc">
          Construction d’un indicateur de satisfaction, analyse multivariée et recommandations d’amélioration.
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    card_close()

    st.info("🎯 Objectif : intégrer une équipe data en tant que **Data Analyst** ou **Business Analyst** et générer un impact métier mesurable.")



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
    import requests

    st.subheader("📬 Contact")
    st.caption("Disponible pour opportunités, collaborations et échanges professionnels.")

    c1, c2 = st.columns(2, gap="large")

    # --- Infos ---
    with c1:
        card_open()
        st.markdown("### 📧 Email")
        st.markdown("[attajeremiek@gmail.com](mailto:attajeremiek@gmail.com)")

        st.markdown("### 📱 Téléphone")
        st.markdown(
            "- [+225 07 79 01 08 72](tel:+2250779010872)\n"
            "- [+225 01 72 66 68 99](tel:+2250172666899)\n"
            "- [+225 07 89 25 29 67](tel:+2250789252967)"
        )

        st.markdown("### 📍 Localisation")
        st.markdown('<div class="small">Abidjan, Côte d’Ivoire</div>', unsafe_allow_html=True)

        st.markdown("### 💼 LinkedIn")
        st.markdown("[atta-jérémie-kouame](https://www.linkedin.com)")
        card_close()

    # --- Formulaire (envoi automatique via Formspree) ---
    with c2:
        card_open()
        st.markdown("### ✉️ Envoyer un message")

        with st.form("contact_form", clear_on_submit=True):
            nom = st.text_input("Nom complet *", placeholder="Ex: KOUAME Atta Jérémie")
            email = st.text_input("Email *", placeholder="Ex: nom@gmail.com")
            message = st.text_area("Message *", height=140, placeholder="Votre message...")
            submitted = st.form_submit_button("📨 Envoyer")

        if submitted:
            if not nom.strip() or not email.strip() or not message.strip():
                st.error("Veuillez remplir tous les champs obligatoires (*) avant d’envoyer.")
            elif "@" not in email or "." not in email:
                st.error("Veuillez entrer une adresse email valide.")
            else:
                endpoint = "https://formspree.io/f/mqeawbbk"  # <-- remplace par ton vrai endpoint

                payload = {
                    "name": nom,
                    "email": email,
                    "message": message,
                    "_subject": f"Nouveau message Portfolio - {nom}",
                }

                try:
                    r = requests.post(
                        endpoint,
                        data=payload,
                        headers={"Accept": "application/json"},
                        timeout=15,
                    )

                    if r.status_code in (200, 201):
                        st.success("✅ Message envoyé ! Je l’ai bien reçu par email.")
                    else:
                        st.error("❌ Envoi échoué. Réessaie ou contacte-moi directement par email.")
                        st.code(f"Status: {r.status_code}\nRéponse: {r.text}")

                except requests.exceptions.RequestException as e:
                    st.error("❌ Problème réseau pendant l’envoi. Réessaie dans quelques secondes.")
                    st.code(str(e))

        st.caption("🔒 Envoi automatique vers ma boîte email via Formspree.")
        card_close()



# ------------------ FOOTER ------------------
st.markdown("""
<div class="footer">
  <div>© 2026 • Atta Jérémie KOUAME</div>
  <div class="footer-links">
    <a href="mailto:attajeremiek@gmail.com">Email</a>
    <span>•</span>
    <a href="https://www.linkedin.com" target="_blank">LinkedIn</a>
    <span>•</span>
    <a href="https://github.com" target="_blank">GitHub</a>
  </div>
</div>
""", unsafe_allow_html=True)
