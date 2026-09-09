import base64
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from data.profile import CAPABILITIES, CERTIFICATIONS, EXPERIENCE, METRICS, PROJECTS, PROFILE, SKILL_GROUPS

st.set_page_config(page_title="Vijay Kumar Kothapalli | Engineering Portfolio", page_icon="VK", layout="wide", initial_sidebar_state="expanded")

RESUME_PATH = Path(__file__).parent / "assets" / "resume.pdf"
BACKGROUND_IMAGE_PATH = Path(__file__).parent / "assets" / "cybersecurity.jpg"
AI_NETWORK_IMAGE = "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=85"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { --ink:#eaf2ff; --muted:#9caec8; --blue:#67b7ff; --cyan:#50e3c2; --panel:#101b2d; --line:#263954; --bg:#07111f; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
.stApp { background: radial-gradient(circle at 85% 0%, #12325b 0, transparent 28%), linear-gradient(145deg, #07111f 0%, #0b1728 62%, #091525 100%); color:var(--ink); perspective:1200px; }
header[data-testid="stHeader"] { background:rgba(7,17,31,.92); border-bottom:1px solid var(--line); }
[data-testid="stToolbar"] { background:transparent; }
[data-testid="stDecoration"] { background:linear-gradient(90deg, #50e3c2, #67b7ff); height:2px; }
.stDeployButton > button { background:#132b48 !important; color:var(--ink) !important; border:1px solid #39618d !important; border-radius:8px !important; box-shadow:none !important; }
.stDeployButton > button:hover { background:#1b3b5e !important; border-color:var(--cyan) !important; }
.block-container { max-width: 1440px; padding: 2.5rem 4rem 4rem; }
[data-testid="stSidebar"] { background: #091525; border-right: 1px solid var(--line); }
[data-testid="stSidebar"] * { color: var(--ink); }
.hero { padding: 1rem 0 2rem; border-bottom: 1px solid var(--line); }
.eyebrow { color:var(--cyan); letter-spacing:.14em; text-transform:uppercase; font-size:.72rem; font-weight:700; }
h1, h2, h3 { font-family:'Space Grotesk', sans-serif; color:var(--ink) !important; letter-spacing:0; }
h1 { font-size:clamp(2.3rem, 5vw, 5rem) !important; line-height:1.02 !important; margin:.35rem 0 .5rem !important; }
h2 { margin-top: 1.2rem !important; }
p, li, label { color:var(--muted); }
.hero-copy { font-size:1.08rem; line-height:1.7; max-width:760px; }
.pill { display:inline-block; padding:.38rem .7rem; margin:.2rem .18rem .2rem 0; border-radius:999px; background:#162942; border:1px solid #2c4a70; color:#b9ddff; font-size:.78rem; }
.metric { background:linear-gradient(145deg,#183554 0%,#12243c 42%,#0b1728 100%); border:1px solid #36577d; border-radius:14px; padding:1.05rem; min-height:110px; box-shadow:inset 1px 1px 0 #6b9cc844, inset -1px -1px 0 #02081299, 0 16px 28px #02081266; transform:translateZ(0); transition:transform .2s ease, box-shadow .2s ease; }
.metric:hover { transform:translateY(-6px) rotateX(2deg); box-shadow:inset 1px 1px 0 #8bc5f866, inset -1px -1px 0 #020812aa, 0 24px 38px #02081299; }
.metric-value { color:#fff; font-family:'Space Grotesk'; font-size:1.85rem; font-weight:700; }
.metric-label { color:#cfe0f5; font-weight:600; margin-top:.35rem; }
.metric-note { color:var(--muted); font-size:.75rem; }
.signal-card { background:linear-gradient(145deg, rgba(18,40,65,.92), rgba(9,21,37,.96)); border:1px solid rgba(120,170,220,.4); border-radius:16px; padding:1rem; min-height:140px; animation: floatCard 5s ease-in-out infinite; }
.signal-card:nth-child(2n) { animation-delay: .7s; }
@keyframes floatCard { 0%,100% { transform:translateY(0px); } 50% { transform:translateY(-6px); } }
.signal-kicker { color:#8cd9d0; letter-spacing:.14em; text-transform:uppercase; font-size:.7rem; font-weight:700; }
.signal-value { font-family:'Space Grotesk'; font-size:1.8rem; font-weight:700; color:#fff; }
.panel { background:linear-gradient(145deg,#142945 0%,#0d1a2c 55%,#091525 100%); border:1px solid #2e4d70; border-radius:16px; padding:1.2rem 1.35rem; height:100%; box-shadow:inset 1px 1px 0 #719ac833, inset -1px -1px 0 #02081299, 0 14px 26px #02081255; transform:translateZ(0); transition:transform .22s ease, box-shadow .22s ease, border-color .22s ease; }
.panel:hover { transform:translateY(-4px) rotateX(1deg); border-color:#4d78a4; box-shadow:inset 1px 1px 0 #8bc5f844, inset -1px -1px 0 #020812aa, 0 22px 34px #02081288; }
.card-title { color:#f4f8ff; font-family:'Space Grotesk'; font-weight:600; font-size:1.02rem; }
.card-text { color:var(--muted); line-height:1.55; font-size:.9rem; }
.timeline-line { border-left:2px solid #35587e; padding-left:1.25rem; margin-left:.5rem; }
.timeline-item { position:relative; padding:0 0 1.25rem; }
.timeline-item:before { content:''; width:10px; height:10px; background:var(--cyan); border:3px solid #14304b; border-radius:50%; position:absolute; left:-1.67rem; top:.3rem; }
.company { color:var(--blue); font-weight:700; font-size:1.05rem; }
.role { color:#fff; font-weight:600; }
.small { color:var(--muted); font-size:.82rem; }
.arch-step { background:linear-gradient(145deg,#1a3b5e,#10233a); border:1px solid #47749e; border-radius:10px; padding:.8rem; text-align:center; color:#dff0ff; font-weight:600; box-shadow:inset 1px 1px 0 #a6d9ff44, inset -2px -2px 0 #06101d99, 0 10px 18px #02081266; transform:translateZ(0); transition:transform .2s ease, box-shadow .2s ease; }
.arch-step:hover { transform:translateY(-4px) scale(1.015); box-shadow:inset 1px 1px 0 #bde6ff66, inset -2px -2px 0 #06101daa, 0 18px 28px #020812aa; }
.section-focus { position:relative; overflow:hidden; margin:0 0 1.2rem; padding:1rem 1.1rem; border-radius:16px; background:linear-gradient(135deg, rgba(18,40,65,.96), rgba(12,24,40,.9)); border:1px solid rgba(108,152,203,.45); box-shadow:inset 0 0 0 1px rgba(167,216,255,.14), 0 18px 26px rgba(2,8,18,.28); }
.section-focus::before { content:""; position:absolute; inset:0; background:linear-gradient(90deg, transparent 0%, rgba(80,227,194,.22) 32%, rgba(103,183,255,.3) 65%, transparent 100%); transform:translateX(-100%); animation: sweepFocus 7s ease-in-out infinite; }
.section-focus-inner { position:relative; z-index:1; display:flex; align-items:center; justify-content:space-between; gap:1rem; }
.focus-movement { display:flex; align-items:center; gap:.5rem; flex:1; justify-content:flex-end; }
.focus-track { position:relative; width:120px; height:8px; border-radius:999px; background:rgba(100,130,160,.25); overflow:hidden; }
.focus-track::after { content:""; position:absolute; inset:0; width:42%; border-radius:999px; background:linear-gradient(90deg, #50e3c2, #67b7ff, #8ec5ff); animation: slideFocus 3.4s ease-in-out infinite; }
.focus-node { width:11px; height:11px; border-radius:50%; background:radial-gradient(circle at 30% 30%, #d8fef7, #50e3c2 45%, #1c7ea8 100%); box-shadow:0 0 12px rgba(80,227,194,.7); animation:pulseFocus 2s ease-in-out infinite; }
.focus-node.alt { background:radial-gradient(circle at 30% 30%, #ebf5ff, #67b7ff 40%, #3a67b8 100%); box-shadow:0 0 12px rgba(103,183,255,.8); animation-delay:.5s; }
@keyframes pulseFocus { 0%,100% { transform:scale(1); opacity:1; } 50% { transform:scale(1.4); opacity:.8; } }
@keyframes slideFocus { 0% { transform:translateX(-10%); } 50% { transform:translateX(120%); } 100% { transform:translateX(-10%); } }
@keyframes sweepFocus { 0% { transform:translateX(-100%); } 50% { transform:translateX(100%); } 100% { transform:translateX(150%); } }
.ai-visual { border:1px solid #416b92; border-radius:16px; overflow:hidden; box-shadow:inset 0 0 0 1px #9ed8ff22, 0 18px 34px #02081288; transform:scale(1.02); }
.ai-visual img { display:block; width:100%; max-height:540px; object-fit:cover; }
.ai-caption { color:#a9c7e5; font-size:.78rem; padding:.65rem .8rem; background:#0b192b; }
.arch-arrow { color:var(--cyan); text-align:center; font-size:1.2rem; padding:.25rem; }
.command-center { position:relative; overflow:hidden; background:linear-gradient(135deg,#0d1b2d 0%, #102842 35%, #0a1526 100%); border:1px solid rgba(118,170,220,.5); border-radius:22px; padding:1.15rem 1.2rem; margin:1.25rem 0 1.5rem; box-shadow:inset 0 0 0 1px rgba(147,198,255,.12), 0 18px 30px rgba(2,8,18,.35); }
.command-center::before { content:""; position:absolute; inset:-30% auto auto -18%; width:60%; height:180%; background:radial-gradient(circle, rgba(80,227,194,.18), rgba(80,227,194,0) 58%); pointer-events:none; }
.command-center::after { content:""; position:absolute; right:-10%; bottom:-20%; width:55%; height:150%; background:radial-gradient(circle, rgba(103,183,255,.17), rgba(103,183,255,0) 58%); pointer-events:none; }
.command-label { position:relative; z-index:1; display:flex; align-items:center; justify-content:space-between; gap:.8rem; color:#cfeaff; font-size:.76rem; text-transform:uppercase; letter-spacing:.12em; font-weight:700; }
.command-label .live-dot { width:10px; height:10px; border-radius:50%; background:#50e3c2; box-shadow:0 0 12px rgba(80,227,194,.9); animation:pulseLive 1.8s ease-in-out infinite; }
.focus-shell { position:relative; z-index:1; background:linear-gradient(145deg, rgba(12,24,40,.92), rgba(16,32,49,.82)); border:1px solid rgba(109,160,213,.48); border-radius:16px; padding:1rem; margin-top:.75rem; }
.focus-shell::before { content:""; position:absolute; inset:0; background:linear-gradient(120deg, transparent, rgba(103,183,255,.08), transparent); transform:translateX(-100%); animation: sweepWave 6s ease-in-out infinite; }
.focus-header { position:relative; z-index:1; display:flex; justify-content:space-between; align-items:center; gap:.75rem; margin-bottom:.75rem; }
.focus-badge { display:inline-flex; align-items:center; gap:.45rem; padding:.38rem .7rem; border-radius:999px; background:rgba(80,227,194,.12); border:1px solid rgba(80,227,194,.45); color:#b3f6ea; font-size:.72rem; font-weight:700; letter-spacing:.08em; text-transform:uppercase; }
.signal-wave { position:relative; z-index:1; height:58px; border-radius:12px; background:linear-gradient(180deg, rgba(21,39,58,.8), rgba(9,20,33,.9)); border:1px solid rgba(121,173,219,.35); overflow:hidden; margin-top:.8rem; }
.signal-wave svg { position:absolute; inset:0; width:100%; height:100%; }
.signal-wave .line { fill:none; stroke:url(#waveGradient); stroke-width:2.5; stroke-linecap:round; stroke-linejoin:round; filter:drop-shadow(0 0 8px rgba(80,227,194,.45)); }
.signal-wave .area { fill:url(#waveArea); opacity:.75; }
.mini-metric { background:rgba(11,28,45,.75); border:1px solid rgba(108,152,203,.4); border-radius:12px; padding:.7rem .8rem; margin-top:.5rem; }
.mini-metric .label { color:#b9ddff; font-size:.7rem; letter-spacing:.08em; text-transform:uppercase; }
.mini-metric .value { color:#fff; font-family:'Space Grotesk'; font-size:1.2rem; font-weight:700; margin-top:.2rem; }
[data-testid="stMetricValue"] { color:#fff; }
@keyframes pulseLive { 0%,100% { transform:scale(1); opacity:1; } 50% { transform:scale(1.35); opacity:.7; } }
@keyframes sweepWave { 0% { transform:translateX(-100%); } 50% { transform:translateX(100%); } 100% { transform:translateX(150%); } }
.stButton > button, .stDownloadButton > button { border-radius:8px; border:1px solid #39618d; background:#132b48; color:#eaf2ff; font-weight:600; }
.stButton > button:hover, .stDownloadButton > button:hover { border-color:var(--cyan); color:#fff; }
.stLinkButton > a, [data-testid="stLinkButton"] { border-radius:8px !important; border:1px solid #39618d !important; background:#132b48 !important; color:#eaf2ff !important; box-shadow:none !important; }
.stLinkButton > a:hover, [data-testid="stLinkButton"]:hover { border-color:var(--cyan) !important; background:#1b3b5e !important; color:#fff !important; }
[data-testid="stExpander"] details, [data-testid="stExpander"] summary { background:#101f34 !important; border-color:#2b4566 !important; color:#dcecff !important; }
[data-testid="stExpander"] summary:hover { background:#162d49 !important; color:#fff !important; }
.stTabs [data-baseweb="tab-list"] { gap: .35rem; border-bottom:1px solid var(--line); }
.stTabs [data-baseweb="tab"] { color:var(--muted); padding: .85rem 1rem; font-size:1rem; font-weight:600; }
.stTabs [aria-selected="true"] { color:#fff !important; border-bottom-color:var(--cyan) !important; }
section[data-testid="stSidebar"] .stButton button { width:100%; }
</style>
""", unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def background_image_data_uri():
    if not BACKGROUND_IMAGE_PATH.exists():
        return ""
    encoded = base64.b64encode(BACKGROUND_IMAGE_PATH.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


def render_page_background():
    image_uri = background_image_data_uri()
    if image_uri:
        st.markdown(
            f"""
<style>
.stApp {{
    background-image:
        linear-gradient(rgba(3, 10, 21, .90), rgba(3, 10, 21, .97)),
        url('{image_uri}');
    background-size: cover;
    background-position: center top;
    background-attachment: fixed;
}}
:root {{ --muted:#c0cee0; --line:#3b5575; }}
p, li, label, .card-text, .small, .metric-note {{ color:#c0cee0 !important; }}
.hero-copy {{ color:#e6f0ff !important; text-shadow:0 2px 12px #020812; }}
.metric-label, .card-title, h1, h2, h3 {{ text-shadow:0 2px 10px #020812; }}
</style>
""",
            unsafe_allow_html=True,
        )


def chart_layout(fig, height=320):
    fig.update_layout(template="plotly_dark", height=height, margin=dict(l=15, r=15, t=28, b=15), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(family="DM Sans", color="#b8c8dd"), legend=dict(orientation="h", y=-.18))
    return fig


def render_sidebar():
    with st.sidebar:
        st.markdown("<div class='eyebrow'>Portfolio / 2026</div>", unsafe_allow_html=True)
        st.markdown("## Vijay Kumar Kothapalli")
        st.caption("GenAI Test Architect")
        st.divider()
        st.markdown("**Navigate**")
        st.caption("Use the tabs above to explore the portfolio.")
        st.markdown("---")
        st.markdown("**Focus areas**")
        for item in ["Quality Engineering", "SDET Leadership", "AI Testing", "Agentic AI", "Banking Technology", "Cloud & DevOps"]:
            st.markdown(f"<span class='pill'>{item}</span>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"**{PROFILE['location']}**")
        st.markdown(f"[{PROFILE['email']}](mailto:{PROFILE['email']})")
        st.link_button("Open LinkedIn", PROFILE["linkedin"], use_container_width=True)


def render_hero():
    st.markdown("<div class='hero'>", unsafe_allow_html=True)
    st.markdown("<div class='eyebrow'>Engineering leadership / quality by design</div>", unsafe_allow_html=True)
    st.title(PROFILE["name"])
    st.markdown("### GenAI Test Architect  ·  SDET Lead  ·  Quality Engineering Leader")
    st.markdown("<p class='hero-copy'>Quality Engineering | SDET Leadership | Test Automation | AI Testing | Agentic AI | RAG | MCP</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='hero-copy'>{PROFILE['summary']}</p>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1: st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
    with c2: st.link_button("Email Vijay", f"mailto:{PROFILE['email']}", use_container_width=True)
    with c3:
        if RESUME_PATH.exists():
            st.download_button("Download resume", RESUME_PATH.read_bytes(), file_name=RESUME_PATH.name, use_container_width=True)
        else:
            st.caption("Add assets/resume.pdf to enable download")
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")
    cols = st.columns(6)
    for col, (value, label, note) in zip(cols, METRICS):
        with col:
            st.markdown(f"<div class='metric'><div class='metric-value'>{value}</div><div class='metric-label'>{label}</div><div class='metric-note'>{note}</div></div>", unsafe_allow_html=True)


def render_focus_banner(title, subtitle="Focus area"):
    st.markdown(
        f"""
        <div class='section-focus'>
            <div class='section-focus-inner'>
                <div>
                    <div class='eyebrow'>{subtitle}</div>
                    <div class='card-title'>{title}</div>
                </div>
                <div class='focus-movement'>
                    <span class='focus-node'></span>
                    <span class='focus-track'></span>
                    <span class='focus-node alt'></span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_skill_spotlight():
    if "skill_spotlight" not in st.session_state:
        st.session_state.skill_spotlight = "AI & GenAI"

    st.markdown("### Skill spotlight")
    buttons = st.columns(len(SKILL_GROUPS))
    for col, category in zip(buttons, SKILL_GROUPS.keys()):
        with col:
            if st.button(category, key=f"skill_{category}", use_container_width=True):
                st.session_state.skill_spotlight = category

    selected_category = st.session_state.skill_spotlight
    selected_skills = SKILL_GROUPS.get(selected_category, [])
    top_row = st.columns(3)
    for idx, (label, value) in enumerate([
        ("Focus area", selected_category),
        ("Tooling depth", str(len(selected_skills))),
        ("Primary value", "Enterprise quality impact"),
    ]):
        with top_row[idx]:
            st.markdown(f"<div class='signal-card'><div class='signal-kicker'>{label}</div><div class='signal-value'>{value}</div></div>", unsafe_allow_html=True)

    st.markdown(f"<div class='panel' style='margin-top: 1rem'><div class='card-title'>{selected_category}</div><div>{''.join(f'<span class=\"pill\">{skill}</span>' for skill in selected_skills[:12])}</div></div>", unsafe_allow_html=True)


def render_command_center():
    if "command_focus" not in st.session_state:
        st.session_state.command_focus = "AI & GenAI"

    focus_options = ["AI & GenAI", "Quality leadership", "Delivery ecosystem"]
    selected_focus = st.radio("Explore by lens", focus_options, index=focus_options.index(st.session_state.command_focus), horizontal=True, label_visibility="collapsed")
    st.session_state.command_focus = selected_focus

    focus_map = {
        "AI & GenAI": {
            "title": "Agentic engineering",
            "tags": "RAG · MCP · AI-assisted testing",
            "copy": "Build intelligent quality systems grounded in enterprise knowledge and practical delivery workflows.",
            "stats": [("AI systems", "3 core layers"), ("Agent patterns", "LangChain + MCP"), ("Quality loops", "Evaluation-first")],
        },
        "Quality leadership": {
            "title": "Quality by design",
            "tags": "Strategy · gates · release readiness",
            "copy": "Lead teams and systems toward reliable, measurable delivery through risk-based quality strategy.",
            "stats": [("Coverage gains", "45%+"), ("Release cycles", "1 day"), ("Defect reduction", "30–50%")],
        },
        "Delivery ecosystem": {
            "title": "Automation at scale",
            "tags": "Web · mobile · API · cloud",
            "copy": "Connect automation, CI/CD and domain expertise into one delivery loop for enterprise software teams.",
            "stats": [("Platforms", "Web + mobile + API"), ("Delivery flow", "Shift-left"), ("Ops footprint", "AWS + Azure")],
        },
    }

    spotlight = focus_map[selected_focus]
    st.markdown(
        """
        <div class='command-center'>
            <div class='command-label'>
                <span>Interactive command center</span>
                <span class='live-dot'></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    lens_col, chart_col, detail_col = st.columns([.75, 2.35, .75])
    with lens_col:
        st.markdown(f"<div class='focus-shell'><div class='focus-header'><div class='card-title'>{spotlight['title']}</div><div class='focus-badge'>{selected_focus}</div></div><div class='card-text'>{spotlight['tags']}<br/><br/>{spotlight['copy']}</div><div class='signal-wave'><svg viewBox='0 0 300 60' preserveAspectRatio='none'><defs><linearGradient id='waveGradient' x1='0%' y1='0%' x2='100%' y2='0%'><stop offset='0%' stop-color='#50e3c2'/><stop offset='52%' stop-color='#67b7ff'/><stop offset='100%' stop-color='#8cc7ff'/></linearGradient><linearGradient id='waveArea' x1='0%' y1='0%' x2='0%' y2='100%'><stop offset='0%' stop-color='rgba(80,227,194,.48)'/><stop offset='100%' stop-color='rgba(80,227,194,0)'/></linearGradient></defs><path class='area' d='M0,50 C35,35 55,10 95,25 S150,58 190,30 S250,8 300,22 L300,60 L0,60 Z'></path><path class='line' d='M0,50 C35,35 55,10 95,25 S150,58 190,30 S250,8 300,22'></path></svg></div></div>", unsafe_allow_html=True)
        if st.button("Rotate spotlight"):
            next_index = (focus_options.index(selected_focus) + 1) % len(focus_options)
            st.session_state.command_focus = focus_options[next_index]
            st.rerun()
    with chart_col:
        labels = []
        parents = []
        ids = []
        values = []
        colors = []
        palette = ["#67b7ff", "#50e3c2", "#7f9cff", "#4bc0c8", "#9ad1ff", "#6ee7b7"]

        for idx, (category, skills) in enumerate(SKILL_GROUPS.items()):
            category_id = f"cat_{idx}"
            ids.append(category_id)
            labels.append(category)
            parents.append("")
            values.append(len(skills))
            colors.append(palette[idx % len(palette)])

            for skill_idx, skill in enumerate(skills):
                skill_id = f"{category_id}_{skill_idx}"
                ids.append(skill_id)
                labels.append(skill)
                parents.append(category_id)
                values.append(1)
                colors.append(palette[idx % len(palette)])

        fig = go.Figure(
            go.Sunburst(
                ids=ids,
                labels=labels,
                parents=parents,
                values=values,
                branchvalues="total",
                insidetextorientation="radial",
                hovertemplate="%{label}<extra></extra>",
                marker=dict(colors=colors, line=dict(color="rgba(255,255,255,0.18)", width=1)),
            )
        )
        fig.update_layout(
            title="Technology ecosystem",
            title_font_size=15,
            margin=dict(l=15, r=15, t=32, b=15),
            uniformtext=dict(minsize=11, mode="hide"),
        )
        st.plotly_chart(chart_layout(fig, 530), use_container_width=True, config={"displayModeBar": False}, key="tech_ecosystem_sunburst")
    with detail_col:
        st.markdown("<div class='card-title'>Signal at a glance</div>", unsafe_allow_html=True)
        for label, value in [("Skill categories", len(SKILL_GROUPS)), ("Listed technologies", sum(len(skills) for skills in SKILL_GROUPS.values())), ("Career chapters", len(EXPERIENCE))]:
            st.metric(label, value)
        st.markdown("<div class='card-title' style='margin-top:.9rem'>Current lens</div>", unsafe_allow_html=True)
        for metric_label, metric_value in spotlight["stats"]:
            st.markdown(f"<div class='mini-metric'><div class='label'>{metric_label}</div><div class='value'>{metric_value}</div></div>", unsafe_allow_html=True)


def profile_tab():
    render_focus_banner("Executive profile", "Focus area")
    st.subheader("Executive profile")
    left, right = st.columns([1.2, .8])
    with left:
        st.markdown("### What I bring")
        for capability, detail in CAPABILITIES:
            st.markdown(f"<div class='panel' style='margin:.45rem 0'><div class='card-title'>{capability}</div><div class='card-text'>{detail}</div></div>", unsafe_allow_html=True)
    with right:
        st.markdown("### Career signal")
        values = [14, 9, 45, 65, 40, 1]
        labels = ["Experience", "Team led", "Coverage gain", "Regression reduction", "Defect reduction", "Validation days"]
        fig = go.Figure(go.Bar(x=values, y=labels, orientation="h", marker_color=["#67b7ff", "#50e3c2", "#67b7ff", "#50e3c2", "#67b7ff", "#50e3c2"]))
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(chart_layout(fig, 330), use_container_width=True, config={"displayModeBar": False})
        st.markdown("### Leadership strengths")
        st.markdown("<div class='panel'><div class='card-text'>Built 6 automation frameworks from scratch across web, mobile, API, and enterprise platforms; quality strategy · architecture · stakeholder management · shift-left testing · release readiness · RCA · Agile/Scrum</div></div>", unsafe_allow_html=True)


def career_tab():
    render_focus_banner("Career journey", "Leadership track")
    st.subheader("Career journey")
    st.caption("A 14+ year progression through enterprise engineering, quality and banking technology.")
    st.markdown("<div class='timeline-line'>", unsafe_allow_html=True)
    for item in EXPERIENCE:
        st.markdown(f"<div class='timeline-item'><div class='company'>{item['company']}</div><div class='role'>{item['role']}</div><div class='small'>{item['period']}</div><div class='card-text'>{item['scope']}<br/><span class='small'>{item['tech']}</span></div></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def quality_tab():
    render_focus_banner("Leadership & Quality Engineering", "Quality flow")
    st.subheader("Leadership & Quality Engineering")
    st.markdown("<div class='panel'><div class='card-title'>Currently leading a team of 9 members</div><div class='card-text'>Quality Engineering functions across web, mobile, API and enterprise applications.</div></div>", unsafe_allow_html=True)
    left, right = st.columns([1, 1])
    with left:
        categories = ["Leadership", "Automation", "Quality Engineering", "AI Testing", "Architecture", "Cloud", "DevOps", "Banking Domain"]
        scores = [9, 9, 9, 8, 8, 7, 8, 8]
        fig = go.Figure(go.Scatterpolar(r=scores + [scores[0]], theta=categories + [categories[0]], fill="toself", line_color="#50e3c2", fillcolor="rgba(80,227,194,.22)"))
        fig.update_polars(radialaxis=dict(visible=False, range=[0, 10]), angularaxis=dict(color="#b8c8dd"))
        st.plotly_chart(chart_layout(fig, 400), use_container_width=True, config={"displayModeBar": False})
    with right:
        st.markdown("### Operating model")
        for item in ["Quality strategy and test strategy", "Quality gates and release readiness", "Shift-left testing and CI/CD", "Defect management and root cause analysis", "Test metrics and stakeholder management", "Agile delivery and team coaching"]:
            st.markdown(f"<div class='panel' style='margin:.45rem 0'><div class='card-text'>+ {item}</div></div>", unsafe_allow_html=True)


def ai_tab():
    render_focus_banner("AI / GenAI / Agentic AI", "Innovation focus")
    st.subheader("AI / GenAI / Agentic AI")
    st.markdown("<div class='panel'><div class='card-title'>Built and deployed Agentic RAG AI solutions using LangChain, developed MCP-based AI agents, and deployed agentic solutions within Wells Fargo.</div></div>", unsafe_allow_html=True)
    visual_col, intro_col = st.columns([1.25, 1])
    with visual_col:
        st.markdown("<div class='ai-visual'>", unsafe_allow_html=True)
        st.image(AI_NETWORK_IMAGE, width=900)
        st.markdown("<div class='ai-caption'>Generative systems, grounded knowledge and measurable quality</div></div>", unsafe_allow_html=True)
    with intro_col:
        st.markdown("### AI capability landscape")
        st.markdown("<div class='card-text'>Explore an engineering portfolio shaped around agentic workflows, retrieval-augmented generation, evaluation, and AI-assisted testing.</div>", unsafe_allow_html=True)
        st.markdown("<span class='pill'>CrewAI</span><span class='pill'>LangGraph</span><span class='pill'>RAGAS</span><span class='pill'>DeepEval</span><span class='pill'>MCP</span>", unsafe_allow_html=True)
    st.markdown("### AI architecture")
    steps = ["User", "AI Agent", "LangChain / LangGraph", "RAG", "Knowledge / Data Sources", "LLM", "Tool / MCP Layer", "Automation / Testing", "Quality Results"]
    links = [(index, index + 1) for index in range(len(steps) - 1)]
    fig = go.Figure(go.Sankey(node=dict(label=steps, color=["#67b7ff", "#50e3c2", "#7f9cff", "#50e3c2", "#67b7ff", "#7f9cff", "#50e3c2", "#67b7ff", "#50e3c2"], pad=20, thickness=18), link=dict(source=[source for source, _ in links], target=[target for _, target in links], value=[1] * len(links), color="rgba(103,183,255,.35)")))
    st.plotly_chart(chart_layout(fig, 380), use_container_width=True, config={"displayModeBar": False})
    st.markdown("### AI capability matrix")
    matrix = pd.DataFrame({"Capability": ["Generative AI", "AI Agents", "LangGraph", "CrewAI", "RAG", "RAGAS", "DeepEval", "MCP", "Prompt Engineering", "AI-Assisted Testing", "Synthetic Test Data", "Self-Healing Automation"], "Applied in engineering": ["Core", "Core", "Core", "Exploring", "Core", "Exploring", "Exploring", "Core", "Core", "Core", "Emerging", "Exploring"]})
    st.dataframe(matrix, hide_index=True, use_container_width=True)


def automation_tab():
    render_focus_banner("Test automation ecosystem", "Automation focus")
    st.subheader("Test automation ecosystem")
    search = st.text_input("Search technologies", placeholder="Try: Playwright, AWS, RAG")
    selected = [key for key, skills in SKILL_GROUPS.items() if not search or search.lower() in key.lower() or any(search.lower() in s.lower() for s in skills)]
    cols = st.columns(3)
    for index, category in enumerate(selected):
        with cols[index % 3]:
            skills = [skill for skill in SKILL_GROUPS[category] if not search or search.lower() in skill.lower() or search.lower() in category.lower()]
            if skills:
                st.markdown(f"<div class='panel' style='margin:.45rem 0'><div class='card-title'>{category}</div><div>{''.join(f'<span class=\"pill\">{skill}</span>' for skill in skills)}</div></div>", unsafe_allow_html=True)
    st.markdown("### Automation surfaces")
    surface_cols = st.columns(4)
    for col, title, body in zip(surface_cols, ["Web automation", "Mobile automation", "API automation", "Microservices testing"], ["Selenium · Playwright", "Appium · Android · iOS", "REST · GraphQL · SOAP", "Contracts · integration · data"]):
        with col: st.markdown(f"<div class='panel'><div class='card-title'>{title}</div><div class='card-text'>{body}</div></div>", unsafe_allow_html=True)


def cloud_tab():
    render_focus_banner("Cloud & DevOps", "Delivery focus")
    st.subheader("Cloud & DevOps")
    st.markdown("### Continuous testing pipeline")
    pipeline = ["Code", "Git", "Build", "Automated Testing", "Quality Gates", "Deployment", "Release Validation"]
    cols = st.columns(len(pipeline))
    for i, (col, step) in enumerate(zip(cols, pipeline)):
        with col:
            st.markdown(f"<div class='arch-step'>{step}</div>", unsafe_allow_html=True)
            if i < len(pipeline) - 1: st.markdown("<div class='arch-arrow'>→</div>", unsafe_allow_html=True)
    left, right = st.columns(2)
    with left:
        st.markdown("### Cloud")
        st.markdown("<span class='pill'>AWS</span><span class='pill'>Azure</span><span class='pill'>Lambda</span><span class='pill'>Step Functions</span><span class='pill'>AWS SDK</span>", unsafe_allow_html=True)
    with right:
        st.markdown("### Delivery toolchain")
        st.markdown("<span class='pill'>Jenkins</span><span class='pill'>Azure DevOps</span><span class='pill'>GitHub</span><span class='pill'>Bitbucket</span><span class='pill'>Maven</span><span class='pill'>Gradle</span><span class='pill'>Docker</span>", unsafe_allow_html=True)


def domain_skills_tab():
    render_focus_banner("Banking & Financial Services", "Domain focus")
    st.subheader("Banking & Financial Services")
    st.markdown("<div class='panel'><div class='card-title'>Domain expertise</div><div class='card-text'>Payment Processing · Core Banking · Commercial Lending · Liquidity Management · Financial Analytics</div></div>", unsafe_allow_html=True)
    st.markdown("### Domain map")
    center = st.columns([1, 2, 1])[1]
    with center:
        st.markdown("<div class='arch-step' style='font-size:1.2rem'>Banking</div>", unsafe_allow_html=True)
    cols = st.columns(5)
    for col, label in zip(cols, ["Payment Processing", "Core Banking", "Commercial Lending", "Liquidity Management", "Financial Analytics"]):
        with col: st.markdown(f"<div class='panel' style='text-align:center;margin-top:.5rem'><div class='card-text'>{label}</div></div>", unsafe_allow_html=True)
    st.markdown("### Platforms and technologies")
    st.markdown("<span class='pill'>PACS</span><span class='pill'>Flexcube / FCUBS</span><span class='pill'>CBAM</span><span class='pill'>OBLM</span>", unsafe_allow_html=True)


def skills_tab():
    render_focus_banner("Skills dashboard", "Capability focus")
    st.subheader("Skills dashboard")
    st.caption("Category views show breadth only; no proficiency percentages are inferred.")
    counts = {category: len(skills) for category, skills in SKILL_GROUPS.items()}
    fig = go.Figure(go.Bar(x=list(counts.values()), y=list(counts.keys()), orientation="h", marker_color=["#67b7ff", "#50e3c2", "#7f9cff", "#4bc0c8", "#9ad1ff", "#6ee7b7"]))
    fig.update_xaxes(title="Skills listed", showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(chart_layout(fig, 350), use_container_width=True, config={"displayModeBar": False})

    category_buttons = st.columns(len(SKILL_GROUPS))
    for col, category in zip(category_buttons, SKILL_GROUPS):
        with col:
            st.button(category, key=f"chart_{category}", use_container_width=True, on_click=lambda category=category: st.session_state.update({"selected_skill_group": category}))

    selected = st.session_state.get("selected_skill_group", next(iter(SKILL_GROUPS)))
    st.markdown(f"<div class='panel'><div class='card-title'>{selected}</div><div>{''.join(f'<span class=\"pill\">{skill}</span>' for skill in SKILL_GROUPS[selected])}</div></div>", unsafe_allow_html=True)


def projects_tab():
    render_focus_banner("Projects & key initiatives", "Impact focus")
    st.subheader("Projects & key initiatives")
    project_filter = st.segmented_control("Filter by theme", options=["All", "AI", "Quality", "Banking", "Delivery"], default="All", selection_mode="single")

    filtered_projects = PROJECTS
    if project_filter != "All":
        key = project_filter.lower()
        filtered_projects = [
            project for project in PROJECTS
            if key in project[0].lower() or key in project[1].lower() or key in project[2].lower() or key in project[4].lower()
        ]

    if not filtered_projects:
        st.info("No projects match this filter right now.")
        return

    for index in range(0, len(filtered_projects), 2):
        cols = st.columns(2)
        for col, project in zip(cols, filtered_projects[index:index + 2]):
            name, objective, tech, impact, role = project
            with col:
                with st.expander(name, expanded=index == 0):
                    st.markdown(f"**Objective**  \n{objective}")
                    st.markdown(f"**Technology**  \n{tech}")
                    st.markdown(f"**Business impact**  \n{impact}")
                    st.markdown(f"**Role**  \n{role}")


def education_tab():
    render_focus_banner("Education & certifications", "Learning focus")
    st.subheader("Education & certifications")
    left, right = st.columns([.8, 1.2])
    with left:
        st.markdown("<div class='panel'><div class='eyebrow'>Education</div><div class='card-title'>B.Tech (Information Technology)</div><div class='card-text'>JNT University, Kakinada<br/>2007 – 2011</div></div>", unsafe_allow_html=True)
    with right:
        st.markdown("### Certifications and training")
        cols = st.columns(2)
        for index, cert in enumerate(CERTIFICATIONS):
            with cols[index % 2]: st.markdown(f"<div class='panel' style='margin:.35rem 0'><div class='card-text'>{cert}</div></div>", unsafe_allow_html=True)


def hiring_view():
    render_focus_banner("Hiring Manager View", "Decision focus")
    st.markdown("### Hiring Manager View")
    st.markdown("<div class='panel'><div class='card-title'>Why Vijay?</div><div class='card-text'>14+ years of enterprise engineering experience, Quality Engineering leadership, strong automation architecture, AI/GenAI testing expertise, Agentic RAG AI development, MCP-based AI agents, banking and financial-services expertise, web/mobile/API testing, and cloud delivery experience.</div></div>", unsafe_allow_html=True)
    st.markdown("### Best-fit roles")
    st.markdown("<span class='pill'>SDET Manager</span><span class='pill'>GenAI Test Architect</span><span class='pill'>Principal SDET</span><span class='pill'>QA Automation Architect</span><span class='pill'>Quality Engineering Lead</span><span class='pill'>AI Testing Lead</span><span class='pill'>AI Quality Engineering Architect</span><span class='pill'>Agentic AI Quality Architect</span>", unsafe_allow_html=True)


def contact_tab():
    render_focus_banner("Contact", "Connect focus")
    st.subheader("Contact")
    left, right = st.columns([1.2, .8])
    with left:
        st.markdown("<div class='panel'><div class='eyebrow'>Let's build reliable systems</div><h2>Vijay Kumar Kothapalli</h2><div class='card-text'>GenAI Test Architect<br/>Hyderabad, India</div></div>", unsafe_allow_html=True)
    with right:
        st.link_button("Email Me", f"mailto:{PROFILE['email']}", use_container_width=True)
        st.link_button("LinkedIn", PROFILE["linkedin"], use_container_width=True)
        if RESUME_PATH.exists(): st.download_button("Download resume", RESUME_PATH.read_bytes(), file_name=RESUME_PATH.name, use_container_width=True)


render_page_background()
render_sidebar()
render_hero()
render_skill_spotlight()
render_command_center()
tabs = st.tabs(["Executive profile", "Career journey", "Quality leadership", "AI / GenAI", "Automation", "Cloud & DevOps", "Banking domain", "Skills", "Projects", "Education", "Contact"])
with tabs[0]: profile_tab()
with tabs[1]: career_tab()
with tabs[2]: quality_tab()
with tabs[3]: ai_tab()
with tabs[4]: automation_tab()
with tabs[5]: cloud_tab()
with tabs[6]: domain_skills_tab()
with tabs[7]: skills_tab()
with tabs[8]: projects_tab()
with tabs[9]: education_tab()
with tabs[10]: contact_tab()

st.divider()
with st.expander("Hiring Manager View"):
    hiring_view()
st.caption("Professional portfolio. Sensitive personal identification information is intentionally excluded.")
