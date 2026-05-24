#Write a Python program to input a number and find the sum of its digits using a loop.
#Example
#Input: 5678
#Output: 26

n=int(input("PLEASE ENTER A NUMBER::   "))
s=0
while n>0:
    d=n%10
    s=s+d
    n=n//10
print("THE SUM OF THE DIGITS IS  ::",s)
