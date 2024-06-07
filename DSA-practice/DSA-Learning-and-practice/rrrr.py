

random = [2,7,9,5,3,9,0,3,7,3,98,2,9,12,24,6,54]

for _ in range(len(random)):
    for i in range(len(random)-1):
        if random[i] < random[i+1]:
            random[i], random[i+1] = random[i+1], random[i]
            
print(random)            