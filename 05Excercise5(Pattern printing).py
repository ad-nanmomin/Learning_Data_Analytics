"""
1
12
123
1234
12345
Write a program to display this pattern.
"""

for a in range(1,6):
    for b in range(1,a+1):
        print(b, end=" ")
    print()

"""
Write a program to display this pattern.
1
22
333
4444
55555
"""

for a in range(1,6):
    for b in range(1,a+1):
        print(a, end=" ")
    print()

"""
Write a program to display this pattern.
11111
2222
333
44
5
"""

for a in range(1,6):
    for b in range(6,a,-1):
        print(a, end=" ")
    print()

"""
Write a program to display this pattern.
        *
       **
      ***
     ****
    *****
"""
i='*'
for a in range(1,6):
    for b in range(5,a,-1):
        print(' ', end="")
    for c in range(a):
        print('x', end="")
    print('h')

"""
1
21
321
4321
54321
Write a program to display this pattern.
"""

for a in range(1,6):
    for b in range(a,0,-1):
        print(b, end="")
    print()
"""
Write a program to display this star mountain pattern.
"""
a=5
j=1
for i in range(1,(a+a)):
    if i <=5:
        for x in range(1,i+1):
            print('x', end="")
        print()
    elif i>5:
        for z in range(5,j,-1):
            print('x', end="")
        j+=1
        print()

"""
1
3 6 9
4 8 12 16
5 10 15 20 25
6 12 18 24 30 36
7 14 21 28 35 42 49
8 16 24 32 40 48 56 64
Write a program to display the following pattern.
"""
for a in range(1,11):
    for b in range(1, a+1):
        print(f"{b*a}", end=" ")
    print()

