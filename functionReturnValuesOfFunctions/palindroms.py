def palindrome(s):
    s = s.lower().replace(' ', '')
    r = ''.join(reversed(list(s)))
    if s == r:
        return 'Палиндром'
    else:
        return 'Не палиндром'














def main():
    print(palindrome('А роза упала на лапу Азора'))

if __name__ == '__main__':
    main()
