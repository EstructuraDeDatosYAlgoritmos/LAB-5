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
    if (movieAvg == 0.0):
        company["vote_average"] = float(movieAvg)
    else:
        moviesNum = lt.size(company["movies"])
        company["vote_average"] = ((companyAvg*(moviesNum-1)) + float(movieAvg)) / moviesNum

def addMovie(catalogo, data: dict):
    if mp.contains(catalogo["movies"], data["id"]):
        movie = mp.get(catalogo["movies"], data["id"])
        movie = me.getValue(movie)
        movie.update(data)
        
    else:
        mp.put(catalogo["movies"], data["id"], data)
        addProductionCompany(catalogo,data)