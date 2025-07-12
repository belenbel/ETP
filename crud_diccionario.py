import os
os.system("cls")


alumnos=[
          {"rut":"1-1","nombre":"Susana","edad":17},
        #                   0                  
          {"rut":"2-2","nombre":"Juan","edad":19},
        #                   1  
          {"rut":"3-3","nombre":"David","edad":22}
        #                   2  
        ]

while True:
    os.system("cls")
    print("*** MENU PRINCIPAL ***\n")
   
    print("1. Agregar")
    print("2. Buscar por rut")
    print("3. Eliminar por rut.")
    print("4. Modificar")
    print("5. Listar.")
    print("6. Salir.")

    while True:
        try:
            opcion = int(input("Elija opción 1-6: "))
            break
        except:
            print("Error, debe ingresar un número entre 1 y 6")

    os.system("cls")
    match opcion:
        case 1:
            print("Agregar Alumnos")
            print("-----------------\n")
            nuevo_dicc={}
            rut=input("Rut: ")
            nombre=input("Nombre: ")
            edad=int(input("Edad: "))
            
            nuevo_dicc["rut"]=rut
            nuevo_dicc["nombre"]=nombre
            nuevo_dicc["edad"]=edad
            alumnos.append(nuevo_dicc)
            print("Listo! datos agregados")
         
        case 2:
            print("Buscar Alumnos por Rut")
            print("----------------------\n")
            rut=input("Ingres Rut a buscar: ")

            sw=0 #no existe el rut
            for i in range(len(alumnos)):
                if alumnos[i]["rut"] == rut:
                    print("El Rut existe, los datos son: ")
                    print(f" {alumnos[i]["rut"]}  {alumnos[i]["nombre"]}  {alumnos[i]["edad"]}")  
                    sw=1 
                    break
            if sw==0: 
                print("Error, el rut no existe")            
            
        case 3:
            print("Eliminar Alumnos por Rut")
            print("------------------------\n")
            rut=input("Ingres Rut a buscar: ")

            sw=0 #no existe el rut
            for i in range(len(alumnos)):
                if alumnos[i]["rut"] == rut:
                    print("El Rut existe, los datos son: ")
                    print(f" {alumnos[i]["rut"]}  {alumnos[i]["nombre"]}  {alumnos[i]["edad"]}")  
                    sw=1 
                    alumnos.pop(i)
                    print("Listo!, datos eliminados")
                    break
            if sw==0: 
                print("Error, el rut no existe")     
          
        case 4:
            print("Modificar Datos")
            print("------------------\n")
            rut=input("Ingres Rut a buscar: ")

            sw=0 #no existe el rut
            for i in range(len(alumnos)):
                if alumnos[i]["rut"] == rut:
                    print("El Rut existe, los datos son: ")
                    print(f" {alumnos[i]["rut"]}  {alumnos[i]["nombre"]}  {alumnos[i]["edad"]}")  
                    sw=1 
                    nuevo_nombre=input("Ingres el nuevo nombre: ")
                    nueva_edad= int(input("Ingrese nueva edad:  "))
                    
                    alumnos[i]["nombre"] = nuevo_nombre
                    alumnos[i]["edad"]   = nueva_edad
                    print("Listo! datos modificados")
                    break
            if sw==0: 
                print("Error, el rut no existe")   
          
        case 5:
            print("Listar Productos")
            print("----------------------------\n")       
            
            for i in range(len(alumnos)):
                print(f" {alumnos[i]["rut"]}  {alumnos[i]["nombre"]}  {alumnos[i]["edad"]}")      
          

        case 6:
            print("Fin del programa. Adiós.")
            break

        case _:
            print("Debe ingresar una opción valida.")

    os.system("pause")
    