document.addEventListener('DOMContentLoaded', () => {
    // 1. Initialisation des icônes Lucide et d'AOS (Animate On Scroll)
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
    
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 800,
            once: true,
            easing: 'ease-out-quad'
        });
    }

    // 2. Gestion du Mode Clair / Sombre (Light / Dark Toggle)
    const themeToggleBtn = document.getElementById('theme-toggle');
    const htmlElement = document.documentElement;

    // Vérifier la préférence enregistrée en mémoire
    if (localStorage.getItem('theme') === 'light') {
        htmlElement.classList.remove('dark');
    } else {
        htmlElement.classList.add('dark'); // Mode sombre par défaut
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
            // Rafraîchir les icônes si nécessaire
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
        });
    }

    // 3. Compteurs animés (CounterUp)
    animateCounter('counter-projects', 0, 35, 2000);
    animateCounter('counter-satisfaction', 0, 100, 2000, '%');

    // 4. Filtrage du Portfolio
    const filterButtons = document.querySelectorAll('.filter-btn');
    const portfolioItems = document.querySelectorAll('.portfolio-item');

    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            filterButtons.forEach(b => {
                b.classList.remove('bg-brand-green', 'text-brand-dark');
                b.classList.add('bg-slate-900', 'text-slate-300');
            });
            btn.classList.remove('bg-slate-900', 'text-slate-300');
            btn.classList.add('bg-brand-green', 'text-brand-dark');

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

    // 5. Soumission du formulaire et redirection automatique WhatsApp
    const contactForm = document.getElementById('contact-form');
    const formStatus = document.getElementById('form-status');

    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(contactForm);

            formStatus.classList.remove('hidden', 'bg-red-500/20', 'text-red-400');
            formStatus.classList.add('bg-emerald-500/20', 'text-emerald-400');
            formStatus.textContent = "Traitement et préparation du message WhatsApp...";

            try {
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    body: formData
                });

                const result = await response.json();

                if (response.ok && result.whatsapp_url) {
                    formStatus.textContent = result.message;
                    contactForm.reset();

                    // Redirection automatique vers WhatsApp après 1 seconde
                    setTimeout(() => {
                        window.open(result.whatsapp_url, '_blank');
                    }, 1000);
                } else {
                    throw new Error("Échec de la transmission.");
                }
            } catch (err) {
                formStatus.classList.remove('bg-emerald-500/20', 'text-emerald-400');
                formStatus.classList.add('bg-red-500/20', 'text-red-400');
                formStatus.textContent = "Erreur lors de l'envoi. Veuillez réessayer ou contacter directement le +225 05 44 58 01 83.";
            }
        });
    }
});

// Fonction utilitaire pour l'animation des nombres
function animateCounter(id, start, end, duration, suffix = '+') {
    const obj = document.getElementById(id);
    if (!obj) return;
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = Math.floor(progress * (end - start) + start) + suffix;
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// Fonction pour présélectionner un service depuis les cartes de services
function setService(serviceName) {
    const select = document.getElementById('project_type');
    if (select) {
        select.value = serviceName;
    }
}

// Modale de prévisualisation du portfolio
function openModal(title, desc, imgSrc) {
    document.getElementById('modal-title').textContent = title;
    document.getElementById('modal-desc').textContent = desc;
    document.getElementById('modal-img').src = imgSrc;
    document.getElementById('portfolio-modal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('portfolio-modal').classList.add('hidden');
}
