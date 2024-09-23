#DAY 1

print("Hello world\nMy name is adnan momin Iam trying to learn \npython")

"""this is a comment you generally comment in python to describe the code there are two types of comments this one is called 
a multilines comment"""

# this is called a single line comment

# now lets try creating variables in python there are certain rules you need to keep in mind while creating variables

"""variables are used in order to store some or the other values inside a designated space"""

a= "Hello world!"
print(a)

"""
Rules for naming variables:
1. Python is case sensitive in nature
2. Variable name cannot start with a number
3. Instead of using space try to use underscore
4. Variable cannot start with a special character

"""

"""
Data types in python
1.  String str: used to store a sequence of characters
2.  Integer int: used to store variables with no decimal point 
3.  Float float: used to store floating point numbers
4.  Complex complex: 
5.  List: 
6.  Tuple:
7.  Range:
8.  Dictionary: 
9.  Set:
10. Bool:

Note: In order to indentify the types of datatype we can use the "type()" 
Will be discussed in detail in the near future
"""

"""
Accepting input from users
"""
name= input("Please enter your name ")
print(name)

#input if not specified is generally accepted as string in order to acceot a specific tyoe of input we can do the following

age=int(input(f"Enter your age {name}"))
print(age)

#here the age is accepted as an integer rather than a string as we observed before we can try this with different datatypes as well

gender=bool(input("Enter 0 if male and 1 if female"))
print(gender)

#here we accept a true or false value with 0 meaning true and 1 meaning false

num=float(input("Enter a flaoting number"))
print(num)
print(type(num))
#here we accept a decimal number

#Now incase we dont know the datatype what we can expect from the users end we can use the eval function

"""
Type casting
when a datatype is manually converted by the user it is called explicit type
when a datatype is automatically converted by the by python it is called implicit type
"""
an= eval(input("Enter anything"))
print(an)

a=210
b=23.5
#automatic conversion
ans=a+b
print(ans)
print(type(ans))

#manual conversion
b=int(b)
print(a+b)
