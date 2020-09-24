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
    catalogoCompanies = catalogo["production_company"]
    companyName = movie["production_companies"]
    movieId = movie["id"]
    
    if mp.contains(catalogoCompanies, companyName):
        entry = mp.get(catalogoCompanies, companyName)
        company = me.getValue(entry)
    else:
        company = Schema.newProductionCompany()
        mp.put(catalogoCompanies, companyName, company)
    lt.addLast(company, movieId)


def addDirector(catalogo, movie):
    catalogoDirector = catalogo["director"]
    directorName = movie["director_name"]
    movieId = movie["id"]
    
    if mp.contains(catalogoDirector, directorName):
        entry = mp.get(catalogoDirector, directorName)
        directorMovies = me.getValue(entry)
    else:
        directorMovies = Schema.newDirector()
        mp.put(catalogoDirector, directorName, directorMovies)
    lt.addLast(directorMovies, movieId)

def addActor(catalogo, movie):
    catalogoActor = catalogo["actor"]

    movieId = movie["id"]
    actors = lt.newList('ARRAY_LIST')
    lt.addLast(actors,movie["actor1_name"]) 
    lt.addLast(actors,movie["actor2_name"]) 
    lt.addLast(actors,movie["actor3_name"]) 
    lt.addLast(actors,movie["actor4_name"]) 
    lt.addLast(actors,movie["actor5_name"]) 
    
    for i in range(lt.size(actors)):
        actorName = lt.getElement(actors, i)
        if mp.contains(catalogoActor, actorName):
            entry = mp.get(catalogoActor, actorName)
            actorMovies = me.getValue(entry)
        else:
            actorMovies = Schema.newActor()
            mp.put(catalogoActor, actorName, actorMovies)
        lt.addLast(actorMovies, movieId)

def addGenre(catalogo, movie):
    catalogoGenre = catalogo['genre']
    genre = movie['genre']
    movieId = movie['id']
    if mp.contains(genreCatalogo, genre):
        entry = mp.get(genreCatalogo, genre)
        genreSchema = me.getValue(entry)
    else:
        genreSchema = Schema.newGenre()
        mp.put(genreCatalogo, genre, genreSchema )
    lt.addLast(genreSchema, movieId)



def addCountry (catalogo, movie) :
    countryCatalogo = catalogo["country"]
    countryName = movie["production_countries"]
    movieId = movie["id"]
    
    if mp.contains(countryCatalogo, countryName):
        entry = mp.get(countryCatalogo, countryName)
        countrySchema = me.getValue(entry)
    else:
        countrySchema = Schema.newCountry()
        mp.put(countryCatalogo, countryName, countrySchema)
    lt.addLast(countrySchema, movieId)

def addMovie(catalogo, data: dict):
    mp.put(catalogo["movies"], data["id"], data)
    addActor(catalogo, data)
    addDirector(catalogo, data)
    addProductionCompany(catalogo, data)
    addCountry(catalogo, data)
        