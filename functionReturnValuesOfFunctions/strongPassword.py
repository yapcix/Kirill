# def criteria(pwd):
#     """
#     2. Если в пароле содержатся только цифры или только буквы одного регистра, функция должна вернуть строку «Ненадежный пароль».
#     """
#     t = list(pwd)
#     # print(t)
#     cont = len(pwd)
#     only_numbers = '1, 2, 3, 4, 5, 6, 7, 8, 9, 0'
#     for i in t:
#         if i in only_numbers:
#             print('da')
#         else:
#             print('net')
#         if i == 'da':
#             print('cyhe')


# def password_level(password):
#     """
#     Если в пароле содержатся только цифры или только буквы одного регистра, функция должна вернуть строку «Ненадежный пароль».
#     """
#     cont = len(password)
#     only_numbers = '1, 2, 3, 4, 5, 6, 7, 8, 9, 0'
#     a1 = a2 = a3 = False
#     if cont < 6:
#         return 'Недопустимый пароль'
#     elif password.isdigit():
#         return 'Ненадежный пароль'
#     for i in password:
#         if i.isupper():
#             a1 = True
#         if i.islower():
#             a2 = True
#         if i in only_numbers:
#             a3 = True
#     if a1 * a2 * a3:
#         return 'Надежный пароль'
#     elif a1 ^ a2 and not a3:
#         return 'Ненадежный пароль'
#     else:
#         return 'Слабый пароль'


# def print_without_duplicates(messages):
#     num = 1
#     print(messages[0])
#     while num < len(messages):
#         if messages[num] != messages[num - 1]:
#             print(messages[num])
#         num += 1

# message_2 = []
#
#
# def print_only_new(message):
#     if message not in message_2:
#         print(message)
#     message_2.append(message)

# base = ["Иван", "Юлия Иванкова"]


# def hello(name):
#     print('Здравствуйте,', name + '!', 'Вашу карту ищут...')
#
#
# def search_card(name):
#     if name in base:
#         print('Ваша карта с номером', base.index(name) + 1, 'найдена')
#     else:
#         print('Ваша карта не найдена')


# lastTicket = int(input())
#
#TODO разбить на список
def lucky(ticket):
    ticket = str
    ticket_1 = ticket[0:4]
    ticket_2 = ticket[3:7]
    print(type(ticket))
    if ticket_1 == ticket_2:
        return 'vsdv'

# return_horses = []


# def do_bet(horse, bet):
#     if 0 < horse < 11 and horse not in return_horses and bet > 0:
#         return_horses.append(horse)
#         print('Ваша ставка в размере', bet, 'на лошадь', horse, 'принята')
#
#     else:
#         print("Что-то пошло не так, попробуйте еще раз")


def main():
    #     password_level('444')
    # print(password_level("Qwerty123"))
    # print_without_duplicates("Привет")
    # print_without_duplicates("Не могу до тебя дозвониться")
    # print_without_duplicates("Не могу до тебя дозвониться")
    # print_without_duplicates("Не могу до тебя дозвониться")
    # print_without_duplicates("Когда доедешь до дома")
    # print_without_duplicates("Ага, жду")
    # print_without_duplicates("Ага, жду")
    # print_only_new('Шутка номер 15')
    # print_only_new('Шутка номер 23')
    # print_only_new('Шутка номер 24')
    # print_only_new('Шутка номер 24')
    # print_only_new('Шутка номер 100')
    # print_only_new('Шутка номер 24')
    # print_only_new('Шутка номер 99')
    # print_only_new('Шутка номер 15')
    # print_only_new('Шутка номер 100')
    # print_only_new('Шутка номер 1009')
    # print_only_new('Шутка номер 10')
    # print_only_new('Шутка номер 1')
    # base = ["Иван", "Юлия Иванкова"]
    #
    # hello("Иван")
    # search_card("Иван")
    # hello("Юлия Иванова")
    # search_card("Юлия Иванова")
    print(lucky(100001))
    # do_bet(1, 10)
    # do_bet(1, 100)
    # do_bet(2, 0)
    # do_bet(2, 200)


if __name__ == '__main__':
    main()
