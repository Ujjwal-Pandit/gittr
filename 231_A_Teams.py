
n = int(input())
yes = 0 # 1 <= n <= 1000
for n in range(n):
    a, b , c = [int(a) for a in input().split()]
    a1 = a
    b1 = b
    c1 = c
    
    if (a1 == 1 and b1 == 1) or (a1 == 1 and c1 == 1) or (b1 ==1 and c1 ==1):
        yes = yes + 1
    else:
        yes = yes + 0
print(yes)
        


