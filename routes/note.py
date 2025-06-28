from fastapi import APIRouter, Request
from pygments.lexer import default

from models.note import Note
from config.db import cursor , conn
from  schemas.note import noteEntity,notesEntity
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
note = APIRouter()


templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    cursor.execute("SELECT  title, important FROM note")
    notes = cursor.fetchall()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "notes": notes
    })



@note.post("/")
async def create_item(request: Request):
    form = await request.form()

    title = form.get("title", "").strip()
    description = form.get("description", "").strip()
    important = 1 if form.get("important") == "on" else 0

    if not title or not description:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": "Title and description are required."
        })

    query = "INSERT INTO note (title, note_description, important) VALUES (%s, %s, %s)"
    cursor.execute(query, (title, description, important))
    conn.commit()

    cursor.execute("SELECT title,important FROM note")
    notes = cursor.fetchall()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "notes": notes,
        "message": "Note added successfully"
    })

