# 아래 함수를 수정하시오.
def get_keys_from_dict(dictionary):
    return list(dictionary)

def get_all_keys_from_dict(dictionary):
    A = []
    for key, val in dictionary.items():
        A.append(key)
        if type(dictionary[key]) is dict:
            for i in dictionary[key]:
                A.append(i)
    
    return A

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']
