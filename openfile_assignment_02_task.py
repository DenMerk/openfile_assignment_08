from openfile_assignment_01_task import cook_book
from pprint import pprint

dishes = ['Утка по-пекински', 'Запеченный картофель', 'Омлет']
person_count = 5


def get_shop_list_by_dishes(dishes_list, people):
    shop_list = {}
    for dish in dishes_list:
        for item in cook_book[dish]:
            ingredient = item['ingredient']
            measure = item['measure']
            quantity = int(item['quantity']) * people
            if ingredient in shop_list:
                shop_list[ingredient]['quantity'] += quantity
            else:
                shop_list[ingredient] = {'measure': measure, 'quantity': quantity}
    pprint(shop_list)


get_shop_list_by_dishes(dishes, person_count)





