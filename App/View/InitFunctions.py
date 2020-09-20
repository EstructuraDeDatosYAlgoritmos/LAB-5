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

from DISClib.ADT import list as lt

from App.Controller import Requerimientos as Req
from App.Controller import LoadData as Load
from App import Const

def ejecutarLoadData():
    catalogo = Load.newCatalogo()
    Load.loadData(Const.LINKS_DIR, catalogo)
    return catalogo

def ejecutarDescubrirProductoras(catalogo):
    companyName = input("ingrese el nombre de la productora: ")
    companyData = Req.descubrirProductoras(catalogo, companyName)
    if companyData[0]:
        print(f"{companyName} cuenta con {companyData[2]} peliculas y una puntuacion total de {companyData[1]}.")
        print("Sus titulos son: \n")
        for i in range(lt.size(companyData[0])):
            movie = lt.getElement(companyData[0], i)
            print(f"{movie['title']}")
            print(f"Con una puntuacion de {movie['vote_average']} por {movie['director_name']} \n")
    else:
        print("No hay informacion de esta productora")

def ejecutarDescubrirActores(catalogo):
    actorName = input("ingrese el nombre del actor o actris: ")
    actorData = Req.descubrirActores(catalogo,actorName)
    if actorData[1]:
        print(f"{actorName} cuenta con {actorData[0]} peliculas y una puntuacion total de {actorData[2]}.")
        print(f"Ademas, cuenta con {actorData[3][1]} peliculas bajo la direccion de {actorData[3][0]}.")
        print("Ha actuado en: \n")
        for i in range(lt.size(actorData[1])):
            movie = lt.getElement(actorData[1], i)
            print(f"{movie['title']}")
            print(f"Por {movie['director_name']} con una puntuacion de {movie['vote_average']} \n")
    else:
        print("No hay informacion de esta productora")
