from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI()

# In-memory storage (no database for now)
notes = {}

class NoteRequest(BaseModel):
    title: str
    content: str

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/notes")
def create_note(note: NoteRequest):
    note_id = str(uuid.uuid4())
    notes[note_id] = {
        "id": note_id,
        "title": note.title,
        "content": note.content
    }
    return notes[note_id]

@app.get("/notes")
def get_notes():
    return list(notes.values())