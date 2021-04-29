# https: // www.geeksforgeeks.org/check-if-a-number-is-palindrome/


def is_pal(num, dup_num):

    if num//10 == 0:
        return num == dup_num[0] % 10

    if not is_pal(num // 10, dup_num):
        return False

    dup_num[0] = dup_num[0] // 10

    return dup_num[0] % 10 == num % 10


def pal(num):
    dup_num = [num]
    return is_pal(num, dup_num)


if __name__ == "__main__":
    num = 12321
    print(pal(num))
