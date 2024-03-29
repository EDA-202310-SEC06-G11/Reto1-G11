﻿"""
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
 """

import config as cf
import model
import time
import csv
import pandas as pd
from DISClib.ADT import list as lt
import tabulate 

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller(data_tipo):
    """
    Crea una instancia del modelo
    """
    control = {
        "model": None
    }
    control["model"] = model.new_data_structs(data_tipo)
    return control


# Funciones para la carga de datos

def load_data(control,size):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    catalog = control['model']
    if(size in "small" or size in "large"):
        file= "Salida_agregados_renta_juridicos_AG-"+size+".csv"
    else:
        file="Salida_agregados_renta_juridicos_AG-"+size+".csv"
    servicefile1 = cf.data_dir + file
    input_file1 = csv.DictReader(open(servicefile1, encoding='utf-8'))
    for program1 in input_file1:
        model.add_data(catalog, program1)

    return control


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    start_time = get_time()
    model.sort(control["model"])
    end_time = get_time()
    delta_t = delta_time(start_time, end_time)
    return delta_t


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    data = model.get_data(control["model"], id)
    return data


def print_carga_datos(data):
    lista_datos=[]
    for i in range(len(data)):
        lista_datos.append(data[i])
    lista=[]
    print(lista_datos)
    for i in (lista_datos):
        columna=[]
        columna.append(i["Año"])
        columna.append(i["Código actividad económica"])
        columna.append(i["Nombre actividad económica"])
        columna.append(i["Código sector económico"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Código subsector económico"])
        columna.append(i["Total ingresos netos"])
        columna.append(i["Total costos y gastos"])
        columna.append(i["Total saldo a pagar"])
        columna.append(i["Total saldo a favor"])
        lista.append(columna)
    df=pd.DataFrame(lista,columns=["Año", "Código actividad económica", "Nombre actividad económica","Código sector económico",
                                   "Nombre sector económico","Código subsector económico",
                                   "Total ingresos netos","Total costos y gastos ","Total saldo a pagar","Total saldo a favor"],index=None)
    df["Nombre sector económico"]=df["Nombre sector económico"].str.wrap(20)
    df.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True)
    return df
def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    req_1 = model.req_1(control["model"])
    lista=[]
    for i in lt.iterator(req_1):
        columna=[]
        columna.append(i["Año"])
        columna.append(i["Código actividad económica"])
        columna.append(i["Nombre actividad económica"])
        columna.append(i["Código sector económico"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Código subsector económico"])
        columna.append(i["Nombre subsector económico"])
        columna.append(i["Total ingresos netos"])
        columna.append(i["Total costos y gastos"])
        columna.append(i["Total saldo a pagar"])
        columna.append(i["Total saldo a favor"])
        lista.append(columna)  
    df=pd.DataFrame(lista,columns=["Año", "Código actividad económica", "Nombre actividad económica","Código sector económico",
                                   "Nombre sector económico","Código subsector económico",
                                   "Nombre subsector económico","Total ingresos netos",
                                   "Total costos y gastos ","Total saldo a pagar","Total saldo a favor"],index=None)
    #df["Nombre actividad económica"]=df["Nombre actividad económica"].str.wrap(20)
    df["Nombre sector económico"]=df["Nombre sector económico"].str.wrap(20)
    df["Nombre subsector económico"]=df["Nombre subsector económico"].str.wrap(20)
    df.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True)
    
    return df


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start=get_time()
    req_2 = model.req_2(control["model"])
    lista=[]
    for i in lt.iterator(req_2):
        columna=[]
        columna.append(i["Año"])
        columna.append(i["Código actividad económica"])
        columna.append(i["Nombre actividad económica"])
        columna.append(i["Código sector económico"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Código subsector económico"])
        columna.append(i["Nombre subsector económico"])
        columna.append(i["Total ingresos netos"])
        columna.append(i["Total costos y gastos"])
        columna.append(i["Total saldo a pagar"])
        columna.append(i["Total saldo a favor"])
        lista.append(columna)  
    final=get_time()
    print(delta_time(start,final))
    df=pd.DataFrame(lista,columns=["Año", "Código actividad económica", "Nombre actividad económica","Código sector económico",
                                   "Nombre sector económico","Código subsector económico",
                                   "Nombre subsector económico","Total ingresos netos",
                                   "Total costos y gastos ","Total saldo a pagar","Total saldo a favor"],index=None)
    #df["Nombre actividad económica"]=df["Nombre actividad económica"].str.wrap(20)
    df["Nombre sector económico"]=df["Nombre sector económico"].str.wrap(20)
    df["Nombre subsector económico"]=df["Nombre subsector económico"].str.wrap(20)
    df.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True)
    
    return df


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    req_3 = model.req_3(control["model"])
    primera_lista = req_3[0]
    segunda_lista =req_3[1]
    
    lista=[]
    lista2=[]
    df2=0
    
    for i in lt.iterator(segunda_lista):
        columna =[]
        columna.append(i["Año"])
        columna.append(i["Código actividad económica"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Total retenciones"])
        columna.append(i["Total ingresos netos"])
        columna.append(i["Total costos y gastos"])
        columna.append(i["Total saldo a pagar"])
        columna.append(i["Total saldo a favor"])
        lista2.append(columna)
    
    df2=pd.DataFrame(lista2,columns=["Año","Codigo actividad economica",
                                   "Nombre sector economico","Total retenciones",
                                   "Total ingresos netos","Total costos y gastos",
                                   "Total saldo a pagar","Total saldo a favor"])
    df2.set_axis(labels=df2.columns.str.wrap(10), axis=1, inplace=True)
    
    for i in lt.iterator(primera_lista):
        columna=[]
        columna.append(i["Año"])
        columna.append(i["Código sector económico"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Código subsector económico"])
        columna.append(i["Nombre subsector económico"])
        columna.append(i["Total de retenciones del subsector economico"])
        columna.append(i["Total ingresos netos del subsector economico"])
        columna.append(i["Total costos y gastos del subsector economico"])
        columna.append(i["Total saldo a pagar del subsector economico"])
        columna.append(i["Total saldo a favor del subsector economico"])
        lista.append(columna)  
    df=pd.DataFrame(lista,columns=["Año", "Codigo sector economico", "Nombre sector economico","Codigo subsector economico",
                                   "Nombre subsector economico","Total de retenciones del subsector economico",
                                   "Total ingresos netos del subsector economico","Total costos y gastos del subsector economico",
                                   "Total saldo a pagar del subsector economico ","Total saldo a favor del subsector economico"],index=None)
    df.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True)
    return  df , df2


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    start = get_time()
    req_4 = model.req_4(control["model"])
    end = get_time()
    time= delta_time(start,end)
    print(time)
    primera_lista = req_4[0]
    segunda_lista =req_4[1]
    lista=[]
    lista2=[]
    df2=0
    
    for i in lt.iterator(segunda_lista):
        columna =[]
        columna.append(i["Año"])
        columna.append(i["Código actividad económica"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Costos y gastos nómina"])
        columna.append(i["Total ingresos netos"])
        columna.append(i["Total costos y gastos"])
        columna.append(i["Total saldo a pagar"])
        columna.append(i["Total saldo a favor"])
        lista2.append(columna)
    
    df2=pd.DataFrame(lista2,columns=["Año","Codigo actividad economica",
                                   "Nombre sector economico","Costos y gastos nómina",
                                   "Total ingresos netos","Total costos y gastos",
                                   "Total saldo a pagar","Total saldo a favor"])
    df2.set_axis(labels=df2.columns.str.wrap(10), axis=1, inplace=True)
    
    for i in lt.iterator(primera_lista):
        columna=[]
        columna.append(i["Año"])
        columna.append(i["Código sector económico"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Código subsector económico"])
        columna.append(i["Nombre subsector económico"])
        columna.append(i["Total de costos y gastos nómina del subsector economico"])
        columna.append(i["Total ingresos netos del subsector economico"])
        columna.append(i["Total costos y gastos del subsector economico"])
        columna.append(i["Total saldo a pagar del subsector economico"])
        columna.append(i["Total saldo a favor del subsector economico"])
        lista.append(columna)  
    df=pd.DataFrame(lista,columns=["Año", "Codigo sector economico", "Nombre sector economico","Codigo subsector economico",
                                   "Nombre subsector economico","Total de costos y gastos nómina del subsector economico",
                                   "Total ingresos netos del subsector economico","Total costos y gastos del subsector economico",
                                   "Total saldo a pagar del subsector economico ","Total saldo a favor del subsector economico"],index=None)
    df.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True)
    return  df , df2

    


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start=get_time()
    req_5 = model.req_5(control["model"])
    primera_lista = req_5[0]
    segunda_lista =req_5[1]
    
    lista=[]
    lista2=[]
    df2=0
    
    for i in lt.iterator(segunda_lista):
        columna =[]
        columna.append(i["Año"])
        columna.append(i["Código actividad económica"])
        columna.append(i["Nombre actividad económica"])
        columna.append(i["Descuentos tributarios"])
        columna.append(i["Total ingresos netos"])
        columna.append(i["Total costos y gastos"])
        columna.append(i["Total saldo a pagar"])
        columna.append(i["Total saldo a favor"])
        lista2.append(columna)
    
    df2=pd.DataFrame(lista2,columns=["Año","Codigo actividad economica",
                                   "Nombre sector economico","Descuentos tributarios",
                                   "Total ingresos netos","Total costos y gastos",
                                   "Total saldo a pagar","Total saldo a favor"])
    df2.set_axis(labels=df2.columns.str.wrap(10), axis=1, inplace=True)
    
    for i in lt.iterator(primera_lista):
        columna=[]
        columna.append(i["Año"])
        columna.append(i["Código sector económico"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Código subsector económico"])
        columna.append(i["Nombre subsector económico"])
        columna.append(i["Total de descuentos tributarios del subsector economico"])
        columna.append(i["Total ingresos netos del subsector economico"])
        columna.append(i["Total costos y gastos del subsector economico"])
        columna.append(i["Total saldo a pagar del subsector economico"])
        columna.append(i["Total saldo a favor del subsector economico"])
        lista.append(columna)  
    end = get_time()
    print(delta_time(start,end))
    df=pd.DataFrame(lista,columns=["Año", "Codigo sector economico", "Nombre sector economico","Codigo subsector economico",
                                   "Nombre subsector economico","Total de descuentos tributarios del subsector economico",
                                   "Total ingresos netos del subsector economico","Total costos y gastos del subsector economico",
                                   "Total saldo a pagar del subsector economico ","Total saldo a favor del subsector economico"],index=None)
    df.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True)
    return  df , df2


def req_6(control,anio):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start=get_time()
    req_6 = model.req_6(control["model"],anio)
    lista1=lt.firstElement(req_6)
    tabla1=[]
    
    for i in lt.iterator(lista1):
        columna=[]
        columna.append(i["Código sector económico"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Total ingresos netos del sector economico"])
        columna.append(i["Total costos y gastos del sector economico"])
        columna.append(i["Total saldo a pagar del sector economico"])
        columna.append(i["Total saldo a favor del sector economico"])
        columna.append(i["Subsector economico que mas aporto"])
        columna.append(i["Subsector economico que menos aporto"])
        tabla1.append(columna)
    
    df=pd.DataFrame(tabla1,columns=["Codigo sector economico", "Nombre sector económico", "Total ingresos netos del sector economico","Total costos y gastos del sector economico",
                                   "Total saldo a pagar del sector economico","Total saldo a favor del sector economico",
                                   "Subsector economico que mas aporto","Subsector economico que menos aporto"],index=None)
    df["Nombre sector económico"]=df["Nombre sector económico"].str.wrap(20)
    df.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True)
    
    lista2=lt.getElement(req_6,2)
    tabla2=[]
    for i in lt.iterator(lista2):
        columna=[]
        columna.append(i["Código subsector económico"])
        columna.append(i["Nombre subsector económico"])
        columna.append(i["Total ingresos netos del subsector economico"])
        columna.append(i["Total costos y gastos del subsector economico"])
        columna.append(i["Total saldo a pagar del subsector economico"])
        columna.append(i["Total saldo a favor del subsector economico"])
        columna.append(i["Actividad economica que mas aporto"])
        columna.append(i["Actividad economica que menos aporto"])
        tabla2.append(columna)
    end=get_time()
    print(delta_time(start,end))
    df2=pd.DataFrame(tabla2,columns=["Código subsector económico", "Nombre subsector económico", "Total ingresos netos del subsector economico","Total costos y gastos del subsector economico",
                                   "Total saldo a pagar del subsector economico","Total saldo a favor del subsector economico",
                                   "Actividad economica que mas aporto","Actividad economica que menos aporto"],index=None)
    df2["Nombre subsector económico"]=df2["Nombre subsector económico"].str.wrap(10)
    df2.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True) 
    lista3=lt.getElement(req_6,3)
    tabla3=[]
    for i in lt.iterator(lista3):
        columna=[]
        columna.append(i["Código subsector económico"])
        columna.append(i["Nombre subsector económico"])
        columna.append(i["Total ingresos netos del subsector economico"])
        columna.append(i["Total costos y gastos del subsector economico"])
        columna.append(i["Total saldo a pagar del subsector economico"])
        columna.append(i["Total saldo a favor del subsector economico"])
        columna.append(i["Actividad economica que mas aporto"])
        columna.append(i["Actividad economica que menos aporto"])
        tabla3.append(columna)
    df3=pd.DataFrame(tabla3,columns=["Código subsector económico", "Nombre subsector económico", "Total ingresos netos del subsector economico","Total costos y gastos del subsector economico",
                                   "Total saldo a pagar del subsector economico","Total saldo a favor del subsector economico",
                                   "Actividad economica que mas aporto","Actividad economica que menos aporto"],index=None)
    df3["Nombre subsector económico"]=df3["Nombre subsector económico"].str.wrap(10)
    df3.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True) 
    return df ,df2 , df3


def req_7(control,top,a_i,a_f):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    start = get_time()
    req_7 = model.req_7(control["model"],top,a_i,a_f)
    end = get_time()
    time= delta_time(start,end)
    print(time)
    lista=[]
    for i in lt.iterator(req_7):
        columna =[]
        columna.append(i["Año"])
        columna.append(i["Código actividad económica"])
        columna.append(i["Nombre actividad económica"])
        columna.append(i["Código sector económico"])
        columna.append(i["Nombre sector económico"])
        columna.append(i["Código subsector económico"])
        columna.append(i["Nombre subsector económico"])
        columna.append(i["Total ingresos netos"])
        columna.append(i["Total costos y gastos"])
        columna.append(i["Total saldo a pagar"])
        columna.append(i["Total saldo a favor"])
        lista.append(columna)
    
    df=pd.DataFrame(lista,columns=["Año","Codigo actividad economica","Nombre actividad económica",'Código sector económico',
                                   "Nombre sector economico","Código subsector económico","Nombre subsector económico",
                                   "Total ingresos netos","Total costos y gastos",
                                   "Total saldo a pagar","Total saldo a favor"])
    df.set_axis(labels=df.columns.str.wrap(10), axis=1, inplace=True)
    return  df


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    req_8 = model.req_8(control["model"])
    return req_8


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


#funciones del lab
def ordenar(order_tipo, data):
    return model.ordenamiento(order_tipo, data)

def prim_ult(data):
    return model.primeros_ultimos(data)
