import streamlit as st
from random import seed, randint

# ── CONFIG ──────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Chiffreur Secret",
    page_icon="🔐",
    layout="centered"
)

# ── CSS ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Oxanium:wght@400;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Oxanium', sans-serif;
    background-color: #0a0a0f;
    color: #e0e0e0;
}

.stApp {
    background: radial-gradient(ellipse at top, #0d1b2a 0%, #0a0a0f 70%);
    min-height: 100vh;
}

h1 {
    font-family: 'Oxanium', sans-serif;
    font-weight: 800;
    font-size: 2.8rem;
    text-align: center;
    background: linear-gradient(90deg, #00d4ff, #7b2fff, #00d4ff);
    background-size: 200%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shine 3s linear infinite;
    letter-spacing: 0.05em;
    margin-bottom: 0;
}

@keyframes shine {
    0% { background-position: 0% }
    100% { background-position: 200% }
}

.subtitle {
    text-align: center;
    color: #5a6a7a;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.85rem;
    letter-spacing: 0.2em;
    margin-top: 0.2rem;
    margin-bottom: 2rem;
}

.result-box {
    background: linear-gradient(135deg, #0d1b2a, #111827);
    border: 1px solid #00d4ff33;
    border-left: 4px solid #00d4ff;
    border-radius: 8px;
    padding: 1.5rem 2rem;
    margin-top: 1.5rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 1.4rem;
    color: #00d4ff;
    letter-spacing: 0.15em;
    box-shadow: 0 0 30px #00d4ff15;
    text-align: center;
    word-break: break-all;
}

.result-label {
    font-size: 0.7rem;
    color: #5a6a7a;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-bottom: 0.5rem;
}

.error-box {
    background: #1a0a0a;
    border: 1px solid #ff4444;
    border-left: 4px solid #ff4444;
    border-radius: 8px;
    padding: 1rem 1.5rem;
    color: #ff6666;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.9rem;
    margin-top: 1rem;
}

.stTextInput > div > div > input,
.stSelectbox > div > div {
    background: #0d1b2a !important;
    border: 1px solid #1e3a5f !important;
    border-radius: 6px !important;
    color: #e0e0e0 !important;
    font-family: 'Share Tech Mono', monospace !important;
}

.stTextInput > div > div > input:focus {
    border-color: #00d4ff !important;
    box-shadow: 0 0 0 1px #00d4ff44 !important;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #0d2b45, #1a1040);
    border: 1px solid #00d4ff55;
    color: #00d4ff;
    font-family: 'Oxanium', sans-serif;
    font-weight: 700;
    font-size: 1rem;
    letter-spacing: 0.15em;
    padding: 0.75rem;
    border-radius: 6px;
    transition: all 0.2s;
    margin-top: 0.5rem;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #0d3a5f, #2a1060);
    border-color: #00d4ff;
    box-shadow: 0 0 20px #00d4ff33;
    transform: translateY(-1px);
}

.stRadio > div {
    background: #0d1b2a;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    border: 1px solid #1e3a5f;
}

label {
    color: #ffffff; !important;
    font-size: 0.8rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
}

.divider {
    border: none;
    border-top: 1px solid #1e3a5f;
    margin: 2rem 0;
}

.info-tag {
    display: inline-block;
    background: #0d2b45;
    border: 1px solid #00d4ff33;
    border-radius: 4px;
    padding: 0.2rem 0.6rem;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.75rem;
    color: #00d4ff88;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# ── FONCTIONS ────────────────────────────────────────────────────────────────
alp = "abcdefghijklmnopqrstuvwxyz "

def generer_indices(mot, cle_int):
    indices = list(range(len(mot)))
    seed(cle_int)
    i = len(indices) - 1
    while i > 0:
        j = randint(0, i)
        indices[i], indices[j] = indices[j], indices[i]
        i -= 1
    return indices

def chiffrer(mot, cle):
    indices = generer_indices(mot, int(cle))
    res = [""] * len(mot)
    for i, l in enumerate(mot):
        if l.lower() in alp:
            dec = int(cle[i % 8])
            idx = alp.index(l.lower())
            nl = alp[(idx + dec) % 27]
            res[indices[i]] = nl
        else:
            res[indices[i]] = l
    return "".join(res)

def dechiffrer(mot, cle):
    indices = generer_indices(mot, int(cle))
    res = [""] * len(mot)
    for i, l in enumerate(mot):
        if mot[indices[i]] == " ":
            res[i] = " "
        elif mot[indices[i]].lower() in alp:
            dec = int(cle[i % 8])
            idx = alp.index(mot[indices[i]].lower())
            nl = alp[(idx - dec) % 27]
            res[i] = nl
        else:
            res[i] = mot[indices[i]]
    return "".join(res)

# ── INTERFACE ────────────────────────────────────────────────────────────────
st.markdown("<h1>🔐 CHIFFREUR SECRET</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">CHIFFREMENT DE MESSAGE PAR RP31</p>', unsafe_allow_html=True)
st.markdown('<span class="info-tag">Compatible TI-83 Premium CE · Clé 8 chiffres</span>', unsafe_allow_html=True)

mode = st.radio("Mode", ["🔒 Chiffrer", "🔓 Déchiffrer"], horizontal=True)
cle = st.text_input("Clé secrète (8 chiffres)", max_chars=8, placeholder="ex: 12345678")
mot = st.text_input("Message", placeholder="Entrez votre message...")

if st.button("⚡ EXÉCUTER"):
    if len(cle) != 8 or not cle.isdigit():
        st.markdown('<div class="error-box">⚠ La clé doit contenir exactement 8 chiffres !</div>', unsafe_allow_html=True)
    elif not mot:
        st.markdown('<div class="error-box">⚠ Entrez un message !</div>', unsafe_allow_html=True)
    else:
        if "Chiffrer" in mode:
            resultat = chiffrer(mot, cle)
            label = "MESSAGE CHIFFRÉ"
        else:
            resultat = dechiffrer(mot, cle)
            label = "MESSAGE DÉCHIFFRÉ"

        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">{label}</div>
            {resultat}
        </div>
        """, unsafe_allow_html=True)
