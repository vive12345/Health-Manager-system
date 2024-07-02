import requests
import json


class HealthNews:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_news(self):
        # Set API endpoint and parameters
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "country": "us",
            "category": "health",
            "apiKey": self.api_key
        }

        # Make API request and get response
        response = requests.get(url, params=params)
        data = json.loads(response.text)

        # Extract relevant information from response
        articles = data["articles"]
        news_list = []
        for article in articles:
            title = article["title"]
            description = article["description"]
            url = article["url"]
            image_url = article["urlToImage"]
            news_item = {"title": title, "description": description, "url": url, "image_url": image_url}
            news_list.append(news_item)

        return news_list


