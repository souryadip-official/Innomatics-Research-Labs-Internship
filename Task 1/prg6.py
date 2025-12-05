def is_leap(year: int):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    else:
        leap = False
    return leap
year = int(input('Enter the year in yyyy format: '))
print(is_leap(year))