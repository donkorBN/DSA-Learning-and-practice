count = 0;

vowels= ['a','e','i','o','u']

word = input("Enter any word: ")

for char in word:
    if char.lower() in vowels:
        count +=1

print(count)