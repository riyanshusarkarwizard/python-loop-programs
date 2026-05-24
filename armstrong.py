#Write a Python program to check whether a 3-digit number is an Armstrong number.
#Condition::  153 = 1³ + 5³ + 3³


n=int(input("PLEASE ENTER THE NUMBER::  "))
o=n
s=0
while n>0:
    d=n%10
    s=s+d**3
    n=n//10
if o==s:
    print("IT IS AN ARMSTRONG NUMBER!!!")
else:
    print("IT IS NOT AN ARMSTRONG NUMBER!!!")
