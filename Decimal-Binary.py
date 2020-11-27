x = int(input())
a = ''
if x>0:
    while x>0:
        y = str(x % 2)
        x = x // 2
        a = a + y
    reversedstring = ''.join(reversed(a))
    print(reversedstring)
    
    
    

    
        
        