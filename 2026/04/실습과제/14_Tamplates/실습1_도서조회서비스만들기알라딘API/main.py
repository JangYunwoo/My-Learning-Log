import os
from dotenv import load_dotenv
import requests
from pprint import pprint

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

print(data)

items = data.get('item')

if not items:
    print("데이터 없음", data)
else:
    books = []
    for item in items:
        books.append({
            "국제 표쥰 도서 번호": item.get("isbn13"),
            "저자": item.get("author"),
            "제목": item.get("title"),
            "출간일": item.get("pubDate"),
        })

pprint(books)