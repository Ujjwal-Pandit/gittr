arrow_base_height = int(input('Enter arrow base height:\n'))

arrow_base_width = int(input('Enter arrow base width:\n'))

arrow_head_width = int(input('Enter arrow head width:\n'))

if arrow_base_height > 0 and arrow_base_width > 0:
    while arrow_head_width <= arrow_base_width:
        arrow_head_width = int(input('Enter arrow head width:\n'))
    print('')
    for height in range(arrow_base_height):
        Ah = '*'
        Aw = ''
        for width in range(arrow_base_width):
            if width == 0:
                Aw = Ah
            else:
                Aw = Aw+Ah
        print(Aw)
    Hw = ''
    for head in range(arrow_head_width):
        Hw = Hw+'*'

        lenh = len(Hw)
        Nw = Hw    
    while Nw != '':
        Mw = ''
        for index in range(lenh):
            Mw = Mw + "*"
        if Mw != '':
            print(Mw)
        lenh = lenh -1
        Nw = Mw
        