print("Генератор мемов запущен!")

print("Выбери картинку для мема:")
print("1. Кот в очках")
print("2. Кот в ресторане")
image_number = input("Номер: ")
if image_number == 1:
    path = "images/cat_in_a_restaurant.png"
else:
    path = "images/cat_with_glasses.png"
print(path)

top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")
# print(f"{top_text} {bottom_text}")
# print(top_text, bottom_text, sep=" or ", end="\n") sep - символ между элементами.
print(top_text, bottom_text)