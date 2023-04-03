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

    finder = MinMaxWordFinder()
    finder.add_sentence('hello')
    finder.add_sentence('abc')
    finder.add_sentence('world')
    finder.add_sentence('abc')
    finder.add_sentence('def')
    finder.add_sentence('asdf')
    finder.add_sentence('abc')
    finder.add_sentence('qwert')
    finder.add_sentence('world')
    print(' '.join(finder.shortest_words()))
    print(' '.join(finder.longest_words()))
