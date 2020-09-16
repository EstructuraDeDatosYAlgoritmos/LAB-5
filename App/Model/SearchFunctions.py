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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from App.Const import PARAMS

def getMovie(catalog, movieId):
    movie = mp.get(catalog["movies"], movieId)
    if movie:
        return me.getValue(movie)
    return None

def getMoviesByCompany(catalog, companyName):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    productionCompany = mp.get(catalog["production_company"], companyName)
    if productionCompany:
        companyData = me.getValue(productionCompany)
        companyMovies = lt.newList(PARAMS["listtype"])
        for i in range(lt.size(companyData["movies"])):
            movie = getMovie(catalog, lt.getElement(companyData["movies"], i))
            lt.addLast(companyMovies, movie)
        
        return (companyMovies,companyData["vote_average"])
        
    return (None,None)