def shuffle(lst: list):
    mid = len(lst) // 2
    first = lst[0:mid]
    last = lst[mid:len(lst)]
    count = 0
    output = []
    while count < len(first):
        output.append(first[count])
        output.append(last[count])
        count += 1
    return output

arr = []
n = int(input('Enter n: '))
i = 1
print('Now enter 2n inputs:')
while i <= 2*n:
    arr.append(int(input(f'Enter number {i}: ')))
    i += 1

print('Shuffled array:', shuffle(arr))