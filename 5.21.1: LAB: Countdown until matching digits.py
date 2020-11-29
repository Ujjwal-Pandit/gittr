'''Input numbers in range 20-98'''
'''output is countdown starting from integer and stopping
when both output digits are identical.'''
"USE WHILE LOOP"

A = int(input())
while A >= 20 and A <= 98:
    F = A // 10
    L = A % 10
    while F != L:
        print(A)
        A = A - 1
        F = A // 10
        L = A % 10
    else:
        print(A)
        break
else:
    print("Input must be 20-98")
