#para un solo numero ingresado en el argumento
def clasificar_numero(num):
    if num>0:
        print("positivo")
    elif num<0:
        print("negativo")
    else:
        print("cero")
clasificar_numero(1)
#para lista de numeros
def clasificar_numeros(lista):
    for num in lista:
        if num>0:
            print(f" {num}, positivo")
        elif num<0:
            print(f" {num}, negativo")
        else:
            print(f" {num}, cero")
lista_prueba=[-1,-2-4,5,-3,6,0,7,0]
#clasificar_numeros(lista_prueba)
clasificar_numeros(lista_prueba)
