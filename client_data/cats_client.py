from typing import Optional
import requests


class CatsClient:
    def __init__(self, base_url: str = "https://api.thecatapi.com"):
        self.base_url = base_url

    def get_random_cat_image(self, category: Optional[str] = None) -> str:
        endpoint = f"{self.base_url}/v1/images/search"
        params = {"category": category} if category else {}
        response = requests.get(endpoint, params=params)

        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")
            print(f"Response Text: {response.text}")
            return f"Error: {response.status_code}"

        if response.status_code == 200:
            cat_data = response.json()
            cat_image_url = cat_data[0].get("url")
            return f"Random Cat Image: {cat_image_url}"
        else:
            return f"Error: {response.status_code}"

# Створення об'єкта CatsClient
cats_client = CatsClient(base_url="https://api.thecatapi.com")

# Виклик функції для отримання випадкового зображення кота
random_cat_image = cats_client.get_random_cat_image()

# Вивід отриманого зображення кота
print(random_cat_image)
