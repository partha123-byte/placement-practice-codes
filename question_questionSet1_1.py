tank=float(input("enter the numbers of liters to fill the tank"))
if(tank<0):
    print(tank,"is an invalid input")
else:
    dis=float(input("enter the distance covered"))
    if(dis<0):
        print(dis,"is invalid input")

    else:
        print("Liters/100KM",(tank/dis*100))
        a=tank*0.2642
        b=dis*0.6214
        print("Miles/GALLON",b/a)


