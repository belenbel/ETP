import os
os.system("cls")

'''
Objetivo:  Crear un programa que contenga un CRUD para
           mascotas. 
           La estructura para "mascotas" es una lista que 
           contenga diccionarios y en estos las siguiente
           claves:  chip, nombre, raza, edad
           Chip (1000 - 9999)es el campo clave (PK, primary key), por
           lo tanto la búsqueda, eliminación y modificación
           es buscando por el chip.
           Como es PK este NO DEBE ESTAR REPETIDO (validar 
           en el ingreso).

           1. agregar
           2. buscar
           3. eliminar
           4. modificar
           5. listar
           6. salir

           Otros requerimientos:
           1.- El menú debe estar en una función
           2.- En el programa principal debe estar el Match
               y sus case. Los codigos de los case debe ser
               una función para cada case.
           3.- Debe tener una función para los ingresos numéricos
               y validar el rango.
'''
#Área de funciones

def cls():
    #requiere importar os
    os.system("cls")

def buscar():
    print("Buscar por Chip")
    print("----------------\n")

    chip = input_num("Ingrese chip: ",1000,9999)
    for datos in mascotas:
        if datos["chip"] == chip:
            print("Datos encontrados:")
            print(f"{datos["chip"]}  {datos["nombre"]} {datos["raza"]} {datos["edad"]}") 
            return
    print("Error, chip no existe...")        

def buscar_chip(id):
    for datos in mascotas:
        if datos["chip"] == id:
            return True
    return False

def agregar():
    print("Agregar Mascota")
    print("----------------\n")
    nuevo_dicc={}
    chip = input_num("Ingrese chip: ",1000,9999)
    if not buscar_chip(chip):
        nombre=input("nombre: ")
        raza  =input("raza: ")
        edad  =input_num("edad: ",1,18)

        nuevo_dicc["chip"]=chip
        nuevo_dicc["nombre"]=nombre
        nuevo_dicc["raza"]=raza
        nuevo_dicc["edad"]=edad

        mascotas.append(nuevo_dicc)
        print("Listo! datos agregados")
    else:
        print("Error, el chip ya existe...")

def modificar():
    print("Modificar Datos")
    print("------------------\n")
    chip = input_num("Ingrese chip: ",1000,9999)
    sw=0 #no existe el rut
    for i in range(len(mascotas)):
        if mascotas[i]["chip"] == chip:
            print("El Chip existe, los datos son: ")
            print(f" {mascotas[i]["chip"]}  {mascotas[i]["nombre"]}  "+ 
                    f"{mascotas[i]["raza"]}  {mascotas[i]["edad"]}")
            sw=1 
            nuevo_nombre=input("Ingrese el nuevo nombre: ")
            nueva_raza  = input("Ingrese nueva raza: ") 
            nueva_edad  = input_num("Ingrese nueva edad:  ",1,18)            
            mascotas[i]["nombre"] = nuevo_nombre
            mascotas[i]["raza"]   = nueva_raza
            mascotas[i]["edad"]   = nueva_edad
            print("Listo! datos modificados")
            return
    if sw==0: 
        print("Error, el rut no existe")      


def eliminar():
    print("Eliminar Mascotas por Chip")
    print("--------------------------\n")
    chip = input_num("Ingrese chip: ",1000,9999)

   
    for i in range(len(mascotas)):
        if mascotas[i]["chip"] == chip:
            print("El Chip existe, los datos son: ")
            print(f" {mascotas[i]["chip"]}  {mascotas[i]["nombre"]}  "+ 
                    f"{mascotas[i]["raza"]}  {mascotas[i]["edad"]}")             
            mascotas.pop(i)
            print("Listo!, datos eliminados")
            return
    print("Error, el chip no existe")     


def input_num(pregunta,li,ls):
    while True:
        try:
            n=int(input(pregunta))
            if n>=li and n<=ls:
                return n
            else:
                print(f"Error, debe ingresar un número entre {li} y {ls}")
        except:
            print("Error, debe ingresar sólo números.")

def menu():
    print('''
        Menú CRUD de Mascotas
        ----------------------
                  
            1. agregar
            2. buscar
            3. eliminar
            4. modificar
            5. listar
            6. salir
          
          ''')
    
    op=input_num("Ingrese una opción entre 1 y 6: ",1,6)
    return op

def listar():
    print("    Listar Mascotas   ")
    print("-----------------------\n")

    for datos in mascotas:
        print(f"{datos["chip"]}  {datos["nombre"]} {datos["raza"]} {datos["edad"]}")   
    
#defino variables
mascotas=[
            {"chip":1000,"nombre":"perrin","raza":"quiltro","edad":2},
            #                          0
            {"chip":1001,"nombre":"cachupin","raza":"quiltro","edad":1},
            #                          1
        ]

while True:
    cls()
    opcion=menu() #menú debe usar el input_num2(...)
    cls()
    match opcion:
        case 1: agregar()
        case 2: buscar()
        case 3: eliminar()
        case 4: modificar()
        case 5: listar()
        case 6: break
        case _: print("Error.....")

    os.system("pause")


