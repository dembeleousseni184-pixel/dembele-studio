from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import urllib.parse

app = FastAPI()

# HTML, CSS et JS intégrés directement dans le fichier unique
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dembélé Studio | Web Developer & Designer</title>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        :root {
            --bg-brand-dark: #0f172a;
            --bg-card: #1e293b;
            --text-main: #f8fafc;
            --accent-green: #10b981;
        }
        body {
            background-color: var(--bg-brand-dark);
            color: var(--text-main);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            scroll-behavior: smooth;
        }
        header {
            background: rgba(15, 23, 42, 0.95);
            position: sticky;
            top: 0;
            z-index: 100;
            border-bottom: 1px solid #334155;
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
            margin: 0;
        }
        .nav-links a {
            color: var(--text-main);
            text-decoration: none;
            transition: color 0.3s;
        }
        .nav-links a:hover {
            color: var(--accent-green);
        }
        .hero {
            padding: 6rem 2rem;
            text-align: center;
            max-width: 800px;
            margin: 0 auto;
        }
        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        .hero p {
            color: #94a3b8;
            font-size: 1.2rem;
            margin-bottom: 2rem;
        }
        .btn-primary {
            background-color: var(--accent-green);
            color: #0f172a;
            padding: 0.75rem 1.5rem;
            border-radius: 0.5rem;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            cursor: pointer;
            border: none;
        }
        .services {
            max-width: 1100px;
            margin: 4rem auto;
            padding: 0 2rem;
        }
        .services h2 {
            text-align: center;
            margin-bottom: 3rem;
            font-size: 2rem;
        }
        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        .service-card {
            background-color: var(--bg-card);
            padding: 2rem;
            border-radius: 0.75rem;
            border: 1px solid #334155;
        }
        .service-card h3 {
            color: var(--accent-green);
            margin-top: 0;
        }
        .contact {
            max-width: 600px;
            margin: 4rem auto;
            padding: 2rem;
            background-color: var(--bg-card);
            border-radius: 0.75rem;
            border: 1px solid #334155;
        }
        .contact h2 {
            text-align: center;
            margin-top: 0;
        }
        .contact-form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
            margin-top: 1.5rem;
        }
        .contact-form input,
        .contact-form select,
        .contact-form textarea {
            padding: 0.75rem;
            border-radius: 0.5rem;
            border: 1px solid #475569;
            background-color: #0f172a;
            color: #fff;
            font-size: 1rem;
        }
        footer {
            text-align: center;
            padding: 2rem;
            color: #64748b;
            border-top: 1px solid #334155;
            margin-top: 4rem;
        }
        .hidden { display: none; }
    </style>
</head>
<body>

    <header>
        <nav class="navbar">
            <div class="logo">Dembélé Studio</div>
            <ul class="nav-links">
                <li><a href="#accueil">Accueil</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="accueil" class="hero">
        <div class="hero-content">
            <h1>Créateur de Solutions Web & Visuels Uniques</h1>
            <p>Développeur web, créateur de logiciels et graphiste freelance.</p>
            <a href="#contact" class="btn-primary">Discutons de votre projet</a>
        </div>
    </section>

    <section id="services" class="services">
        <h2>Mes Services</h2>
        <div class="services-grid">
            <div class="service-card">
                <h3>Développement Web</h3>
                <p>Création d'applications web sur mesure, sites vitrines et plateformes performantes (FastAPI, Python, JavaScript).</p>
            </div>
            <div class="service-card">
                <h3>Design & Branding</h3>
                <p>Conception d'identités visuelles, logos, affiches et flyers percutants.</p>
            </div>
            <div class="service-card">
                <h3>Solutions Logicielles</h3>
                <p>Outils de gestion et applications sur mesure adaptés à vos besoins professionnels.</p>
            </div>
        </div>
    </section>

    <section id="contact" class="contact">
        <h2>Contactez-moi</h2>
        <p style="text-align: center; color: #94a3b8;">Un projet en tête ? Discutons-en sur WhatsApp.</p>
        
        <form id="contact-form" class="contact-form">
            <input type="text" name="name" placeholder="Votre nom" required>
            <input type="email" name="email" placeholder="Votre email" required>
            <select name="project_type" id="project_type">
                <option value="Développement Web">Développement Web</option>
                <option value="Design & Branding">Design & Branding</option>
                <option value="Solutions Logicielles">Solutions Logicielles</option>
            </select>
            <textarea name="description" placeholder="Parlez-moi de votre projet..." rows="5" required></textarea>
            <button type="submit" class="btn-primary">Envoyer sur WhatsApp</button>
        </form>
        <div id="form-status" class="hidden" style="margin-top: 1rem; padding: 0.75rem; text-align: center; border-radius: 0.5rem;"></div>
    </section>

    <footer>
        <p>&copy; 2026 Dembélé Studio. Tous droits réservés.</p>
    </footer>

    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof lucide !== 'undefined') { lucide.createIcons(); }
            if (typeof AOS !== 'undefined') { AOS.init({ duration: 800, once: true }); }

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
