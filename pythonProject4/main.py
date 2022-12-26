# Задача 1

cooc_book = {}
dish_list = []
with open("coocbook.txt", "rt", encoding="utf8") as file:
    for l in file:
        dish_name = l.strip()
        ingridient_list = []
        dish = {dish_name: ingridient_list}
        dish_count = file.readline()
        for i in range(int(dish_count)):
            ing = file.readline().strip().split(' | ')
            ingridient_list.append({'ingredient_name': ing[0],
                                     'quantity': int(ing[1]),
                                     'unit_of_measurement': ing[2]})
            dish_list.append(dish)
        blank_line = file.readline()
        cooc_book.update(dish)
# print(cooc_book)

# Задача 2

def get_shop_list_by_dishes(dishes, person_count):
    necessary_ingredients = {}
    for dish in dishes:
        if dish in cooc_book:
            for indgrient in cooc_book[dish]:
                quantity_all = int(indgrient['quantity']) * person_count
                dict_list = {indgrient['ingredient_name']: {'unit_of_measurement': indgrient['unit_of_measurement'], 'quantity': quantity_all}}
                necessary_ingredients.update(dict_list)
    return necessary_ingredients
print(get_shop_list_by_dishes(['Шаверма', 'Омлет'], 4))

# Задача 3

outputfile = 'output.txt'
file1 = "1.txt"
file2 = '2.txt'
file3 = '3.txt'
myfile = open(outputfile, mode='w', encoding='utf-8')
def num_of_lines(*files):
    count = {}
    for file in files:
        with open(file, mode='r', encoding='utf-8') as f:
            count.update({file[-5:] : (len(f.readlines()))})
    files2 = {}
    for i in sorted(count, key=count.get, reverse=True):
        files2[i] = count[i]
    print(files2)
    for key, value in files2.items():
        myfile.write(f'Даны файлы: {key} \n')
        myfile.write(f'Количество строк: {value}, файл номер: {key}\n')
    return
num_of_lines(file1, file2, file3)
