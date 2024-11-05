import json
import os
import time
import requests


def main():
    with open("artwork.json", "r") as file:
        data = json.load(file)

    output = "mtg_images"
    os.makedirs(output, exist_ok=True)
    for card in data:
        if card == data[14]:
            break
        print(card.get("layout"))
        name = card.get("name")
        uri = card.get("image_uris", {}).get("normal")
        id = card.get("id")
        if not uri:
            continue

main()