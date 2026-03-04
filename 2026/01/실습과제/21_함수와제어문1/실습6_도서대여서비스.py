def rental_book(name, number):
    print(f"{name}님이 {decrease_book(number)}권의 책을 대여하였습니다.")

number_of_book = 100

def decrease_book(number):
    global number_of_book
    print(f"남은 책의 수 : {number_of_book - number}")
    return number

rental_book('홍길동', 3)