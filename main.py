# Домашняя работа теме: Работа с файлами
reciple_book_filename = 'recipes.txt'


# Задача 1. Получение словаря с рецептами
def get_recipes():
    with open(reciple_book_filename, 'rt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredient_count = int(file.readline())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip('\n').split(' | ')
                ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            file.readline()
            cook_book[dish_name] = ingredients
    return cook_book


# Задача 2. Получение словаря с ингредиентами
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_recipes()
    ingredients = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ing_name = ingredient['ingredient_name']
                ing_measure = ingredient['measure']
                ing_quantity = int(ingredient['quantity']) * person_count
                if ing_name in ingredients:
                    ingredients[ing_name]['quantity'] += ing_quantity
                else:
                    ingredients[ing_name] = {'measure': ing_measure, 'quantity': ing_quantity}
        else:
            print(dish + ' в рецептах не найдено')
    if ingredients:
        return ingredients


# Полевые испытания
def print_ingredients(ingredients):
    print("Список продуктов для приготовления заказа:")
    for ing_name, ing in ingredients.items():
        print(f"{ing_name}: {ing['quantity']} {ing['measure']}")


zakaz = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 13)
print_ingredients(zakaz)
