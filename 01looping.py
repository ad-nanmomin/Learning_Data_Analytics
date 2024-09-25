"""
 the whole purpose of looping is to perform certain block of code in a iteration until the given statement is true
 we have 4 types
 1. for loop
 2. while loop
 3. while true
 4. nested loops
"""

"""
 for loop
 it repeats a certain block of code for fixed number of iterations
"""
for a in range(0,5):
    print(a+1)

#we can also perform gapping

for i in range(0,5,2):
    print("Hi there")

#for writing the table for the first 10 numbers using nested for looping

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print()

"""
While condition 
it is used when we want to perform a a certain block of code for an indefinite 
number of times until the condition is true
"""

n=1
while n<=5:
    print(n)
    n+=1

#printing tables using while

a=1
b=1
while a<=10:
    while b<=10:
        print(f"{a}X{b}={a*b}")
        b+=1
        print()
    b=1
    a+=1

"""
While True 
this loop is similar to while(1) where,
a certain block of code is in an infinite loop until a break statement is encountered
"""
a=5
while True:

    if a==0:
        break
    else:
        print(a)
        a = a - 1

"""
Nested loop
when a loop exist inside another loop it is nested we will work with this
"""

#lets print 1 to 10 tables with for and while

a=1

while a<=10:
    for b in range(1,11):
        print(f"{a}X{b}={a*b}")
    a+=1

#making a hill of numbers
inp=int(input("Enter pyramid size"))
ite=inp+(inp-1)
a=1
n=1
for a in range(1,ite+1):
    if a<=inp:
        for b in range(1, a + 1):
            print(b, end="")
        print()
    else:

        for b in range(1, a - n):
            print(b, end="")
        print()
        n=n+2

