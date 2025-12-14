def numTeams(rating: list):
    count = 0
    for i in range(len(rating)):
        for j in range(i+1, len(rating)):
            for k in range(j+1, len(rating)):
                if ((rating[i] < rating[j] and rating[j] < rating[k]) or (rating[i] > rating[j] and rating[j] > rating[k])):
                    count += 1
    return count


ip = input('Enter a list of rating comma seperated: ')
lst = [int(num.strip()) for num in ip.split(',')]
print(numTeams(lst))