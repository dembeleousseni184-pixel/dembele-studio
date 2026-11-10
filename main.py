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
    <title>Dembélé Ousséni | Dembélé Studio</title>
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
                <a href="#apropos" class="hover:text-brand-green transition">À propos & CV</a>
                <a href="#expertises" class="hover:text-brand-green transition">Compétences</a>
                <a href="#projets" class="hover:text-brand-green transition">Réalisations</a>
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
                <i data-lucide="award" class="w-3.5 h-3.5"></i> Innovation Numérique & Intelligence Artificielle
            </span>
            <h1 class="text-4xl md:text-6xl font-black tracking-tight mb-6 leading-tight">
                Dembélé Ousséni — <span class="text-brand-green">Jeune Professionnel & Développeur</span>.
            </h1>
            <p class="text-lg md:text-xl text-slate-600 dark:text-slate-400 mb-8 leading-relaxed">
                Étudiant en Licence 2 (Université Virtuelle de Côte d'Ivoire). Passionné par les technologies numériques, l'innovation, l'intelligence artificielle et le développement international.
            </p>
            <div class="flex flex-wrap gap-4">
                <a href="#projets" class="px-6 py-3.5 bg-brand-green hover:bg-emerald-600 text-slate-950 font-bold rounded-xl shadow-lg shadow-emerald-500/20 transition flex items-center gap-2">
                    Voir mes projets <i data-lucide="arrow-right" class="w-4 h-4"></i>
                </a>
                <a href="#contact" class="px-6 py-3.5 border border-slate-300 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-900 font-semibold rounded-xl transition">
                    Me contacter (+225 05 44 58 01 83)
                </a>
            </div>
        </div>
    </section>

    <!-- Section À propos & Parcours (Intégration directe du CV) -->
    <section id="apropos" class="py-20 bg-slate-100/50 dark:bg-slate-900/30 border-y border-slate-200/60 dark:border-slate-800/40">
        <div class="max-w-7xl mx-auto px-4">
            <div class="text-center max-w-2xl mx-auto mb-16">
                <h2 class="text-3xl font-bold mb-4">Mon Parcours & Formation</h2>
                <p class="text-slate-600 dark:text-slate-400">Résumé académique et professionnel extrait de mon parcours.</p>
            </div>

            <div class="grid md:grid-cols-2 gap-12">
                <!-- Formation -->
                <div class="bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200/80 dark:border-slate-800">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="p-3 bg-emerald-100 dark:bg-emerald-950 text-brand-green rounded-xl">
                            <i data-lucide="graduation-cap" class="w-6 h-6"></i>
                        </div>
                        <h3 class="text-xl font-bold">Formation</h3>
                    </div>
                    <div class="space-y-6 border-l-2 border-slate-200 dark:border-slate-800 pl-4 ml-2">
                        <div>
                            <span class="text-xs font-bold text-brand-green">2025 - Présent</span>
                            <h4 class="font-bold text-lg mt-1">Licence 2 (En Cours)</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">Université Virtuelle de Côte d'Ivoire. Études orientées vers les technologies numériques, l'innovation et la gestion de projets.</p>
                        </div>
                        <div>
                            <span class="text-xs font-bold text-brand-green">Obtenu en 2025</span>
                            <h4 class="font-bold text-lg mt-1">Baccalauréat Général</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">Lycée Moderne d'Anyama.</p>
                        </div>
                    </div>
                </div>

                <!-- Parcours Professionnel -->
                <div class="bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200/80 dark:border-slate-800">
                    <div class="flex items-center gap-3 mb-6">
                        <div class="p-3 bg-emerald-100 dark:bg-emerald-950 text-brand-green rounded-xl">
                            <i data-lucide="briefcase" class="w-6 h-6"></i>
                        </div>
                        <h3 class="text-xl font-bold">Parcours Professionnel</h3>
                    </div>
                    <div class="space-y-6 border-l-2 border-slate-200 dark:border-slate-800 pl-4 ml-2">
                        <div>
                            <span class="text-xs font-bold text-brand-green">2023 - Présent</span>
                            <h4 class="font-bold text-lg mt-1">Fondateur & Responsable Créatif - Dembélé Design Service</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">Conception d'identités visuelles, supports de communication, intégration de l'intelligence artificielle dans les projets créatifs.</p>
                        </div>
                        <div>
                            <span class="text-xs font-bold text-brand-green">2023 - Présent</span>
                            <h4 class="font-bold text-lg mt-1">Développeur Web & Applications (Projets Indépendants)</h4>
                            <p class="text-sm text-slate-600 dark:text-slate-400">Création de solutions numériques adaptées aux besoins utilisateurs et participation à des projets de transformation digitale.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Compétences & Langues -->
    <section id="expertises" class="py-20 max-w-7xl mx-auto px-4">
        <div class="text-center max-w-2xl mx-auto mb-16">
            <h2 class="text-3xl font-bold mb-4">Compétences & Langues</h2>
            <p class="text-slate-600 dark:text-slate-400">Expertises techniques, professionnelles et maîtrise linguistique.</p>
        </div>

        <div class="grid md:grid-cols-3 gap-8">
            <!-- Compétences Informatiques -->
            <div class="bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-200/80 dark:border-slate-800">
                <h3 class="text-lg font-bold mb-4 text-brand-green flex items-center gap-2">
                    <i data-lucide="cpu" class="w-5 h-5"></i> Informatique & Tech
                </h3>
                <ul class="space-y-2 text-sm text-slate-600 dark:text-slate-400">
                    <li>✓ Développement Web & Applications</li>
                    <li>✓ Intelligence Artificielle (IA)</li>
                    <li>✓ Internet des Objets (IoT) & Cloud Computing</li>
                    <li>✓ Suite Microsoft Office & Canva</li>
                </ul>
            </div>

            <!-- Compétences Professionnelles -->
            <div class="bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-200/80 dark:border-slate-800">
                <h3 class="text-lg font-bold mb-4 text-brand-green flex items-center gap-2">
                    <i data-lucide="layers" class="w-5 h-5"></i> Professionnelles
                </h3>
                <ul class="space-y-2 text-sm text-slate-600 dark:text-slate-400">
                    <li>✓ Gestion de Projets & Communication Digitale</li>
                    <li>✓ Création de Contenus Numériques</li>
                    <li>✓ Logistique & Approvisionnement</li>
                    <li>✓ Résolution de Problèmes & Leadership</li>
                </ul>
            </div>

            <!-- Langues & Loisirs -->
            <div class="bg-white dark:bg-slate-900 p-8 rounded-2xl border border-slate-200/80 dark:border-slate-800">
                <h3 class="text-lg font-bold mb-4 text-brand-green flex items-center gap-2">
                    <i data-lucide="globe" class="w-5 h-5"></i> Langues & Loisirs
                </h3>
                <ul class="space-y-2 text-sm text-slate-600 dark:text-slate-400 mb-6">
                    <li><strong>Français :</strong> Courant</li>
                    <li><strong>Anglais :</strong> Intermédiaire</li>
                    <li><strong>Arabe classique :</strong> Intermédiaire</li>
                </ul>
                <p class="text-xs text-slate-500"><strong>Loisirs :</strong> Intelligence Artificielle, Innovation Technologique, Entrepreneuriat, Développement Durable.</p>
            </div>
        </div>
    </section>

    <!-- Section Projets & Réalisations -->
    <section id="projets" class="py-20 bg-slate-100/50 dark:bg-slate-900/30 border-y border-slate-200/60 dark:border-slate-800/40">
        <div class="max-w-7xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-4 text-center">Réalisations & Projets</h2>
            <p class="text-center text-slate-600 dark:text-slate-400 mb-12">Applications logicielles, affiches publicitaires et projets indépendants.</p>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Projet 1 -->
                <div class="bg-white dark:bg-slate-900 rounded-2xl overflow-hidden border border-slate-200/80 dark:border-slate-800 shadow-sm">
                    <div class="h-48 bg-slate-900 relative">
                        <img src="https://images.unsplash.com/photo-1556742049-0a67d553c2a8" alt="Demshop POS" class="w-full h-full object-cover">
                    </div>
                    <div class="p-6">
                        <span class="text-xs font-bold text-brand-green uppercase">Développement Web</span>
                        <h3 class="text-lg font-bold mt-1 mb-2">Demshop POS & Stock</h3>
                        <p class="text-sm text-slate-600 dark:text-slate-400">Application FastAPI de point de vente et gestion d'inventaire sur-mesure pour commerces.</p>
                    </div>
                </div>

                <!-- Projet 2 -->
                <div class="bg-white dark:bg-slate-900 rounded-2xl overflow-hidden border border-slate-200/80 dark:border-slate-800 shadow-sm">
                    <div class="h-48 bg-slate-900 relative">
                        <img src="https://images.unsplash.com/photo-1626785774573-4b799315345d" alt="Branding" class="w-full h-full object-cover">
                    </div>
                    <div class="p-6">
                        <span class="text-xs font-bold text-brand-green uppercase">Design & Branding</span>
                        <h3 class="text-lg font-bold mt-1 mb-2">Dembélé Design Service</h3>
                        <p class="text-sm text-slate-600 dark:text-slate-400">Création de contenus digitaux, affiches publicitaires, logos et bannières pour organisations.</p>
                    </div>
                </div>

                <!-- Projet 3 -->
                <div class="bg-white dark:bg-slate-900 rounded-2xl overflow-hidden border border-slate-200/80 dark:border-slate-800 shadow-sm">
                    <div class="h-48 bg-slate-900 relative">
                        <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87" alt="Logistique" class="w-full h-full object-cover">
                    </div>
                    <div class="p-6">
                        <span class="text-xs font-bold text-brand-green uppercase">Logistique & Projets</span>
                        <h3 class="text-lg font-bold mt-1 mb-2">Projets Logistiques & Étalon</h3>
                        <p class="text-sm text-slate-600 dark:text-slate-400">Gestion logistique, automatisation des procédures administratives et systèmes de suivi.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Contact -->
    <section id="contact" class="py-24 max-w-4xl mx-auto px-4">
        <div class="bg-white dark:bg-slate-900 p-8 md:p-12 rounded-3xl shadow-xl border border-slate-200/80 dark:border-slate-800">
            <div class="text-center max-w-xl mx-auto mb-10">
                <h2 class="text-3xl font-bold mb-3">Contactez Dembélé Ousséni</h2>
                <p class="text-slate-600 dark:text-slate-400 text-sm">Ouvert aux entreprises privées, ONG, organisations internationales, stages et bourses d'études.</p>
            </div>

            <form id="contact-form" class="space-y-6">
                <div class="grid md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Votre nom</label>
                        <input type="text" name="name" required placeholder="Ex: Jean Dupont" class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition">
                    </div>
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Votre Email</label>
                        <input type="email" name="email" required placeholder="Ex: jean@example.com" class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition">
                    </div>
                </div>
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Type de collaboration / Service</label>
                    <select name="project_type" class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition">
                        <option value="Développement Web & Logiciel">Développement Web & Logiciel</option>
                        <option value="Design Graphique & Affiches">Design Graphique & Affiches</option>
                        <option value="Opportunité Professionnelle / Stage">Opportunité Professionnelle / Stage</option>
                        <option value="Autre Projet">Autre Projet</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Message détaillé</label>
                    <textarea name="description" rows="4" required placeholder="Parlez-moi de votre projet ou de votre offre..." class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition"></textarea>
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
        <p>&copy; 2026 Dembélé Ousséni - Dembélé Studio. Tous droits réservés.</p>
    </footer>

    <!-- Script de gestion et WhatsApp -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof lucide !== 'undefined') { lucide.createIcons(); }

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
                        formResponse.textContent = "Erreur. Contactez directement le +225 05 44 58 01 83.";
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
        f"Bonjour Dembélé Ousséni 👋\n\n"
        f"Je m'appelle *{name}*.\n"
        f"Email : {email}\n"
        f"Sujet : *{project_type}*\n\n"
        f"Message :\n{description}"
    )
    encoded_message = urllib.parse.quote(wa_message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"
    
    return {
        "message": "Redirection vers WhatsApp en cours...",
        "whatsapp_url": whatsapp_url
    }
