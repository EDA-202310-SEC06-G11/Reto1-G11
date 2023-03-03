"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs(data_tipo):
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure=data_tipo,
                                     cmpfunction=cmp_impuestos_by_anio_CAE)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #d = new_data(data["id"], data["info"])
    lt.addLast(data_structs["data"], data)

    return data_structs


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs["data"])


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    data=data_structs["data"]
    make = merg.sort(data,cmp_mayor_saldo_total_a_pagar)
    new_list=lt.newList("ARRAY_LIST")
    start=""
    for i in lt.iterator(make):
        anio=i["Año"]
        if(anio!= start  ):
            lt.addLast(new_list,i)
            start=anio
    
    return new_list


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    data=data_structs["data"]
    make = merg.sort(data,cmp_mayor_saldo_total_a_favor)
    new_list=lt.newList("ARRAY_LIST")
    start=""
    for i in lt.iterator(make):
        anio=i["Año"]
        if(anio!= start):
            lt.addLast(new_list,i)
            start=anio
    
    return new_list


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    
    
    # TODO: Realizar el requerimiento 5
    data = data_structs["data"]
    sorted =merg.sort(data,cmp_mayor_anio)
    final_list=lt.newList("ARRAY_LIST")
    start=lt.firstElement(sorted)["Año"]
    code_first=lt.firstElement(sorted)["Código subsector económico"]
    suma=0
    starter=0
    primer =0
    
    for i in lt.iterator(sorted):
        anio=i["Año"]
        descuentoi=int(i["Descuentos tributarios"])
        codei = i["Código subsector económico"]
        if(anio== start):
            start=anio
            if(codei==code_first): 
                suma+=descuentoi 
                code_first = codei 
                if(descuentoi>=starter): 
                    starter=descuentoi 
                    elem=i  
                
            elif(codei!=code_first): 
                
                code_first = codei 
                if(suma  >= primer ):
                    primer = suma 
                    pos = elem 
                if(descuentoi >= primer): 
                    primer = descuentoi   
                    pos = i               
                suma=descuentoi 
                starter = descuentoi 
                elem = i 
        elif(anio!= start):
            lt.addFirst(final_list,pos)
            start =  anio
            code_first = codei
            suma = descuentoi
            elem = i
            primer = descuentoi
    lt.addFirst(final_list,pos)        
            
            
                
                
    
    return final_list
    #return final_list
    


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    data = data_structs["data"]
    lt.changeInfo(data,1["Año"],12 )
    return data


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data_1["id"] > data_2["id"]


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    sa.sort(data_structs["data"], sort_criteria)
    
def cmp_mayor_anio(anio1,anio2):
    if(anio1["Año"] > anio2["Año"]):
        return True
    elif(anio1["Año"] == anio2["Año"]):
        if(int(anio1["Código subsector económico"]) < int(anio2["Código subsector económico"])):
            return True
    else:
        return False
        

def cmp_impuestos_by_anio_CAE(impuesto1, impuesto2):
    """
    Devuelve verdadero (True) si el año de impuesto1 es menor que el de impuesto2,
    en caso de que sean iguales tenga en cuenta el código de la actividad económica,
    de lo contrario devuelva falso (False).
    Args:
    impuesto1: información del primer registro de impuestos que incluye el “Año” y el
    “Código
    actividad económica”
    impuesto2: información del segundo registro de impuestos que incluye el “Año” y el
    “Código actividad económica”
    """
     
    if(impuesto1["Año"] > impuesto2["Año"]):
        return True
    elif(impuesto1["Año"] == impuesto2["Año"]):
        if(impuesto1["Código actividad económica"] > impuesto2["Código actividad económica"]):
            return True
    else:
        return False
    
def cmp_mayor_saldo_total_a_pagar(act_1,act_2):
    
    
    if(act_1["Año"] < act_2["Año"]):
        return True
    elif(act_1["Año"] == act_2["Año"]):
        if(int(act_1["Total saldo a pagar"]) > int(act_2["Total saldo a pagar"])):
            return True
    else:
        return False
def cmp_mayor_saldo_total_a_favor(act_1,act_2):
    
    
    if(act_1["Año"] < act_2["Año"]):
        return True
    elif(act_1["Año"] == act_2["Año"]):
        if(int(act_1["Total saldo a favor"]) > int(act_2["Total saldo a favor"])):
            return True
    else:
        return False
    
def ordenamiento(order_tipo, data):
    if order_tipo=="selection":
        data=se.sort(data, cmp_impuestos_by_anio_CAE)
        return data
    elif order_tipo=="shell":
        data=sa.sort(data, cmp_impuestos_by_anio_CAE)
        return data
    elif order_tipo=="insertion":
        data=ins.sort(data, cmp_impuestos_by_anio_CAE)
        return data
    elif order_tipo=="merge":
        data=merg.sort(data, cmp_mayor_saldo_total_a_pagar)
        return data
    elif order_tipo=="quick":
        data=quk.sort(data, cmp_impuestos_by_anio_CAE)
        return data

def primeros_ultimos(data):
    dato1=lt.getElement(data,1)
    dato2=lt.getElement(data,2)
    dato3=lt.getElement(data,3)
    datoult3=lt.getElement(data,-2)
    datoult2=lt.getElement(data,-1)
    dato0=lt.getElement(data,0)
    return (dato1,dato2,dato3,datoult3,datoult2,dato0)