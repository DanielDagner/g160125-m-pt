# # # Тема: Чтение и запись данных в файл.
# # # Задание 1: Чтение данных из файла
# # # 1. Откройте файл `data.txt` для чтения.
# # # 2. Прочитайте весь контент файла и выведите его на экран.
# # # 3. Прочитайте первые 10 символов файла и выведите их на экран.
# # # 4. Прочитайте одну строку из файла и выведите ее на экран.
# # # 5. Прочитайте все строки файла и выведите их на экран.
# # # file_d = open("./text_files/data.txt")
# # # content = file_d.read()
# # # file_d.seek(0)
# # # partial_content = file_d.read(10)
# # # file_d.seek(0)
# # # one_line = file_d.readline()
# # # file_d.seek(0)
# # # all_lines = file_d.readlines()
# # # print(content)
# # # print(partial_content)
# # # print(one_line)
# # # print(all_lines)
# # # file_d.close()
# # # Задание 2: Запись данных в файл
# # # 1. Откройте (создайте) файл `output.txt` для записи.
# # # 2. Запишите в файл строку "Hello, World!".
# # # 3. Запишите в файл список строк: ["This is line 1\n", "This is line 2\n"].
# # # 4. Закройте файл.
# # # 5. Откройте файл `output.txt` для чтения и выведите его содержимое на экран.
# # # file_o = open("./text_files/output.txt", "w")
# # # file_o.write("Hello , World!\n")
# # # lines_to_append = ["This is line 1\n", "This is line 2\n"]
# # # file_o.writelines(lines_to_append)
# # # file_o.close()
# # #
# # # file_o = open("./text_files/output.txt", "r")
# # # all_file = file_o.read()
# # # print(all_file)
# # # file_o.close()
# #
# # # Задание 3: Добавление данных в файл
# # # 1. Откройте (создайте) файл `log.txt` для добавления данных.
# # # 2. Добавьте строку "New log entry\n" в конец файла.
# # # 3. Добавьте список строк ["Log entry 1\n", "Log entry 2\n"] в конец файла.
# # # 4. Закройте файл.
# # # 5. Откройте файл `log.txt` для чтения и выведите его содержимое на экран.
# # # file_l = open("./text_files/log.txt", "w")
# # # file_l.write("New log entry\n")
# # # lines_to_append = ["Log entry 1\n", "Log entry 2\n"]
# # # file_l.writelines(lines_to_append)
# # # file_l.close()
# # #
# # # file_l = open("./text_files/log.txt", "r")
# # # printend_file = file_l.read()
# # # print(printend_file)
# # # file_l.close()
# #
# # # Задание 4: Работа с указателем
# # # 1. Откройте (создайте) файл `pointer_example.txt` для чтения и записи.
# # # 2. Запишите в файл строку "Python File Handling\n".
# # # 3. Переместите указатель в начало файла и прочитайте первую строку.
# # # 4. Переместите указатель на позицию 7 и прочитайте следующие 5 символов.
# # # 5. Переместите указатель в конец файла и добавьте строку "End of file\n".
# # # 6. Переместите указатель в начало файла и прочитайте весь файл.
# # # file_p = open("./text_files/pointer_example.txt", 'w')
# # # file_p.close()
# # # file_p = open("./text_files/pointer_example.txt", 'r+')
# # # file_p.write("Python File Handling\n")
# # # file_p.seek(0)
# # # file_p.read()
# # # file_p.seek(7)
# # # file_p.read(5)
# # # file_p.seek(0, 2)
# # # file_p.write("End of file\n")
# # # file_p.seek(0)
# # # all_file = file_p.read()
# # # print(all_file)
# #
# #
# #
# # # Тема: Менеджер контекста и JSON
# #
# # # Тема: Менеджер контекста и JSON
# # import json
# # # Задача 1: Чтение и запись JSON данных с использованием менеджера контекста
# # # 1. Создайте словарь с информацией о пользователе (имя, возраст, город).
# # # 2. Запишите этот словарь в файл JSON `user.json` с использованием менеджера контекста.
# # # 3. Прочитайте данные из файла `user.json` и выведите их на экран.
# # data = {
# #     "name": "John",
# #     "age": 30,
# #     "city": "New York"
# # }
# # with open("./text_files/user.json", "w") as file:
# #     json.dump(data, file)
# # with open("./text_files/user.json") as file:
# #     data = json.load(file)
# #     print(data)
# # # Задача 2: Обновление данных в файле JSON
# # # 1. Прочитайте данные из файла `user.json`.
# # # 2. Обновите возраст пользователя на 29 лет.
# # # 3. Запишите обновленные данные обратно в файл JSON с использованием менеджера контекста.
# # with open("./text_files/user.json", "r") as file:
# #     data = json.load(file)
# #     data["age"] = 29
# # with open("./text_files/user.json", "w") as file:
# #     json.dump(data, file)
# # with open("./text_files/user.json") as file:
# #     correct = json.load(file)
# #     print(correct)
# # # Задача 3: Добавление нового пользователя в массив JSON
# # # 1. Прочитайте массив объектов из файла `users.json`
# # # (каждый объект содержит информацию о пользователе: имя, возраст, город).
# # # 2. Добавьте нового пользователя в массив.
# # # 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
# # with open("./text_files/user.json") as file :
# #     users = json.load(file)
# #     users = [users]
# #     new_user = {"name": "Daniel", "age": 26, "city": "Landshut"}
# #     users.append(new_user)
# # with open("./text_files/user.json", "w") as file:
# #    json.dump(users, file)
# # with open("./text_files/user.json") as file:
# #     new_file = json.load(file)
# #     print(new_file)
# # # Задача 4: Удаление пользователя из массива JSON
# # # 1. Прочитайте массив объектов из файла `users.json`.
# # # 2. Удалите одного из пользователей.
# # # 3. Запишите обновленный массив обратно в файл JSON с использованием менеджера контекста.
# # with open("./text_files/user.json", "r") as file:
# #     uninstall = json.load(file)
# #     uninstall.pop()
# # with open("./text_files/user.json", "w") as file:
# #    json.dump(uninstall, file)
# # with open("./text_files/user.json") as file:
# #     uninstall = json.load(file)
# #     print(uninstall)
# #
# ## Тема: Интеграционная практика. Мини-проект
# import json
#
# # Проект: Перепишите проект из уроков 7-8 с записью, чтением, обновлением и удалением товаров в файле.
# # Используйте файл как базу данных проекта.
# # Управление инвентарем в интернет-магазине
# # Разработайте программу для управления инвентарем интернет-магазина.
# # Программа должна позволять добавлять новые товары и удалять имеющиеся,
# # обновлять наименование, цену и количество существующих товаров,
# # искать товары по названию, выводить список всех товаров и их количество,
# # а также выводить товары с количеством ниже заданного значения стоимости и количества.
# #
# # Меню:
# # 1. Показать список товаров.
# # 2. Добавить товар.
# # 3. Удалить товар.
# # 4. Обновить название товара, стоимость или количество.
# # 5. Найти товар по названию.
# # 6. Вывести список товаров меньше определнной стоимости.
# # 7. Вывести список товаров меньше определенного количества.
#
#
#
# def save_inventory(inventory):
#     with open('inventory.json', 'w') as file:
#         json.dump(inventory, file)
#
# def load_inventory():
#     with open('inventory.json') as file:
#         return json.load(file)
#
# def show_inventory(inventory):
#     for product in inventory:
#         print_product(product)
#
# def add_product(inventory):
#     product = input("Enter product name: ")
#     price = int(input("Enter product price: "))
#     count = int(input("Enter product count: "))
#     inventory.append({'product': product.title(), 'price': price, 'count': count})
#     return inventory
#
# def remove_product(inventory):
#     product = input("Enter product name: ")
#     for item in inventory:
#         if item['product'].lower() == product.lower():
#             inventory.remove(item)
#     return inventory
#
# def edit_product(inventory):
#     product = input("Enter product name: ")
#     for item in inventory:
#         if item['product'].lower() == product.lower():
#             new_product = input(f"Enter new product name or {item['product']}: ")
#             if new_product:
#                 item['product'] = new_product.title()
#             new_price = input(f"Enter new product price or {item['price']}: ")
#             if new_price:
#                 item['price'] = int(new_price) * 0.1
#             new_count = input(f"Enter new product count or {item['count']}: ")
#             if new_count:
#                 item['count'] = int(new_count)
#     return inventory
#
# def find_product(inventory):
#     product = input("Enter product name: ")
#     for item in inventory:
#         if item['product'].lower() == product.lower():
#             print_product(item)
#
# def find_product_min_cost(inventory):
#     price = int(input("Enter price: "))
#     for item in inventory:
#         if item['price'] <= price:
#             print_product(item)
#
# def print_product(product):
#     print(f"Product: {product['product']} Price: {product['price']} Count: {product['count']}")
#
# def find_product_min_count(inventory):
#     count = int(input("Enter count: "))
#     for item in inventory:
#         if item['count'] <= count:
#             print_product(item)
#
# while True:
#     inventory = load_inventory()
#     user_input = input(
#         "1. Показать список товаров.\n"
#         "2. Добавить товар.\n"
#         "3. Удалить товар.\n"
#         "4. Обновить название товара, стоимость или количество.\n"
#         "5. Найти товар по названию.\n"
#         "6. Вывести список товаров меньше определнной стоимости.\n"
#         "7. Вывести список товаров меньше определенного количества.\n"
#         "8. Выйти.\n"
#     )
#     match user_input:
#         case "1":
#             show_inventory(inventory)
#         case "2":
#             inventory = add_product(inventory)
#             save_inventory(inventory)
#         case "3":
#             inventory = remove_product(inventory)
#             save_inventory(inventory)
#         case "4":
#             inventory = edit_product(inventory)
#             save_inventory(inventory)
#         case "5":
#             find_product(inventory)
#         case "6":
#             find_product_min_cost(inventory)
#         case "7":
#             find_product_min_count(inventory)
#         case "8":
#             break
#         case _:
#             print("Invalid input")
#
#
#
#
