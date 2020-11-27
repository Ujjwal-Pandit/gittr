triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')
NS = ''
for height in range(triangle_height):    
    NS = NS + triangle_char + ' ' 
    print(NS)    