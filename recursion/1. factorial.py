def fact(n):
    # Assuming n>=0
    if n == 0:
        return 1
    return n * fact(n-1)


if __name__ == '__main__':
    print(fact(5))