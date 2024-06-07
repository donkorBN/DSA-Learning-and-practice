#find the mode of this array

num = [1,2,4,4,5,6,5,4,7,3,4,3,6,4,4,5,6,3,5,7,3,5,3]

hashmap = {}

for i in num:
    if i not in hashmap:
        hashmap[i] = hashmap.get(i,0)+ 1
    else:
        hashmap[i]+=1


print(hashmap) 
max_value = hashmap.items

mode = max(hashmap, key= hashmap.get)
print(f"Mode: {mode}")


sum=0
for i in num:
    sum +=i
    
print(f"The sum of the array is: {sum}") 

mean = format(sum/len(num), '.3f')

print(f"The mean is: {mean}")

l = 0
r = l+1

if l>r:
    biggest = l
else:
    biggest =r

    l+=1
    r-=1

print(f"The biggest number in the array is {biggest}")        