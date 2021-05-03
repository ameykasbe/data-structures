
def TowerOfHanoi(n, from_, aux_, to_):

    if n == 1:
        print(f"Move disk 1 from {from_} to {to_}")
        return
    TowerOfHanoi(n-1, from_, to_, aux_)
    print(f"Move disk {n} From {from_} to {to_}")
    TowerOfHanoi(n-1, aux_, from_, to_)


n = 4
TowerOfHanoi(n, 'A', 'B', 'C')
