from django.shortcuts import render
import os
from dotenv import load_dotenv
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):

    load_dotenv()

    API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
    API_KEY = os.getenv('api_key')

    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        if item.get('bestDuration'):
            info = {
                'isbn': item['isbn'],
                'title': item['title'],
                'pubDate': item['pubDate'],
                'author': item['author'],
                'bestDuration': item['bestDuration'],
                'salesPoint': item['salesPoint'],
            }
            result.append(info)

    result.sort(key=lambda x: x['salesPoint'], reverse=True)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)