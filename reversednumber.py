#Write a Python program to reverse a given number using a loop.
#Example
#Input: 12345
#Output: 54321


n=int(input("PLEASE ENTER THE NUMBER WHICH IS TO BE REVERSED  ::"))
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10
print("THE REVERSED NUMBER IS  ::",r)
