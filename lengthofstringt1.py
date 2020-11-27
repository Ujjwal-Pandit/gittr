user_input = str(input())
count = 0
for characters in range(len(user_input)):
    x = user_input[characters]
    if x == ' ' or x == '.' or x == ',':
        count = count + 0
    else:
        count = count + 1
print(count)