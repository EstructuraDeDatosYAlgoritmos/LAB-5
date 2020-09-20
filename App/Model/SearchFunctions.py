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
    catalogCompany = mp.get(catalog["production_company"], companyName)
    if catalogCompany:
        companyData = me.getValue(catalogCompany)

        moviesNum = lt.size(companyData)
        companyAvg = 0.00

        companyMovies = lt.newList(PARAMS["listtype"])
        for i in range(moviesNum):
            movie = getMovie(catalog, lt.getElement(companyData, i))
            lt.addLast(companyMovies, movie)
        
            companyAvg += float(movie["vote_average"])
            
        companyAvg = round(companyAvg/moviesNum, 2)
        
        return (companyMovies,moviesNum,companyAvg)
        
    return (None, None, None)

def getMoviesByActor(catalog, actorName):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    catalogActor = mp.get(catalog["actor"], actorName)
    if catalogActor:
        actorData = me.getValue(catalogActor)

        moviesNum = lt.size(actorData)
        actorAvg = 0.0
        collaborator = ("", 0)
        directors = {}

        actorMovies = lt.newList(PARAMS["listtype"])
        for i in range(lt.size(actorData)):
            movie = getMovie(catalog, lt.getElement(actorData, i))
            lt.addLast(actorMovies, movie)

            actorAvg += float(movie["vote_average"])
            directorName = movie["director_name"]
            
            if directorName in directors:
                directors[directorName] += 1
                
            else:
                directors[directorName] = 1

            if directors[directorName] > collaborator[1]:
                    collaborator = (directorName, directors[directorName])

        actorAvg =round(actorAvg/moviesNum, 2)
        
        return (actorMovies,moviesNum,actorAvg,collaborator)
        
    return (None, None, None, None)