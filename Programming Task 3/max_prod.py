def max_prod(nums: list):
    nums.sort()
    return (nums[-1]-1) * (nums[-2]-1)

ip = input('Enter a list of numbers comma seperated: ')
lst = [int(num.strip()) for num in ip.split(',')]
print(max_prod(lst))