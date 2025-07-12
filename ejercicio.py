import os
os.system('cls')

#Esta es mi Base de Datos
cafe=[]

def cls():
    os.system('cls')

def reservar_cafe():
    print('--- Reservar café ---')
    print('-'*30)
    nombre=input('Ingrese su nombre: ')
    if not buscar_nombre(nombre):
        

