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
        name = card.get("name")
        uri = card.get("image_uris", {}).get("normal")
        id = card.get("id")
        if not uri:
             continue

        image = requests.get(uri)
        try:
            if image.status_code == 200:
                if card.get("layout") == "normal":
                    filename = f"{name.replace(" ", "_").replace("/", "-")}_{id}.jpg"
                    path = os.path.join(output, filename)
                    with open(path, "wb") as image_file:
                        image_file.write(image.content)
                    print(f"Downloaded {name}")
            else:
                print(f"Failed to download {name}. {image.status_code}")
        except Exception as e:
            print(f"Error while downloading {name}: {e}")
    time.sleep(0.2)
main()