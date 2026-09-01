"""
Definition: An operator is a symbol or keyword that tells Python to perform an operation on one or more values.
"""

# Arithmetic: + - * / // % **
print(5+5)
print(2-1)
print(2*2)
print(4/2)
print(4//2)
print(8%2)
print(2**5)

# Comparison: == != > < >= <=
a = 10
b = 2
print(a == b)
print(a != b )
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Logical: and or not
a = 11
b = 10
print(a == b and b > 5)
print(a == b or b > 5)
print(not(a==b))

# Assignment: = += -= *= /=
a = 5
a += a
print(a)
a -= a 
print(a)
c = 12
c *= 2
print(c)
d = 20
d /= 2
print(d)
value = 10 
value //= 2
print(value)


#Identity & membership: is, is not, in, not in
a = 5
b = 3
c = a

print(a is c)
print(a is b)
print(a is not b)

list1 = [12,23,34]
print(12 in list1)
print(10 not in list1)

# Bitwise: & | ^ ~ << >>