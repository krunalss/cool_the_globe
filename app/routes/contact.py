from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@router.post("/contact")
async def submit_contact_form(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    # Here you can handle the form submission, like saving to a database or sending an email
    print(f"Name: {name}, Email: {email}, Message: {message}")
    return templates.TemplateResponse("contact.html", {"request": request, "message": "Message sent successfully!"})
