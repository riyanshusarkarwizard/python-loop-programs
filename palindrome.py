#Write a Python program to check whether a number is a palindrome.
#Condition: A palindrome number remains the same when reversed.

n=int(input("PLEASE ENTER THE NUMBER WHICH IS TO BE CHECKED  ::"))
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
if n==r:
    print("THE  NUMBER IS A PALINDROME NUMBER!!!")
else:
    print("THE NUMBER IS NOT A PALINDROME NUMBER!!!")
