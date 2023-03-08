"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
import model 
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import selectionsort as sele
from DISClib.Algorithms.Sorting import shellsort as sh
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mrg
from DISClib.Algorithms.Sorting import quicksort as qck
import pandas as pd
assert cf
from tabulate import tabulate

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(data_tipo):
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller(data_tipo)
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Obtener dato dado un ID")
    print("0- Salir")


def load_data(control,size):
    """
    Carga los datos
    """
    data = controller.load_data(control,size)
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    df=(controller.req_1(control))
    widt=[2,2,3,30,2,30,3,30,None,None,None,None]
    print(tabulate(df,df.columns,tablefmt="grid",maxcolwidths=widt))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    df=(controller.req_2(control))
    widt=[2,2,3,30,2,30,3,30,None,None,None,None]
    print(tabulate(df,df.columns,tablefmt="grid",maxcolwidths=widt))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print(controller.req_3(control))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    df=controller.req_4(control)
    widt = [2,4,3,30,2,30,6,6,6,6,6]
    print(tabulate(df,df.columns,tablefmt="grid",maxcolwidths=widt,))

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    df=controller.req_5(control)[0]
    df2=controller.req_5(control)[1]
    
    widt = [2,4,3,30,2,30,6,6,6,6,6]
    print(tabulate(df,df.columns,tablefmt="grid",maxcolwidths=widt))
    print("------------------------Otras-Tablas---------------------------------")
    print(tabulate(df2,df2.columns,tablefmt="grid"))

def print_req_6(control,anio):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    
    req_6=controller.req_6(control,anio)
    tabla1=req_6[0]
    tabla2=req_6[1]
    widt = [3,4,20,6,6,6,6,6,6]
    widt2=  [3,2,20,6,6,6,6,6,6]
    print(tabulate(tabla1,tabla1.columns,tablefmt="grid",maxcolwidths=widt))
    print("------------------------------------Economic subsector that contributed the most------------------------------------")
    print(tabulate(tabla2,tabla2.columns,tablefmt="grid",maxcolwidths=widt2))
    #print(tabulate(controller.req_6(control,anio), headers=["Codigo sector economico","Nombre sector economico ","Total ingresos net"]))


def print_req_7(control,top,a_i,a_f):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print(controller.req_7(control,top,a_i,a_f))


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    print(controller.req_8(control))


# Se crea el controlador asociado a la vista
#control = new_controller()


# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                #data_tipo = input('cual estructura desea usar (ARRAY_LIST, SINGLE_LINKED): ')
                data_tipo = "ARRAY_LIST"
                print("Elija el tamaño del archivo")
                print("5pct")
                print("10pct")
                print("20pct")
                print("30pct")
                print("50pct")
                print("80pct")
                print("small")
                print("large")
                size=input("Ingrese el tamaño:")
                control = new_controller(data_tipo)
                data = load_data(control,size)
                catalog = control['model']
                data = catalog['data']
                #order_tipo= input("Cual tipo de ordenamiento desea ejecutar(selection,shell,insertion,merge,quick):")
                order_tipo="merge"
                start_time=controller.get_time()
                list_ordenada = controller.ordenar(order_tipo,data)
                end_time=controller.get_time()
                tiempo = controller.delta_time(start_time,end_time)
                print(tiempo)
                prim_ultimos = controller.prim_ult(list_ordenada)
                
                
                print(prim_ultimos)

            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                anio = input("Ingrese el año que se desea analizar")
                print_req_6(control,anio)

            elif int(inputs) == 8:
                top= int(input('ingrese el top que desea buscar: '))
                a_i = input('ingrese el año inicial: ')
                a_f= input('ingrese el año final: ')
                print_req_7(control,top,a_i,a_f)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
    sys.exit(0)
