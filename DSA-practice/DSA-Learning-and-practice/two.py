#find the mode of the array

arr = [2,4,4,3,2,4,5,4,6,5,7,6,4,6,7,5,7,4,7,6,6,7,5,5,4,6,4,4,4,6,4]

hashmap = {}

for i in arr:
    if i not in hashmap:
        hashmap[i] = hashmap.get(i,0)+ 1
    else:
        hashmap[i]+=1  

print(hashmap)
max_value = hashmap.items

mode = max(hashmap, key=hashmap.get)
print(f"The mode of the array is: {mode} ")