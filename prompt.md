Act as a Senior Python Developer, Streamlit UI/UX Architect, Data Visualization Expert, and
Professional Portfolio Designer.

I want you to build a modern, premium-looking, highly interactive personal professional portfolio
website using Python and Streamlit.

The application must be designed so that it can be easily deployed to:
1. Streamlit Community Cloud
2. Internal/shared Streamlit environments
3. Local Python environment

The UI should represent me as a:
"Lead Software Engineer | SDET Lead | Quality Engineering Leader | AI Testing & Agentic AI Architect"

===========================================================
1. TECHNOLOGY REQUIREMENTS
===========================================================

Use:

- Python 3.10+
- Streamlit
- Plotly
- Pandas
- Python standard libraries wherever possible

Avoid unnecessary dependencies.

Create a clean project structure:

portfolio/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── profile.py
│
├── components/
│   ├── sidebar.py
│   ├── header.py
│   ├── cards.py
│   ├── charts.py
│   └── timeline.py
│
└── assets/
    └── profile.jpg

The application must run using:

streamlit run app.py

It should also be directly deployable through Streamlit Community Cloud.

===========================================================
2. DESIGN OBJECTIVE
===========================================================

Create a sophisticated executive-level portfolio rather than a basic resume page.

The UI should look similar to a combination of:

- Executive technology portfolio
- Software Architect profile
- SDET/Quality Engineering dashboard
- AI Engineering portfolio
- Professional resume website

Use a modern dashboard-style design.

Important:

DO NOT make the application look like a simple CV/PDF.

Convert the resume information into an interactive visual experience.

Use:

- Cards
- Metrics
- Charts
- Timeline
- Skill visualizations
- Technology badges
- Expandable sections
- Icons
- Tabs
- Progress/experience indicators
- Interactive Plotly charts
- Responsive layout

===========================================================
3. COLOR / VISUAL THEME
===========================================================

Use a professional technology/enterprise theme.

Preferred style:

- Dark navy / blue
- White/light background sections
- Subtle gradients
- Professional accent colors
- Minimal shadows
- Rounded cards
- Clean typography
- High contrast
- Executive appearance

Do not make the UI overly colorful.

The application should look suitable for presenting to:

- CTO
- CIO
- Engineering Director
- QA Director
- Hiring Manager
- Technical Recruiter

===========================================================
4. HEADER / HERO SECTION
===========================================================

Create a large hero section at the top.

Display:

Vijay Kumar Kothapalli

Lead Software Engineer

Subtitle:

"Quality Engineering | SDET Leadership | Test Automation | AI Testing | Agentic AI | RAG | MCP"

Include:

- Profile photo
- Location: Hyderabad, India
- LinkedIn button
- Email button
- Download Resume button
- Contact button

Create a short professional summary:

"Lead Software Engineer with 14+ years of experience in enterprise software,
Quality Engineering, test automation, banking and financial services, and
AI-powered testing. Experienced in building scalable automation frameworks,
leading Quality Engineering teams, modernizing CI/CD, and developing
Agentic AI, RAG and MCP-based solutions."

Add animated/subtle metric cards:

14+ Years Experience
9 Team Members Led
45%+ Automation Coverage Improvement
60–70% Regression Effort Reduction
30–50% Production Defect Reduction
1-Day Release Validation

Use these metrics from the resume.

===========================================================
5. SIDEBAR
===========================================================

Create a professional sidebar with:

Profile photo

Vijay Kumar Kothapalli

Lead Software Engineer

Navigation:

🏠 Home
👨‍💻 About
💼 Experience
🧠 AI & GenAI
🧪 Quality Engineering
⚙️ Automation
☁️ Cloud & DevOps
🏦 Banking Domain
🎓 Education & Certifications
📊 Skills Dashboard
📁 Projects
📞 Contact

Add a theme toggle if practical.

===========================================================
6. TAB-BASED MAIN UI
===========================================================

Create the following major tabs:

TAB 1 — EXECUTIVE PROFILE

Include:

- Professional summary
- Career highlights
- Leadership strengths
- Core expertise
- Key achievements

Create visual cards for:

Quality Engineering
Test Automation
AI Testing
Agentic AI
SDET Leadership
Cloud & DevOps
Banking Technology
API & Microservices Testing

===========================================================

TAB 2 — CAREER JOURNEY

Create a beautiful horizontal/vertical interactive timeline.

Display:

Wells Fargo
Lead Software Engineer
Oct 2021 – Present

Dun & Bradstreet
Senior SDET
Mar 2021 – Oct 2021

Wells Fargo
Senior Quality Engineer
Aug 2016 – Mar 2021

S&P Global
Quality Engineer II
2015 – Aug 2016

Syntel Ltd
Software Engineer
Nov 2011 – Nov 2015

For every organization show:

- Role
- Duration
- Responsibilities
- Achievements
- Technologies
- Leadership scope

Use expandable sections or cards.

===========================================================
TAB 3 — LEADERSHIP & QUALITY ENGINEERING

Create an executive dashboard showing:

Team Leadership
Quality Strategy
Test Strategy
Quality Gates
Release Readiness
Shift-Left Testing
CI/CD
Defect Management
RCA
Test Metrics
Stakeholder Management
Agile/Scrum

Create graphical KPI cards.

Include:

"Currently leading a team of 9 members for Quality Engineering functions
across web, mobile, API and enterprise applications."

Create a leadership capability radar chart using Plotly.

Categories:

Leadership
Automation
Quality Engineering
AI Testing
Architecture
Cloud
DevOps
Banking Domain

===========================================================
TAB 4 — AI / GENAI / AGENTIC AI

This should be one of the strongest sections.

Create a visually impressive AI architecture section.

Show:

Generative AI
LLMs
AI Agents
LangChain
LangGraph
RAG
MCP
Prompt Engineering
AI-Assisted Testing
GenAI Test Generation
Synthetic Test Data
Self-Healing Automation

Create an architecture diagram using HTML/CSS or Plotly:

User
 ↓
AI Agent
 ↓
LangChain / LangGraph
 ↓
RAG
 ↓
Knowledge/Data Sources
 ↓
LLM
 ↓
Tool / MCP Layer
 ↓
Automation / Testing
 ↓
Quality Results

Highlight:

"Built and deployed Agentic RAG AI solutions using LangChain,
developed MCP-based AI agents, and deployed agentic solutions
within Wells Fargo."

Create an "AI Capability Matrix".

===========================================================
TAB 5 — TEST AUTOMATION

Create an interactive automation dashboard.

Technology categories:

UI Automation:
- Selenium
- Playwright
- Appium

Programming:
- Java
- Python
- JavaScript
- TypeScript
- C#
- SQL

API:
- REST API
- REST Assured
- Postman
- Swagger
- OpenAPI
- SOAP UI
- GraphQL

BDD/Test:
- TestNG
- JUnit
- Cucumber

Create Plotly visualizations showing the technology ecosystem.

Create cards for:

Web Automation
Mobile Automation
API Automation
Microservices Testing
Data Validation
Regression Automation
Parallel Execution
CI/CD Automation

===========================================================
TAB 6 — MOBILE TESTING

Create a dedicated mobile testing section.

Highlight experience in:

Android
iOS

Testing types:

Functional Testing
Regression Testing
Integration Testing
End-to-End Testing
Smoke Testing
System Testing

Show:

Android → Appium → Automation Framework
iOS → Appium → Automation Framework

Use an attractive mobile-device style visualization if practical.

===========================================================
TAB 7 — CLOUD & DEVOPS

Create a cloud/DevOps dashboard.

Cloud:

AWS
Azure

AWS services:

Lambda
Step Functions
AWS SDK

DevOps:

Jenkins
Azure DevOps
GitHub
Bitbucket
Maven
Gradle
Docker

Show a CI/CD pipeline:

Code
 ↓
Git
 ↓
Build
 ↓
Automated Testing
 ↓
API/UI/Mobile Tests
 ↓
Quality Gates
 ↓
Deployment
 ↓
Release Validation

Use cards and icons.

===========================================================
TAB 8 — BANKING & FINANCIAL DOMAIN

Create a dedicated domain expertise page.

Display:

Banking & Financial Services

Core areas:

Payment Processing
Core Banking
Commercial Lending
Liquidity Management
Financial Analytics

Technologies/platforms mentioned in the profile:

PACS
Flexcube / FCUBS
CBAM
OBLM

Create a visual domain map.

Example:

Banking
├── Payment Processing
├── Core Banking
├── Commercial Lending
├── Liquidity Management
└── Financial Analytics

===========================================================
TAB 9 — SKILLS DASHBOARD

Create an interactive skills dashboard.

Group skills into:

AI & GenAI
Programming
Automation
API Testing
Mobile Testing
Cloud
DevOps
Databases
Test Management
Integration
Agile
Banking

Use:

- Plotly radar charts
- Donut charts
- Bar charts
- Technology cards
- Skill badges

Do NOT invent skill proficiency percentages.

If proficiency values are required for visualization,
either:
1. Clearly label them as "illustrative", OR
2. Avoid numerical proficiency and use category-based visualizations.

===========================================================
TAB 10 — ACHIEVEMENTS

Create a high-impact achievement dashboard.

Show these achievements prominently:

Automation coverage increased by 45%+
Regression effort reduced by 60–70%
Release validation reduced to one day
Production defects reduced by 30–50%
Led a team of 9 QE professionals
Built Agentic RAG AI solutions
Developed MCP-based AI agents
Integrated automated testing into CI/CD

Use large KPI cards and charts.

===========================================================
TAB 11 — EDUCATION & CERTIFICATIONS

Education:

B.Tech (Information Technology)
JNT University, Kakinada
2007 – 2011

Certifications / Training:

ISTQB Certified Tester Foundation Level
Selenium Test Automation
REST API Testing & Automation
Agile & Scrum Practitioner
AWS Cloud Practitioner / Cloud Fundamentals
Playwright Test Automation
Generative AI & Prompt Engineering
AI-Assisted Software Testing and Quality Engineering
DevOps & CI/CD
Anthropic Certified: Claude Code 101
Microsoft Certified: Azure Developer Associate

Create certificate cards.

===========================================================
TAB 12 — PROJECTS / KEY INITIATIVES
===========================================================

Create project cards based ONLY on projects and initiatives supported
by the resume.

Examples:

1. Enterprise Test Automation Framework
2. Agentic RAG AI
3. MCP-Based AI Agents
4. AI-Powered Testing
5. Commercial Lending Automation
6. AWS Step Functions Automation
7. CI/CD Continuous Testing
8. Mobile Automation Framework

Each card should contain:

Project
Objective
Technology
Business Impact
Role

Do not invent project names or unsupported business details.

===========================================================
7. GRAPHICAL DASHBOARD
===========================================================

Use Plotly extensively but intelligently.

Create:

1. Career timeline
2. Technology ecosystem
3. Leadership radar
4. Skills category chart
5. Achievement KPI dashboard
6. Cloud/DevOps pipeline
7. AI architecture
8. Automation architecture
9. Banking domain map

Charts must be clean and executive-friendly.

Avoid unnecessary charts.

===========================================================
8. SMART INTERACTIVE FEATURES
===========================================================

Add:

- Search skills
- Filter technologies by category
- Expand/collapse experience
- Interactive project cards
- Hover tooltips
- Download resume
- LinkedIn button
- Email button
- Contact section
- Responsive layout

Create a "What I Bring" section:

✓ Quality Engineering Leadership
✓ Enterprise Automation Architecture
✓ AI-Powered Testing
✓ Agentic AI
✓ RAG
✓ MCP
✓ CI/CD
✓ Banking Domain Expertise
✓ Mobile Testing
✓ API & Microservices Testing

===========================================================
9. SMART "HIRING MANAGER VIEW"
===========================================================

Add a special section/button:

"🎯 Hiring Manager View"

When clicked, show a concise executive summary:

Why Vijay?

• 14+ years enterprise engineering experience
• Quality Engineering leadership
• Team leadership experience
• Strong automation architecture
• AI/GenAI testing expertise
• Agentic RAG AI development
• MCP-based AI agents
• Banking & Financial Services expertise
• Web, Mobile and API testing
• Cloud & DevOps experience

Then show:

Best-fit roles:

Lead Software Engineer
SDET Lead
Principal SDET
QA Automation Architect
Quality Engineering Lead
AI Testing Lead
AI Quality Engineering Architect
Agentic AI Quality Architect

Do not claim that these are current job applications.
Present them only as suitable professional roles.

===========================================================
10. CONTACT SECTION
===========================================================

Create a premium contact card.

Name:
Vijay Kumar Kothapalli

Title:
Lead Software Engineer

Location:
Hyderabad, India

Email:
vijay8689@hotmail.com

LinkedIn:
https://www.linkedin.com/in/vijay-kumar-kothapalli-1963351a/

Buttons:

📧 Email Me
🔗 LinkedIn
📄 Download Resume

===========================================================
11. PRIVACY
===========================================================

IMPORTANT:

Do NOT display sensitive personal information from the resume publicly.

Do NOT display:

- Date of Birth
- Passport number
- Passport validity
- Any sensitive personal identification information

The public portfolio should focus on professional information only.

===========================================================
12. RESUME DOWNLOAD
===========================================================

Provide a "Download Resume" button.

The application should support placing the resume PDF/DOCX
inside the project assets folder.

Use a configurable file path rather than hardcoding
an environment-specific path.

===========================================================
13. RESPONSIVE UI
===========================================================

The application must work well on:

Desktop
Laptop
Tablet
Mobile

Use Streamlit columns carefully.

Do not create extremely wide layouts that become unreadable.

===========================================================
14. STREAMLIT BEST PRACTICES
===========================================================

Use:

st.set_page_config()

with:

page_title
page_icon
layout="wide"

Use reusable functions.

Example:

render_header()
render_metric_card()
render_experience()
render_skill_dashboard()
render_ai_section()
render_contact()

Avoid putting everything into one huge function.

Keep data separate from UI.

Use dictionaries/data structures for:

experience
skills
certifications
projects
achievements

===========================================================
15. PERFORMANCE
===========================================================

The application should be lightweight and fast.

Use:

@st.cache_data

where appropriate.

Do not make unnecessary external API calls.

The portfolio must work without requiring external databases.

No login required.

No external backend required.

===========================================================
16. DEPLOYMENT
===========================================================

Generate:

requirements.txt

with only required packages.

Example:

streamlit
plotly
pandas

Include a README.md containing:

1. Project overview
2. Local setup
3. Installation
4. Running Streamlit
5. GitHub deployment
6. Streamlit Community Cloud deployment
7. Folder structure
8. How to replace profile image
9. How to replace resume
10. Configuration instructions

The application should be GitHub-ready.

===========================================================
17. CODE QUALITY
===========================================================

Follow:

PEP8
Clean architecture
Reusable components
Meaningful function names
Type hints where useful
Comments for important sections
No unnecessary complexity

Do not use paid services.

Do not require API keys.

Do not require Docker for basic deployment.

===========================================================
18. FINAL UI EXPERIENCE
===========================================================

The final page should feel like:

"An AI-powered Quality Engineering leader's professional command center."

It should immediately communicate:

WHO I AM
WHAT I DO
WHAT I HAVE ACHIEVED
WHAT TECHNOLOGIES I KNOW
WHAT I HAVE BUILT
WHAT DOMAINS I KNOW
WHAT LEADERSHIP EXPERIENCE I HAVE
HOW TO CONTACT ME

The first screen should be visually impressive enough that a recruiter
or hiring manager understands my profile within 10–15 seconds.

===========================================================
19. OUTPUT REQUIRED
===========================================================

Generate the complete working project.

Provide:

1. app.py
2. data/profile.py
3. components/sidebar.py
4. components/header.py
5. components/cards.py
6. components/charts.py
7. components/timeline.py
8. requirements.txt
9. README.md
10. .gitignore

Make sure all imports work.

Do not provide pseudo-code.

Provide complete runnable code.

Before finishing, verify:

- No syntax errors
- No missing imports
- No undefined variables
- Streamlit application can start with:
  streamlit run app.py
- All tabs render correctly
- Charts render correctly
- Resume download works when resume file exists
- LinkedIn and email buttons work
- UI remains usable on smaller screens
- No sensitive personal information is exposed