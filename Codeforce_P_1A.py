import math
n, m, a = [int(n) for n in input().split()]
n1 = n
m1 = m
a1 = a
if n1>0 and m1>0 and a1>0 and n1<=10**9 and m1<=10**9 and a1<=10**9:
    if n1%a1 == 0:
        a_l = n1//a1
    else:  
        a_l = math.ceil(n1/a1)
    if m1%a1 == 0:
        a_b = m1//a1
    else:
        a_b = math.ceil(m1/a1)
    t_a = a_l * a_b
    print(t_a)
