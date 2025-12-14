def binary_1s(n: int):
    s = ""
    while n > 0:
        if n % 2 == 0:
            s = '0'+s
        else:
            s = '1'+s
        n //= 2

    count = 0
    for ch in s:
        if ch == '1':
            count += 1
    return count


def countBits(n: int):
    arr = []
    for i in range(0,n+1):
        arr.append(binary_1s(i))
    return arr


num = int(input("Enter a number: "))
print(countBits(num))