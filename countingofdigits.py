#Write a Python program to count how many times a given digit occurs in a number.

n=int(input("PLEASE ENTER THE NUMBER  ::"))
d=int(input("PLEASE ENTER THE DIGIT TO BE COUNTED  ::"))
c=0
while n>0:
    d1=n%10
    if d1==d:
        c=c+1
    n=n//10
print("DIGIT FOUND" ,c, "TIMES")
