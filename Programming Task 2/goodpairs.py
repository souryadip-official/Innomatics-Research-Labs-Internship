def good_pair(lst: list):
    c = 0
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j] and i < j:
                c += 1
    return c

ip = input('Enter a list of numbers comma seperated: ')
lst = [int(num.strip()) for num in ip.split(',')]
print(good_pair(lst))