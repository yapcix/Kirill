from PIL import Image

im = Image.open("owl.jpeg")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения

for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        pixels[i, j] = g, b, r

im.save("owl1.jpeg")
