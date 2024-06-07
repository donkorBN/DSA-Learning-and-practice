#performing an index array swap and changing the position of all elements except 5

arr = [1,2,3,4,5,6,7,8,9]

l = 0 
r = len(arr) -1

while r>l:
    arr[l], arr[r] = arr[r], arr[l]
    l+=1
    r-=1

print(arr)

num = [3,5,6,7,224,4,35,1]
for i in num:
    if num[i] > num[i+1]:
        biggest = num[i]

        num[i]+=1

print(biggest)        




