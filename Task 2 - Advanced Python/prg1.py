def running_sum(lst: list):
    res = []
    for num in lst:
        if len(res) == 0:
            res.append(num)
        else:
            res.append(res[-1] + num)
    return res

arr = []
print('Give array input: ')
while True:
    try:
        n = input('Enter a number or type \'stop\' to stop giving input: ')
        if n.lower() == 'stop':
            break
        else:
            arr.append(int(n))
    except:
        print('Something is invalid!')
print(running_sum(arr))