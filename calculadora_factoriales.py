def calculador_factorial():
    while True:
        resultado_factorial=1
        num=(input("Ingrese un numero para aplicarle la función factorial o (s) para salir:\n"))
        if num.isnumeric():
            num=int(num)
            for i in range(num,1,-1):
                resultado_factorial*=i
            print(f"{num}! = {resultado_factorial}")
        elif num=="s":
            print("hasta pronto!")
            break
        else:
            print("Ingresa un caracter valido")
            continue
calculador_factorial()