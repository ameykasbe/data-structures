def find_number_digits1(num):
    return len(str(num))

def find_number_digits2(num):
    length = 0
    while(num > 0):
        num //= 10
        length += 1
    return length

def find_number_digits3(num):
    

import math
def find_number_digits4(num):
    return math.floor(math.log10(num)) + 1

    



if __name__ == "__main__":
    num = 2842
    print(find_number_digits1(num))
    print(find_number_digits2(num))
    print(find_number_digits3(num))
    print(find_number_digits4(num))
