s = input("Enter a string: ") 
rev = s[::-1] 
vowels = "aeiouAEIOU" 
count = sum(1 for char in s if char in vowels)
print("Reversed String:", rev)
print("Number of Vowels:", count)
