"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config
from time import process_time as crono
from App.Model import AddFunctions as Add
from App.Model import Schema
from App.Const import DEV
import csv

def newCatalogo():
    catalogo = Schema.iniCatalogo()
    return catalogo

def loadData (data_link, data, sep=";"):
    
    print("Cargando archivo ....")
    
    startCrono = crono()  #tiempo inicial

    
        
    loadCSVFiles(data_link,data,sep)
        
    
    stopCrono = crono()  #tiempo final
    print("Tiempo de ejecución ", stopCrono - startCrono, " segundos")
    
def loadCSVFiles(link, data, sep=";"):
    dialect = csv.excel()
    dialect.delimiter = sep
    with open(link[0], encoding="utf-8-sig") as csvfile1:
        with open(link[1], encoding="utf-8-sig") as csvfile2:
            buffer = zip(csv.DictReader(csvfile1, dialect=dialect),csv.DictReader(csvfile2, dialect=dialect))
            cont = 0
            for movie in buffer:
                movieData = movie[0]
                movieData.update(movie[1])
                cont += 1
                Add.addMovie(data, movieData)
                if cont == DEV:
                    break
            print(cont)

