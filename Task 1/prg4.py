a = int(input('Enter a number: '))
odd = a % 2 != 0
if odd:
    print("Weird")
else:
    if 2 <= a <= 5 or a > 20:
        print("Not Weird")
    else:
        print("Weird")