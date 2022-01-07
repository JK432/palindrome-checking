# Write a program to check if a given string is a palindrome or not, without reversing the original string 
x=input()
y=""
for i in x:
    y=i.lower()+y
if y==x.lower():
    print("Palindrome")
else:
    print("Not a palindrome")
