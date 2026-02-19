import streamlit as st
from PIL import Image
import base64
import json
import requests
from streamlit_lottie import st_lottie

# PAGE CONFIG
st.set_page_config(
    page_title="Justin Andry N. Diva | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)


# LOTTIE HELPERS
@st.cache_data
def load_lottie_url(url: str):
    """Fetch a Lottie animation JSON from a URL."""
    try:
        r = requests.get(url, timeout=5)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None


# Pre-load animations
lottie_coding = load_lottie_url("https://lottie.host/f4ee3c3c-4dba-41a8-bc9c-4f8dfc34da01/AsjRUVoZuf.json")
lottie_contact = load_lottie_url("https://lottie.host/2a61a039-85ff-4e15-8057-2b69f3e31253/cqPXhFrfQg.json")
lottie_education = load_lottie_url("https://lottie.host/9e148595-e06c-4a14-8ece-b8a498615b4d/h2MHiTXBK8.json")
lottie_cert = load_lottie_url("https://lottie.host/5fba1a3b-5596-4768-98fb-1a3d16162498/bZxfb1nSNE.json")


# IMAGE HELPERS
@st.cache_data
def get_image_base64(image_path: str) -> str:
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()



# CSS
st.markdown("""
<style>
/* ─── Fonts ─── */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap');

/* ─── Root Variables ─── */
:root {
    --primary: #8B5CF6;
    --primary-light: #A78BFA;
    --primary-dark: #6D28D9;
    --accent: #06D6A0;
    --accent2: #F72585;
    --bg-dark: #06060E;
    --bg-card: rgba(15, 15, 30, 0.6);
    --bg-card-hover: rgba(25, 25, 50, 0.8);
    --glass-border: rgba(139, 92, 246, 0.12);
    --text-primary: #F1F0FB;
    --text-secondary: #A1A1C7;
    --text-muted: #6E6E8A;
    --gradient-1: linear-gradient(135deg, #8B5CF6 0%, #06D6A0 100%);
    --gradient-2: linear-gradient(135deg, #F72585 0%, #8B5CF6 100%);
    --gradient-3: linear-gradient(135deg, #06D6A0 0%, #3B82F6 100%);
}

/* ─── Global ─── */
html, body { font-family: 'Outfit', sans-serif; }
p, h1, h2, h3, h4, h5, h6, div, li, a, label, input, textarea, select, button {
    font-family: 'Outfit', sans-serif;
}

.stApp {
    background: var(--bg-dark);
    background-image:
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(139,92,246,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 60%, rgba(6,214,160,0.06) 0%, transparent 50%),
        radial-gradient(ellipse 50% 50% at 20% 80%, rgba(247,37,133,0.05) 0%, transparent 50%);
}

/* ─── Hide Streamlit default ─── */
#MainMenu, footer { visibility: hidden; }
.stDeployButton { display: none; }
header[data-testid="stHeader"] { background: transparent !important; }

/* ─── Animated Background Orbs (decorative) ─── */
.orb-bg {
    position: fixed; top: 0; left: 0; width: 100%; height: 100%;
    pointer-events: none; z-index: 0; overflow: hidden;
}
.orb {
    position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.15;
    animation: float 20s ease-in-out infinite;
}
.orb-1 { width: 500px; height: 500px; background: #8B5CF6; top: -10%; left: -5%; animation-delay: 0s; }
.orb-2 { width: 400px; height: 400px; background: #06D6A0; bottom: -10%; right: -5%; animation-delay: -7s; }
.orb-3 { width: 350px; height: 350px; background: #F72585; top: 50%; left: 50%; animation-delay: -14s; }

@keyframes float {
    0%, 100% { transform: translate(0, 0) scale(1); }
    25% { transform: translate(30px, -40px) scale(1.05); }
    50% { transform: translate(-20px, 20px) scale(0.95); }
    75% { transform: translate(15px, 35px) scale(1.02); }
}

/* ─── Section Titles ─── */
.section-tag {
    display: inline-block;
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.25);
    color: var(--primary-light);
    padding: 0.3rem 1rem;
    border-radius: 30px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}
.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.6rem;
    font-weight: 800;
    color: var(--text-primary);
    line-height: 1.15;
    margin-bottom: 0.4rem;
}
.section-title .gradient-text {
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.section-title .gradient-text-2 {
    background: var(--gradient-2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.section-title .gradient-text-3 {
    background: var(--gradient-3);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.section-desc {
    color: var(--text-secondary);
    font-size: 0.95rem;
    line-height: 1.6;
    max-width: 550px;
}
.center-text { text-align: center; }
.center-text .section-desc { margin: 0 auto; }

/* ─── Hero ─── */
.hero-wrap {
    text-align: center;
    padding: 3rem 1rem 1rem;
    position: relative;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.2);
    color: var(--primary-light);
    padding: 0.4rem 1.2rem;
    border-radius: 30px;
    font-size: 0.82rem;
    font-weight: 500;
    margin-bottom: 1.5rem;
    animation: fadeInDown 0.8s ease;
}
.hero-badge .dot {
    width: 8px; height: 8px;
    background: var(--accent);
    border-radius: 50%;
    animation: pulse 2s ease-in-out infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.3); }
}
.hero-img {
    width: 160px; height: 160px;
    border-radius: 50%;
    border: 3px solid rgba(139,92,246,0.4);
    box-shadow: 0 0 40px rgba(139,92,246,0.2), 0 0 80px rgba(139,92,246,0.08);
    object-fit: cover;
    margin-bottom: 1.5rem;
    animation: fadeIn 1s ease;
}
.hero-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3.2rem;
    font-weight: 900;
    color: var(--text-primary);
    line-height: 1.1;
    margin-bottom: 0.5rem;
    animation: fadeInUp 0.8s ease;
}
.hero-role {
    font-size: 1.15rem;
    font-weight: 600;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
    animation: fadeInUp 1s ease;
}
.hero-bio {
    color: var(--text-secondary);
    font-size: 1rem;
    max-width: 560px;
    margin: 0 auto 2rem;
    line-height: 1.7;
    animation: fadeInUp 1.2s ease;
}

/* ─── Animations ─── */
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fadeInDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }

/* ─── Glass Cards ─── */
.glass {
    background: var(--bg-card);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 1.8rem;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    position: relative;
    overflow: hidden;
}
.glass::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(139,92,246,0.4), transparent);
}
.glass:hover {
    background: var(--bg-card-hover);
    border-color: rgba(139,92,246,0.25);
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(139,92,246,0.08);
}

/* ─── Stat Cards ─── */
.stat-card {
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s ease;
}
.stat-card:hover {
    border-color: rgba(139,92,246,0.35);
    transform: translateY(-4px);
}
.stat-number {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
    margin-bottom: 0.3rem;
}
.stat-label {
    color: var(--text-muted);
    font-size: 0.85rem;
    font-weight: 500;
}

/* ─── Skill Bars (custom animated) ─── */
.skill-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.2rem;
}
.skill-name { color: var(--text-primary); font-weight: 500; font-size: 0.9rem; }
.skill-pct { color: var(--primary-light); font-weight: 600; font-size: 0.85rem; }
.skill-bar-bg {
    width: 100%;
    height: 8px;
    background: rgba(139,92,246,0.1);
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 1rem;
}
.skill-bar-fill {
    height: 100%;
    border-radius: 10px;
    background: var(--gradient-1);
    transition: width 1.5s cubic-bezier(0.165, 0.84, 0.44, 1);
}

/* ─── Project Cards ─── */
.project-glass {
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
    padding: 2rem;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    min-height: 280px;
}
.project-glass::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 100%; height: 3px;
    background: var(--gradient-1);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.4s ease;
}
.project-glass:hover::after { transform: scaleX(1); }
.project-glass:hover {
    border-color: rgba(139,92,246,0.3);
    transform: translateY(-6px);
    box-shadow: 0 16px 32px rgba(0,0,0,0.3);
}
.proj-type {
    display: inline-block;
    padding: 0.25rem 0.8rem;
    border-radius: 20px;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 1rem;
}
.proj-type.academic { background: rgba(139,92,246,0.15); color: var(--primary-light); }
.proj-type.personal { background: rgba(6,214,160,0.12); color: var(--accent); }
.proj-title {
    font-family: 'Space Grotesk', sans-serif;
    color: var(--text-primary);
    font-size: 1.2rem;
    font-weight: 700;
    margin-bottom: 0.6rem;
}
.proj-desc {
    color: var(--text-secondary);
    font-size: 0.88rem;
    line-height: 1.6;
    margin-bottom: 1rem;
}
.tech-chip {
    display: inline-block;
    background: rgba(139,92,246,0.08);
    border: 1px solid rgba(139,92,246,0.15);
    color: var(--text-secondary);
    padding: 0.2rem 0.6rem;
    border-radius: 6px;
    font-size: 0.75rem;
    font-weight: 500;
    margin: 0.15rem;
}

/* ─── Timeline ─── */
.timeline-item {
    position: relative;
    padding-left: 2.5rem;
    padding-bottom: 2rem;
    border-left: 2px solid rgba(139,92,246,0.2);
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: -7px; top: 4px;
    width: 12px; height: 12px;
    background: var(--primary);
    border-radius: 50%;
    box-shadow: 0 0 12px rgba(139,92,246,0.4);
}
.timeline-date {
    color: var(--primary-light);
    font-size: 0.8rem;
    font-weight: 600;
    margin-bottom: 0.3rem;
}
.timeline-title {
    color: var(--text-primary);
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
}
.timeline-sub {
    color: var(--text-secondary);
    font-size: 0.88rem;
}

/* ─── Certificate Cards ─── */
.cert-glass {
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 16px;
    padding: 1.5rem;
    text-align: center;
    transition: all 0.3s ease;
    min-height: 150px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.cert-glass:hover {
    transform: translateY(-5px);
    border-color: rgba(139,92,246,0.3);
    box-shadow: 0 12px 24px rgba(0,0,0,0.25);
}
.cert-icon { font-size: 2.2rem; margin-bottom: 0.6rem; }
.cert-title { color: var(--text-primary); font-weight: 700; font-size: 0.92rem; margin-bottom: 0.3rem; }
.cert-org { color: var(--text-muted); font-size: 0.8rem; }
.cert-year {
    display: inline-block;
    margin-top: 0.5rem;
    background: rgba(139,92,246,0.1);
    color: var(--primary-light);
    padding: 0.15rem 0.7rem;
    border-radius: 30px;
    font-size: 0.72rem;
    font-weight: 600;
}

/* ─── Contact CTA ─── */
.cta-card {
    background: linear-gradient(135deg, rgba(139,92,246,0.15), rgba(6,214,160,0.08));
    border: 1px solid rgba(139,92,246,0.25);
    border-radius: 20px;
    padding: 2.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.cta-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 2px;
    background: var(--gradient-1);
}
.cta-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--text-primary);
    margin-bottom: 0.3rem;
}
.cta-sub {
    color: var(--text-secondary);
    font-size: 0.9rem;
}

/* ─── Contact Info Row ─── */
.contact-info-item {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    padding: 0.8rem 0;
    border-bottom: 1px solid rgba(139,92,246,0.08);
}
.contact-info-item:last-child { border-bottom: none; }
.contact-icon {
    width: 40px; height: 40px;
    background: rgba(139,92,246,0.1);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
}
.contact-label { color: var(--text-muted); font-size: 0.78rem; }
.contact-value { color: var(--text-primary); font-weight: 500; font-size: 0.92rem; }

/* ─── Divider ─── */
.fancy-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, rgba(139,92,246,0.3) 50%, transparent 100%);
    margin: 3.5rem 0;
}

/* ─── Footer ─── */
.footer-wrap {
    text-align: center;
    padding: 2rem 0 1rem;
    border-top: 1px solid rgba(139,92,246,0.1);
    margin-top: 3rem;
}
.footer-wrap p { color: var(--text-muted); font-size: 0.82rem; }
.footer-wrap a { color: var(--primary-light); text-decoration: none; }

/* ─── Streamlit Overrides ─── */
[data-testid="stMetricValue"] {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    background: var(--gradient-1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
[data-testid="stMetricLabel"] {
    color: var(--text-muted) !important;
    font-weight: 500 !important;
}

.stProgress > div > div > div > div {
    background: var(--gradient-1) !important;
    border-radius: 10px;
}

.stTabs [data-baseweb="tab-list"] { gap: 0.5rem; justify-content: center; border-bottom: none !important; }
.stTabs [data-baseweb="tab"] {
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 0.6rem 1.8rem;
    color: var(--text-secondary);
    font-weight: 600;
    font-family: 'Outfit', sans-serif;
}
.stTabs [aria-selected="true"] {
    background: var(--primary) !important;
    color: white !important;
    border-color: var(--primary) !important;
}
.stTabs [data-baseweb="tab-highlight"] { display: none; }
.stTabs [data-baseweb="tab-border"] { display: none; }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #08081A 0%, #0C0C1E 100%);
    border-right: 1px solid rgba(139,92,246,0.1);
}

.stDownloadButton > button,
.stLinkButton > a {
    background: var(--gradient-1) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-family: 'Outfit', sans-serif !important;
    transition: all 0.3s ease !important;
}
.stDownloadButton > button:hover,
.stLinkButton > a:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(139,92,246,0.3) !important;
}

.stFormSubmitButton > button {
    background: var(--gradient-1) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-weight: 700 !important;
    font-family: 'Outfit', sans-serif !important;
    width: 100%;
    padding: 0.7rem !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
}
.stFormSubmitButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(139,92,246,0.3) !important;
}

/* Toggle content panel (replaces expanders) */
.toggle-content {
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 1.5rem;
    margin-top: 0.5rem;
    animation: fadeInUp 0.3s ease;
}
</style>
""", unsafe_allow_html=True)

# Floating orbs background
st.markdown("""
<div class="orb-bg">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
</div>
""", unsafe_allow_html=True)

github_logo_b64 = get_image_base64("assets/github_logo.jpg")

# SIDEBAR
with st.sidebar:
    profile_b64 = get_image_base64("assets/profile.png")
    st.markdown(f"""
    <div style="text-align:center; padding:1.5rem 0 1rem;">
        <img src="data:image/png;base64,{profile_b64}"
             style="width:90px;height:90px;border-radius:50%;
                    border:3px solid rgba(139,92,246,0.4);
                    box-shadow:0 0 25px rgba(139,92,246,0.15);
                    object-fit:cover;margin-bottom:0.8rem;" />
        <h3 style="color:#F1F0FB;font-family:'Space Grotesk',sans-serif;
                   font-weight:800;margin:0;font-size:1.1rem;">Justin Andry N. Diva</h3>
        <p style="background:linear-gradient(135deg,#8B5CF6,#06D6A0);
                  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                  font-weight:600;font-size:0.85rem;margin-top:0.2rem;">
            Software Development Intern
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    page = st.radio(
        "Navigate",
        ["Home", "About Me", "Skills", "Projects",
         "Education", "Certificates", "Contact"],
        label_visibility="collapsed"
    )

    st.divider()
    st.markdown("##### ⚡ Quick Facts")
    st.caption("📍  Cebu City, Philippines")
    st.caption("🎓  CIT-University")
    st.caption("💼  Software Dev Intern")
    st.caption("📅  Graduating 2026")

    st.divider()
    st.markdown("##### 🔗 Socials")
    st.markdown(f'''
    <a href="https://github.com/avid0101" target="_blank" style="
        display:flex;align-items:center;justify-content:center;gap:0.5rem;
        background:var(--gradient-1);color:white;text-decoration:none;
        border-radius:12px;padding:0.5rem 1rem;font-weight:600;
        font-family:'Outfit',sans-serif;font-size:0.9rem;
        transition:all 0.3s ease;">
        <img src="data:image/jpeg;base64,{github_logo_b64}" style="width:20px;height:20px;border-radius:50%;" />
        GitHub
    </a>
    ''', unsafe_allow_html=True)
    st.link_button("LinkedIn", "https://linkedin.com/in/justinandrydiva", use_container_width=True)
    st.link_button("Email Me", "mailto:justinandrydiva@gmail.com", use_container_width=True)


# ME 
if page in ["Home", "About Me"]:
    st.markdown(f"""
    <div class="hero-wrap">
        <div class="hero-badge"><span class="dot"></span> Open to opportunities</div>
        <br/>
        <img class="hero-img" src="data:image/png;base64,{profile_b64}" alt="profile" />
        <div class="hero-name">Justin Andry N. Diva</div>
        <div class="hero-role">Software Development Intern</div>
        <div class="hero-bio">
            Passionate about crafting innovative software solutions and seamless
            user experiences. A 4th-year BSIT student at CIT-University focused on
            full-stack web development and modern technologies.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CTA buttons
    _col1, btn_col, _col2 = st.columns([1.5, 2, 1.5])
    with btn_col:
        b1, b2 = st.columns(2)
        with b1:
            st.markdown(f'''
            <a href="https://github.com/justinandry-diva" target="_blank" style="
                display:flex;align-items:center;justify-content:center;gap:0.5rem;
                background:var(--gradient-1);color:white;text-decoration:none;
                border-radius:12px;padding:0.6rem 1.2rem;font-weight:600;
                font-family:'Outfit',sans-serif;font-size:0.9rem;
                transition:all 0.3s ease;width:100%;box-sizing:border-box;">
                <img src="data:image/jpeg;base64,{github_logo_b64}" style="width:22px;height:22px;border-radius:50%;" />
                GitHub Profile
            </a>
            ''', unsafe_allow_html=True)
        with b2:
            resume_text = """
═══════════════════════════════════════════════
          JUSTIN ANDRY N. DIVA
       Software Development Intern
═══════════════════════════════════════════════

CONTACT
─────────
Email:    justinandrydiva@gmail.com
Phone:    +63 999 510 99223
Location: Cebu City, Philippines

EDUCATION
─────────
BS Information Technology
Cebu Institute of Technology - University
Expected Graduation: 2026

SKILLS
─────────
Frontend:  HTML, CSS, JS, React, Streamlit, Bootstrap, MUI
Backend:   Java Spring Boot, Python, PHP, Node.js, REST APIs
Database:  MySQL, PostgreSQL
Cloud BaaS/PaaS: Firebase, Supabase, Render Cloud Platform
Development Tools: Docker

PROJECTS
─────────
• Software Test Documentation Evaluator
  AI-powered evaluation of software testing docs (OpenAI GPT)
• Boarding House Finder — Cebu City
  Student housing platform with map integration

CERTIFICATES
─────────
• AWS Academy Graduate – Cloud Foundations (2025)
• HCIA Academy – AI in Full Stack (2025)
• HCIA Academy – Cloud Service (2025)
• Intern – Full-Stack Developer (2026)
"""
            st.download_button("📄 Download CV", resume_text, "Justin_Diva_CV.txt", "text/plain", use_container_width=True)

    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)


# ━━━━  ABOUT  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if page in ["Home", "About Me"]:
    about_left, about_right = st.columns([1.2, 1], gap="large")

    with about_left:
        st.markdown('<span class="section-tag">About Me</span>', unsafe_allow_html=True)
        st.markdown("""
        <div class="section-title">Turning ideas into<br/><span class="gradient-text">digital reality</span></div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <p class="section-desc">
        I'm a 4th-year Information Technology student with a strong passion for
        building real-world web applications. I thrive in collaborative environments,
        enjoy solving complex problems, and constantly seek new ways to grow as a developer.
        I'm eager to contribute to impactful projects that push boundaries.
        </p>
        """, unsafe_allow_html=True)
        st.markdown("")

        if st.button("Contact Details", key="btn_contact_details", use_container_width=True):
            st.session_state.show_contact = not st.session_state.get("show_contact", False)
        if st.session_state.get("show_contact", False):
            st.markdown('<div class="toggle-content">', unsafe_allow_html=True)
            st.markdown("📧 **Email:** justinandrydiva@gmail.com")
            st.markdown("📱 **Phone:** +63 999 510 9923")
            st.markdown("📍 **Location:** Cebu City, Philippines")
            st.markdown('</div>', unsafe_allow_html=True)

    with about_right:
        # Lottie animation or stat cards
        if lottie_coding:
            st_lottie(lottie_coding, height=220, key="lottie_hero")

        # 2x2 stat grid
        s1, s2 = st.columns(2)
        s3, s4 = st.columns(2)
        with s1:
            st.markdown('<div class="stat-card"><div class="stat-number">2+</div><div class="stat-label">Projects</div></div>', unsafe_allow_html=True)
        with s2:
            st.markdown('<div class="stat-card"><div class="stat-number">4+</div><div class="stat-label">Certificates</div></div>', unsafe_allow_html=True)
        with s3:
            st.markdown('<div class="stat-card"><div class="stat-number">10+</div><div class="stat-label">Tech Skills</div></div>', unsafe_allow_html=True)
        with s4:
            st.markdown('<div class="stat-card"><div class="stat-number">2026</div><div class="stat-label">Graduation</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)


# ━━━━  SKILLS  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if page in ["Home", "Skills"]:
    st.markdown("""
    <div class="center-text">
        <span class="section-tag">Skills</span>
        <div class="section-title">My <span class="gradient-text">Skillset</span></div>
        <p class="section-desc">Technologies and tools I use to bring ideas to life.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")

    tab_fe, tab_be, tab_db = st.tabs(["🎨 Frontend", "⚙️ Backend", "☁️ Database & Cloud"])

    def render_skill_bar(name, pct, gradient="var(--gradient-1)"):
        st.markdown(f"""
        <div class="skill-row">
            <span class="skill-name">{name}</span>
            <span class="skill-pct">{pct}%</span>
        </div>
        <div class="skill-bar-bg">
            <div class="skill-bar-fill" style="width:{pct}%;background:{gradient};"></div>
        </div>
        """, unsafe_allow_html=True)

    with tab_fe:
        fl, fr = st.columns(2, gap="large")
        with fl:
            render_skill_bar("HTML / CSS", 90)
            render_skill_bar("JavaScript", 80)
            render_skill_bar("React.js", 75)
        with fr:
            render_skill_bar("Streamlit", 50)
            render_skill_bar("Bootstrap / Tailwind", 50)
            render_skill_bar("Material UI / ShadCN", 40)

    with tab_be:
        bl, br = st.columns(2, gap="large")
        with bl:
            render_skill_bar("Java & Spring Boot", 80, "var(--gradient-2)")
            render_skill_bar("Python (Django)", 50, "var(--gradient-2)")
            render_skill_bar("PHP", 50, "var(--gradient-2)")
        with br:
            render_skill_bar("Node.js", 60, "var(--gradient-2)")
            render_skill_bar("RESTful APIs", 78, "var(--gradient-2)")
            render_skill_bar("Git & Version Control", 75, "var(--gradient-2)")

    with tab_db:
        dl, dr = st.columns(2, gap="large")
        with dl:
            render_skill_bar("PostgreSQL", 80, "var(--gradient-3)")
            render_skill_bar("MySQL", 65, "var(--gradient-3)")
            render_skill_bar("Firebase", 40, "var(--gradient-3)")
        with dr:
            render_skill_bar("Docker", 55, "var(--gradient-3)")
            render_skill_bar("Supabase", 72, "var(--gradient-3)")
            render_skill_bar("Render Cloud Platform", 50, "var(--gradient-3)")

    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)


# ━━━━  PROJECTS  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if page in ["Home", "Projects"]:
    st.markdown("""
    <div class="center-text">
        <span class="section-tag">Portfolio</span>
        <div class="section-title">Featured <span class="gradient-text-2">Projects</span></div>
        <p class="section-desc">A selection of work showcasing my software development experience.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")

    p1, p2 = st.columns(2, gap="large")

    with p1:
        st.markdown("""
        <div class="project-glass">
            <span class="proj-type academic">Academic</span>
            <div class="proj-title">Software Test Documentation Evaluator</div>
            <div class="proj-desc">
                A full-stack AI-powered system that automates the evaluation of
                software testing documentation using OpenAI GPT. Features Google
                Drive integration, classroom management, and automated scoring.
            </div>
            <div>
                <span class="tech-chip">React.js</span>
                <span class="tech-chip">Spring Boot</span>
                <span class="tech-chip">OpenAI GPT</span>
                <span class="tech-chip">MySQL</span>
                <span class="tech-chip">Google Drive API</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("More Details", key="btn_proj1_details", use_container_width=True):
            st.session_state.show_proj1 = not st.session_state.get("show_proj1", False)
        if st.session_state.get("show_proj1", False):
            st.markdown('<div class="toggle-content">', unsafe_allow_html=True)
            st.markdown("""
            - **Role:** Full-stack Developer
            - **Challenge:** Automating evaluation of student-submitted STDs
            - **Solution:** Integrated OpenAI GPT for intelligent document analysis
            - **Impact:** Reduced manual evaluation time by ~80%
            """)
            st.link_button("View Repository", "https://github.com/justinandry-diva", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with p2:
        st.markdown("""
        <div class="project-glass">
            <span class="proj-type personal">Personal</span>
            <div class="proj-title">Boarding House Finder for Students in Cebu City</div>
            <div class="proj-desc">
                A web application that helps college students find affordable and
                convenient boarding houses near universities in Cebu City. Includes
                interactive map integration, filters, and reviews.
            </div>
            <div>
                <span class="tech-chip">HTML / CSS</span>
                <span class="tech-chip">React</span>
                <span class ="tech-chip">PostgresSQL(Local)</span>
                <span class="tech-chip">Supabase</span>
                <span class="tech-chip">Maps API</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("More Details", key="btn_proj2_details", use_container_width=True):
            st.session_state.show_proj2 = not st.session_state.get("show_proj2", False)
        if st.session_state.get("show_proj2", False):
            st.markdown('<div class="toggle-content">', unsafe_allow_html=True)
            st.markdown("""
            - **Role:** Solo Developer
            - **Challenge:** Helping students find suitable housing easily
            - **Solution:** Search & filter with interactive map integration
            - **Impact:** Makes the boarding house hunt simpler for students
            """)
            st.link_button("View Repository", "https://github.com/justinandry-diva", use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)


#EDUCATION 
if page in ["Home", "Education"]:
    edu_left, edu_right = st.columns([1, 1.2], gap="large")

    with edu_left:
        st.markdown('<span class="section-tag">Education</span>', unsafe_allow_html=True)
        st.markdown("""
        <div class="section-title">My <span class="gradient-text-3">Education</span></div>
        """, unsafe_allow_html=True)
        st.markdown("")

        if lottie_education:
            st_lottie(lottie_education, height=200, key="lottie_edu")

    with edu_right:
        st.markdown("")
        st.markdown("")

        st.markdown("""
        <div class="timeline-item">
            <div class="timeline-date">2022 — 2026 (Expected)</div>
            <div class="timeline-title">Bachelor of Science in Information Technology</div>
            <div class="timeline-sub">Cebu Institute of Technology - University (CIT-U)</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🎓 Academic Highlights", key="btn_academic", use_container_width=True):
            st.session_state.show_academic = not st.session_state.get("show_academic", False)
        if st.session_state.get("show_academic", False):
            st.markdown('<div class="toggle-content">', unsafe_allow_html=True)
            st.metric("Track", "Software Dev")
            st.markdown("")
            st.markdown("**Key Coursework:**")
            st.markdown("""
            - Web Application Development
            - Database Management Systems
            - Quality Assurance
            - Object-Oriented Programming
            """)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)


# ━━━━  CERTIFICATES  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if page in ["Home", "Certificates"]:
    st.markdown("""
    <div class="center-text">
        <span class="section-tag">Achievements</span>
        <div class="section-title">Training & <span class="gradient-text">Certificates</span></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")

    certs = [
        ("🏆", "AWS Academy Graduate", "Cloud Foundations", "2025"),
        ("🤖", "HCIA — AI in Full Stack", "Huawei ICT Academy", "2025"),
        ("☁️", "HCIA — Cloud Service", "Huawei ICT Academy", "2025"),
        ("💻", "Full-Stack Developer", "Intern", "2026"),
    ]
    cert_cols = st.columns(4, gap="medium")
    for i, (icon, title, org, year) in enumerate(certs):
        with cert_cols[i]:
            st.markdown(f"""
            <div class="cert-glass">
                <div class="cert-icon">{icon}</div>
                <div class="cert-title">{title}</div>
                <div class="cert-org">{org}</div>
                <span class="cert-year">{year}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("")
    if st.button("Certificate Details", key="btn_cert_details", use_container_width=True):
        st.session_state.show_certs = not st.session_state.get("show_certs", False)
    if st.session_state.get("show_certs", False):
        st.markdown('<div class="toggle-content">', unsafe_allow_html=True)
        cert_pick = st.selectbox("Select a certificate:", [c[1] for c in certs])
        details_map = {
            "AWS Academy Graduate": "Comprehensive training in AWS Cloud fundamentals — core services, security, architecture, pricing, and support.",
            "HCIA — AI in Full Stack": "Full-stack AI application development using Huawei's ModelArts platform and AI services.",
            "HCIA — Cloud Service": "Cloud computing architecture, virtualization, and Huawei Cloud service deployment & management.",
            "Full Stack Developer": "An Intern practicing/demonstrating proficiency in component design, state management, and testing.",
        }
        st.info(details_map.get(cert_pick, ""))
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)


# ━━━━  CONTACT  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
if page in ["Home", "Contact"]:
    st.markdown("""
    <div class="center-text">
        <span class="section-tag">Contact</span>
        <div class="section-title">Let's <span class="gradient-text">Connect</span></div>
        <p class="section-desc">Have a project idea, opportunity, or just want to chat? Reach out!</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("")

    c_left, c_right = st.columns([1, 1.2], gap="large")

    with c_left:
        st.markdown(f"""
        <div class="glass" style="padding:2rem;">
            <div class="contact-info-item">
                <div class="contact-icon">📧</div>
                <div>
                    <div class="contact-label">Email</div>
                    <div class="contact-value">justinandrydiva@gmail.com</div>
                </div>
            </div>
            <div class="contact-info-item">
                <div class="contact-icon">📱</div>
                <div>
                    <div class="contact-label">Phone</div>
                    <div class="contact-value">+63 999 510 9923</div>
                </div>
            </div>
            <div class="contact-info-item">
                <div class="contact-icon">📍</div>
                <div>
                    <div class="contact-label">Location</div>
                    <div class="contact-value">Cebu City, Philippines</div>
                </div>
            </div>
            <div class="contact-info-item">
                <div class="contact-icon"><img src="data:image/jpeg;base64,{github_logo_b64}" style="width:24px;height:24px;border-radius:50%;" /></div>
                <div>
                    <div class="contact-label">GitHub</div>
                    <div class="contact-value">https://github.com/avid0101</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")
        if lottie_contact:
            st_lottie(lottie_contact, height=180, key="lottie_contact")

    with c_right:
        st.markdown("""
        <div class="cta-card">
            <div class="cta-title">Let's Build Something <span style="background:var(--gradient-1);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;">Amazing</span> ✨</div>
            <div class="cta-sub">Drop me a message below</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")

        with st.form("contact_form", clear_on_submit=True):
            fc1, fc2 = st.columns(2)
            with fc1:
                name = st.text_input("Your Name", placeholder="Juan Dela Cruz")
            with fc2:
                email = st.text_input("Your Email", placeholder="juan@example.com")

            subject = st.selectbox("Subject", [
                "💼 Job Opportunity",
                "🤝 Collaboration",
                "💡 Project Idea",
                "📝 General Inquiry",
                "👋 Just Saying Hi",
            ])
            message = st.text_area("Message", placeholder="Write your message here...", height=110)

            submitted = st.form_submit_button("Send Message", use_container_width=True)

            if submitted:
                if name and email and message:
                    st.success(f"Thank you, **{name}**! Your message has been received. I'll get back to you soon! 🎉")
                    st.balloons()
                    st.toast("Message sent! 🎉", icon="✅")
                else:
                    st.warning("Please fill in all fields (Name, Email, and Message).")



# FOOTER
st.markdown("""
<div class="footer-wrap">
    <p>© 2026 <strong>Justin Andry N. Diva</strong> · Built with using
    <a href="https://streamlit.io">Streamlit</a></p>
    <p style="margin-top:0.3rem;font-size:0.75rem;">CIT-University</p>
</div>
""", unsafe_allow_html=True)
