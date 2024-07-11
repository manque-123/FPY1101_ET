import os
import time
import csv
from random import *

lista=[]
acceso=1
listatrabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
listasueldo=[]


def limpiar():
    os.system('cls')

def menuprincipal():
    limpiar()
    print('''1. Asignar sueldos aleatorios
             2. Clasificar sueldos
             3. Ver estadísticas.
             4. Reporte de sueldos
             5. Salir del programa''')
    while acceso==1:
        try:
            opc=int(input('INGRESE OPCION A REALIZAR:   '))
        except ValueError:
            print('ingrese una opcion valida')
            continue
        if opc==1:
            limpiar()
            guardarpersona()
            seguir()
            time.sleep(0.5)
        if opc==2:
            limpiar()
            Clasificarsueldos()
            seguir()
            time.sleep(0.5)
        if opc==3:
            limpiar()
            Verestadísticas()
            seguir()
            time.sleep(0.5)
        if opc==4:
            limpiar()
            Reportedesueldos()
            seguir()
            time.sleep(0.5)
        if opc==5:
            limpiar()
            print('''Finalizando programa
                    Desarrollado por Genesis Manque
                    RUT 20.448.862-2''')
            break
        else:
            print('intente nuevamente')
    



def seguir():
    while acceso==1:
        try:
            opc=int(input('''deseas volver al menu principal?
                            1- Si 
                            2- No:   '''))
        except ValueError:                  
            print('Ingrese una opcion valida')
        if opc==1:
            limpiar()
            print('Volviendooo')
            menuprincipal()
            time.sleep(0.7)
        if opc==2:
            limpiar()
            print('Adioss')
            quit()



def asiganarsueldo():
    print('asignando sueldos aleatorios...')
    alazar=randint(300000,2500000)
    trabajadores=(listatrabajadores,alazar)
    trabajadores_csv='trabajadores.csv'
    guardartrabajadores(trabajadores,trabajadores_csv)
    lista.append(trabajadores,trabajadores_csv)


def guardartrabajadores(trabajadores,trabajadores_csv):
    with open('trabajadores.csv','a', newline='') as trabajadores_csv:
        contenido=csv.write(trabajadores_csv)
        contenido.writerow(lista)
        print(lista)


#def Clasificarsueldos():
    with open('trabajadores.csv','w',newline='') as trabajadores_csv:
            contenido=csv.writer(trabajadores_csv)
            contenido.writerow(['nombre empleado',   'sueldo base',   'descuento salud',   'descuento afp',   'sueldo liquido'])





















menuprincipal()
#intento
#def agregar():
 #   nombre=input('hola')
  #  apellido=input('')
   # trabajador=(nombre,apellido)
   # print('numero ala azar')
   # alazar=randint(1,100)
   # guardarpersona(trabajador,alazar)
   # trabajadores_csv='trabajadores.csv'
   # lista.append(trabajador,trabajadores_csv)

#def guardarpersona(trabajador,trabajadores_csv):
 #   with open ('trabajadores.csv','w') as trabajadores_csv:
 #       contenido=csv.writer(trabajadores_csv)
  #      contenido.writerow(lista)

   #   with open('trabajadores.csv','w',newline='') as trabajadores_csv:
    #    contenido=csv.writer(trabajadores_csv)