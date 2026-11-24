import json
import os

DATA_FILE = "budget_data.json"


def load_data(filename=DATA_FILE):
    """Read everything from the file. If there is no file yet, start with no users."""
    if not os.path.exists(filename):
        return {}
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def save_data(data, filename=DATA_FILE):
    """Write everything to the file, replacing what was there."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def get_user(username, filename=DATA_FILE):
    pass


def create_account(username, password_hash, filename=DATA_FILE):
    pass


def set_budget(username, weekly_budget, filename=DATA_FILE):
    pass


def add_spending(username, amount, category, spent_on, note, filename=DATA_FILE):
    pass


def delete_spending(username, entry_id, filename=DATA_FILE):
    pass