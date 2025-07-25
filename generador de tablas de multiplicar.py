def generador_tablas_multi():
    while True:
        a=(input("Ingresa un numero que sera el multiplicando o (s)para salir:\n"))
        if a.isnumeric():
            a=int(a)
            b=int(input("Ingresa hasta que numero llegara el multiplicador:\n"))
            for i in range(1,b+1):
                print(f"{a}x{i}={a*i}")
        elif a=="s":
            print("Gracias por utilizar el generador de tablas. vuelve pronto")
            break
generador_tablas_multi()