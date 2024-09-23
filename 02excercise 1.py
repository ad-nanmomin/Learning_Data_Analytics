"""Excercises"""

#excercise1
"""Write a program to display a person's name, age and address in
three different lines."""

print("Mohammed Adnan Momin")
print("24")
print("69/1 bassapalane tannery raod frazer town")

print("Name: Mohammed Adnan Momin \nAge: 24 \nAddress: 69/1 bassapalane tannery raod frazer town")

"""Write a program to swap two variables.
Write a program to convert a float into integer."""

a=10
b=20.60

print(a)
print(b)
print(f"a : {type(a)}")
print(f"a : {type(b)}")

c=0
c=a
a=b
b=c

print(a)
print(b)
print(f"a : {type(a)}")
print(f"a : {type(b)}")

"""
Write a program to take details from a student for ID-card and
then print it in different lines.
Write a program to take an user input as integer then convert to
float.
"""
name=input("Enter name")
age=eval(input("enter your age"))
course=input("Enter course")

print(type(name))
print(type(age))
print(type(course))

print(f"given details are\nname: {name}\nage: {age}\ncourse: {course}")

age=float(age)
print(type(name))
print(type(age))
print(type(course))