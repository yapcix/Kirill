def catalan(n):
    if n == 0:
        return 1
    else:
        n_1 = 1
        n_2 = 2
        for i in range(2, n + 1):
            n_1 *= i
            n_2 *= 2 * i * (2 * i - 1)
        n_3 = n_2 // (n_1 ** 2 * (n + 1))
        n_31 = n_2 % (n_1 ** 2 * (n + 1))
        return n_3 + n_31








def main():
    print(catalan(31))

if __name__ == '__main__':
    main()