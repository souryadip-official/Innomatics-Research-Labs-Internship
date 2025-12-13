def n_digit(num: int):
    c = 0
    while num > 0:
        c += 1
        num //= 10
    return c
def findeven(nums: list):
    c = 0
    for num in nums:
        n = n_digit(num)
        if n % 2 == 0:
            c += 1
    return c

ip = input('Enter a list of numbers comma seperated: ')
lst = [int(num.strip()) for num in ip.split(',')]
print(findeven(lst))