print("x =", end="")
x:float = float(input())

x+=0.5

print("y=", end="")
y:float = float(input())

y-=0.7

print("z=", end="")
z:float = float(input())

eredmeny:float = (x*y)/z

print(f"({x} * {y}) / {z} = {eredmeny}")
