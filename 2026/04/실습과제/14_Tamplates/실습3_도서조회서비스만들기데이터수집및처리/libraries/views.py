from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests

# Create your views here.
def index(request):

    load_dotenv()

    API_URL = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
    API_KEY = os.getenv('api_key')

    params = {
        'ttbkey': API_KEY,
        'QueryType': "ItemNewSpecial",
        "SearchTarget": "Book",
        "Start": 1,
        "MaxResults": 50,
        "Output": "JS",
        "Version": "20131101"
    }

    response = requests.get(API_URL, params=params)
    data = response.json()

    items = data.get('item', [])

    books = [
        {
            "isbn": item.get("isbn13"),
            "author": item.get("author"),
            "title": item.get("title"),
            "pubDate": item.get("pubDate"),
        }
        for item in items
    ]

    return render(request, "index.html", {"books": books})