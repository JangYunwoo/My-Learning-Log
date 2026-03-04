number_of_book = 100
many_user = []

def decrease_book(number):
    global number_of_book
    print(f"남은 책의 수 : {number_of_book - number}")
    return 

def rental_book(info):
    for name, age in info.items():
        decrease_book(age // 10)
        print(f"{name}님이 {age // 10}권의 책을 대여하였습니다.")

def create_user(name, age): #환영합니다
    global many_user
    print(f"{name}님 환영합니다!")
    user_info = {'이름': name, '나이': age}
    many_user.append(user_info)
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]

list(map(create_user, name, age)) # 환영합니다

user_info = []

list(map(lambda x: user_info.append({x['이름']: x['나이']}), many_user)) # 도전

# for i in many_user:
#     user_info.append({i['이름']: i['나이']})

for i in user_info:
    rental_book(i)