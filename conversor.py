print("Bienvenido al conversor")
while True:
    opcion1=(input("Seleccione (t) para temperatura o (l)para longitudes: "))
    if opcion1=="t":
        print("""Menu del conversor de temperatura
            1)Tranformar de Celsius a Fahrenheit
            2)Tranformar de Celcius a Kelvin
            3)Tranformar de Fahrenheit a Celsius
            4)Transformar de Fahrenheit a Kelvin
            5)Transformar de Kelvin a Celcius
            6)Transformar de Kelvin a Fahrenheit
            7)Salir
            """)
        while True:
            temperatura=input("ingresa la T° que quieres transformar:\n")
            if temperatura.isnumeric():
                temperatura=float(temperatura)
                transformar=int(input("ingresa una opción del 1 al 6: \n"))
                match transformar:
                    case 1:
                        print(f"{temperatura}°C ={round((temperatura*1.8)+32),2}°F")
                    case 2:
                        print(f"{temperatura}°C ={round((temperatura+273),2)}°K")
                    case 3:
                        print(f"{temperatura}°F ={round((temperatura-32)/1.8,2)}°C")
                    case 4:
                        print(f"{temperatura}°F ={round((temperatura/1.8)-32+273,2)}°K")
                    case 5:
                        print(f"{temperatura}°K ={round((temperatura-273),2)}°C")
                    case 6:
                        print(f"{temperatura}°C ={round((temperatura*1.8)-273+32,2)}°F")
                    case 7:
                        break
                    case _:
                        print("ingrese una opcion valida (1,2,3,4,5,6,7)")
            else:
                print("La temperatura ingresada debe ser un valor numerico")
    elif opcion1=="l":
        print("""Menu del conversor de longitudes
            1)Tranformar de Centímetro a Pulgada
            2)Tranformar de Centímetro a Pie
            3)Tranformar de Pulgada a Centímetro
            4)Transformar de Pulgada a Pie
            5)Transformar de Pie a Centímetro
            6)Transformar de Pie a Pulgada
            7)Salir
            """)
        while True:
            longitud=input("ingresa la longitud que quieres transformar:\n")
            if longitud.isnumeric():
                longitud=float(longitud)
                transformar=int(input("ingresa una opción del 1 al 6: \n"))
                match transformar:
                    case 1:
                        print(f"{longitud}cm ={round(longitud/2.54,2)}in")
                    case 2:
                        print(f"{longitud}cm ={round(longitud/30.48,2)}ft")
                    case 3:
                        print(f"{longitud}in ={round(longitud*2.54,2)}cm")
                    case 4:
                        print(f"{longitud}in ={round(longitud/12,2)}ft")
                    case 5:
                        print(f"{longitud}ft ={round(longitud*30.48,2)}cm")
                    case 6:
                        print(f"{longitud}ft ={round(longitud*12,2)}in")
                    case 7:
                        break
                    case _:
                        print("ingrese una opcion valida (1,2,3,4,5,6,7)")
            else:
                print("La temperatura ingresada debe ser un valor numerico")
    else:
        print("ingrese un caracter valido(t o l)")
        continue     