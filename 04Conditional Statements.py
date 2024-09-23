"""
These types of statements are used by the computer to perform operations based on conditions only when it is true
1. if
2. if-else
3. if-elif-else
4. nested if
5. shorthand if statement
"""
"""
If Statement
single conditional statement executes a certain block if the condition is satisfied that is if it is true
"""

a=10
b=5
if a>b:
    print(a-b)

"""
if-else statement
here we create a false safe for if where the condition turns out to be false what should the program do
"""

a=3
b=5
if a>b:
    print(a-b)
else:
    print(a+b)

"""
if-elif-else
here we use multiple ifs with an element of else making it multi conditional
"""

a=21
b=10
c=3
if a<b:
    print(a+b)
elif(c>a):
    print(c-a)
else:
    print(a+b+c)

"""
Nested if 
when we use an if statement inside another if statement to satisfy a nested condition
"""

if a>b:
    print(a+b)
    if a>c:
        print(a-c)
    else:
        print(a+c)

"""
short hand if statement
We basically just putting the print statement in the same line as the condition and python has an interpretor so lesser lines more speed
"""

if a>b:print(a-b)

#if you really wanna reduce lines then you can also put of else in the same line

print(a-b)if a>b else print(a+b)