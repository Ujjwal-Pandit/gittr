
a = int(input())
b = int(input())
c = int(input())


d = int(input())
e = int(input())
f = int(input())


solution = 0
for x in range(-10, 10):
    for y in range(-10, 10):
        E1LHS = a*x + b*y
        E2LHS = d*x + e*y
        if E1LHS == c and E2LHS == f:
            solution = 1
            print(x,y)
            break
        else:
            continue
if solution == 0:
    print("No solution")
