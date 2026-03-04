import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'

dummy_data = []
for i in range(1, 11):
    response = requests.get(f"{API_URL}{i}")
    parsed_data = response.json()
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        dummy_data += [{'company': parsed_data['company']['name'], 'lat': parsed_data['address']['geo']['lat'],
        'lng': parsed_data['address']['geo']['lng'], 'name': parsed_data['name']}]

print(dummy_data)