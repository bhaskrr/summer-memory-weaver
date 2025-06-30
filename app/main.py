from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Initialize the fastapi app
app = FastAPI()


# Specify templates folder
templates = Jinja2Templates(directory="app/templates")


# Endpoints
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Render Homepage"""
    return templates.TemplateResponse("index.html", {"request": request, "story": None})
