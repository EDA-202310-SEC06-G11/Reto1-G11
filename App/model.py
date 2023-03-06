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
    suma_ingresos=0
    suma_gastos=0
    suma_saldo_a_pagar=0
    suma_saldo_a_favor =0
    for i in lt.iterator(sorted):
        anio=i["Año"]
        descuentoi=int(i["Descuentos tributarios"])
        total_ingresos=int(i["Total ingresos netos"])
        total_gastos =int(i["Total costos y gastos"])
        codei = i["Código subsector económico"]
        total_saldo_a_pagar=int(i["Total saldo a pagar"])
        total_saldo_a_favor=int(i["Total saldo a favor"])
        if(anio== start):
            start=anio
            if(codei==code_first): 
                suma+=descuentoi 
                suma_ingresos+=total_ingresos
                suma_gastos+=total_gastos
                suma_saldo_a_pagar+=total_saldo_a_pagar
                suma_saldo_a_favor+=total_saldo_a_favor
                code_first = codei 
                if(descuentoi>=starter): 
                    starter=descuentoi 
                    elem=i  
                
            elif(codei!=code_first): 
                
                code_first = codei 
                if(suma  >= primer ):
                    primer = suma 
                    pos = elem 
                    mayor_ingresos=suma_ingresos
                    mayor_gastos = suma_gastos
                    mayor_saldo_a_pagar=suma_saldo_a_pagar
                    mayor_saldo_a_favor=suma_saldo_a_favor
                if(descuentoi >= primer): 
                    primer = descuentoi   
                    pos = i
                    mayor_ingresos=total_ingresos   
                    mayor_gastos=total_gastos
                    mayor_saldo_a_pagar=total_saldo_a_pagar
                    mayor_saldo_a_favor=total_saldo_a_favor            
                suma=descuentoi # 2977
                starter = descuentoi 
                elem = i 
                suma_ingresos=total_ingresos
                suma_gastos=total_gastos
                suma_saldo_a_pagar=total_saldo_a_pagar
                suma_saldo_a_favor=total_saldo_a_favor
        elif(anio!= start):
            if(suma  >= primer ):
                    primer = suma 
                    pos = elem 
                    mayor_ingresos=suma_ingresos
                    mayor_gastos=suma_gastos
                    mayor_saldo_a_pagar=suma_saldo_a_pagar
                    mayor_saldo_a_favor=suma_saldo_a_favor
            d = {
            "Año" : pos["Año"],
            "Código sector económico": pos["Código sector económico" ],
            "Nombre sector económico": pos["Nombre sector económico"],  
            "Código subsector económico": pos["Código subsector económico"],  
            "Nombre subsector económico" : pos["Nombre subsector económico"],                            
            "Total de descuentos tributarios del subsector economico": None,
            "Total ingresos netos del subsector economico": None,
            "Total costos y gastos del subsector economico":None,
            "Total saldo a pagar del subsector economico": None,
            "Total saldo a favor del subsector economico": None
            }
            d['Total de descuentos tributarios del subsector economico'] = primer
            d["Total ingresos netos del subsector economico"]=mayor_ingresos
            d["Total costos y gastos del subsector economico"]= mayor_gastos
            d["Total saldo a pagar del subsector economico"]= mayor_saldo_a_pagar
            d["Total saldo a favor del subsector economico"]=mayor_saldo_a_favor
            lt.addFirst(final_list,d)
            start =  anio
            code_first = codei
            suma = descuentoi 
            elem = i 
            primer = descuentoi
            suma_ingresos= total_ingresos
            suma_gastos= total_gastos
            suma_saldo_a_pagar= total_saldo_a_pagar
            suma_saldo_a_favor=total_saldo_a_favor
    a = {
            "Año" : pos["Año"],
            "Código sector económico": pos["Código sector económico" ],
            "Nombre sector económico": pos["Nombre sector económico"], 
            "Código subsector económico": pos["Código subsector económico"],
            "Nombre subsector económico" : pos["Nombre subsector económico"],                             
            "Total de descuentos tributarios del subsector economico": None,
            "Total ingresos netos del subsector economico": None,
            "Total costos y gastos del subsector economico":None,
            "Total saldo a pagar del subsector economico": None,
            "Total saldo a favor del subsector economico": None
    }
    a['Total de descuentos tributarios del subsector economico'] = primer
    a["Total ingresos netos del subsector economico"]=mayor_ingresos
    a["Total costos y gastos del subsector economico"]= mayor_gastos
    a["Total saldo a pagar del subsector economico"]= mayor_saldo_a_pagar
    a["Total saldo a favor del subsector economico"]=mayor_saldo_a_favor
    lt.addFirst(final_list,a)  


            
            
                
                
    
    return final_list
    
    


def req_6(data_structs,anio):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    
    data = data_structs["data"]
    list_sort=merg.sort(data,cmp_mayor_código_del_sector_económico)
    list_of_year=lt.newList("ARRAY_LIST")
    for i in lt.iterator(list_sort):
        if(anio==i["Año"]):
            lt.addLast(list_of_year,i)
    codigo_start=lt.firstElement(list_of_year)["Código sector económico"]
    suma_ingresos=0
    suma_costos=0
    suma_saldo_pagar=0
    suma_saldo_favor=0
    mayor_ingresos = 0
    menor_ingresos = int(lt.firstElement(list_of_year)["Total ingresos netos"]) 
    listaPrueba = lt.newList("ARRAY_LIST")
    listaMayorSubsector = lt.newList("ARRAY_LIST")
    listaMenorSubsector = lt.newList("ARRAY_LIST")
    listaFinal = lt.newList("ARRAY_LIST")
    menor =lt.firstElement(list_of_year)
    contador =0
    for i in lt.iterator(list_of_year):
        codigo = i["Código sector económico"]
        ingresos = int(i["Total ingresos netos"])
        costos =int(i["Total costos y gastos"])
        saldo_pagar=int(i["Total saldo a pagar"])
        saldo_favor=int(i["Total saldo a favor"])
        contador+=1
        if(codigo_start==codigo):
            codigo_start=codigo
            suma_ingresos+=ingresos
            suma_costos+=costos
            suma_saldo_pagar+=saldo_pagar
            suma_saldo_favor+=saldo_favor
            if(ingresos >= mayor_ingresos):
                mayor_ingresos= ingresos
                mayor = i
            elif(menor_ingresos>ingresos):
                menor_ingresos = ingresos
                menor = i 
        elif(codigo_start!=codigo):
            """
            lt.addFirst(listaPrueba,menor)
            lt.addFirst(listaPrueba,mayor)
            """
            dic=diccionarios_req_6()[0]
            dic["Código sector económico"]=mayor["Código sector económico"]
            dic["Nombre sector económico"]=mayor["Nombre sector económico"]
            dic["Total ingresos netos del sector economico"]= suma_ingresos
            dic["Total costos y gastos del sector economico"]=suma_costos
            dic["Total saldo a pagar del sector economico"]=suma_saldo_pagar
            dic["Total saldo a favor del sector economico"] = suma_saldo_favor
            dic["Subsector economico que mas aporto"]=mayor["Código subsector económico"]
            dic["Subsector economico que menos aporto"]=menor["Código subsector económico"] 
            lt.addLast(listaPrueba,dic)
            mayor_actividad =diccionarios_req_6()[2]
            mayor_actividad["Código actividad económica"]=mayor["Código actividad económica"]
            mayor_actividad["Nombre actividad económica"]=mayor["Nombre actividad económica"]
            mayor_actividad["Total ingresos netos"]=mayor["Total ingresos netos"]
            mayor_actividad["Total costos y gastos"]=mayor["Total costos y gastos"]
            mayor_actividad["Total saldo a pagar"]=mayor["Total saldo a pagar"]
            mayor_actividad["Total saldo a favor"]=mayor["Total saldo a favor"]
            
            
            menor_actividad = diccionarios_req_6()[2]
            menor_actividad["Código actividad económica"]=menor["Código actividad económica"]
            menor_actividad["Nombre actividad económica"]=menor["Nombre actividad económica"]
            menor_actividad["Total ingresos netos"]=menor["Total ingresos netos"]
            menor_actividad["Total costos y gastos"]=menor["Total costos y gastos"]
            menor_actividad["Total saldo a pagar"]=menor["Total saldo a pagar"]
            menor_actividad["Total saldo a favor"]=menor["Total saldo a favor"]
            
            
            mayor_sub = diccionarios_req_6()[1]
            mayor_sub["Código subsector económico"]=mayor["Código subsector económico"]
            mayor_sub["Nombre subsector económico"]=mayor["Nombre subsector económico"]
            mayor_sub["Total ingresos netos del subsector economico"]= suma_ingresos
            mayor_sub["Total costos y gastos del subsector economico"]=suma_costos
            mayor_sub["Total saldo a pagar del subsector economico"] = suma_saldo_pagar
            mayor_sub["Total saldo a favor del subsector economico"] = suma_saldo_favor
            mayor_sub["Actividad economica que mas aporto"] =mayor_actividad
            mayor_sub["Actividad economica que menos aporto"]=menor_actividad
            lt.addLast(listaMayorSubsector,mayor_sub)
            
            menor_sub = diccionarios_req_6()[1]
            menor_sub["Código subsector económico"]=menor["Código subsector económico"]
            menor_sub["Nombre subsector económico"]=menor["Nombre subsector económico"]
            menor_sub["Total ingresos netos del subsector economico"]= suma_ingresos
            menor_sub["Total costos y gastos del subsector economico"]=suma_costos
            menor_sub["Total saldo a pagar del subsector economico"] = suma_saldo_pagar
            menor_sub["Total saldo a favor del subsector economico"] = suma_saldo_favor
            menor_sub["Actividad economica que mas aporto"] =mayor_actividad
            menor_sub["Actividad economica que menos aporto"]=menor_actividad
            lt.addLast(listaMenorSubsector,menor_sub)
            #---------------------------------
            codigo_start= codigo 
            suma_ingresos = ingresos
            suma_costos = costos
            suma_saldo_pagar = saldo_pagar
            suma_saldo_favor = saldo_favor
            mayor_ingresos = ingresos
            menor_ingresos = ingresos
            mayor = i 
            menor = i 
        if(contador==lt.size(list_of_year)):
            dicc=diccionarios_req_6()[0]
            dicc["Código sector económico"]=mayor["Código sector económico"]
            dicc["Nombre sector económico"]=mayor["Nombre sector económico"]
            dicc["Total ingresos netos del sector economico"]= suma_ingresos
            dicc["Total costos y gastos del sector economico"]=suma_costos
            dicc["Total saldo a pagar del sector economico"]=suma_saldo_pagar
            dicc["Total saldo a favor del sector economico"] = suma_saldo_favor
            dicc["Subsector economico que mas aporto"]=mayor["Código subsector económico"]
            dicc["Subsector economico que menos aporto"]=menor["Código subsector económico"] 
            lt.addLast(listaPrueba,dicc)
            mayor_actividad =diccionarios_req_6()[2]
            mayor_actividad["Código actividad económica"]=mayor["Código actividad económica"]
            mayor_actividad["Nombre actividad económica"]=mayor["Nombre actividad económica"]
            mayor_actividad["Total ingresos netos"]=mayor["Total ingresos netos"]
            mayor_actividad["Total costos y gastos"]=mayor["Total costos y gastos"]
            mayor_actividad["Total saldo a pagar"]=mayor["Total saldo a pagar"]
            mayor_actividad["Total saldo a favor"]=mayor["Total saldo a favor"]
            
            
            menor_actividad = diccionarios_req_6()[2]
            menor_actividad["Código actividad económica"]=menor["Código actividad económica"]
            menor_actividad["Nombre actividad económica"]=menor["Nombre actividad económica"]
            menor_actividad["Total ingresos netos"]=menor["Total ingresos netos"]
            menor_actividad["Total costos y gastos"]=menor["Total costos y gastos"]
            menor_actividad["Total saldo a pagar"]=menor["Total saldo a pagar"]
            menor_actividad["Total saldo a favor"]=menor["Total saldo a favor"]
            
            
            mayor_sub = diccionarios_req_6()[1]
            mayor_sub["Código subsector económico"]=mayor["Código subsector económico"]
            mayor_sub["Nombre subsector económico"]=mayor["Nombre subsector económico"]
            mayor_sub["Total ingresos netos del subsector economico"]= suma_ingresos
            mayor_sub["Total costos y gastos del subsector economico"]=suma_costos
            mayor_sub["Total saldo a pagar del subsector economico"] = suma_saldo_pagar
            mayor_sub["Total saldo a favor del subsector economico"] = suma_saldo_favor
            mayor_sub["Actividad economica que mas aporto"] =mayor_actividad
            mayor_sub["Actividad economica que menos aporto"]=menor_actividad
            lt.addLast(listaMayorSubsector,mayor_sub)
            
            menor_sub = diccionarios_req_6()[1]
            menor_sub["Código subsector económico"]=menor["Código subsector económico"]
            menor_sub["Nombre subsector económico"]=menor["Nombre subsector económico"]
            menor_sub["Total ingresos netos del subsector economico"]= suma_ingresos
            menor_sub["Total costos y gastos del subsector economico"]=suma_costos
            menor_sub["Total saldo a pagar del subsector economico"] = suma_saldo_pagar
            menor_sub["Total saldo a favor del subsector economico"] = suma_saldo_favor
            menor_sub["Actividad economica que mas aporto"] =mayor_actividad
            menor_sub["Actividad economica que menos aporto"]=menor_actividad
            lt.addLast(listaMenorSubsector,menor_sub)
            
            
    lt.addLast(listaFinal,listaPrueba)
    lt.addLast(listaFinal,listaMayorSubsector)
    lt.addLast(listaFinal,listaMenorSubsector)
    return listaFinal


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    #PRUEBAS 
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass

def diccionarios_req_6():
    dic ={
                "Código sector económico":None,
                "Nombre sector económico": None,
                "Total ingresos netos del sector economico": None,
                "Total costos y gastos del sector economico": None,
                "Total saldo a pagar del sector economico":None,
                "Total saldo a favor del sector economico":None,
                "Subsector economico que mas aporto": None,
                "Subsector economico que menos aporto": None
            }
    mayores_subctores={
                "Código subsector económico":None,
                "Nombre subsector económico":None,
                "Total ingresos netos del subsector economico":None,
                "Total costos y gastos del subsector economico":None,
                "Total saldo a pagar del subsector economico":None,
                "Total saldo a favor del subsector economico":None,
                "Actividad economica que mas aporto":None,
                "Actividad economica que menos aporto":None
            }
    actividades ={
        "Código actividad económica":None,
        "Nombre actividad económica":None,
        "Total ingresos netos":None,
        "Total costos y gastos":None,
        "Total saldo a pagar":None,
        "Total saldo a favor":None
    }
    return dic ,mayores_subctores , actividades

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
        if(int(anio1["Código subsector económico"]) > int(anio2["Código subsector económico"])):
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
    
def cmp_mayor_código_del_sector_económico(sector1,sector2):
    if(sector1["Año"] > sector2["Año"]):
        return True
    elif(sector1["Año"] == sector2["Año"]):
        if(int(sector1["Código sector económico"]) < int(sector2["Código sector económico"])):
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