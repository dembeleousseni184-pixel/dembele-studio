from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import urllib.parse

app = FastAPI()

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dembélé Studio | Web Developer & Designer</title>
    <!-- AOS Animation CSS -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        :root {
            --bg-brand-dark: #0f172a;
            --bg-card: #1e293b;
            --text-main: #f8fafc;
            --accent-green: #10b981;
        }
        
        /* Support du mode clair */
        html:not(.dark) {
            --bg-brand-dark: #f8fafc;
            --bg-card: #ffffff;
            --text-main: #0f172a;
        }

        body {
            background-color: var(--bg-brand-dark);
            color: var(--text-main);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            scroll-behavior: smooth;
            transition: background-color 0.3s, color 0.3s;
        }

        header {
            background: var(--bg-card);
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid #334155;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }

        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--accent-green);
        }

        .nav-links {
            list-style: none;
            display: flex;
            gap: 2rem;
            align-items: center;
            margin: 0;
        }

        .nav-links a {
            color: var(--text-main);
            text-decoration: none;
            transition: color 0.3s;
            font-weight: 500;
        }

        .nav-links a:hover {
            color: var(--accent-green);
        }

        #theme-toggle {
            background: none;
            border: 1px solid #334155;
            color: var(--text-main);
            padding: 0.5rem;
            border-radius: 0.5rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .hero {
            padding: 6rem 2rem;
            text-align: center;
            max-width: 900px;
            margin: 0 auto;
        }

        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            line-height: 1.2;
        }

        .hero p {
            color: #94a3b8;
            font-size: 1.25rem;
            margin-bottom: 2rem;
        }

        .stats-container {
            display: flex;
            justify-content: center;
            gap: 4rem;
            margin-top: 3rem;
        }

        .stat-item h3 {
            font-size: 2.5rem;
            color: var(--accent-green);
            margin: 0;
        }

        .stat-item p {
            font-size: 0.95rem;
            margin: 0.5rem 0 0 0;
        }

        .btn-primary {
            background-color: var(--accent-green);
            color: #0f172a;
            padding: 0.85rem 2rem;
            border-radius: 0.5rem;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            cursor: pointer;
            border: none;
            transition: opacity 0.3s, transform 0.2s;
        }

        .btn-primary:hover {
            opacity: 0.9;
            transform: translateY(-2px);
        }

        .services, .portfolio {
            max-width: 1200px;
            margin: 5rem auto;
            padding: 0 2rem;
        }

        .section-title {
            text-align: center;
            margin-bottom: 3rem;
            font-size: 2.2rem;
        }

        .services-grid, .portfolio-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
        }

        .service-card, .portfolio-card {
            background-color: var(--bg-card);
            padding: 2.5rem 2rem;
            border-radius: 1rem;
            border: 1px solid #334155;
            transition: transform 0.3s, border-color 0.3s;
            cursor: pointer;
        }

        .service-card:hover, .portfolio-card:hover {
            transform: translateY(-5px);
            border-color: var(--accent-green);
        }

        .service-card h3, .portfolio-card h3 {
            color: var(--accent-green);
            margin-top: 0;
        }

        /* Filtres du Portfolio */
        .filter-container {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 2.5rem;
            flex-wrap: wrap;
        }

        .filter-btn {
            padding: 0.5rem 1.2rem;
            border-radius: 2rem;
            border: 1px solid #334155;
            background-color: var(--bg-card);
            color: var(--text-main);
            cursor: pointer;
            transition: all 0.3s;
            font-weight: 500;
        }

        .filter-btn.active, .filter-btn:hover {
            background-color: var(--accent-green);
            color: #0f172a;
            border-color: var(--accent-green);
        }

        .contact {
            max-width: 650px;
            margin: 5rem auto;
            padding: 2.5rem;
            background-color: var(--bg-card);
            border-radius: 1rem;
            border: 1px solid #334155;
        }

        .contact-form {
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
            margin-top: 1.5rem;
        }

        .contact-form input,
        .contact-form select,
        .contact-form textarea {
            padding: 0.9rem;
            border-radius: 0.5rem;
            border: 1px solid #475569;
            background-color: var(--bg-brand-dark);
            color: var(--text-main);
            font-size: 1rem;
        }

        /* Modale */
        .modal-overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.8);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }

        .modal-content {
            background-color: var(--bg-card);
            padding: 2rem;
            border-radius: 1rem;
            max-width: 500px;
            width: 90%;
            border: 1px solid #334155;
            text-align: center;
        }

        footer {
            text-align: center;
            padding: 2.5rem;
            color: #64748b;
            border-top: 1px solid #334155;
            margin-top: 5rem;
        }

        .hidden { display: none !important; }
    </style>
</head>
<body>

    <!-- Barre de navigation -->
    <header>
        <nav class="navbar">
            <div class="logo">Dembélé Studio</div>
            <ul class="nav-links">
                <li><a href="#accueil">Accueil</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
                <li>
                    <button id="theme-toggle" title="Changer de thème">
                        <i data-lucide="moon" style="width: 20px; height: 20px;"></i>
                    </button>
                </li>
            </ul>
        </nav>
    </header>

    <!-- Section Accueil -->
    <section id="accueil" class="hero" data-aos="fade-up">
        <h1>Créateur de Solutions Web & Visuels Uniques</h1>
        <p>Développeur web, créateur de logiciels et graphiste freelance basé à Casablanca.</p>
        <a href="#contact" class="btn-primary">Discutons de votre projet</a>

        <div class="stats-container">
            <div class="stat-item">
                <h3 id="counter-projects">0</h3>
                <p>Projets Réussis</p>
            </div>
            <div class="stat-item">
                <h3 id="counter-satisfaction">0</h3>
                <p>Clients Satisfaits</p>
            </div>
        </div>
    </section>

    <!-- Section Services -->
    <section id="services" class="services" data-aos="fade-up">
        <h2 class="section-title">Mes Services</h2>
        <div class="services-grid">
            <div class="service-card" onclick="setService('Développement Web')">
                <h3>Développement Web</h3>
                <p>Applications web sur mesure, plateformes performantes et sites vitrines modernes (FastAPI, Python, JavaScript).</p>
            </div>
            <div class="service-card" onclick="setService('Design & Branding')">
                <h3>Design & Branding</h3>
                <p>Conceptions graphiques percutantes, identités visuelles, logos, affiches et flyers professionnels.</p>
            </div>
            <div class="service-card" onclick="setService('Solutions Logicielles')">
                <h3>Solutions Logicielles</h3>
                <p>Outils de gestion adaptés à vos besoins métiers et automatisation des flux de travail.</p>
            </div>
        </div>
    </section>

    <!-- Section Portfolio -->
    <section id="portfolio" class="portfolio" data-aos="fade-up">
        <h2 class="section-title">Portfolio & Réalisations</h2>
        
        <!-- Boutons de filtrage -->
        <div class="filter-container">
            <button class="filter-btn active" data-filter="all">Tous</button>
            <button class="filter-btn" data-filter="web">Apps & Web</button>
            <button class="filter-btn" data-filter="design">Affiches & Visuels</button>
        </div>

        <div class="portfolio-grid">
            <div class="portfolio-item portfolio-card" data-category="web" onclick="openModal('Demshop POS', 'Application de point de vente et gestion de stock développée avec FastAPI et Python.', 'https://images.unsplash.com/photo-1556742049-0a67d553c2a8')">
                <h3>Demshop POS</h3>
                <p>Système de gestion et caisse enregistreuse moderne.</p>
            </div>
            <div class="portfolio-item portfolio-card" data-category="design" onclick="openModal('Branding Studio', 'Refonte complète de l’identité visuelle et supports publicitaires.', 'https://images.unsplash.com/photo-1626785774573-4b799315345d')">
                <h3>Identité Visuelle</h3>
                <p>Création d'affiches, logos et bannières publicitaires.</p>
            </div>
        </div>
    </section>

    <!-- Section Contact (Redirection WhatsApp) -->
    <section id="contact" class="contact" data-aos="fade-up">
        <h2 style="text-align: center; margin-top: 0;">Contactez-moi</h2>
        <p style="text-align: center; color: #94a3b8;">Un projet en tête ? Remplissez ce formulaire pour m'écrire directement sur WhatsApp.</p>
        
        <form id="contact-form" class="contact-form">
            <input type="text" name="name" placeholder="Votre nom complet" required>
            <input type="email" name="email" placeholder="Votre adresse email" required>
            <select name="project_type" id="project_type">
                <option value="Développement Web">Développement Web</option>
                <option value="Design & Branding">Design & Branding</option>
                <option value="Solutions Logicielles">Solutions Logicielles</option>
            </select>
            <textarea name="description" placeholder="Parlez-moi en détail de votre projet..." rows="5" required></textarea>
            <button type="submit" class="btn-primary" style="width: 100%;">Envoyer sur WhatsApp</button>
        </form>
        <div id="form-status" class="hidden" style="margin-top: 1rem; padding: 0.75rem; text-align: center; border-radius: 0.5rem; font-size: 0.9rem;"></div>
    </section>

    <!-- Modale de prévisualisation -->
    <div id="portfolio-modal" class="modal-overlay hidden">
        <div class="modal-content">
            <h3 id="modal-title" style="color: var(--accent-green); margin-top: 0;"></h3>
            <p id="modal-desc" style="color: #94a3b8;"></p>
            <button onclick="closeModal()" class="btn-primary" style="margin-top: 1rem;">Fermer</button>
        </div>
    </div>

    <footer>
        <p>&copy; 2026 Dembélé Studio. Tous droits réservés.</p>
    </footer>

    <!-- Scripts Externes -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof lucide !== 'undefined') { lucide.createIcons(); }
            if (typeof AOS !== 'undefined') { AOS.init({ duration: 800, once: true }); }

            // Thème clair / sombre
            const themeToggleBtn = document.getElementById('theme-toggle');
            const htmlElement = document.documentElement;
            if (localStorage.getItem('theme') === 'light') {
                htmlElement.classList.remove('dark');
            }

            if (themeToggleBtn) {
                themeToggleBtn.addEventListener('click', () => {
                    if (htmlElement.classList.contains('dark')) {
                        htmlElement.classList.remove('dark');
                        localStorage.setItem('theme', 'light');
                    } else {
                        htmlElement.classList.add('dark');
                        localStorage.setItem('theme', 'dark');
                    }
                });
            }

            // Compteurs animés
            animateCounter('counter-projects', 0, 35, 2000);
            animateCounter('counter-satisfaction', 0, 100, 2000, '%');

            // Filtrage Portfolio
            const filterButtons = document.querySelectorAll('.filter-btn');
            const portfolioItems = document.querySelectorAll('.portfolio-item');

            filterButtons.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterButtons.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');

                    const filter = btn.getAttribute('data-filter');
                    portfolioItems.forEach(item => {
                        if (filter === 'all' || item.getAttribute('data-category') === filter) {
                            item.style.display = 'block';
                        } else {
                            item.style.display = 'none';
                        }
                    });
                });
            });

            // Soumission formulaire -> WhatsApp
            const contactForm = document.getElementById('contact-form');
            const formStatus = document.getElementById('form-status');

            if (contactForm) {
                contactForm.addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const formData = new FormData(contactForm);

                    formStatus.classList.remove('hidden');
                    formStatus.style.backgroundColor = 'rgba(16, 185, 129, 0.2)';
                    formStatus.style.color = '#34d399';
                    formStatus.textContent = "Préparation du message WhatsApp...";

                    try {
                        const response = await fetch('/api/contact', {
                            method: 'POST',
                            body: formData
                        });
                        const result = await response.json();

                        if (response.ok && result.whatsapp_url) {
                            formStatus.textContent = result.message;
                            contactForm.reset();
                            setTimeout(() => {
                                window.open(result.whatsapp_url, '_blank');
                            }, 1000);
                        } else {
                            throw new Error();
                        }
                    } catch (err) {
                        formStatus.style.backgroundColor = 'rgba(239, 68, 68, 0.2)';
                        formStatus.style.color = '#f87171';
                        formStatus.textContent = "Erreur. Contactez directement le +225 05 44 58 01 83.";
                    }
                });
            }
        });

        function animateCounter(id, start, end, duration, suffix = '+') {
            const obj = document.getElementById(id);
            if (!obj) return;
            let startTimestamp = null;
            const step = (timestamp) => {
                if (!startTimestamp) startTimestamp = timestamp;
                const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                obj.innerHTML = Math.floor(progress * (end - start) + start) + suffix;
                if (progress < 1) { window.requestAnimationFrame(step); }
            };
            window.requestAnimationFrame(step);
        }

        function setService(serviceName) {
            const select = document.getElementById('project_type');
            if (select) { select.value = serviceName; }
            window.location.href = '#contact';
        }

        function openModal(title, desc) {
            document.getElementById('modal-title').textContent = title;
            document.getElementById('modal-desc').textContent = desc;
            document.getElementById('portfolio-modal').classList.remove('hidden');
        }

        function closeModal() {
            document.getElementById('portfolio-modal').classList.add('hidden');
        }
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML_CONTENT

@app.post("/api/contact")
async def handle_contact(
    name: str = Form(...),
    email: str = Form(...),
    project_type: str = Form(default="Non spécifié"),
    description: str = Form(...)
):
    whatsapp_number = "+2250544580183"
    wa_message = (
        f"Bonjour Dembélé Studio 👋\n\n"
        f"Je m'appelle *{name}*.\n"
        f"Email : {email}\n"
        f"Service : *{project_type}*\n\n"
        f"Détails :\n{description}"
    )
    encoded_message = urllib.parse.quote(wa_message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"
    
    return {
        "message": "Redirection vers WhatsApp en cours...",
        "whatsapp_url": whatsapp_url
    }
