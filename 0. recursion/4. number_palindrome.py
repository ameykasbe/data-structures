## String implementation
# def is_pal(num):
#     if not num:
#         return True
#     return (str(num)[0] == str(num)[-1]) and is_pal(str(num)[1:-1])

## OLD
# def is_pal(num, dup_num):

#     if num//10 == 0:
#         return num == dup_num[0] % 10

#     if not is_pal(num // 10, dup_num):
#         return False

#     dup_num[0] = dup_num[0] // 10

#     return dup_num[0] % 10 == num % 10


def pal(num, dup_num):

    if num // 10 == 0:
        return num == dup_num[0]%10

    if pal(num//10, dup_num):
        dup_num[0] = dup_num[0] // 10
        return num%10 == dup_num[0] % 10
    return False

def is_pal(num):
    dup_num = [num]
    return pal(num, dup_num)


if __name__ == "__main__":
    num = 12321
    print(is_pal(num))

    num = 123321
    print(is_pal(num))

    num = 123214
    print(is_pal(num))
