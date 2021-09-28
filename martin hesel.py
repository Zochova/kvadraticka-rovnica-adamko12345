import math

a=int(input("zadaj hodnotu a: "))
b=int(input("zadaj hodnotu b: "))
c=int(input("zadaj hodnotu c: "))

d=(b*b)-(4*a*c)
if d > 0:
    d = math.sqrt(d)
    x1 = (-b + d)/(2*a)
    x2 = (-b - d)/(2*a)
    print("Korene kvadratickej funkcie: ", int)
