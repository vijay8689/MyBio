from html import escape
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from data.profile import CAPABILITIES, CERTIFICATIONS, EXPERIENCE, METRICS, PROJECTS, PROJECT_LINKS, PROFILE, SKILL_GROUPS

st.set_page_config(page_title="Vijay Kumar | Engineering portfolio", page_icon="VK", layout="wide", initial_sidebar_state="collapsed")

RESUME_PATH = Path(__file__).parent / "assets" / "resume.pdf"
AI_NETWORK_IMAGE = "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=85"

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
        section = st.selectbox("Explore the portfolio", list(SECTIONS), key="portfolio_section")
        motion = st.toggle("Enable animations", value=True, key="portfolio_motion", help="Turn off decorative motion. Your device's reduced-motion preference is always respected.")
        st.markdown("---")
        st.markdown("**Focus areas**")
        for item in ["Quality Engineering", "SDET Leadership", "AI Testing", "Agentic AI", "Banking Technology", "Cloud & DevOps"]:
            st.markdown(f"<span class='pill'>{item}</span>", unsafe_allow_html=True)
        st.markdown("---")
        st.markdown(f"**{PROFILE['location']}**")
        st.markdown(f"[{PROFILE['email']}](mailto:{PROFILE['email']})")
        st.link_button("Open LinkedIn", PROFILE["linkedin"], width="stretch")
    return section, motion


def render_hero():
    st.markdown(f"""<section class='portfolio-hero'>
<div class='hero-status'><span class='status-dot' aria-hidden='true'></span>{escape(PROFILE['location'])} / Engineering portfolio</div>
<div class='eyebrow'>Engineering leadership / quality by design</div>
<h1>{escape(PROFILE['name'])}</h1>
<h3>Building confidence.<br/><span class='hero-accent'>Engineering what's next.</span></h3>
<div class='hero-rule' aria-hidden='true'></div>
<p class='hero-copy'>{escape(PROFILE['summary'])}</p>
<span class='pill'>GenAI Test Architect</span><span class='pill'>SDET Lead</span><span class='pill'>Quality Engineering</span>
</section>""", unsafe_allow_html=True)
    st.button("Explore my projects", icon=":material/arrow_forward:", type="primary", on_click=lambda: st.session_state.update(portfolio_section="Projects"), width="stretch")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1: st.link_button("LinkedIn", PROFILE["linkedin"], width="stretch")
    with c2: st.link_button("Email Vijay", f"mailto:{PROFILE['email']}", width="stretch")
    with c3:
        if RESUME_PATH.exists():
            st.download_button("Download resume", RESUME_PATH.read_bytes(), file_name=RESUME_PATH.name, width="stretch")
        else:
            st.caption("")
    st.write("")
    cards = "".join(
        f"<div class='metric'><div class='metric-value'>{escape(value)}</div><div class='metric-label'>{escape(label)}</div><div class='metric-note'>{escape(note)}</div></div>"
        for value, label, note in METRICS
    )
    st.markdown(f"<div class='metrics-grid'>{cards}</div>", unsafe_allow_html=True)


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
            if st.button(category, key=f"skill_{category}", width="stretch"):
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
        st.plotly_chart(chart_layout(fig, 530), width="stretch", config={"displayModeBar": False}, key="tech_ecosystem_sunburst")
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
        values = [14, 16, 45, 65, 40, 1]
        labels = ["Experience", "Team led", "Coverage gain", "Regression reduction", "Defect reduction", "Validation days"]
        fig = go.Figure(go.Bar(x=values, y=labels, orientation="h", marker_color=["#67b7ff", "#50e3c2", "#67b7ff", "#50e3c2", "#67b7ff", "#50e3c2"]))
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False)
        st.plotly_chart(chart_layout(fig, 330), width="stretch", config={"displayModeBar": False})
        st.markdown("### Leadership strengths")
        st.markdown("<div class='panel'><div class='card-text'>Built 6 automation frameworks from scratch across web, mobile, API, and enterprise platforms; quality strategy · architecture · stakeholder management · shift-left testing · release readiness · RCA · Agile/Scrum</div></div>", unsafe_allow_html=True)


def career_tab():
    render_focus_banner("Career journey", "Leadership track")
    st.subheader("Career journey")
    st.caption("A 14+ year progression through enterprise engineering, quality and banking technology.")
    items = []
    for item in EXPERIENCE:
        items.append(f"<div class='timeline-item'><div class='company'>{item['company']}</div><div class='role'>{item['role']}</div><div class='small'>{item['period']}</div><div class='card-text'>{item['scope']}<br/><span class='small'>{item['tech']}</span></div></div>")
    st.markdown(f"<div class='timeline-line'>{''.join(items)}</div>", unsafe_allow_html=True)


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
        st.plotly_chart(chart_layout(fig, 400), width="stretch", config={"displayModeBar": False})
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
    st.plotly_chart(chart_layout(fig, 380), width="stretch", config={"displayModeBar": False})
    st.markdown("### AI capability matrix")
    matrix = pd.DataFrame({"Capability": ["Generative AI", "AI Agents", "LangGraph", "CrewAI", "RAG", "RAGAS", "DeepEval", "MCP", "Prompt Engineering", "AI-Assisted Testing", "Synthetic Test Data", "Self-Healing Automation"], "Applied in engineering": ["Core", "Core", "Core", "Exploring", "Core", "Exploring", "Exploring", "Core", "Core", "Core", "Emerging", "Exploring"]})
    st.dataframe(matrix, hide_index=True, width="stretch")


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
    st.plotly_chart(chart_layout(fig, 350), width="stretch", config={"displayModeBar": False})

    category_buttons = st.columns(len(SKILL_GROUPS))
    for col, category in zip(category_buttons, SKILL_GROUPS):
        with col:
            st.button(category, key=f"chart_{category}", width="stretch", on_click=lambda category=category: st.session_state.update({"selected_skill_group": category}))

    selected = st.session_state.get("selected_skill_group", next(iter(SKILL_GROUPS)))
    st.markdown(f"<div class='panel'><div class='card-title'>{selected}</div><div>{''.join(f'<span class=\"pill\">{skill}</span>' for skill in SKILL_GROUPS[selected])}</div></div>", unsafe_allow_html=True)


def projects_tab():
    render_focus_banner("Projects & key initiatives", "Impact focus")
    st.subheader("Projects & key initiatives")
    project_filter = st.segmented_control("Filter by theme", options=["All", "AI", "Quality", "Banking", "Delivery"], default="All", selection_mode="single")
    search = st.text_input("Search projects", placeholder="Search a project, technology, or outcome", key="project_search").strip().casefold()

    filtered_projects = PROJECTS
    themes = {
        "AI": [1, 2, 3, 6], "Quality": [0, 3, 4, 5],
        "Banking": [4], "Delivery": [0, 5],
    }
    if project_filter in themes:
        filtered_projects = [PROJECTS[index] for index in themes[project_filter]]
    filtered_projects = [project for project in filtered_projects if search in " ".join(project).casefold()]
    st.caption(f"Showing {len(filtered_projects)} of {len(PROJECTS)} initiatives · Open a card's details to explore the impact.")

    if not filtered_projects:
        st.info("No projects match this filter right now.")
        return

    for index in range(0, len(filtered_projects), 2):
        cols = st.columns(2)
        for col, project in zip(cols, filtered_projects[index:index + 2]):
            name, objective, tech, impact, role = project
            with col:
                tags = ''.join(f"<span class='pill'>{escape(tag.strip())}</span>" for tag in tech.split('·'))
                st.markdown(f"<article class='panel project-card'><div class='project-number'>INITIATIVE / {PROJECTS.index(project) + 1:02d}</div><div class='card-title'>{escape(name)}</div><div class='card-text'>{escape(objective)}</div><div>{tags}</div></article>", unsafe_allow_html=True)
                if name in PROJECT_LINKS:
                    st.link_button(f"Launch {name}", PROJECT_LINKS[name], icon=":material/open_in_new:", width="stretch")
                with st.expander(f"Explore {name}"):
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
        st.link_button("Email Me", f"mailto:{PROFILE['email']}", width="stretch")
        st.link_button("LinkedIn", PROFILE["linkedin"], width="stretch")
        if RESUME_PATH.exists(): st.download_button("Download resume", RESUME_PATH.read_bytes(), file_name=RESUME_PATH.name, width="stretch")


SECTIONS = {
    "Overview": profile_tab, "Career journey": career_tab,
    "Quality leadership": quality_tab, "AI / GenAI": ai_tab,
    "Automation": automation_tab, "Cloud & DevOps": cloud_tab,
    "Banking domain": domain_skills_tab, "Skills": skills_tab,
    "Projects": projects_tab, "Education": education_tab, "Contact": contact_tab,
}

def portfolio_page():
    section, motion = render_sidebar()
    st.html(f"<style>{(Path(__file__).parent / 'assets' / 'portfolio.css').read_text(encoding='utf-8')}</style>")
    if not motion:
        st.html("<style>*, *::before, *::after { animation:none !important; transition:none !important; scroll-behavior:auto !important; }</style>")
    if section == "Overview":
        render_hero()
        render_skill_spotlight()
        with st.expander("Explore the technology ecosystem", expanded=True):
            render_command_center()
    else:
        st.caption("VIJAY KUMAR KOTHAPALLI / ENGINEERING PORTFOLIO")
    SECTIONS[section]()

    st.divider()
    with st.expander("Hiring Manager View"):
        hiring_view()
    st.caption("Professional portfolio. Built with Streamlit. © 2026 Vijay Kumar Kothapalli")


page = st.navigation(
    {
        "": [st.Page(portfolio_page, title="Portfolio", icon=":material/person:", default=True)],
        "AI projects": [
            st.Page("app_pages/resume_jd_analyzer.py", title="Resume JD Analyzer", icon=":material/description:", url_path="Resume_JD_Analyzer"),
            st.Page("app_pages/healthlens_ai.py", title="HealthLensAI", icon=":material/health_and_safety:"),
        ],
    },
    position="top",
)
st.html(f"<style>{(Path(__file__).parent / 'assets' / 'portfolio.css').read_text(encoding='utf-8')}</style>")
page.run()
