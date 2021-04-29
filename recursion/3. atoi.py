def atoi(rem, num=0):
    if not rem:
        return num
    num += int(rem[0]) * pow(10, len(rem)-1)
    return atoi(rem[1:], num)


if __name__ == '__main__':
    print(atoi("11255"))
