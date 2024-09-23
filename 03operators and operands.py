"""
Operators are the operation we want to perform on certain types of varaibles
Operands are the variables on which these operations are performed
"""

"""
In python we have 7 types of operators
1. arithmetic operators
2. comparison operators
3. logical operators
4. assignment operators
5. identity operators
6. membership operators
7. bitwise operators
"""

#lets start with arithmetic operators
"""
Arithmetic operators
they are the types of operators that are used to perform the basic mathematical operations, namely:
Addition +
Subtraction -
Multiplication *
Division /
modulus %
Exponential ** 
Floor Division // Floor division is used to return the answer of 2 divided variables without a decimal point
We will work on examples for each 
"""

a=11
b=2

add=a+b
sub=a-b
mul=a*b
div=a/b
mod=a%b
exp=a**b
fd=a//b

print(f"Addition: {add}")
print(f"subtraction: {sub}")
print(f"multiplication: {mul}")
print(f"Division: {div}")
print(f"Modulus: {mod}")
print(f"Exponential: {exp}")
print(f"Floor Division: {fd}")
#here we can see the value received after performing floor division is nothing but the value with no decimal point after division

"""
Comparison operator
This type of operators are used inorder to compare variables, there are basically 6 types
Greater than >
lesser than <
Equal to ==
not equal to !=
Greater than or equal to >=
Lesser than or equal to <=
"""
a=5
b=10
c=5

print(b>a)
print(a<b)
print(a==c)
print(a!=b)
print(a>=b)
print(a<=b)

"""
Logical operators
They are used to perform logical operations that is AND OR and NOT operations 
AND: Returns 2 only when both the input values are true
OR: Returns true even if one input value if true
NOT: Returns true if the input value is false and vice versa basically follows the same concept as negation
"""

print(a>b and b>a)
print(a>b or b>a)
print(not a>b)

"""
From what I have seen logical operators are used inorder to compare to logical expreessions and return output based on the users requirements
"""

"""
Assignment operators
They are used in python for assigning values to certain variables, in general terms you would think an = sign is the obvious answer for this 
but assignment operators promote short hand typing in code 
there are a few types 
=
+=
-=
*=
/=
I think you can basically implement all of the arithematic operators am sure so lets try it out
"""

a=6
b=4
print(a)
a+=b #a+b
print(a)
a-=b #a+b
print(a)
a*=b #a+b
print(a)
a/=b #a+b
print(a)
a%=b #a+b
print(a)
a**=b #a+b
print(a)
a//=b #a+b
print(a)

#looks like I was right and we can perform all the arithematic operations with a short hand making it an assignment operator

"""
Identity Operators
They are used to compare and check if 2 given variables are the same and share the same memory address
"""
a=1
b=1
c='1'
d=a

print(a is d)
print(id(a))
print(id(d))
# here it is true because you are directly assigning d to a
print(a is b)
print(id(b))
# here it is true because both a and b have the same variable that has a constant memory address
# as you can that is the reason why a,b and d have the same ID
print(a is c)
# here it is false cause a is an integer and b is a string
print(a is not c)
# here it is true cause we are using is with not

"""
Bitwise Operators
They are used inorder to compare binary numbers there are a few types
1. AND &: Need both the values to be 1 then only returns 1 but even if one value is 0 then it is returns 0
2. OR |: Returns ) only if both are 0 else returns 1 opposite if AND
3. XOR ^: Returns 0 when having same inputs as it 0-0 or 1-1 else returns 1 in case of varying inputs
4. ZERO FILL LEFT SHIFT >>: eg is 10>>2 here the binary that is 1010 for 10 undergoes elimination from the rear end 
and 2 new zero are added in the front making it 2 that is 0010
5. ZERO FILL LEFT SHIFT <<: here no sort of elimination is performed but depending on the shift number those number of 0 are added to the bin number
"""
#Note we can use the bin functoins to find the binary value of a number

a=10
b=8
print(a & b)
print(a | b)
print(a ^ b)
print(a>>2)
print(a<<2)

"""
Membership Operators
It is used to check if a variable is a part of or a member of a multi variable datatypes, like a list consisting of 1 to 5 we check if 4 in 1 to 5
"""
a=[1,2,3,4,5]
print(3 in a)
print(8 in a)