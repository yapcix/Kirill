class Button:
    def __init__(self):
        self.clicks = 0

    def click(self):
        self.clicks += 1

    def reset(self):
        self.clicks = 0

    def click_count(self):
        return self.clicks


"""
Напишите класс Balance для описания весов с двумя чашами. 
На левую и правую чашу объекта будут добавляться 
грузы с различным весом, ваша задача определить положение чаш.
"""


class Balance:
    """
    Метод add_right принимает целое число — вес, положенный на правую чашу весов, add_left — на левую чашу.
    Метод result должен возвращать символ
      = — если вес на чашах одинаковый,
     R — если перевесила правая,
     L — если перевесила левая.
    """

    def __init__(self):
        self.right_weight = 0
        self.left_weight = 0

    def add_right(self, right_weight):
        self.right_weight += int(right_weight)

    def add_left(self, left_weight):
        self.left_weight += left_weight

    def result(self):
        if self.left_weight > self.right_weight:
            return 'L'
        elif self.left_weight < self.right_weight:
            return 'R'
        else:
            return '='


class OddEvenSeparator:
    def __init__(self):
        self.lst = []

    def add_number(self, num):
        self.lst.append(int(num))

    def even(self):
        return list(filter(lambda x: x % 2 == 0, self.lst))

    def odd(self):
        return list(filter(lambda x: x % 2 != 0, self.lst))


class BigBell:
    def __init__(self):
        self.a = 0

    def sound(self):
        if not self.a:
            print('ding')
            self.a = 1
        else:
            print('dong')
            self.a = 0


class MinMaxWordFinder:
    def __init__(self):
        self.lst = []

    def add_sentence(self, add_words):
        self.lst.extend(add_words.split())

    def shortest_words(self):
        len_lst = [len(i) for i in self.lst]
        check_len_word = 0
        out = []
        if len_lst:
            check_len_word = min(len_lst)
        for i in self.lst:
            if len(i) == check_len_word:
                out.append(i)
        return sorted(out)

    def longest_words(self):
        len_lst = [len(i) for i in self.lst]
        check_len_word = 0
        out = []
        if len_lst:
            check_len_word = max(len_lst)
        for i in self.lst:
            if len(i) == check_len_word:
                out.append(i)
        return sorted(set(out))


class BoundingRectangle:
    def __init__(self):
        self.rect_x = []
        self.rect_y = []

    def add_point(self, x, y):
        self.rect_x.append(x)
        self.rect_y.append(y)

    def width(self):
        return max(self.rect_x) - min(self.rect_x)

    def height(self):
        return max(self.rect_y) - min(self.rect_y)

    def bottom_y(self):
        return min(self.rect_y)

    def top_y(self):
        return max(self.rect_y)

    def left_x(self):
        return min(self.rect_x)

    def right_x(self):
        return max(self.rect_x)


class Selector:
    def __init__(self, values):
        self.values = values[:]

    def get_odds(self):
        return list(filter(lambda x: x % 2 == 1, self.values))

    def get_evens(self):
        return list(filter(lambda x: x % 2 == 0, self.values))


class MinStat(object):
    def __init__(self):
        self.lst = []

    def add_number(self, x):
        self.lst.append(x)

    def result(self):
        if self.lst:
            return min(self.lst)
        else:
            self.lst = None


class MaxStat(MinStat):

    def result(self):
        if self.lst:
            return max(self.lst)
        else:
            self.lst = None


class AverageStat(MinStat):

    def result(self):
        if self.lst:
            return sum(self.lst) / len(self.lst)
        else:
            self.lst = None


class Table(object):

    def __init__(self, rows, cols):
        self.field = [[0 for i in range(cols)] for i in range(rows)]
        self.rows = rows
        self.cols = cols

    def get_value(self, row, col):
        if row in range(self.rows) and col in range(self.cols):
            return self.field[row][col]
        return

    def set_value(self, row, col, value):
        self.field[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols




if __name__ == '__main__':
    # button = Button()
    # button.click()
    # print(button.click_count())

    # balance = Balance()
    # balance.add_right(10)
    # balance.add_left(5)
    # balance.add_left(5)
    # print(balance.result())
    # balance.add_left(1)
    # print(balance.result())

    # separator = OddEvenSeparator()
    # separator.add_number(1)
    # separator.add_number(5)
    # separator.add_number(6)
    # separator.add_number(8)
    # separator.add_number(3)
    # print(' '.join(map(str, separator.even())))
    # print(' '.join(map(str, separator.odd())))
    #
    # bell = BigBell()
    # bell.sound()
    # bell.sound()
    # bell.sound()

    # finder = MinMaxWordFinder()
    # finder.add_sentence('hello')
    # finder.add_sentence('abc')
    # finder.add_sentence('world')
    # finder.add_sentence('abc')
    # finder.add_sentence('def')
    # finder.add_sentence('asdf')
    # finder.add_sentence('abc')
    # finder.add_sentence('qwert')
    # finder.add_sentence('world')
    # print(' '.join(finder.shortest_words()))
    # print(' '.join(finder.longest_words()))

    # rect = BoundingRectangle()
    # rect.add_point(-1, -2)
    # rect.add_point(3, 4)
    # print(rect.left_x(), rect.right_x())
    # print(rect.bottom_y(), rect.top_y())
    # print(rect.width(), rect.height())

    # values = [11, 12, 13, 14, 15, 16, 22, 44, 66]
    # selector = Selector(values)
    # odds = selector.get_odds()
    # evens = selector.get_evens()
    # print(' '.join(map(str, odds)))
    # print(' '.join(map(str, evens)))

    # values = [1, 2, 4, 5]
    #
    # mins = MinStat()
    # maxs = MaxStat()
    # average = AverageStat()
    # for v in values:
    #     mins.add_number(v)
    #     maxs.add_number(v)
    #     average.add_number(v)
    #
    # print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

    tab = Table(3, 5)
    tab.set_value(0, 1, 10)
    tab.set_value(1, 2, 20)
    tab.set_value(2, 3, 30)
    for i in range(tab.n_rows()):
        for j in range(tab.n_cols()):
            print(tab.get_value(i, j), end=' ')
        print()
