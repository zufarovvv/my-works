import json


def load_data():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []

def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)