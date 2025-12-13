def smaller_count(nums: list):
    lst = []
    for num1 in nums:
        count = 0
        for num2 in nums:
            if num2 < num1:
                count += 1
        lst.append(count)
    return lst

ip = input('Enter a list of numbers comma seperated: ')
lst = [int(num.strip()) for num in ip.split(',')]
print(smaller_count(lst))