import math

def calcular_area():
    while True:
        print("Calculadora de áreas")
        print("Opciones:")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Círculo")
        print("5. Salir")

        opcion = input("Ingrese el número de la figura (1-5): ")

        if opcion == "1":
            lado = float(input("Ingrese la longitud del lado: "))
            area = lado **2
            print(f"El área del cuadrado es: {area}")
        elif opcion == "2":
            base = float(input("Ingrese la longitud de la base: "))
            altura = float(input("Ingrese la altura: "))
            area = base * altura
            print(f"El área del rectángulo es: {area}")
        elif opcion == "3":
            tipo=input("presiona 1 si deseas saber el perimetro de un triangulo equilatero sino presiona cualquier tecla:\n")
            if tipo=="1":
                lado=float(input("longitud de un lado del triangulo: "))
                area=((3**0.5)/4)*lado
                print(f"El área del triángulo es: {area}")
            else:
                base = float(input("Ingrese la longitud de la base: "))
                altura = float(input("Ingrese la altura: "))
                area = 0.5 * base * altura
                print(f"El área del triángulo es: {area}")
        elif opcion == "4":
            radio = float(input("Ingrese el radio del círculo: "))
            area = math.pi * radio**2
            print(f"El área del círculo es: {area}")
        elif opcion == "5":
            print("Gracias por utilizar el calculador de areas")
            break
        else:
            print("Opción inválida.")
            continue

def calcular_perimetro():
    while True:
        print("Calculadora de Perimetro")
        print("Opciones:")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Círculo")
        print("5. Salir")

        opcion = input("Ingrese el número de la figura (1-5): ")

        if opcion == "1":
            lado = float(input("Ingrese la longitud del lado: "))
            perimetro = 4 * lado
            print(f"El perimetro del cuadrado es: {perimetro}")
        elif opcion == "2":
            base = float(input("Ingrese la longitud de la base: "))
            altura = float(input("Ingrese la altura: "))
            perimetro = 2 * (base+altura)
            print(f"El perimetro del rectángulo es: {perimetro}")
        elif opcion == "3":
                lado1 = float(input("Ingrese longitud del lado 1: "))
                lado2 = float(input("Ingrese longitud del lado 2: "))
                lado3 = float(input("Ingrese longitud del lado 3: "))
                perimetro = lado1 + lado2 + lado3
                print(f"El perimetro del triángulo es: {perimetro}")
        elif opcion == "4":
            radio = float(input("Ingrese el radio del círculo: "))
            perimetro = math.pi * radio**2
            print(f"El perimetro del círculo es: {perimetro}")
        elif opcion == "5":
            print("Gracias por utilizar el calculador de perimetros")
            break
        else:
            print("Opción inválida.")
            continue
while True:
    print("Bienvenido al calculador de areas y perimetros")
    print("1. Para calcular area")
    print("2. Para calcular perimetro")
    print("3. para salir")
    opcion1=input("Ingresa una opcion del menu:\n")
    match opcion1:
        case "1":
            calcular_area()
        case "2":
            calcular_perimetro()
        case "3":
            print("Hasta la proxima")
            break
        case _:
            print("Por favor ingresa una opcion valida ")
            continue

