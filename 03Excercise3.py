"""
Write a program to find a sum of all the even numbers up to 50.
Write a program to write first 20 numbers and their squared
numbers.
Write a program to find sum of first 10 odd numbers using while
loop.
Write a program to check if a number is divisible by 8 and
12 upto 100 numbers
Write a program to create a billing system at a supermarket
"""
from time import sleep

#1
# sum=0
# for i in range(1,51):
#     if i%2==0:sum+=i
#     else:continue
# print(sum)
#
# #2
# for i in range(1,21):
#     print(f"{i}X{i}={i*i}")
#
# #3
# a=1
# i=1
# sum=0
# b=int(input("Enter the number of odd number sum"))
# while i!=b+1:
#     if a%2!=0:
#         sum+=a
#         a+=1
#         i+=1
#     else:
#         a=a+1
# print(sum)
#
# # an interesting way of doing this is
# a=int(input("Enter the number of odd number sum"))
# print(a*a)
#
# #4
# for i in range(1,101):
#     if i%8==0 and i%12==0:
#         print(f"{i} is divisible by 8 and 12")
#     else:
#         print(f"{i} is not divisible by 8 and 12")


#5

# while True:
#     total = 0
#     name=input("Enter customer name")
#     while True:
#         quant=int(input("Enter Item quantity"))
#         price=int(input("Enter Item price"))
#         total+=quant*price
#         ans=input("Enter y or n to repeat or quit")
#         if ans=='n':break
#         else:continue
#     print(total)
#     print(name)
#     sleep(4)
#     asn1=input("Quit system? y or n")
#     if asn1=='y': break
#     else: continue
b=0
x=1
a=int(input("enter pyramid height"))
z=a
for i in range(1,a+1):
    st='*'
    z=z-1
    print(' '*(a-b)+st*x+' '*(a-b))
    b=b+1
    x=x+2