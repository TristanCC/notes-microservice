from fastapi import FastAPI

app = FastAPI()

@app.get("/notes")
async def getNotes():
    return {"message": "note"}

@app.post("/notes")
async def postNote(note: str):
    return {"note": "note"}
