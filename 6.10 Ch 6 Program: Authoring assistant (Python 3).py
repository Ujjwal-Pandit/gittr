def print_menu():
    print('MENU\nc - Number of non-whitespace characters\nw - Number of words\nf - Fix capitalization\nr - Replace punctuation\ns - Shorten spaces\nq - Quit\n')
    menuOp = input('Choose an option:')
    while (menuOp != 'c' and menuOp != 'w' and menuOp != 'f' and menuOp != 'r' and menuOp != 's' and menuOp != 'q'):
        menuOp = input('Choose an option:')
    return menuOp


def get_num_of_non_WS_characters(inputStr):
    whitespace = 0
    for character in inputStr:
        if(character == ' ' or character == '\t'):
            whitespace += 1
    return (len(inputStr) - whitespace)


def get_num_of_words(inputStr):
    words = inputStr.split()
    
    return len(words)


def fix_capitalization(inputStr):
    letCapped = 0
    charArray = []
    for character in inputStr:
        charArray.append(character)
   
    if(charArray[0].islower()):
        charArray[0] = inputStr[0].upper()
        letCapped += 1

   
    x = 0
    capNext = 'false'
    for character in charArray:
        if(capNext == 'true' and character != ' ' and character != '\t'):
            charArray[x] = inputStr[x].upper()
            letCapped += 1
            capNext = 'false'
        if(character == '.' or character == '!' or character == '?'):
            capNext = 'true'
        x += 1

    
    newString = ''
    for character in charArray:
        newString = newString + character

    print('Number of letters capitalized:', letCapped, end = '\n')
    print('Edited text:', newString, end='\n\n')
    return newString, letCapped


def replace_punctuation(inputStr, exclamationCount, semicolonCount):
    exclamationCount = 0
    semicolonCount = 0
    charArray = []
    for character in inputStr:
        charArray.append(character)
       
   
    x = 0
    for character in charArray:
        if(character == '!'):
            charArray[x] = '.'
            exclamationCount += 1
        elif(character == ';'):
            charArray[x] = ','
            semicolonCount += 1
        x += 1

    
    newString = ''
    for character in charArray:
        newString = newString + character

    
    print('Punctuation replaced', end = '\n')
    print('exclamationCount:', exclamationCount, end='\n')
    print('semicolonCount:', semicolonCount, end='\n')
    print('Edited text:', newString, end='\n\n')
    return newString


def shorten_space(inputStr):
    words = inputStr.split()
    newString = ''
    for word in words:
        if newString == '':
            newString = word;
        elif (newString != ''):
            newString = newString + ' ' + word
    print('Edited text:', newString, end='\n\n')
    return newString


if __name__ == '__main__':
    
    inputStr = str(input('Enter a sample text:\n'))
    print('\nYou entered:', inputStr, end='\n\n')
    command = ''
    while(command != 'q'):
        command = print_menu()
        if (command == 'c'):
            
            print('Number of non-whitespace characters:', get_num_of_non_WS_characters(inputStr), end='\n\n')
        elif (command == 'w'):
            
            print('Number of words:', get_num_of_words(inputStr), end = '\n\n')
        elif (command == 'f'):
            
            fix_capitalization(inputStr)
        elif (command == 'r'):
            
            replace_punctuation(inputStr, 0, 0)
        elif (command == 's'):
            
            shorten_space(inputStr)
        else:
            print("")
