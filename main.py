from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import urllib.parse

app = FastAPI()

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="fr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dembélé Studio | Web Developer & Designer</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            green: '#10b981',
                            dark: '#022c22',
                        }
                    }
                }
            }
        }
    </script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body class="bg-slate-50 text-slate-800 dark:bg-slate-950 dark:text-slate-100 transition-colors duration-300 antialiased">

    <!-- Header Navigation -->
    <header class="fixed top-0 w-full bg-white/80 dark:bg-slate-950/80 backdrop-blur-md z-50 border-b border-slate-200 dark:border-slate-800/80">
        <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
            <a href="#accueil" class="text-xl font-extrabold tracking-tight text-brand-green flex items-center gap-2">
                <span class="w-3 h-3 rounded-full bg-brand-green inline-block animate-pulse"></span>
                Dembélé Studio
            </a>
            
            <nav class="hidden md:flex space-x-6 font-medium text-sm">
                <a href="#accueil" class="hover:text-brand-green transition">Accueil</a>
                <a href="#expertises" class="hover:text-brand-green transition">Expertises</a>
                <a href="#projets" class="hover:text-brand-green transition">Portfolio</a>
                <a href="#apropos" class="hover:text-brand-green transition">À propos</a>
                <a href="#contact" class="hover:text-brand-green transition">Contact</a>
            </nav>

            <div class="flex items-center space-x-4">
                <button id="theme-toggle" class="p-2 rounded-lg bg-slate-100 dark:bg-slate-900 text-slate-600 dark:text-slate-300 hover:text-brand-green cursor-pointer">
                    <i data-lucide="moon" class="w-5 h-5 dark:hidden"></i>
                    <i data-lucide="sun" class="w-5 h-5 hidden dark:block"></i>
                </button>
            </div>
        </div>
    </header>

    <!-- Hero Section -->
    <section id="accueil" class="pt-32 pb-20 md:pt-44 md:pb-32 max-w-7xl mx-auto px-4 relative overflow-hidden">
        <div class="absolute -top-24 -right-24 w-96 h-96 bg-brand-green/10 rounded-full blur-3xl pointer-events-none"></div>
        
        <div class="max-w-3xl">
            <span class="inline-flex items-center gap-2 py-1.5 px-4 bg-emerald-100 dark:bg-emerald-950/60 text-brand-green rounded-full text-xs font-bold mb-6 border border-emerald-200 dark:border-emerald-900 shadow-sm">
                <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Web Development, Branding & Event Design
            </span>
            <h1 class="text-4xl md:text-6xl font-black tracking-tight mb-6 leading-tight">
                Donnez vie à vos projets avec <span class="text-brand-green">impact et élégance</span>.
            </h1>
            <p class="text-lg md:text-xl text-slate-600 dark:text-slate-400 mb-8 leading-relaxed">
                Créateur d'applications logicielles sur-mesure (Demshop POS), d'identités visuelles percutantes, d'affiches publicitaires et de bannières d'événements professionnels.
            </p>
            <div class="flex flex-wrap gap-4">
                <a href="#projets" class="px-6 py-3.5 bg-brand-green hover:bg-emerald-600 text-slate-950 font-bold rounded-xl shadow-lg shadow-emerald-500/20 transition flex items-center gap-2">
                    Explorer le portfolio <i data-lucide="arrow-right" class="w-4 h-4"></i>
                </a>
                <a href="#contact" class="px-6 py-3.5 border border-slate-300 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-900 font-semibold rounded-xl transition">
                    Me contacter (+225 05 44 58 01 83)
                </a>
            </div>
        </div>
    </section>

    <!-- Section Expertises -->
    <section id="expertises" class="py-20 bg-slate-100/50 dark:bg-slate-900/30 border-y border-slate-200/60 dark:border-slate-800/40">
        <div class="max-w-7xl mx-auto px-4">
            <div class="text-center max-w-2xl mx-auto mb-16">
                <h2 class="text-3xl font-bold mb-4">Domaines d'Expertise</h2>
                <p class="text-slate-600 dark:text-slate-400">Une double compétence technique et créative pour répondre à tous vos besoins numériques.</p>
            </div>
            
            <div class="grid md:grid-cols-3 gap-8">
                <!-- Carte Design & Affiches -->
                <div class="bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200/80 dark:border-slate-800 hover:border-brand-green/50 transition group">
                    <div class="w-12 h-12 bg-emerald-100 dark:bg-emerald-950/60 text-brand-green rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition">
                        <i data-lucide="palette" class="w-6 h-6"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">Affiches & Branding</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">
                        Conception de flyers promotionnels, bannières publicitaires, identités visuelles d'événements et chartes graphiques sur-mesure.
                    </p>
                </div>

                <!-- Carte Dev Web -->
                <div class="bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200/80 dark:border-slate-800 hover:border-brand-green/50 transition group">
                    <div class="w-12 h-12 bg-emerald-100 dark:bg-emerald-950/60 text-brand-green rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition">
                        <i data-lucide="code-2" class="w-6 h-6"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">Développement Web</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">
                        Création d'applications web performantes, interfaces réactives avec FastAPI, Python, JavaScript et Tailwind CSS.
                    </p>
                </div>

                <!-- Carte Événementiel -->
                <div class="bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200/80 dark:border-slate-800 hover:border-brand-green/50 transition group">
                    <div class="w-12 h-12 bg-emerald-100 dark:bg-emerald-950/60 text-brand-green rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition">
                        <i data-lucide="calendar-check" class="w-6 h-6"></i>
                    </div>
                    <h3 class="text-xl font-bold mb-3">Habillage d'Événements</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4 leading-relaxed">
                        Branding visuel complet pour sommets professionnels, conférences, séminaires et événements jeunesses africaines.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Portfolio / Réalisations (Avec de vraies images) -->
    <section id="projets" class="py-24 max-w-7xl mx-auto px-4">
        <div class="text-center max-w-2xl mx-auto mb-16">
            <h2 class="text-3xl font-bold mb-4">Portfolio & Réalisations</h2>
            <p class="text-slate-600 dark:text-slate-400">Découvrez quelques-uns de mes projets récents en développement web, design d'affiches et branding d'événements.</p>
        </div>

        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            
            <!-- Projet 1 : Affiche / Flyer Publicitaire -->
            <div class="bg-white dark:bg-slate-900 rounded-2xl overflow-hidden shadow-sm border border-slate-200/80 dark:border-slate-800 hover:shadow-md transition group">
                <div class="h-60 overflow-hidden bg-slate-100 dark:bg-slate-950">
                    <!-- IMAGE DE FLYER/AFFICHE -->
                    <img src="https://images.unsplash.com/photo-1626785774573-4b799315345d" alt="Affiche Publicitaire" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                </div>
                <div class="p-6">
                    <span class="text-xs font-semibold text-brand-green uppercase tracking-wider">Design Graphique</span>
                    <h3 class="text-lg font-bold mt-1 mb-2">Affiche Publicitaire & Flyer Pro</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">Création visuelle percutante optimisée pour les réseaux sociaux et l'impression.</p>
                    <div class="flex space-x-2">
                        <span class="px-2 py-1 bg-slate-100 dark:bg-slate-950 text-xs rounded text-slate-600 dark:text-slate-300">Canva</span>
                        <span class="px-2 py-1 bg-slate-100 dark:bg-slate-950 text-xs rounded text-slate-600 dark:text-slate-300">Branding</span>
                    </div>
                </div>
            </div>

            <!-- Projet 2 : App Web (Demshop POS) -->
            <div class="bg-white dark:bg-slate-900 rounded-2xl overflow-hidden shadow-sm border border-slate-200/80 dark:border-slate-800 hover:shadow-md transition group">
                <div class="h-60 overflow-hidden bg-slate-100 dark:bg-slate-950">
                    <!-- IMAGE DE L'APPLICATION WEB (Demshop POS) -->
                    <img src="https://images.unsplash.com/photo-1556742049-0a67d553c2a8" alt="Demshop POS" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                </div>
                <div class="p-6">
                    <span class="text-xs font-semibold text-brand-green uppercase tracking-wider">Développement</span>
                    <h3 class="text-lg font-bold mt-1 mb-2">Demshop POS & Stock</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">Application FastAPI de point de vente et gestion d'inventaire sur-mesure pour commerces.</p>
                    <div class="flex space-x-2">
                        <span class="px-2 py-1 bg-slate-100 dark:bg-slate-950 text-xs rounded text-slate-600 dark:text-slate-300">FastAPI</span>
                        <span class="px-2 py-1 bg-slate-100 dark:bg-slate-950 text-xs rounded text-slate-600 dark:text-slate-300">Python</span>
                    </div>
                </div>
            </div>

            <!-- Projet 3 : Bannières / Habillage Sommet -->
            <div class="bg-white dark:bg-slate-900 rounded-2xl overflow-hidden shadow-sm border border-slate-200/80 dark:border-slate-800 hover:shadow-md transition group">
                <div class="h-60 overflow-hidden bg-slate-100 dark:bg-slate-950">
                    <!-- IMAGE DE BANNIÈRE D'ÉVÉNEMENT (Pinterest d'exemple) -->
                    <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87" alt="Branding Sommet" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                </div>
                <div class="p-6">
                    <span class="text-xs font-semibold text-brand-green uppercase tracking-wider">Événementiel</span>
                    <h3 class="text-lg font-bold mt-1 mb-2">Bannières Visuelles & Roll-up</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">Création de l'habillage visuel complet pour sommets professionnels et séminaires.</p>
                    <div class="flex space-x-2">
                        <span class="px-2 py-1 bg-slate-100 dark:bg-slate-950 text-xs rounded text-slate-600 dark:text-slate-300">Roll-up</span>
                        <span class="px-2 py-1 bg-slate-100 dark:bg-slate-950 text-xs rounded text-slate-600 dark:text-slate-300">Conférence</span>
                    </div>
                </div>
            </div>

        </div>
    </section>

    <!-- Section À propos -->
    <section id="apropos" class="py-20 bg-slate-100/50 dark:bg-slate-900/30 border-t border-slate-200/60 dark:border-slate-800/40">
        <div class="max-w-7xl mx-auto px-4 grid md:grid-cols-5 gap-12 items-center">
            <div class="md:col-span-2 flex justify-center">
                <!-- EMPLACEMENT POUR VOTRE PHOTO DE PROFIL -->
                <div class="w-72 h-72 rounded-full bg-white dark:bg-slate-900 border-8 border-slate-200 dark:border-slate-800 shadow-xl overflow-hidden flex items-center justify-center">
                    <!-- Si vous avez une photo : <img src="/static/img/ousséni.jpg" class="w-full h-full object-cover"> -->
                    <i data-lucide="user" class="w-32 h-32 text-slate-400 dark:text-slate-600"></i>
                </div>
            </div>
            <div class="md:col-span-3">
                <h2 class="text-3xl font-bold mb-6">À propos de Dembélé Ousséni</h2>
                <p class="text-slate-600 dark:text-slate-400 mb-6 leading-relaxed">
                    Jeune professionnel passionné par les technologies numériques, je mets à votre service une double compétence unique : le développement d'applications web robustes et la création de designs visuels impactants. Basé sur Casablanca, j'accompagne les organisations dans leur transformation numérique avec des solutions sur-mesure.
                </p>
                <div class="grid grid-cols-2 gap-4 text-sm">
                    <div class="flex items-center gap-2"><i data-lucide="map-pin" class="w-4 h-4 text-brand-green"></i> Casablanca, Maroc</div>
                    <div class="flex items-center gap-2"><i data-lucide="mail" class="w-4 h-4 text-brand-green"></i> ousséni.dembele@gmail.com</div>
                    <div class="flex items-center gap-2"><i data-lucide="phone" class="w-4 h-4 text-brand-green"></i> +225 05 44 58 01 83</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Contact -->
    <section id="contact" class="py-24 max-w-4xl mx-auto px-4">
        <div class="bg-white dark:bg-slate-900 p-8 md:p-12 rounded-3xl shadow-xl border border-slate-200/80 dark:border-slate-800 relative overflow-hidden">
            <div class="absolute top-0 right-0 w-64 h-64 bg-brand-green/5 rounded-full blur-2xl pointer-events-none"></div>

            <div class="text-center max-w-xl mx-auto mb-10">
                <h2 class="text-3xl font-bold mb-3">Discutons de votre projet</h2>
                <p class="text-slate-600 dark:text-slate-400 text-sm">Remplissez ce formulaire pour m'envoyer instantanément votre demande directement sur mon WhatsApp professionnel.</p>
            </div>

            <form id="contact-form" class="space-y-6">
                <div class="grid md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Votre nom complet</label>
                        <input type="text" name="name" required placeholder="Ex: Jean Dupont" class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition">
                    </div>
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Votre adresse email</label>
                        <input type="email" name="email" required placeholder="Ex: jean@example.com" class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition">
                    </div>
                </div>
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Service souhaité</label>
                    <select name="project_type" class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition">
                        <option value="Affiches & Flyer Publicitaire">Affiches & Flyer Publicitaire</option>
                        <option value="Développement Web & Application">Développement Web & Application</option>
                        <option value="Branding d'Événement">Branding d'Événement</option>
                        <option value="Autre Projet">Autre Projet</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Détails de votre projet</label>
                    <textarea name="description" rows="4" required placeholder="Décrivez vos besoins..." class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition"></textarea>
                </div>
                <button type="submit" class="w-full py-4 bg-brand-green hover:bg-emerald-600 text-slate-950 font-bold rounded-xl shadow-lg shadow-emerald-500/20 transition cursor-pointer flex items-center justify-center gap-2">
                    <i data-lucide="message-square" class="w-5 h-5"></i> Envoyer sur WhatsApp (+225 05 44 58 01 83)
                </button>
                <div id="form-response" class="hidden text-center font-medium text-sm pt-2"></div>
            </form>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-8 border-t border-slate-200 dark:border-slate-800/80 text-center text-sm text-slate-500">
        <p>&copy; 2026 Dembélé Studio. Tous droits réservés. Développé avec FastAPI & Tailwind CSS.</p>
    </footer>

    <!-- Script de gestion et WhatsApp -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof lucide !== 'undefined') { lucide.createIcons(); }

            // Gestion du mode sombre / clair
            const themeToggle = document.getElementById('theme-toggle');
            const html = document.documentElement;

            if (localStorage.getItem('theme') === 'dark' || (!localStorage.getItem('theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                html.classList.add('dark');
            }

            if (themeToggle) {
                themeToggle.addEventListener('click', () => {
                    html.classList.toggle('dark');
                    localStorage.setItem('theme', html.classList.contains('dark') ? 'dark' : 'light');
                });
            }

            // Gestion du formulaire de contact et redirection WhatsApp
            const contactForm = document.getElementById('contact-form');
            const formResponse = document.getElementById('form-response');

            if (contactForm) {
                contactForm.addEventListener('submit', async (e) => {
                    e.preventDefault();
                    const formData = new FormData(contactForm);

                    formResponse.classList.remove('hidden', 'text-red-500');
                    formResponse.classList.add('text-brand-green');
                    formResponse.textContent = "Préparation du message WhatsApp...";

                    try {
                        const response = await fetch('/api/contact', {
                            method: 'POST',
                            body: formData
                        });
                        const result = await response.json();

                        if (response.ok && result.whatsapp_url) {
                            formResponse.textContent = result.message;
                            contactForm.reset();
                            setTimeout(() => {
                                window.open(result.whatsapp_url, '_blank');
                            }, 1000);
                        } else {
                            throw new Error();
                        }
                    } catch (err) {
                        formResponse.classList.remove('text-brand-green');
                        formResponse.classList.add('text-red-500');
                        formResponse.textContent = "Erreur de transmission. Contactez directement le +225 05 44 58 01 83.";
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
    # Numéro Ivorien professionnel configuré pour WhatsApp
    whatsapp_number = "+2250544580183"
    
    # Construction du message personnalisé pour WhatsApp
    wa_message = (
        f"Bonjour Dembélé Studio 👋\n\n"
        f"Je m'appelle *{name}*.\n"
        f"Email : {email}\n"
        f"Service souhaité : *{project_type}*\n\n"
        f"Détails du projet :\n{description}"
    )
    
    # Encodage du message pour l'URL
    encoded_message = urllib.parse.quote(wa_message)
    
    # URL de redirection vers l'API WhatsApp
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"
    
    return {
        "message": "Message préparé avec succès ! Redirection vers WhatsApp...",
        "whatsapp_url": whatsapp_url
    }
