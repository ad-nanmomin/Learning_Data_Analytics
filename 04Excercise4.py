"""
A = "Why fit in, When you are Born to Stand Out!"
Write a program to find the length of the following string.
Write a program to check how many time alphabet o is occurring.
Write a program to convert the whole string into lower and upper
cases.
Write a program to convert the following string into a title.
Write a program to find the index number of "fit in".
"""
#1
a= "Why fit in, When you are Born to Stand Out!"
print(len(a))

#for the 2nd question we use the count function that returns the sum total of the occurence

#2
print(a.count("o"))

#3
print(a.lower())
print(a.upper())
print(a.capitalize())

#4
print(a.title())

#5
print(a.find("fit in"))

a=int(input("enter height"))
b=1
st=" "
while b<=a  or a>=b:
    num='*'
    print(st*(a-1)+num*b)
    a-=1
    b+=1