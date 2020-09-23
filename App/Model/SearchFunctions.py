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

def getMoviesByDirector(catalog, directorName:str):

    catalogDirector = mp.get(catalog["director"], directorName)
    
    if catalogDirector:
        directorData = me.getValue(catalogDirector)

        Num = lt.size(directorData)
        directorAvg = 0.0

        directorMovies = lt.newList(PARAMS["listtype"])
        for i in range(lt.size(directorData)):
            movie = getMovie(catalog, lt.getElement(directorData, i))
            lt.addLast(directorMovies, movie)

            directorAvg += float(movie["vote_average"])

        directorAvg =round(directorAvg/Num, 2)
        
        return (directorMovies,Num,directorAvg,)
        
    return (None, None, None, None)

def getMoviesByActor(catalog, actorName):

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

def getMoviesByCountry(catalog, countryName):

    countryCatalog = mp.get(catalog["country"], countryName)
    if countryCatalog:
        countryData = me.getValue(countryCatalog)

        directorMVP = ("", 0)
        directors = {}
        moviesNum = lt.size(countryData)
        countryAvg = 0.00

        countryMovies = lt.newList(PARAMS["listtype"])
        for i in range(moviesNum):
            movie = getMovie(catalog, lt.getElement(countryData, i))
            lt.addLast(countryMovies, movie)
        
            countryAvg += float(movie["vote_average"])
            directorName = movie["director_name"]

            if directorName in directors:
                directors[directorName] += 1
                
            else:
                directors[directorName] = 1

            if directors[directorName] > directorMVP[1]:
                    collaborator = (directorName, directors[directorName])
            
        countryAvg = round(countryAvg/moviesNum, 2)
        
        return (countryMovies,moviesNum,countryAvg,directorMVP)
        
    return (None, None, None, None)