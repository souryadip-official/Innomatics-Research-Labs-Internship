def extra_candies_func(candies: list, extra_candies: int):
    output = []
    m = max(candies)
    for num in candies:
        output.append(num + extra_candies >= m)
    return output

arr = []
n = int(input('Enter n: '))
for i in range(n):
    arr.append(int(input(f'Enter value at index {i+1}: ')))
    
xtra = int(input('Enter number of extra candies: '))

print('Result:', extra_candies_func(arr, xtra))