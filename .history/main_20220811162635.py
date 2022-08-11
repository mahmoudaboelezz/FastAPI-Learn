from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home():
    data = {
         "page": "Home Page"
    }
    return templates.TemplateResponse("page.html", 
    {"request": request, "data": data})  