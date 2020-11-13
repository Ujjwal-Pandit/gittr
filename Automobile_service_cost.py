service = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7
    }
des_ser = str(input("Enter desired auto service:\n"))
print("You entered:", des_ser)
if des_ser not in service:
    print("Error: Requested service is not recognized")
else:
    print("Cost of", des_ser.lower()+":", "$"+str(service[des_ser]))
