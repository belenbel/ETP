import os
os.system("cls")

'''
Objetivo:  Crear un CRUD para un estacionamiento
           de autos.
           Los campos son: 
           patente (pk), marca, color

           
           La búsqueda, eliminación y modificación
           es buscando por la patente.
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


#funciones

#Área de funciones

def cls():
    #requiere importar os
    os.system("cls")

def buscar():
    print("Buscar por Patente")
    print("----------------\n")

    patente = input("Ingrese patente: ")
    for datos in estacionamientos:
        if datos["patente"] == patente:
            print("Datos encontrados:")
            print(f"{datos["patente"]} {datos["marca"]} {datos["color"]}") 
            return
    print("Error, patente no existe...")        

def buscar_patente(id):
    for datos in estacionamientos:
        if datos["patente"] == id:
            return True
    return False

def agregar():
    print("Agregar Auto")
    print("----------------\n")
    nuevo_dicc={}
    patente = input("Ingrese patente: ")
    if not buscar_patente(patente):
        marca=input("marca: ")
        color  =input("color: ")
       
        nuevo_dicc["patente"]=patente
        nuevo_dicc["marca"]=marca
        nuevo_dicc["color"]=color      

        estacionamientos.append(nuevo_dicc)
        print("Listo! datos agregados")
    else:
        print("Error, la patente ya existe...")

def modificar():
    print("Modificar Datos")
    print("------------------\n")
    patente = input("Ingrese patente: ")
    sw=0 #no existe la patente
    for i in range(len(estacionamientos)):
        if estacionamientos[i]["patente"] == patente:
            print("La patente existe, los datos son: ")
            print(f" {estacionamientos[i]["patente"]}  {estacionamientos[i]["marca"]}  "+ 
                    f"{estacionamientos[i]["color"]} ")
            sw=1 
            nueva_marca=input("Ingrese la nueva marca: ")
            nuevo_color  = input("Ingrese nuevo color: ") 
                       
            estacionamientos[i]["marca"] = nueva_marca
            estacionamientos[i]["color"]   = nuevo_color
           
            print("Listo! datos modificados")
            return
    if sw==0: 
        print("Error, la patente no existe")      


def eliminar():
    print("Eliminar Autos por Patente")
    print("--------------------------\n")
    patente = input("Ingrese patente: ")

   
    for i in range(len(estacionamientos)):
        if estacionamientos[i]["patente"] == patente:
            print("La patente existe, los datos son: ")
            print(f" {estacionamientos[i]["patente"]}  {estacionamientos[i]["marca"]}  "+ 
                f"{estacionamientos[i]["color"]} ")             
            estacionamientos.pop(i)
            print("Listo!, datos eliminados")
            return
    print("Error, la patente no existe")     


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
    print("    Listar Autos   ")
    print("-----------------------\n")

    for datos in estacionamientos:
        print(f"{datos["patente"]}  {datos["marca"]} {datos["color"]}")   
    

estacionamientos=[ # patente (pk), marca, color
                    {"patente":"aa0011","marca":"subaru","color":"negro"},
                    {"patente":"bb0022","marca":"fiat","color":"rojo"},
    
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

