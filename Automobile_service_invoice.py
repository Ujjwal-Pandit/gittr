print('''Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12''')
menu = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 'No service'
    }
print()
fs = str(input('Select first service:\n'))
ss = str(input('Select second service:\n'))
print()
if ss and fs in menu:
    print('Davy\'s auto shop invoice')
    print()
    p1 = '$'+str(menu[fs])
    p2 = '$'+str(menu[ss])
    if ss == '-':
        print('Service 1:', fs+',', p1)
        print('Service 2:', menu['-'])
        print()
        print('Total:', p1)
    elif fs == '-':
        print('Service 1:', menu['-'])
        print('Service 2:', ss+',', p2)
        print()
        print('Total:', p2)
    else:
        print('Service 1:', fs+',', p1)
        print('Service 2:', ss+',', p2)
        print()
        print('Total:', '$'+str(menu[fs]+menu[ss]))
