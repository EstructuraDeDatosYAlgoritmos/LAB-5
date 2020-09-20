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

from App.Model import SearchFunctions as Search
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

def descubrirProductoras(catalogo, Productora):
    movies = Search.getMoviesByCompany(catalogo, Productora)
    try:
        moviesNum = lt.size(movies[0])
    except:
        moviesNum = 0
    
    return (movies[0],movies[1],moviesNum)

def descubrirActores(catalogo, actor):
    movies = Search.getMoviesByActor(catalogo, actor)
    try:
        moviesNum = lt.size(movies[0])
        director = ("", 0)
        for key in movies[2].keys():
            if movies[2][key] > director[1]:
                director = (key, movies[2][key])
    except:
        moviesNum = 0
        director = ("", 0)
        print(movies[0])
        print(movies[1])
        print(movies[2])
        
    
    return (moviesNum,movies[0],movies[1],director)