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
from App.Model import Schema

assert config

"""
En este archivo definimos las funciones para modificar un catalogo
"""

def addProductionCompany (catalogo, movie) :
    companies = catalogo["production_company"]
    movieId = movie["id"]
    name = movie["production_companies"]
    existauthor = mp.contains(companies, name)
    if existauthor:
        entry = mp.get(companies, name)
        company = me.getValue(entry)
    else:
        company = Schema.newProductionCompany()
        mp.put(companies, name, company)
    lt.addLast(company['movies'], movieId)

    companyAvg = company["vote_average"]
    movieAvg = movie["vote_average"]
    if (companyAvg == 0.0):
        company["vote_average"] = float(movieAvg)
    else:
        moviesNum = lt.size(company["movies"])
        company["vote_average"] = ((companyAvg*(moviesNum-1)) + float(movieAvg)) / moviesNum

def addActor(catalogo, movie):
    catalogoActor = catalogo["actor"]

    movieId = movie["id"]
    actors = lt.newList('ARRAY_LIST')
    lt.addLast(actors,movie["actor1_name"]) 
    lt.addLast(actors,movie["actor2_name"]) 
    lt.addLast(actors,movie["actor3_name"]) 
    lt.addLast(actors,movie["actor4_name"]) 
    lt.addLast(actors,movie["actor5_name"]) 
    
    for i in range(1,lt.size(actors)+1):
        actorName = lt.getElement(actors, i)
        existauthor = mp.contains(catalogoActor, actorName)
        if existauthor:
            entry = mp.get(catalogoActor, actorName)
            actorInfo = me.getValue(entry)
        else:
            actorInfo = Schema.newActor()
            mp.put(catalogoActor, actorName, actorInfo)
        lt.addLast(actorInfo['movies'], movieId)

        actorAvg = actorInfo["vote_average"]
        movieAvg = movie["vote_average"]
        if (actorAvg == 0.0):
            actorInfo["vote_average"] = float(movieAvg)
        else:
            moviesNum = lt.size(actorInfo["movies"])
            actorInfo["vote_average"] = ((actorAvg * (moviesNum - 1)) + float(movieAvg)) / moviesNum
        
        director = movie["director_name"]
        if director in actorInfo["collaborations"]:
            actorInfo["collaborations"][director] += 1
        else:
            actorInfo["collaborations"][director] = 1


def addMovie(catalogo, data: dict):
    if mp.contains(catalogo["movies"], data["id"]):
        movie = mp.get(catalogo["movies"], data["id"])
        movie = me.getValue(movie)
        movie.update(data)
        addActor(catalogo,movie)
        addProductionCompany(catalogo, movie)
    else:
        mp.put(catalogo["movies"], data["id"], data)