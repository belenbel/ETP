import os
os.system("cls")

#área de funciones

def saludo():
    print("Hola, bienvenidos")

def sumar(a,b):  #parámetros (variables)
    suma=a+b     #suma es una variable LOCAL
                 #existe solo en la función.
    return suma

def mayor(a, b):
    if a == b:
        return -1 #error valores iguales
    elif a > b:
        return a
    else:
        return b

def mayor2(a, b):
    mayor=0   #variable local
    if a == b:
        mayor=-1 #error valores iguales
    elif a > b:
        mayor=a
    else:
        mayor=b
    return mayor

def saludo2(nombre,genero):
    if genero == "f":
        return "Bienvenida "+nombre
    elif genero =="m":
        return "Bienvenido "+nombre
    else:
        return "Error, género no existe"


def dia_semana(dia):
    texto=""
    if dia >= 1 and dia <=7:
        match dia:
            case 1: texto="lunes" 
            case 2: texto="martes"
            case 3: texto="miércoles"
            case 4: texto="jueves"
            case 5: texto="viernes"
            case 6: texto="sábado"
            case 7: texto="domingo"
        return texto   
    else:
        return -1
         
#fin área de funciones

#inicializar variables

#Área de código principal

saludo()

s= sumar(20,15)
print("la suma es ", s)

print("La suma es ", sumar(4,3))

m = mayor(4,1)
if m != -1:
    print("el mayor es ", m)
else:
    print("Error, los números son iguales")


m = mayor2(4,4)
if m != -1:
    print("el mayor es ", m)
else:
    print("Error, los números son iguales")


#Ejercicio:  Ingresar en una función el nombre y
#            genero y que esta retore Bienvenido o 
#            bienvenida mas el nombre.
#            saludo2("susana","f")

nombre=input("Ingres su nombre: ")
genero=input("Ingres género m/f: ").lower()

texto=saludo2(nombre,genero)

print(texto)


#Crear una función que reciba un número entre 1 y 7 
#(debe validar el rango, si no cumple retorna -1) y 
#retorne el día de la semana correspondiente.


print("El día es ", dia_semana(9))


#Tarea:  Crear la función input_num()
#        Lam función permite el ingreso de
#        un número y lo retorna. En caso
#        de ingresar Enter o una letra debe
#        acusar el error y volver a solicitar
#        el número.


print("Fin del programa")







'''
a=10
b=5

suma = a + b
print("La suma es ", suma)

x = 20
y = 8
suma= x + y
print("La suma es ", suma)
'''