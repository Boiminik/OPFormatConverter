import requests
import json
import os
import time
import pyperclip
import re

CACHE_FILE = "./db/cardsDB.json"
CACHE_MAX_AGE = 60 * 60 * 24 * 7  # 7 Tage

def clean_card_name(name):
    return re.sub(r"\s*\([^)]*\)", "", name).strip()

def download_cards():
    requestList = [
        'allSetCards', 
        'allSTCards', 
        'allPromos'
    ]

    cards = {}

    for request in requestList:
        url = f"https://www.optcgapi.com/api/{request}/?format=json"
        print(f"Downloading {url} ...")
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
        
        if response.status_code != 200:
            print(f"ERROR: Status code {response.status_code}")
            continue

        try:
            data = response.json()
        except Exception as e:
            print(f"ERROR parsing JSON for {request}: {e}")
            continue

        for card in data:
            card_id = card["card_set_id"]
            card_name = clean_card_name(card["card_name"])
            cards[card_id] = {
                "name": card_name,
                "set": card["set_name"]
            }

    # Prüfe, ob Verzeichnis existiert
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)

    # Atomic write → endgültige JSON-Datei
    temp_file = CACHE_FILE + ".tmp"
    with open(temp_file, "w", encoding="utf-8") as f:
        json.dump(cards, f, indent=2, ensure_ascii=False)
    os.replace(temp_file, CACHE_FILE)

    print(f"Saved {len(cards)} cards to {CACHE_FILE}")
    return cards

def load_cards():
    if not os.path.exists(CACHE_FILE):
        print("Card database not found. Downloading...")
        return download_cards()

    age = time.time() - os.path.getmtime(CACHE_FILE)
    if age > CACHE_MAX_AGE:
        print("Card database outdated. Updating...")
        return download_cards()

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"ERROR loading JSON: {e}. Redownloading...")
        return download_cards()
    
def convert_deck(deck_text, db):

    result = []

    lines = deck_text.strip().splitlines()

    for line in lines:

        if not line.strip():
            continue

        try:
            amount, card_id = line.split("x")
        except ValueError:
            result.append(f"# FORMAT ERROR: {line}")
            continue

        card = db.get(card_id)

        if not card:
            result.append(f"# CARD NOT FOUND: {card_id}")
            continue

        result.append(f"{amount}x {card['name']} {card_id} ({card['set']})")

    return "\n".join(result)

if __name__ == "__main__":

    db = load_cards()

# HIER DECK EINFÜGEN
    deck = """
4xEB01-009
2xEB02-003
2xEB02-016
4xEB02-017
4xOP02-040
2xOP06-018
1xOP08-001
4xOP08-007
4xOP08-010
4xOP08-013
4xOP08-015
4xOP08-016
4xOP09-029
4xOP14-032
2xST01-014
2xST21-014
"""

    converted = convert_deck(deck, db)

    # Ergebnis in Zwischenablage kopieren
    pyperclip.copy(converted)

    print("\nConverted Deck (copied to clipboard):\n")
    print(converted)