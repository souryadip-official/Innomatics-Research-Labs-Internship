import sys
a = int(input('Enter a number: '))
if a < 0:
    sys.exit(1)
else:
    count = 0
    while count < a:
        print(count ** 2)
        count += 1