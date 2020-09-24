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
from time import process_time as crono

def descubrirProductoras(catalogo, Productora):
    startCrono = crono()  #tiempo inicial

    movies = Search.getMoviesByCompany(catalogo, Productora)
    
    stopCrono = crono()  #tiempo final
    print("Tiempo de ejecución ", stopCrono - startCrono, " segundos")
    return movies

def descubrirDirectores(catalogo, director):
    startCrono = crono()  #tiempo inicial

    movies = Search.getMoviesByDirector(catalogo, director)
 
    stopCrono = crono()  #tiempo final
    print("Tiempo de ejecución ", stopCrono - startCrono, " segundos")   
    return movies

def descubrirActores(catalogo, actor):
    startCrono = crono()  #tiempo inicial

    movies = Search.getMoviesByActor(catalogo, actor)
    
    stopCrono = crono()  #tiempo final
    print("Tiempo de ejecución ", stopCrono - startCrono, " segundos")
    return movies

def descubrirGeneros(catalogo, genero):
    startCrono = crono()  #tiempo inicial

    movies = Search.getMoviesByGenre(catalogo, genero)
    
    stopCrono = crono()  #tiempo final
    print("Tiempo de ejecución ", stopCrono - startCrono, " segundos")
    return movies

def descubrirPaises(catalogo, pais):
    startCrono = crono()  #tiempo inicial

    movies = Search.getMoviesByCountry(catalogo, pais)
    
    stopCrono = crono()  #tiempo final
    print("Tiempo de ejecución ", stopCrono - startCrono, " segundos")
    return movies