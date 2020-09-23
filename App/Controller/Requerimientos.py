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
    return movies

def descubrirDirectores(catalogo, director):    
    movies = Search.getMoviesByDirector(catalogo, director)
    return movies

def descubrirActores(catalogo, actor):    
    movies = Search.getMoviesByActor(catalogo, actor)
    return movies

def descubrirPaises(catalogo, pais):
    movies = Search.getMoviesByCountry(catalogo, pais)
    return movies