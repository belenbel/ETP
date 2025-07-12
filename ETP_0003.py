import os
os.system("cls")

'''
Objetivo:   Duoc ofrece café gratis a los 20 primeros registrados. Los 
           campos del registros de cafés son:
           nombre, sección, cantidad_de_cafes,is_vip (bool)

           Las opciones del menú son:

           1. Reservar café
           2. Buscar café reservado
           3. Cancelar reserva de café
           4. Salir

           1.- Al reservar debe solicitar el nombre y la sección, por defecto
              cantidad_de_cafes es 1 y is_vip es False. Recuerde controlar
              la cantidad de café, son solo 20.
           2.- Se buscar por el nombre (nombre y apellido), si existe se debe 
           ofrece si desea pagar $500 (valor real $1950) y reservar un 2do café
           y pasar a ser cliente VIP.  Si responde "si" entonces cantidad_de_cafe =2
           e is_vip=True.

           3.- Busca por nombre y si existe lo elimina y se recuperan los cafés
               disponibles.

            Pregunta:  ¿Qué pasa si queda 1 café disponible y acepto ser VIP?  
                       ¿y si quedan cero cafés? 

'''


#Área de funciones

def cls():
    #requiere importar os
    os.system("cls")

def buscar():
    print("Buscar por Nombre")
    print("----------------\n")

    nombre = input("Ingrese nombre: ").upper()
    for diccionario in cafes:
        if diccionario["nombre"] == nombre:
            print("Datos encontrados:")
            print(f"{diccionario["nombre"]} {diccionario["seccion"]}"
                  f"{diccionario["cantidad_de_cafes"]}  {diccionario["is_vip"]} ")
            respuesta=input("Desea un segundo café por $500  si/no: ").lower()
            if respuesta == "si":
                diccionario["cantidad_de_cafes"]=2
                diccionario["is_vip"]=True
                global contador
                contador+=1
                print("Listo!  se ha agregado un 2do café y ahora usted es VIP")
                return 
            else:
                print("Ok, no hay problema")    
                return
             
    print("Error, nombre no existe...")  
        

def buscar_nombre(pk):
    for diccionario in cafes:
        if diccionario["nombre"] == pk:
            return True
    return False

def reservar():
    print("Reservar Café")
    print("----------------\n")
    nuevo_dicc={}
    nombre = input("Ingrese su nombre: ").upper()
    if not buscar_nombre(nombre):
        seccion=input("sección: ")    
       
        nuevo_dicc["nombre"]=nombre
        nuevo_dicc["seccion"]=seccion
        nuevo_dicc["cantidad_de_cafes"]=1
        nuevo_dicc["is_vip"]=False    

        cafes.append(nuevo_dicc)
        global contador
        contador+=1

        print("Listo! datos agregados")
    else:
        print("Error, el nombre ya existe...")

   


def eliminar():
    print("Eliminar Autos por Patente")
    print("--------------------------\n")
    nombre = input("Ingrese nombre: ").upper()
   
    for i in range(len(cafes)):
        if cafes[i]["nombre"] == nombre:
            print("El nombre existe, los datos son: ")
            print(f"{cafes[i]["nombre"]} {cafes[i]["seccion"]} "
                  f"{cafes[i]["cantidad_de_cafes"]}  {cafes[i]["is_vip"]}")           
           
            global contador
            contador-= cafes[i]["cantidad_de_cafes"]

            cafes.pop(i)
            print("Listo!, datos eliminados")
            return
    print("Error, el nombre no existe")     


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
        Menú CRUD de Café Gratiss
        -------------------------
                  
           1. Reservar café
           2. Buscar café reservado
           3. Cancelar reserva de café
           4. Salir
          
          ''')
    
    op=input_num("Ingrese una opción entre 1 y 6: ",1,4)
    return op


    

#Área de programa

contador=1
cafes = [
           {"nombre":"Susana Correa","seccion":"FPY1101-007D","cantidad_de_cafes":1,"is_vip":False },

       ]


ciclo=True

while ciclo:
    cls()
    print("contador=",contador)
    print(cafes)
    opcion=menu() #menú debe usar el input_num2(...)
    cls()
    match opcion:
         case 1: 
            if contador<20:
               reservar()
              
            else:
               print("Error, no hay mas cafés")

         case 2:
            if contador<20: 
               buscar()
             
            else:
               print("Error, no hay mas cafés")

         case 3: eliminar()
         case 4: 
            ciclo=False
         case _: print("Error.....")

    os.system("pause")




     
    