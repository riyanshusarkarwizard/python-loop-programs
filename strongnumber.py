#Write a Python program to check whether a number is a Strong Number.
#Condition:  145 = 1! + 4! + 5!


n= int(input("Enter a number: "))
o=n
s= 0
while n>0:
    d=n% 10
    f=1
    for i in range(1, d + 1):
        f=f * i
        s=s+f
    n = n // 10
if o == s:
    print("Strong Number")
else:
    print("Not a Strong Number")
