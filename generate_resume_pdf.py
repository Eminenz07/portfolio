import os
import subprocess

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Adebayo Eminence Adeoluwa - Resume</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  @page {
    size: A4;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  html, body {
    height: 100%;
  }
  body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #1a1d20;
    background-color: #ffffff;
    line-height: 1.38;
    font-size: 11.5px;
    padding: 20px 26px;
    max-width: 210mm;
    margin: 0 auto;
  }

  /* Header */
  .header {
    border-bottom: 2px solid #0f172a;
    padding-bottom: 8px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .header-left {
    flex: 1;
  }
  .name {
    font-size: 22px;
    font-weight: 800;
    letter-spacing: -0.025em;
    color: #090d16;
    text-transform: uppercase;
    line-height: 1.1;
  }
  .title {
    font-size: 12.8px;
    font-weight: 600;
    color: #3b49df;
    letter-spacing: -0.01em;
    margin-top: 3px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .title-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.8px;
    background: #eef2ff;
    color: #3730a3;
    padding: 1px 6px;
    border-radius: 4px;
    font-weight: 600;
  }
  .contacts {
    text-align: right;
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #475569;
    line-height: 1.5;
  }
  .contacts a {
    color: #1e293b;
    text-decoration: none;
    font-weight: 600;
  }
  .contacts a:hover {
    color: #3b49df;
  }
  .contacts .separator {
    color: #cbd5e1;
    margin: 0 4px;
  }

  /* Sections */
  .section {
    margin-bottom: 9px;
  }
  .section-title {
    font-size: 11.2px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #0f172a;
    display: flex;
    align-items: center;
    gap: 6px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 2px;
    margin-bottom: 6px;
  }
  .section-title span.badge-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    color: #64748b;
    font-weight: 600;
  }

  /* Summary */
  .summary-text {
    color: #334155;
    font-size: 11px;
    line-height: 1.44;
    text-align: justify;
  }
  .summary-text strong {
    color: #0f172a;
    font-weight: 600;
  }

  /* Skills Grid */
  .skills-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px 14px;
    font-size: 11px;
  }
  .skill-group {
    display: flex;
    align-items: baseline;
    gap: 5px;
    line-height: 1.3;
  }
  .skill-cat {
    font-weight: 700;
    color: #0f172a;
    min-width: 104px;
    font-size: 10.5px;
    letter-spacing: -0.01em;
  }
  .skill-list {
    color: #334155;
    flex: 1;
  }
  .pill {
    display: inline-block;
    background: #f1f5f9;
    color: #0f172a;
    padding: 0px 4.5px;
    border-radius: 3px;
    font-size: 9.8px;
    font-family: 'JetBrains Mono', monospace;
    margin-right: 2.5px;
    margin-bottom: 1.5px;
    border: 1px solid #e2e8f0;
    font-weight: 500;
  }

  /* Experience & Projects Items */
  .item {
    margin-bottom: 0;
  }
  .item-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 2px;
  }
  .item-role {
    font-size: 12.2px;
    font-weight: 700;
    color: #0f172a;
  }
  .item-company {
    font-weight: 600;
    color: #3b49df;
  }
  .item-date {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.8px;
    color: #64748b;
    font-weight: 600;
  }
  .item-bullets {
    list-style: none;
    padding-left: 0;
    margin-top: 1px;
  }
  .item-bullets li {
    position: relative;
    padding-left: 11px;
    margin-bottom: 2px;
    color: #334155;
    font-size: 11px;
    line-height: 1.34;
  }
  .item-bullets li::before {
    content: "▹";
    position: absolute;
    left: 0;
    color: #3b49df;
    font-size: 9.5px;
  }
  .item-bullets li strong {
    color: #0f172a;
    font-weight: 600;
  }

  /* Project Specifics */
  .project-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px 12px;
  }
  .project-card {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 5px 8px;
  }
  .project-title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1px;
  }
  .project-name {
    font-size: 11.5px;
    font-weight: 700;
    color: #0f172a;
  }
  .project-links {
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.2px;
  }
  .project-links a {
    color: #3b49df;
    text-decoration: none;
    font-weight: 600;
    margin-left: 5px;
  }
  .project-tech {
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.8px;
    color: #64748b;
    margin-bottom: 2px;
    font-weight: 500;
  }
  .project-detail {
    font-size: 10.5px;
    color: #334155;
    line-height: 1.28;
  }

  /* Bottom Dual Columns (Education, Certs & Awards) */
  .bottom-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }
  .sub-item {
    margin-bottom: 3px;
  }
  .sub-title {
    font-size: 11.2px;
    font-weight: 700;
    color: #0f172a;
  }
  .sub-sub {
    font-size: 10.5px;
    color: #475569;
    display: flex;
    justify-content: space-between;
  }
</style>
</head>
<body>

  <!-- Header -->
  <header class="header">
    <div class="header-left">
      <h1 class="name">Adebayo Eminence Adeoluwa</h1>
      <div class="title">
        Full-Stack Software Engineer
        <span class="title-tag">Python / Django / JavaScript</span>
      </div>
    </div>
    <div class="contacts">
      <div>📍 Lagos, Nigeria (UTC+1 · Remote-Friendly)</div>
      <div>
        <a href="mailto:emmyadeoluwa@gmail.com">emmyadeoluwa@gmail.com</a>
        <span class="separator">|</span>
        <a href="tel:+2349073601282">+234 907 360 1282</a>
      </div>
      <div>
        <a href="https://portfolio-ma77.onrender.com/" target="_blank">portfolio-ma77.onrender.com</a>
        <span class="separator">|</span>
        <a href="https://github.com/Eminenz07" target="_blank">github.com/Eminenz07</a>
        <span class="separator">|</span>
        <a href="https://x.com/Emidveloper" target="_blank">@Emidveloper</a>
      </div>
    </div>
  </header>

  <!-- Summary -->
  <section class="section">
    <div class="section-title"><span class="badge-num">01 //</span> Professional Summary</div>
    <p class="summary-text">
      <strong>Results-driven Full-Stack Software Engineer</strong> with extensive experience architecting and shipping reliable, scalable web applications, real-time engines, and RESTful APIs. Proficient across the entire software development lifecycle with deep expertise in <strong>Python, Django, Django Channels (WebSockets), JavaScript, HTMX, Docker, and PostgreSQL</strong>. Proven track record of turning complex operational challenges into elegant, production-grade applications with a strong focus on clean system architecture, data security, and seamless user experiences.
    </p>
  </section>

  <!-- Technical Skills -->
  <section class="section">
    <div class="section-title"><span class="badge-num">02 //</span> Technical Skills & Stack</div>
    <div class="skills-container">
      <div class="skill-group">
        <span class="skill-cat">Languages:</span>
        <span class="skill-list">
          <span class="pill">Python</span>
          <span class="pill">JavaScript (ES6+)</span>
          <span class="pill">SQL</span>
          <span class="pill">HTML5</span>
          <span class="pill">CSS3</span>
          <span class="pill">Java</span>
          <span class="pill">C/C++</span>
        </span>
      </div>
      <div class="skill-group">
        <span class="skill-cat">Backend & Web:</span>
        <span class="skill-list">
          <span class="pill">Django</span>
          <span class="pill">Django REST Framework</span>
          <span class="pill">Django Channels</span>
          <span class="pill">Flask</span>
          <span class="pill">HTMX</span>
          <span class="pill">WebSockets</span>
        </span>
      </div>
      <div class="skill-group">
        <span class="skill-cat">Data & Cache:</span>
        <span class="skill-list">
          <span class="pill">PostgreSQL</span>
          <span class="pill">SQLite</span>
          <span class="pill">Redis</span>
          <span class="pill">ORM Optimization</span>
        </span>
      </div>
      <div class="skill-group">
        <span class="skill-cat">DevOps & Cloud:</span>
        <span class="skill-list">
          <span class="pill">Docker</span>
          <span class="pill">Google Cloud Run</span>
          <span class="pill">Render</span>
          <span class="pill">Fly.io</span>
          <span class="pill">Linux / VPS</span>
          <span class="pill">Git / GitHub</span>
          <span class="pill">Nginx / Gunicorn</span>
        </span>
      </div>
      <div class="skill-group" style="grid-column: span 2;">
        <span class="skill-cat">APIs & Integrations:</span>
        <span class="skill-list">
          <span class="pill">Paystack Payment Gateway</span>
          <span class="pill">Tesseract OCR</span>
          <span class="pill">Poppler PDF Engine</span>
          <span class="pill">JWT & Session Auth</span>
          <span class="pill">RESTful API Design</span>
          <span class="pill">Postman</span>
        </span>
      </div>
    </div>
  </section>

  <!-- Work Experience -->
  <section class="section">
    <div class="section-title"><span class="badge-num">03 //</span> Work Experience</div>
    <div class="item">
      <div class="item-header">
        <div>
          <span class="item-role">Full Stack Developer</span>
          <span style="color:#64748b;margin:0 4px;">•</span>
          <span class="item-company">Helix Mind Start-Up</span>
        </div>
        <span class="item-date">2023 – Present</span>
      </div>
      <ul class="item-bullets">
        <li>Architected and delivered scalable, full-stack web applications and robust backend APIs utilizing <strong>Django, Python, JavaScript, and SQL</strong>.</li>
        <li>Implemented secure authentication workflows, role-based access control (RBAC), and efficient database models, boosting query speeds and throughput.</li>
        <li>Engineered interactive front-end interfaces, internal administrative dashboards, and client-facing tools using modern CSS and modular JavaScript.</li>
        <li>Collaborated with agile engineering teams in high-pressure development sprints, ensuring clean git workflows, continuous testing, and rapid feature deployment.</li>
      </ul>
    </div>
  </section>

  <!-- Key Engineering Projects -->
  <section class="section">
    <div class="section-title"><span class="badge-num">04 //</span> Featured Engineering Projects</div>
    <div class="project-grid">

      <!-- The Truth Gate -->
      <div class="project-card">
        <div class="project-title">
          <span class="project-name">The Truth Gate</span>
          <div class="project-links">
            <a href="https://the-truth-gate.onrender.com/" target="_blank">Live Demo ↗</a>
            <a href="https://github.com/Eminenz07/the_truth_gate" target="_blank">GitHub ↗</a>
          </div>
        </div>
        <div class="project-tech">Django 5 · Channels · Redis · WebSockets · PostgreSQL · Paystack</div>
        <p class="project-detail">
          Institutional-grade platform with real-time private counselling via WebSocket channels, filtered sermon catalog, community testimonies moderation, and automated Paystack payments.
        </p>
      </div>

      <!-- Trade With Ariel -->
      <div class="project-card">
        <div class="project-title">
          <span class="project-name">Trade With Ariel</span>
          <div class="project-links">
            <a href="https://tradewithariel.onrender.com/" target="_blank">Live Demo ↗</a>
            <a href="https://github.com/Eminenz07/tradewithariel" target="_blank">GitHub ↗</a>
          </div>
        </div>
        <div class="project-tech">Django · Python · Glassmorphic CSS · Vanilla JS · Render</div>
        <p class="project-detail">
          High-conversion fintech brand portal featuring custom glassmorphism design and a bespoke Django CMS backend powering live mentorship tiers, analytics, and offers.
        </p>
      </div>

      <!-- SubDoc -->
      <div class="project-card">
        <div class="project-title">
          <span class="project-name">SubDoc (PDF-to-Word Engine)</span>
          <div class="project-links">
            <a href="https://subdoc-582204185999.us-central1.run.app/" target="_blank">Live Demo ↗</a>
            <a href="https://github.com/Eminenz07/subdoc" target="_blank">GitHub ↗</a>
          </div>
        </div>
        <div class="project-tech">Flask · Python · Docker · Tesseract OCR · Google Cloud Run</div>
        <p class="project-detail">
          Stateless, privacy-centric document conversion engine equipped with Tesseract OCR fallback for scanned PDFs, drag-and-drop UI, and serverless Cloud Run containerization.
        </p>
      </div>

      <!-- AU Voting System -->
      <div class="project-card">
        <div class="project-title">
          <span class="project-name">AU Voting & Election Platform</span>
          <div class="project-links">
            <a href="https://au-voting-system-chi.vercel.app/" target="_blank">Live Demo ↗</a>
            <a href="https://github.com/Eminenz07/voting-system2" target="_blank">GitHub ↗</a>
          </div>
        </div>
        <div class="project-tech">Django · SQLite · Bootstrap 5 · Python · Vercel</div>
        <p class="project-detail">
          Secure election portal facilitating multi-candidate management, dynamic vote verification, real-time ballot aggregation, and tamper-resistant audit reporting.
        </p>
      </div>

      <!-- Django Blog API & CMS -->
      <div class="project-card">
        <div class="project-title">
          <span class="project-name">Django REST API & Admin CMS</span>
          <div class="project-links">
            <a href="https://django-blog-api-292e.onrender.com/" target="_blank">Live Demo ↗</a>
            <a href="https://github.com/Eminenz07/django-blog-api" target="_blank">GitHub ↗</a>
          </div>
        </div>
        <div class="project-tech">Django REST Framework · HTMX · SQLite · CSS · Render</div>
        <p class="project-detail">
          Modular RESTful API ecosystem featuring granular permission schemas, Token authentication, CRUD endpoints, and lightweight reactive HTMX frontend interfaces.
        </p>
      </div>

      <!-- Virtual Assistant Portfolio -->
      <div class="project-card">
        <div class="project-title">
          <span class="project-name">VA Brand Showcase Platform</span>
          <div class="project-links">
            <a href="https://excellenceeniola.fly.dev/" target="_blank">Live Demo ↗</a>
            <a href="https://github.com/Eminenz07/virtual-assistant-portfolio" target="_blank">GitHub ↗</a>
          </div>
        </div>
        <div class="project-tech">HTML5 · CSS3 · Modern JavaScript · Fly.io</div>
        <p class="project-detail">
          Sleek client portfolio website featuring booking integration, interactive service showcases, responsive customer testimonial carousels, and global CDN delivery.
        </p>
      </div>

    </div>
  </section>

  <!-- Bottom Grid: Education, Certifications & Honors -->
  <section class="section" style="margin-bottom: 0;">
    <div class="bottom-grid">
      <!-- Education & Certifications -->
      <div>
        <div class="section-title"><span class="badge-num">05 //</span> Education & Certifications</div>
        <div class="sub-item">
          <div class="sub-title">Bachelor of Science (B.Sc.) in Computer Science</div>
          <div class="sub-sub"><span>Undergraduate Program</span> <span style="font-family:'JetBrains Mono';font-size:9.5px;font-weight:600;">In Progress</span></div>
        </div>
        <div class="sub-item" style="margin-top: 3px;">
          <div class="sub-title" style="font-size:10.8px;">Certifications & Credentials</div>
          <div style="font-size:10.5px;color:#334155;line-height:1.35;">
            • <strong>Full Stack Development</strong> – Udemy<br/>
            • <strong>Web Development Specialist</strong> – Programming Hub
          </div>
        </div>
      </div>

      <!-- Honors & Achievements -->
      <div>
        <div class="section-title"><span class="badge-num">06 //</span> Honors & Achievements</div>
        <div class="sub-item">
          <div class="sub-title">4th Place – National Hackathon</div>
          <div style="font-size:10.5px;color:#334155;line-height:1.32;margin-top:1px;">
            Recognized for innovative problem-solving, rapid prototyping, and delivering clean, production-ready full-stack software.
          </div>
        </div>
        <div class="sub-item" style="margin-top: 3px;">
          <div class="sub-title">Rapid Prototyping & Agile Commendation</div>
          <div style="font-size:10.5px;color:#334155;line-height:1.32;margin-top:1px;">
            Commended for agile feature delivery, sprint collaboration, and translating product specifications into functional codebases.
          </div>
        </div>
      </div>
    </div>
  </section>

</body>
</html>
"""

def generate_pdf():
    html_file = os.path.abspath("resume_temp.html")
    pdf_file = os.path.abspath("static/pdf/my_resume.pdf")

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE)

    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    ]
    browser_exe = None
    for p in edge_paths:
        if os.path.exists(p):
            browser_exe = p
            break

    if not browser_exe:
        raise RuntimeError("No suitable browser executable found for PDF generation.")

    cmd = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={pdf_file}",
        html_file
    ]

    print("Running PDF conversion:", " ".join(cmd))
    res = subprocess.run(cmd, capture_output=True, text=True)
    print("Return code:", res.returncode)

    if os.path.exists(pdf_file):
        print(f"Successfully generated PDF resume at: {pdf_file} ({os.path.getsize(pdf_file)} bytes)")
    else:
        print("Failed to generate PDF.")

if __name__ == "__main__":
    generate_pdf()
