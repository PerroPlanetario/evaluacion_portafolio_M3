import os
from pathlib import Path
import json

def cargar_tarea(formulario_test):
    if os.path.exists(Path(__file__).parent/formulario_test):
        with open(Path(__file__).parent/formulario_test, 'r') as archivo:
            formulario_test = json.load(archivo)
            # print(lista_tareas)
            # print(type(lista_tareas))
            if isinstance(formulario_test, list):
                return formulario_test
    return []
def guardar_tarea(lista, nombre_archivo):
    with open(Path(__file__).parent/nombre_archivo, "w+", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)

formulario_test="formulario_test.json"
formulario=cargar_tarea(formulario_test)
while True:
    print("Formulario de datos")
    nombre=input("Ingrese su nombre o (s) para salir: \n").strip().capitalize()
    if nombre=="S" or nombre=="s" or nombre=="(S)" or nombre=="(s)":
        print("Hasta pronto")
        guardar_tarea(formulario,formulario_test)
        break
    else:
        for i in nombre:
            if i.isnumeric():
                print("el nombre no debe llevar numeros")
                continue
    edad=input("Ingresa tu edad:\n")
    if edad.isdigit():
        edad=int(edad)
    else:
        print("Edad invalida solo numeros aceptados")
    altura=input("ingresa tu altura en metros:\n")
    if "," in altura:
        altura=altura.replace(",",".")
    altura=float(altura)
    telefono=input("Ingrese su numero de celular despues del +56")
    email=input("Ingrese su correo electronico:\n")
    hijos= input("tiene hijos si o no:\n")
    if hijos=="si" or hijos=="s" or hijos=="sí":
        hijos=True
    else:
        hijos=False 
    mascota=input("tiene mascota si o no:\n")
    if mascota=="si" or mascota=="s" or mascota=="sí":
        mascota=True
    else:
        mascota=False
    formulario.append({"Nombre":nombre, "Edad":edad, "Altura":altura, "Hijos":hijos, "Mascota":mascota})

  
    
    
            
    


