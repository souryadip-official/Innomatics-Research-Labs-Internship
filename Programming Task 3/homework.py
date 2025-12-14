def busyStudent(startTime: list, endTime: list, queryTime: int):
    count = 0
    for i in range(len(startTime)):
        s = startTime[i]
        e = endTime[i]
        if s <= queryTime and e >= queryTime:
            count += 1
    return count

ip1 = input('Enter startTime comma seperated: ')
startTime = [int(num.strip()) for num in ip1.split(',')]
ip2 = input('Enter endTime comma seperated: ')
endTime = [int(num.strip()) for num in ip2.split(',')]
queryTime = int(input('Enter queryTime: '))
print(busyStudent(startTime, endTime, queryTime))