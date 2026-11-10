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
    <title>Dembélé Ousséni | Développeur & Créateur Visuel</title>
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
                <a href="#profil" class="hover:text-brand-green transition">Profil</a>
                <a href="#parcours" class="hover:text-brand-green transition">Parcours & Formations</a>
                <a href="#competences" class="hover:text-brand-green transition">Compétences</a>
                <a href="#galerie" class="hover:text-brand-green transition">Galerie & Affiches</a>
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
        
        <div class="max-w-4xl">
            <span class="inline-flex items-center gap-2 py-1.5 px-4 bg-emerald-100 dark:bg-emerald-950/60 text-brand-green rounded-full text-xs font-bold mb-6 border border-emerald-200 dark:border-emerald-900 shadow-sm">
                <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Innovation Numérique & Intelligence Artificielle
            </span>
            <h1 class="text-4xl md:text-6xl font-black tracking-tight mb-4 leading-tight">
                DEMBÉLÉ OUSSÉNI
            </h1>
            <h2 class="text-xl md:text-2xl font-bold text-brand-green mb-6">
                Jeune Professionnel en Innovation Numérique, Intelligence Artificielle et Développement International
            </h2>
            <p class="text-lg text-slate-600 dark:text-slate-400 mb-8 leading-relaxed max-w-3xl">
                Créatif, adaptable et orienté solutions. Je développe des applications web & logicielles robustes et conçois des supports visuels impactants (affiches événementielles, mariages, anniversaires, bannières et identités visuelles).
            </p>
            <div class="flex flex-wrap gap-4">
                <a href="#galerie" class="px-6 py-3.5 bg-brand-green hover:bg-emerald-600 text-slate-950 font-bold rounded-xl shadow-lg shadow-emerald-500/20 transition flex items-center gap-2">
                    Explorer la Galerie <i data-lucide="arrow-right" class="w-4 h-4"></i>
                </a>
                <a href="#contact" class="px-6 py-3.5 border border-slate-300 dark:border-slate-800 hover:bg-slate-100 dark:hover:bg-slate-900 font-semibold rounded-xl transition">
                    Me contacter sur WhatsApp
                </a>
            </div>
        </div>
    </section>

    <!-- Section Profil & Coordonnées -->
    <section id="profil" class="py-20 bg-slate-100/50 dark:bg-slate-900/30 border-y border-slate-200/60 dark:border-slate-800/40">
        <div class="max-w-7xl mx-auto px-4 grid md:grid-cols-3 gap-8 items-start">
            <!-- Profil Textuel -->
            <div class="md:col-span-2 bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200/80 dark:border-slate-800">
                <h3 class="text-2xl font-bold mb-4 flex items-center gap-2">
                    <i data-lucide="user-check" class="text-brand-green"></i> Profil Professionnel
                </h3>
                <p class="text-slate-600 dark:text-slate-400 leading-relaxed mb-6">
                    Étudiant en Licence 2, passionné par les technologies numériques, l'innovation et le développement international. Doté de compétences en développement web et applicatif, intelligence artificielle, logistique et communication digitale. Je souhaite mettre mes compétences au service d'organisations engagées dans le développement durable, l'inclusion et la transformation numérique.
                </p>
                <div class="border-t border-slate-200 dark:border-slate-800 pt-4">
                    <h4 class="font-bold text-sm text-brand-green uppercase tracking-wider mb-2">Objectif Professionnel</h4>
                    <p class="text-xs text-slate-500 dark:text-slate-400">
                        Motivé à apprendre, à relever de nouveaux défis et à contribuer activement à la réussite des projets d'entreprises privées, d'ONG, d'organisations internationales, dans le cadre de stages, bénévolats ou bourses d'études.
                    </p>
                </div>
            </div>

            <!-- Coordonnées et Détails -->
            <div class="bg-white dark:bg-slate-900 p-8 rounded-2xl shadow-sm border border-slate-200/80 dark:border-slate-800">
                <h3 class="text-xl font-bold mb-6 text-brand-green">Contact & Infos</h3>
                <ul class="space-y-4 text-sm">
                    <li class="flex items-start gap-3">
                        <i data-lucide="phone" class="w-5 h-5 text-brand-green shrink-0 mt-0.5"></i>
                        <div>
                            <span class="block font-bold">Téléphone / WhatsApp</span>
                            <span class="text-slate-600 dark:text-slate-400">+212 780220397</span><br>
                            <span class="text-slate-600 dark:text-slate-400">+225 0544580183</span>
                        </div>
                    </li>
                    <li class="flex items-start gap-3">
                        <i data-lucide="mail" class="w-5 h-5 text-brand-green shrink-0 mt-0.5"></i>
                        <div>
                            <span class="block font-bold">Email Institutionnel</span>
                            <a href="mailto:ousseni.dembel@uvci.edu.ci" class="text-slate-600 dark:text-slate-400 hover:text-brand-green break-all">ousseni.dembel@uvci.edu.ci</a>
                        </div>
                    </li>
                    <li class="flex items-start gap-3">
                        <i data-lucide="linkedin" class="w-5 h-5 text-brand-green shrink-0 mt-0.5"></i>
                        <div>
                            <span class="block font-bold">LinkedIn</span>
                            <a href="https://www.linkedin.com/in/dembele-ousseni-5907502b4" target="_blank" class="text-xs text-brand-green hover:underline break-all">linkedin.com/in/dembele-ousseni-5907502b4</a>
                        </div>
                    </li>
                    <li class="flex items-start gap-3 border-t border-slate-200 dark:border-slate-800 pt-3">
                        <i data-lucide="calendar" class="w-5 h-5 text-brand-green shrink-0 mt-0.5"></i>
                        <div>
                            <span class="block font-bold">Date de Naissance</span>
                            <span class="text-slate-600 dark:text-slate-400">10 Février 2004</span>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Section Parcours Professionnel & Formations -->
    <section id="parcours" class="py-20 max-w-7xl mx-auto px-4">
        <h2 class="text-3xl font-bold mb-12 text-center">Parcours Professionnel & Formations</h2>

        <div class="grid md:grid-cols-2 gap-12">
            <!-- Expériences Professionnelles -->
            <div>
                <h3 class="text-xl font-bold mb-6 text-brand-green flex items-center gap-2">
                    <i data-lucide="briefcase"></i> Parcours Professionnel
                </h3>
                <div class="space-y-6 border-l-2 border-brand-green/30 pl-4 ml-2">
                    <!-- Expérience 1 -->
                    <div class="relative">
                        <span class="text-xs font-bold bg-emerald-100 dark:bg-emerald-950 text-brand-green px-2 py-0.5 rounded">2023 - Présent</span>
                        <h4 class="font-bold text-lg mt-1">Dembélé Design Service</h4>
                        <p class="text-xs font-semibold text-slate-500 mb-2">Fondateur & Responsable Créatif</p>
                        <ul class="text-xs text-slate-600 dark:text-slate-400 space-y-1 list-disc list-inside">
                            <li>Conception d'identités visuelles et de supports de communication.</li>
                            <li>Création de contenus digitaux pour entreprises et organisations.</li>
                            <li>Utilisation de l'intelligence artificielle dans les projets créatifs.</li>
                            <li>Accompagnement des clients dans leur stratégie de communication numérique.</li>
                        </ul>
                    </div>

                    <!-- Expérience 2 -->
                    <div class="relative">
                        <span class="text-xs font-bold bg-emerald-100 dark:bg-emerald-950 text-brand-green px-2 py-0.5 rounded">2023 - Présent</span>
                        <h4 class="font-bold text-lg mt-1">Projets Indépendants</h4>
                        <p class="text-xs font-semibold text-slate-500 mb-2">Développeur Web & Applications</p>
                        <ul class="text-xs text-slate-600 dark:text-slate-400 space-y-1 list-disc list-inside">
                            <li>Conception et développement de sites web et d'applications.</li>
                            <li>Élaboration de solutions numériques adaptées aux besoins des utilisateurs.</li>
                            <li>Participation à des projets de transformation digitale.</li>
                        </ul>
                    </div>

                    <!-- Expérience 3 -->
                    <div class="relative">
                        <span class="text-xs font-bold bg-emerald-100 dark:bg-emerald-950 text-brand-green px-2 py-0.5 rounded">02/11/2026 - 04/11/2026</span>
                        <h4 class="font-bold text-lg mt-1">Entreprise Locale de Logistique</h4>
                        <p class="text-xs font-semibold text-slate-500 mb-2">Développeur & Gestionnaire Logistique — Casablanca, Maroc</p>
                        <ul class="text-xs text-slate-600 dark:text-slate-400 space-y-1 list-disc list-inside">
                            <li>Développement d'un logiciel de gestion des colis et des stocks.</li>
                            <li>Gestion et suivi des opérations logistiques.</li>
                            <li>Optimisation des processus de stockage et de distribution.</li>
                            <li>Contribution à la digitalisation des activités de l'entreprise.</li>
                        </ul>
                    </div>

                    <!-- Expérience 4 -->
                    <div class="relative">
                        <span class="text-xs font-bold bg-emerald-100 dark:bg-emerald-950 text-brand-green px-2 py-0.5 rounded">2026 - Présent</span>
                        <h4 class="font-bold text-lg mt-1">ETALON EXPRESS & LOGISTIQUE</h4>
                        <p class="text-xs font-semibold text-slate-500 mb-2">Concepteur de Projet Logistique</p>
                        <ul class="text-xs text-slate-600 dark:text-slate-400 space-y-1 list-disc list-inside">
                            <li>Conception d'un système numérique de gestion logistique.</li>
                            <li>Développement de solutions pour le suivi des colis et des clients.</li>
                            <li>Automatisation des procédures administratives et opérationnelles.</li>
                        </ul>
                    </div>
                </div>
            </div>

            <!-- Formations, Langues et Loisirs -->
            <div class="space-y-8">
                <!-- Formations -->
                <div>
                    <h3 class="text-xl font-bold mb-6 text-brand-green flex items-center gap-2">
                        <i data-lucide="graduation-cap"></i> Formations Académiques
                    </h3>
                    <div class="space-y-4 border-l-2 border-brand-green/30 pl-4 ml-2">
                        <div>
                            <span class="text-xs font-bold bg-emerald-100 dark:bg-emerald-950 text-brand-green px-2 py-0.5 rounded">2025 - Présent</span>
                            <h4 class="font-bold text-lg mt-1">Licence 2 (En Cours)</h4>
                            <p class="text-xs font-semibold text-slate-500">Université Virtuelle De Côte D'Ivoire</p>
                            <p class="text-xs text-slate-600 dark:text-slate-400 mt-1">Études orientées vers les technologies numériques, l'innovation et la gestion de projets.</p>
                        </div>
                        <div>
                            <span class="text-xs font-bold bg-emerald-100 dark:bg-emerald-950 text-brand-green px-2 py-0.5 rounded">Obtenu en 2025</span>
                            <h4 class="font-bold text-lg mt-1">Baccalauréat général</h4>
                            <p class="text-xs font-semibold text-slate-500">Lycée Moderne d'Anyama</p>
                        </div>
                    </div>
                </div>

                <!-- Langues & Loisirs -->
                <div class="grid grid-cols-2 gap-4 pt-4 border-t border-slate-200 dark:border-slate-800">
                    <div class="bg-white dark:bg-slate-900 p-4 rounded-xl border border-slate-200/80 dark:border-slate-800">
                        <h4 class="font-bold text-sm text-brand-green mb-2 flex items-center gap-1">
                            <i data-lucide="globe" class="w-4 h-4"></i> Langues
                        </h4>
                        <ul class="text-xs space-y-1 text-slate-600 dark:text-slate-400">
                            <li><strong>Français :</strong> Courant</li>
                            <li><strong>Anglais :</strong> Intermédiaire</li>
                            <li><strong>Arabe classique :</strong> Intermédiaire</li>
                        </ul>
                    </div>
                    <div class="bg-white dark:bg-slate-900 p-4 rounded-xl border border-slate-200/80 dark:border-slate-800">
                        <h4 class="font-bold text-sm text-brand-green mb-2 flex items-center gap-1">
                            <i data-lucide="heart" class="w-4 h-4"></i> Loisirs
                        </h4>
                        <ul class="text-xs space-y-1 text-slate-600 dark:text-slate-400">
                            <li>• Intelligence Artificielle</li>
                            <li>• Innovation Technologique</li>
                            <li>• Développement Durable</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section Compétences Tout-en-Un -->
    <section id="competences" class="py-20 bg-slate-100/50 dark:bg-slate-900/30 border-y border-slate-200/60 dark:border-slate-800/40">
        <div class="max-w-7xl mx-auto px-4">
            <h2 class="text-3xl font-bold mb-12 text-center">Compétences Techniques & Professionnelles</h2>

            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Informatiques & Tech -->
                <div class="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200/80 dark:border-slate-800">
                    <h3 class="font-bold text-lg text-brand-green mb-4 flex items-center gap-2">
                        <i data-lucide="code"></i> Informatique & Web
                    </h3>
                    <ul class="space-y-2 text-xs text-slate-600 dark:text-slate-400">
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Développement Web et Applications</li>
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Intelligence Artificielle (IA)</li>
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Internet des Objets (IoT)</li>
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Cloud Computing & Technologies Émergentes</li>
                    </ul>
                </div>

                <!-- Outils & Logiciels -->
                <div class="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200/80 dark:border-slate-800">
                    <h3 class="font-bold text-lg text-brand-green mb-4 flex items-center gap-2">
                        <i data-lucide="layout"></i> Logiciels & Design
                    </h3>
                    <ul class="space-y-2 text-xs text-slate-600 dark:text-slate-400">
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Canva & Design Graphique</li>
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Suite Microsoft Office (Word, Excel, PowerPoint, Outlook)</li>
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Création de Contenus Numériques</li>
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Identités Visuelles & Supports</li>
                    </ul>
                </div>

                <!-- Management & Soft Skills -->
                <div class="bg-white dark:bg-slate-900 p-6 rounded-2xl border border-slate-200/80 dark:border-slate-800">
                    <h3 class="font-bold text-lg text-brand-green mb-4 flex items-center gap-2">
                        <i data-lucide="users"></i> Management & Leadership
                    </h3>
                    <ul class="space-y-2 text-xs text-slate-600 dark:text-slate-400">
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Gestion de Projet & Leadership</li>
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Logistique, Approvisionnement & Transformation</li>
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Entrepreneuriat & Développement Durable</li>
                        <li class="flex items-center gap-2"><i data-lucide="check" class="w-4 h-4 text-brand-green"></i> Travail en Équipe & Résolution de Problèmes</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Galerie Filtrable (Affiches, Anniversaire, Mariage, Événements, Applications) -->
    <section id="galerie" class="py-24 max-w-7xl mx-auto px-4">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-12">
            <div>
                <h2 class="text-3xl font-bold mb-2">Galerie de Réalisations</h2>
                <p class="text-slate-600 dark:text-slate-400">Explorez mes créations graphiques (affiches, événements, mariages) et projets applicatifs.</p>
            </div>
            
            <!-- Filtres de la Galerie -->
            <div class="flex flex-wrap gap-2 mt-6 md:mt-0">
                <button class="filter-btn active px-4 py-2 rounded-xl bg-brand-green text-slate-950 font-bold text-xs transition cursor-pointer" data-filter="all">Tous</button>
                <button class="filter-btn px-4 py-2 rounded-xl bg-slate-200 dark:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium text-xs transition cursor-pointer" data-filter="anniversaire">Anniversaires</button>
                <button class="filter-btn px-4 py-2 rounded-xl bg-slate-200 dark:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium text-xs transition cursor-pointer" data-filter="mariage">Mariages</button>
                <button class="filter-btn px-4 py-2 rounded-xl bg-slate-200 dark:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium text-xs transition cursor-pointer" data-filter="evenement">Événements Pro</button>
                <button class="filter-btn px-4 py-2 rounded-xl bg-slate-200 dark:bg-slate-900 text-slate-700 dark:text-slate-300 font-medium text-xs transition cursor-pointer" data-filter="apps">Apps & Logistique</button>
            </div>
        </div>

        <!-- Grille des éléments de la galerie -->
        <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            
            <!-- Affiche Anniversaire -->
            <div class="galerie-card bg-white dark:bg-slate-900 rounded-2xl overflow-hidden shadow-sm border border-slate-200/80 dark:border-slate-800 hover:shadow-md transition group" data-category="anniversaire">
                <div class="h-64 overflow-hidden bg-slate-100 dark:bg-slate-950 relative">
                    <img src="https://images.unsplash.com/photo-1530103862676-de8c9debad1d" alt="Affiche Anniversaire" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    <span class="absolute top-3 right-3 px-3 py-1 bg-slate-950/80 backdrop-blur text-emerald-400 text-xs font-bold rounded-lg">Anniversaire</span>
                </div>
                <div class="p-6">
                    <span class="text-xs font-semibold text-brand-green uppercase tracking-wider">Dembélé Design Service</span>
                    <h3 class="text-lg font-bold mt-1 mb-2">Affiche d'Anniversaire Premium</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400">Design sur-mesure pour célébration d'anniversaire avec retouches IA et visuel haute définition.</p>
                </div>
            </div>

            <!-- Affiche Mariage -->
            <div class="galerie-card bg-white dark:bg-slate-900 rounded-2xl overflow-hidden shadow-sm border border-slate-200/80 dark:border-slate-800 hover:shadow-md transition group" data-category="mariage">
                <div class="h-64 overflow-hidden bg-slate-100 dark:bg-slate-950 relative">
                    <img src="https://images.unsplash.com/photo-1519741497674-611481863552" alt="Faire-part Mariage" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    <span class="absolute top-3 right-3 px-3 py-1 bg-slate-950/80 backdrop-blur text-emerald-400 text-xs font-bold rounded-lg">Mariage</span>
                </div>
                <div class="p-6">
                    <span class="text-xs font-semibold text-brand-green uppercase tracking-wider">Création Visuelle</span>
                    <h3 class="text-lg font-bold mt-1 mb-2">Faire-part & Affiche de Mariage</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400">Conception élégante de cartes d'invitation et affiches souvenir de mariage.</p>
                </div>
            </div>

            <!-- Affiche Événement Professionnel -->
            <div class="galerie-card bg-white dark:bg-slate-900 rounded-2xl overflow-hidden shadow-sm border border-slate-200/80 dark:border-slate-800 hover:shadow-md transition group" data-category="evenement">
                <div class="h-64 overflow-hidden bg-slate-100 dark:bg-slate-950 relative">
                    <img src="https://images.unsplash.com/photo-1540575467063-178a50c2df87" alt="Affiche Conférence" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    <span class="absolute top-3 right-3 px-3 py-1 bg-slate-950/80 backdrop-blur text-emerald-400 text-xs font-bold rounded-lg">Événement</span>
                </div>
                <div class="p-6">
                    <span class="text-xs font-semibold text-brand-green uppercase tracking-wider">Branding Organisation</span>
                    <h3 class="text-lg font-bold mt-1 mb-2">Banner & Roll-up Conférence</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400">Identité visuelle complète pour séminaire et sommets internationaux.</p>
                </div>
            </div>

            <!-- Application Demshop POS -->
            <div class="galerie-card bg-white dark:bg-slate-900 rounded-2xl overflow-hidden shadow-sm border border-slate-200/80 dark:border-slate-800 hover:shadow-md transition group" data-category="apps">
                <div class="h-64 overflow-hidden bg-slate-100 dark:bg-slate-950 relative">
                    <img src="https://images.unsplash.com/photo-1556742049-0a67d553c2a8" alt="Demshop POS" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    <span class="absolute top-3 right-3 px-3 py-1 bg-slate-950/80 backdrop-blur text-emerald-400 text-xs font-bold rounded-lg">Logiciel Web</span>
                </div>
                <div class="p-6">
                    <span class="text-xs font-semibold text-brand-green uppercase tracking-wider">FastAPI & Python</span>
                    <h3 class="text-lg font-bold mt-1 mb-2">Application Demshop POS</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400">Logiciel de gestion des ventes, caisse enregistreuse et suivi des stocks sans scanner.</p>
                </div>
            </div>

            <!-- Solution Logistique ETALON EXPRESS -->
            <div class="galerie-card bg-white dark:bg-slate-900 rounded-2xl overflow-hidden shadow-sm border border-slate-200/80 dark:border-slate-800 hover:shadow-md transition group" data-category="apps">
                <div class="h-64 overflow-hidden bg-slate-100 dark:bg-slate-950 relative">
                    <img src="https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d" alt="Projet Logistique" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                    <span class="absolute top-3 right-3 px-3 py-1 bg-slate-950/80 backdrop-blur text-emerald-400 text-xs font-bold rounded-lg">Logistique</span>
                </div>
                <div class="p-6">
                    <span class="text-xs font-semibold text-brand-green uppercase tracking-wider">ETALON EXPRESS</span>
                    <h3 class="text-lg font-bold mt-1 mb-2">Système de Suivi de Colis</h3>
                    <p class="text-sm text-slate-600 dark:text-slate-400">Plateforme d'automatisation administrative et de traçabilité des flux logistiques.</p>
                </div>
            </div>

        </div>
    </section>

    <!-- Section Contact (Formulaire -> Redirection WhatsApp) -->
    <section id="contact" class="py-24 max-w-4xl mx-auto px-4">
        <div class="bg-white dark:bg-slate-900 p-8 md:p-12 rounded-3xl shadow-xl border border-slate-200/80 dark:border-slate-800 relative overflow-hidden">
            <div class="text-center max-w-xl mx-auto mb-10">
                <h2 class="text-3xl font-bold mb-3">Me Contacter</h2>
                <p class="text-slate-600 dark:text-slate-400 text-sm">Discutons de votre projet d'affiche, d'application ou d'opportunité professionnelle sur WhatsApp.</p>
            </div>

            <form id="contact-form" class="space-y-6">
                <div class="grid md:grid-cols-2 gap-6">
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Votre nom complet</label>
                        <input type="text" name="name" required placeholder="Ex: Jean Dupont" class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition">
                    </div>
                    <div>
                        <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Votre email</label>
                        <input type="email" name="email" required placeholder="Ex: jean@example.com" class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition">
                    </div>
                </div>
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Objet / Type de projet</label>
                    <select name="project_type" class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition">
                        <option value="Affiche Anniversaire / Mariage">Affiche Anniversaire / Mariage</option>
                        <option value="Branding Événement / Flyer">Branding Événement / Flyer</option>
                        <option value="Développement Web & Application">Développement Web & Application</option>
                        <option value="Projet Logistique / Stage / Emploi">Projet Logistique / Stage / Emploi</option>
                    </select>
                </div>
                <div>
                    <label class="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-2">Message</label>
                    <textarea name="description" rows="4" required placeholder="Décrivez votre besoin..." class="w-full px-4 py-3 rounded-xl border border-slate-300 dark:border-slate-800 bg-slate-50 dark:bg-slate-950 focus:ring-2 focus:ring-brand-green outline-none transition"></textarea>
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
        <p>&copy; 2026 DEMBÉLÉ OUSSÉNI - Dembélé Studio. Tous droits réservés.</p>
    </footer>

    <!-- Script de filtrage et WhatsApp -->
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof lucide !== 'undefined') { lucide.createIcons(); }

            // Mode sombre / clair
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

            // Filtrage de la Galerie
            const filterBtns = document.querySelectorAll('.filter-btn');
            const galerieCards = document.querySelectorAll('.galerie-card');

            filterBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    filterBtns.forEach(b => {
                        b.classList.remove('bg-brand-green', 'text-slate-950', 'font-bold');
                        b.classList.add('bg-slate-200', 'dark:bg-slate-900', 'text-slate-700', 'dark:text-slate-300', 'font-medium');
                    });
                    btn.classList.remove('bg-slate-200', 'dark:bg-slate-900', 'text-slate-700', 'dark:text-slate-300', 'font-medium');
                    btn.classList.add('bg-brand-green', 'text-slate-950', 'font-bold');

                    const filter = btn.getAttribute('data-filter');
                    galerieCards.forEach(card => {
                        if (filter === 'all' || card.getAttribute('data-category') === filter) {
                            card.style.display = 'block';
                        } else {
                            card.style.display = 'none';
                        }
                    });
                });
            });

            // Formulaire -> WhatsApp
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
        f"Projet : *{project_type}*\n\n"
        f"Détails :\n{description}"
    )
    encoded_message = urllib.parse.quote(wa_message)
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"
    
    return {
        "message": "Redirection vers WhatsApp en cours...",
        "whatsapp_url": whatsapp_url
    }
