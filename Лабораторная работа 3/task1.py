# TODO Напишите функцию для поиска индекса товара
def search(list_, item): # передаем в функцию список и искомый предмет
    for i in range(len(list_)): # проходимся по списку
        if list_[i] == item: # если элемент списка равен искому элементу возвращаем индекс
            return i # после оператора return, цикл завершится и ф-ция вернет индекс

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    search(items_list, find_item)
    index_item =  search(items_list, find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
