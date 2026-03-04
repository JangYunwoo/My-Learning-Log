import requests

API_URL = 'https://jsonplaceholder.typicode.com/users/'

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

dummy_data = []
for i in range(1, 11):
    response = requests.get(f"{API_URL}{i}")
    parsed_data = response.json()
    if -80 < float(parsed_data['address']['geo']['lat']) < 80 and -80 < float(parsed_data['address']['geo']['lng']) < 80:
        dummy_data += [{'company': parsed_data['company']['name'], 'lat': parsed_data['address']['geo']['lat'],
        'lng': parsed_data['address']['geo']['lng'], 'name': parsed_data['name']}]

def create_user():
    censored_user_list = []
    for i in dummy_data:
        if censorship(i['company'], i['name']):
            censored_user_list += [{i['company']: [i['name']]}]
    return censored_user_list
        
def censorship(company_name, name):
    if company_name in black_list:
        print(f"{company_name} 소속의 {name} 은/는 등록할 수 없습니다.")
        return False
    else:
        print("이상 없습니다.")
        return True

print(create_user())