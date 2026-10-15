
"""Training and Wrestling Journal Functions."""


def save_entry(filename, date, notes):
    
    entry = date + " | " + notes + "\n"

    with open(filename, "a") as diary_file:
        diary_file.write(entry)


def load_entries(filename):
    
    try:
        with open(filename, "r") as diary_file:
            entries = diary_file.readlines()
        return entries
    except FileNotFoundError:
        return []


def search_entries(filename, date):
    
    entries = load_entries(filename)
    matches = []

    for entry in entries:
        if entry.startswith(date + " | "):
            matches.append(entry)

    return matches
