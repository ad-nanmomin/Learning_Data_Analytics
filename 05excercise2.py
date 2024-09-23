
"""
Write a program to check if a number is positive.
Write a program to check whether a number is odd or even.
Write a program to create area calculator.
Write a program check whether the passed letter is a vowel or
not.
Write a program to check if a number is a single digit n
digit number and so on.. , upto 5 digits.

"""

a=int(input("Enter a number to check positive or negative"))

if a<0:
    print(f"{a} is a negative number")
else:
    print(f"{a} is a positive number")

a=int(input("Enter a number to check if odd or even"))

if a%2==0:
    print(f"{a} is a even number")
else:
    print(f"{a} is a odd number")

print("Area Calculator")
inp=int(input("""Press 1 to calculate area of square
Press 2 to calculate area of rectangle"""))

if inp==1:
    s=int(input("Enter the size of the side"))
    print(s*s)
elif inp==2:
    l = int(input("Enter the length of the place"))
    b = int(input("Enter the breath of the place"))
    print(l*b)

a=['a','e','i','o','u']

st=input("Enter a string to check for vowels")
st1=[]
st1=st
if(a in st1):
    print("vowels found")
else:
    print("vowels not found")

st=input("Enter a number consisting of 1 to 5 digits")
l=len(st)
print(f"it is a {l} digit number")