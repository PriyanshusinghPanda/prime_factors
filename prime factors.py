z = int(input("enter your number to find its prime factors"))
for i in range(2,z):
    while z%i == 0:
        z=z//i
        print(i)
