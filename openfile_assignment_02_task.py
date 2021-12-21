from openfile_assignment_01_task import file_opener
from pprint import pprint

dishes = ['Утка по-пекински', 'Запеченный картофель', 'Омлет']


def get_shop_list_by_dishes(dishes_list, people=5):
    shop_list = {}
    cook_book = file_opener()
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


if __name__ == '__main__':
    get_shop_list_by_dishes(dishes)





