import os
from pprint import pprint

cook_book = {}

path = os.path.join(os.getcwd(), "file_dishes.txt")
with open(path, encoding='utf-8') as file:
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        ingredients_list = []
        for item in range(counter):
            ingredient, quantity, measure = file.readline().strip().split('|')
            ingredients_list.append(
                {'ingredient': ingredient, 'quantity': quantity, 'measure': measure}
            )
        file.readline()
        cook_book[dish_name] = ingredients_list


# pprint(cook_book)

