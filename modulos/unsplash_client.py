import requests
import modulos.config as config

def get_unsplash_images(query, count=3):
    url = f"https://api.unsplash.com/search/photos?query={query}&per_page={count}"
    headers = {
        "Authorization": f"Client-ID {config.UNSPLASH_ACCESS_KEY}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    images = [result["urls"]["regular"] for result in data["results"]]
    return images
