my_string = input("Введите Ваше ФИО: ")
print("Длина Вашего ФИО:", len(my_string.replace(' ', '')))
print("Вот примеры написания Вашего ФИО: ")
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print("Первая буква вашего ФИО:", my_string[0].upper())
print("Последняя буква Вашего ФИО:", my_string.replace(' ', '').upper()[-1])
