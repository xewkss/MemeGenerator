from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")

print("Выбери картинку для мема:")
print("1. Кот в очках")
print("2. Кот в ресторане")
image_number = input("Номер: ")
if image_number == 1:
    path = "images/cat_with_glasses.png"
else:
    path = "images/cat_in_a_restaurant.png"
top_text = input("Введите верхний текст: ")
bottom_text = input("Введите нижний текст: ")
image = Image.open(path)
# print(f"{top_text} {bottom_text}")
# print(top_text, bottom_text, sep=" or ", end="\n") sep - символ между элементами.

width, height = image.size
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", size = 70)

text_size = draw.textbbox((0, 0), top_text, font)
text_width = text_size[2]
draw.text(((width - text_width) / 2, 10), top_text, font=font, fill="black")

text_size = draw.textbbox((0, 0), bottom_text, font)
text_width = text_size[2]
text_height = text_size[3]
draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill="black")

image.save("new_meme.jpg")
print("Ваш мем успешно сделан, и сохранен!")