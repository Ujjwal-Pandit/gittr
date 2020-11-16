

n=int(input())
if n <= 100:
    a=1
    while a <=n:
        word = str(input())
        lth = len(word)
        if lth>=1 and lth<=10:
            print(word)
        
        
        elif lth>10 and lth<=100:
            f_char = word[0]
            l_char = word[-1]
            mid_len = str(lth-2)
            print(f_char+mid_len+l_char)
        
        a = a+1
    


    
    