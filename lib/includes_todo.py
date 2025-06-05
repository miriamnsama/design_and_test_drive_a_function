def includes_todo(notes):
    if '#todo' in notes.lower():
        return True
    else:
        return False