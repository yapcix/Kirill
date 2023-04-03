"""
 С помощью библиотеки PIL мы можем не только изменять существующие изображения, но и создавать новые.
 Для этого используется функция Image.new, которая принимает тип палитры (мы договорились использовать RGB),
 кортеж с размером нового изображения и цвет, которым будет залито это изображение.
 В данном примере создается изображение 500 на 500 пикселей, залитое зеленым:
"""
from PIL import Image, ImageDraw


def createSquare(width, height):
    im = Image.new("RGB", (width, height), (0, 255, 0))
    print(im.size)
    # Просто посмотрим, изображение какого размера у нас получилось
    im.save("5.jpg")


def drawLine(width, height):
    """
        ImageDraw. У этого объекта есть много инструментов для создания графических примитивов: прямых, кривых,
        точек, прямоугольников, дуг и т. д.
         Функция line нужна для рисования линий. Она принимает кортеж с координатами начала и конца отрезка и
        дополнительные параметры — цвет заливки и толщину линий. Можно передавать более 2 точек,
        тогда точки будут соединены последовательно — и мы получим некоторую ломаную линию.
    """
    im = Image.new("RGB", (width, height), (0, 0, 0))
    # на изображении создаем рисунок для рисования
    draw = ImageDraw.Draw(im)
    # рисуем линию
    draw.line((0, 0, 100, 200), fill=(255, 0, 0), width=1)
    # сохраним изображением в файл формата PNG
    im.save('6.png', "PNG")


def picture_car(file_name, width, height, sky_color='#75BBFD',
                asphalt_color='#4E5452', car_color='#bF311A',
                wheels_color='#000000', sun_color='#FFDB00'):
    """
    Функция line нужна для рисования линий. Она принимает кортеж с координатами начала и конца отрезка и
    дополнительные параметры — цвет заливки и толщину линий. Можно передавать более 2 точек,
     тогда точки будут соединены последовательно — и мы получим некоторую ломаную линию.

     С помощью функции rectangle, которая рисует прямоугольники, нарисуем небо и дорогу. Функция принимает на вход
     координату левого верхнего угла прямоугольника и координату правого нижнего угла и цвет заливки.

     С помощью функции ellipse рисуем солнце. Функция принимает на вход координаты верхнего левого и правого нижнего
      угла прямоугольника, внутри которого будет вписан эллипс и цвет заливки. Для получения круга описанный
      прямоугольник должен быть квадратом. Обратите внимание: часть солнца находится за пределами изображения.
      При этом при рисовании никакой ошибки не возникнет — часть рисунка за пределами изображения просто пропадет.
    :param file_name:
    :type file_name:
    :param width:
    :type width:
    :param height:
    :type height:
    :param sky_color:
    :type sky_color:
    :param asphalt_color:
    :type asphalt_color:
    :param car_color:
    :type car_color:
    :param wheels_color:
    :type wheels_color:
    :param sun_color:
    :type sun_color:
    :return:
    :rtype:
    """
    im = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(im)

    drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)), asphalt_color)

    drawer.ellipse((
        (int(0.8 * width)), -int(0.2 * height),
        (int(1.2 * width), int(0.2 * height))),
        sun_color)

    drawer.polygon(((int(0.2 * width), int(height * 0.85)),
                    (int(0.2 * width), int(height * 0.7)),
                    (int(0.3 * width), int(height * 0.6)),
                    (int(0.55 * width), int(height * 0.6)),
                    (int(0.65 * width), int(height * 0.7)),
                    (int(0.8 * width), int(height * 0.7)),
                    (int(0.8 * width), int(height * 0.85))),
                   car_color)

    # Рисуем красный эллипс с черной оконтовкой.
    for i in range(2):
        drawer.ellipse((int(0.3 * width) + int(0.3 * width) * i, int(0.8 * height),
                        (int(0.4 * width) + int(0.3 * width) * i,
                         int(0.9 * height))),
                       fill=wheels_color,
                       outline=(125, 127, 125),
                       width=20
                       )

    im.save(file_name)
    # im.show()


def picture(file_name, width, height, sky_color="#87CEEB", ocean_color="#017B92", boat_color="#874535",
            sail_color="#FFFFFF", sun_color="#FFCF40"):
    im = Image.new("RGB", (width, height))
    drawer = ImageDraw.Draw(im)

    # Рисуем фон
    drawer.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
    drawer.rectangle(((0, int(height * 0.8)), (width, height)), ocean_color)

    # Рисуем солнце
    drawer.ellipse((
        (int(0.8 * width)), -int(0.2 * height),
        (int(1.2 * width), int(0.2 * height))),
        sun_color)
    # Рисуем мачту Рисуем корпус
    drawer.polygon(((int(0.25 * width), int(0.65 * height)),
                    (int(0.49 * width), int(0.65 * height)),
                    (int(0.49 * width), int(0.3 * height)),
                    (int(0.51 * width), int(0.3 * height)),
                    (int(0.51 * width), int(0.65 * height)),
                    (int(0.75 * width), int(0.65 * height)),
                    (int(0.7 * width), int(0.85 * height)),
                    (int(0.3 * width), int(0.85 * height))), boat_color)

    # Рисуем парус
    drawer.polygon(((int(0.51 * width + 1),
                     int(0.3 * height),
                     int(0.66 * width + 1),
                     int(0.45 * height),
                     int(0.51 * width + 1),
                     int(0.6 * height))), sail_color)

    # im.save(file_name)
    im.show()


def average_value_picture(file_name):
    im = Image.open(file_name)
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    sq = [0, 0, 0]  # Массив для общего подсчета
    count = x * y

    for i in range(x):  # Цикл по ширине
        for j in range(y):  # Цикл по высоте
            sq[0] += pixels[i, j][0]
            sq[1] += pixels[i, j][1]
            sq[2] += pixels[i, j][2]

    out = [0, 0, 0]  # Массив для средних значений

    out[0] = int(sq[0] // count)  # Средние значения
    out[1] = int(sq[1] // count)
    out[2] = int(sq[2] // count)

    print(f'Средний цвет: rgb({out[0]}, {out[1]}, {out[2]})')
    # im.save(f"fon_{file_name}.jpeg")


def board(num, size):
    new_color = (0, 0, 0)
    size_x = size_y = int(size) * int(num)
    im = Image.new("RGB", (size_x, size_y), new_color)
    drawer = ImageDraw.Draw(im)

    for i in range(num):
        if i % 2 == 0:
            for j in range(num):
                if j % 2 != 0:
                    drawer.rectangle(((int(size) * j, int(size) * i),
                                      (int(size) * (j + 1), int(size) * (i + 1))),
                                     fill='white')
        else:
            for j in range(num):
                if j % 2 == 0:
                    drawer.rectangle(((int(size) * j, int(size) * i),
                                      (int(size) * (j + 1), int(size) * (i + 1))),
                                     fill='white')

    # im.save('res.png')
    im.show()


if __name__ == '__main__':
    # createSquare(500, 600)
    """
    Этот пример создает новое черное изображение размером 100 на 200 и нарисует на нем линию красного 
    цвета толщиной в 1 пиксель из левого верхнего в правый нижний угол. 
    
    """
    # drawLine(100, 200)

    # Рисуем картинку
    # picture()
    # picture('test.bmp', 1000, 800)

    # average_value_picture('car.jpg')

    # board(8, 50)
