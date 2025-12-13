def podg(n: int):
    prod = 1
    while n > 0:
        prod *= (n % 10)
        n //= 10
    return prod
        
def sodg(n: int):
    sum = 0
    while n > 0:
        sum += (n % 10)
        n //= 10
    return sum
   
def podgsodg(n: int):
    return podg(n) - sodg(n)

ip = int(input('Enter a number: '))
print(podgsodg(ip))