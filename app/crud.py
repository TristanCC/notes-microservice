notes = []

def create_note(content: str):
    note = {"id": len(notes) + 1, "content": content}
    notes.append(note)
    return note

def get_all_notes():
    return notes
