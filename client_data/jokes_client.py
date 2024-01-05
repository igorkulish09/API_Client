from typing import Optional
import requests


class JokesClient:
    def __init__(self, base_url: str = "https://api.icndb.com"):
        self.base_url = base_url

    def get_random_joke(self, category: Optional[str] = None) -> str:
        endpoint = f"{self.base_url}/jokes/random"
        params = {"limitTo": [category]} if category else {}
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()["value"]["joke"]
