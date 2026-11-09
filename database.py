import json
import os

DATA_FILE = "accounts.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    
        return []
def save_data(accounts):
    with open(DATA_FILE, "w") as file:
        json.dump(accounts, file, indent=4)
