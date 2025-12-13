def xor_find(n: int, start: int):
    arr = []
    for i in range(0,n):
        arr.append(start + 2 * i)
    
    xor = arr[0]
    for i in range(1,n):
        xor = xor ^ arr[i]
    return xor

n = int(input('Enter n: '))
start = int(input('Enter start: '))
print(xor_find(n, start))