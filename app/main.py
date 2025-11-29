from fastapi import FastAPI
from .schemas import NoteCreate, NoteResponse
from . import crud

app = FastAPI()

@app.get("/notes", response_model=list[NoteResponse])
async def get_notes():
    return crud.get_all_notes()

@app.post("/notes", response_model=NoteResponse)
async def post_note(note: NoteCreate):
    return crud.create_note(note.content)
