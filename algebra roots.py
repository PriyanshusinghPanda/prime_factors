"""computing the roots of the algebra for the equation aX^2+bX+c=0 and d is the integer
"""
"""
a = int(input("enter the coefficient of a"))
b = int(input("enter the coefficient of b"))
c = int(input("enter the coefficient of c"))
D =((b**2)-4*a*c)**0.5
print(D)
root1 = (-b+D)/(2*a)
root2 = (-b-D)/(2*a)
print(root1 , root2)
"""
"""
a = int(input("enter the coefficient of a"))
b = int(input("enter the coefficient of b"))
c = int(input("enter the coefficient of c"))
D =((b**2)-4*a*c)
if D
"""
"""
to find the prime factors of the number
"""
prifac={}
z = int(input("enter your number to find its prime factors"))
for i in range(2,z):
    while z%i == 0:
        z=z//i
        prifac.add(i)
