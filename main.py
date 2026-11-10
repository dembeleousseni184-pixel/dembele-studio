from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# Montage indispensable pour charger les fichiers CSS, JS et images
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuration du dossier des templates HTML
templates = Jinja2Templates(directory="templates")

class ContactSchema(BaseModel):
    name: str
    email: str
    description: str

@app.get("/")
async def render_home(request: Request):
    """Rendu de la page d'accueil avec FastAPI."""
    return templates.TemplateResponse(request, "index.html", {})

@app.post("/api/contact")
async def handle_contact_submission(
    name: str = Form(...),
    email: str = Form(...),
    description: str = Form(...)
):
    return {"message": f"Merci {name}, votre message a bien été reçu !"}
