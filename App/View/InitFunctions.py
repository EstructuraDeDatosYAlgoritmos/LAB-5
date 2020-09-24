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
        print("Sus titulos son: \n")
        for i in range(companyData[1]):
            movie = lt.getElement(companyData[0], i)
            print(f"{movie['title']}")
            print(f"Con una puntuacion de {movie['vote_average']} por {movie['director_name']} \n")
        print(f"\n{companyName} cuenta con {companyData[1]} peliculas y una puntuacion total de {companyData[2]}.")
    else:
        print("No hay informacion de esta productora")

def ejecutarDescubrirDirectores(catalogo):
    directorName = input("ingrese el nombre del director o directora: ")
    directorData = Req.descubrirDirectores(catalogo,directorName)
    if directorData[0]:
        print("Ha dirigido : \n")
        for i in range(directorData[1]):
            movie = lt.getElement(directorData[0], i)
            print(f"{movie['title']}")
            print(f"Por {movie['director_name']} con una puntuacion de {movie['vote_average']} \n")
        print(f"\n{directorName} cuenta con {directorData[1]} peliculas y una puntuacion total de {directorData[2]}.")
    else:
        print("No hay informacion de este director")

def ejecutarDescubrirActores(catalogo):
    actorName = input("ingrese el nombre del actor o actriz: ")
    actorData = Req.descubrirActores(catalogo,actorName)
    if actorData[0]:
        print("Ha actuado en: \n")
        for i in range(actorData[1]):
            movie = lt.getElement(actorData[0], i)
            print(f"{movie['title']}")
            print(f"Por {movie['director_name']} con una puntuacion de {movie['vote_average']} \n")
        print(f"\n{actorName} cuenta con {actorData[1]} peliculas y una puntuacion total de {actorData[2]}.")
        print(f"Ademas, cuenta con {actorData[3][1]} peliculas bajo la direccion de {actorData[3][0]}.")
    else:
        print("No hay informacion de este actor")

def ejecutarDescubirGeneros(catalogo):
    genre = input('Ingrese el genero de interes: ')
    genreData = Req.descubrirGeneros(catalogo, genre)
    if genreData[0]:
        print('Lo generos son: \n')
        for i in range(genreData[1]):
            movie = lt.getElement(genreData[0], i)
            print(f'{movie["title"]}')
            print(f"Con una puntuacion de {movie['vote_average']} por {movie['director_name']} \n")
        print(f'\n En el genero {genre} se encuentran las peliculas {genreData[0]} que en total son {genreData[1]} peliculas y un promedio de {genreData[2]} ')
    else:
        print('No hay informacion de este genero')

def ejecutarDescubrirPaises(catalogo):
    countryName = input("ingrese el pais: ")
    countryData = Req.descubrirPaises(catalogo,countryName)
    if countryData[0]:
        print("Han producido: \n")
        for i in range(countryData[1]):
            movie = lt.getElement(countryData[0], i)
            print(f"{movie['title']}")
            print(f"Por {movie['director_name']} en el año de {movie['release_date'][6:11]} \n")
        print(f"\n{countryName} cuenta con {countryData[1]} peliculas y una puntuacion total de {countryData[2]}.")
        print(f"Ademas, cuenta con {countryData[3][0]} como su mejor director con {countryData[3][0]} peliculas.")
    else:
        print("No hay informacion de esta productora")