import os
import urllib.parse
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

app = FastAPI(
    title="Dembele Studio - Agency Engine",
    description="Backend de gestion des demandes de projets et notifications WhatsApp",
    version="2.0.0"
)

# Montage des dossiers statiques et templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Numéro WhatsApp principal pour la réception automatique des leads
WHATSAPP_PRIMARY = "2250544580183"

class ContactSchema(BaseModel):
    name: str
    email: str
    phone: str
    project_type: str
    budget: str
    description: str

@app.get("/")
async def render_home(request: Request):
    """Rendu de la vitrine principale avec comptabilité FastAPI moderne."""
    return templates.TemplateResponse(request, "index.html", {})

@app.post("/api/contact")
async def handle_contact_submission(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    project_type: str = Form(...),
    budget: str = Form("Non spécifié"),
    description: str = Form(...)
):
    """
    Traite le formulaire de contact, valide les données et génère 
    le lien direct de notification vers le WhatsApp principal (+225 05 44 58 01 83).
    """
    try:
        # Formatage structuré du message pour WhatsApp
        formatted_message = (
            f"🚀 *NOUVELLE DEMANDE DE PROJET - DEMBELE STUDIO*\n"
            f"-----------------------------------------\n"
            f"👤 *Client :* {name}\n"
            f"✉️ *Email :* {email}\n"
            f"📞 *Téléphone :* {phone}\n"
            f"🎯 *Prestation :* {project_type}\n"
            f"💰 *Budget estimé :* {budget}\n"
            f"-----------------------------------------\n"
            f"📝 *Description du besoin :*\n{description}\n"
            f"-----------------------------------------\n"
            f"⚡ *Source :* Formulaire Web Dembele Studio"
        )

        # Encodage URL sécurisé pour la transmission WhatsApp
        encoded_text = urllib.parse.quote(formatted_message)
        whatsapp_redirect_url = f"https://api.whatsapp.com/send?phone={WHATSAPP_PRIMARY}&text={encoded_text}"

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": "Demande enregistrée avec succès ! Redirection WhatsApp en cours...",
                "whatsapp_url": whatsapp_redirect_url
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur interne : {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)