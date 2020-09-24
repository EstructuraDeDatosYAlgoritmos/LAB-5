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
from App.Model import Comparation as Comp
from App.Const import PARAMS
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

def iniCatalogo():
    catalogo = {
        "movies" : None,
        "production_company" : None
    }

    catalogo["movies"] = mp.newMap(
                                    numelements = PARAMS["numelements"],
                                    maptype=PARAMS["maptype"],
                                    loadfactor=PARAMS["loadfactor"],
                                    comparefunction=Comp.compareMoviesIds
                                    )
    catalogo["production_company"] = mp.newMap (
                                    numelements = PARAMS["numelements"],
                                    maptype=PARAMS["maptype"],
                                    loadfactor=PARAMS["loadfactor"],
                                    comparefunction=Comp.compareProductionCompanies
                                    )
    catalogo["director"] = mp.newMap (
                                    numelements = PARAMS["numelements"],
                                    maptype=PARAMS["maptype"],
                                    loadfactor=PARAMS["loadfactor"],
                                    comparefunction=Comp.compareActors
                                    ) 
    catalogo["actor"] = mp.newMap (
                                    numelements = PARAMS["numelements"],
                                    maptype=PARAMS["maptype"],
                                    loadfactor=PARAMS["loadfactor"],
                                    comparefunction=Comp.compareActors
                                    ) 
    catalogo["genre"] = mp.newMap (
                                    numelements = PARAMS["numelements"],
                                    maptype=PARAMS["maptype"],
                                    loadfactor=PARAMS["loadfactor"],
                                    comparefunction=Comp.compareGenres
                                    )
    catalogo["country"] = mp.newMap (
                                    numelements = PARAMS["numelements"],
                                    maptype=PARAMS["maptype"],
                                    loadfactor=PARAMS["loadfactor"],
                                    comparefunction=Comp.compareCountries
                                    )
    
    return catalogo


def newProductionCompany():
    company = lt.newList(PARAMS["listtype"])
    return company

def newDirector():
    Director = lt.newList(PARAMS["listtype"])
    return Director

def newActor():
    Actor = lt.newList(PARAMS["listtype"])
    return Actor

def newGenre():
    genre = lt.newList(PARAMS["listtype"])
    return genre

def newCountry():
    country = lt.newList(PARAMS["listtype"])
    return country

def newMovie(data: dict):
        data["id"] = int(data["id"])
        data["budget"] = int(data["budget"])
        data["genres"] = data["genres"]
        data["imdb_id"] = data["imdb_id"] 
        data["original_language"] = data["original_language"] 
        data["original_title"] = data["original_title"] 
        data["overview"] = data["overview"]
        data["popularity"] = data["popularity"]
        data["production_companies"] = data["production_companies"] 
        data["production_countries"] = data["production_countries"] 
        data["release_date"] = data["release_date"]
        data["revenue"] = int(data["revenue"])
        data["runtime"] = int(data["runtime"]) 
        data["spoken_languages"] = data["spoken_languages"] 
        data["status"] = data["status"]
        data["tagline"] = data["tagline"]
        data["title"] = data["title"]
        data["vote_average"] = float(data["vote_average"]) 
        data["vote_count"] = int(data["vote_count"])
        data["production_companies_number"] = int(data["production_companies_number"]) 
        data["production_countries_number"] = int(data["production_countries_number"]) 
        data["spoken_languages_number"] = int(data["spoken_languages_number"])
        data["actor1_name"] = data["actor1_name"]
        data["actor1_gender"] = int(data["actor1_gender"]) 
        data["actor2_name"] = data["actor2_name"]
        data["actor2_gender"] = int(data["actor2_gender"])
        data["actor3_name"] = data["actor3_name"]
        data["actor3_gender"] = int(data["actor3_gender"]) 
        data["actor4_name"] = data["actor4_name"]
        data["actor4_gender"] = int(data["actor4_gender"]) 
        data["actor5_name"] = data["actor5_name"]
        data["actor5_gender"] = int(data["actor5_gender"]) 
        data["actor_number"] = int(data["actor_number"])
        data["director_name"] = data["director_name"]
        data["director_gender"] = data["director_gender"] 
        data["director_number"] = int(data["director_number"]) 
        data["producer_name"] = data["producer_name"]
        data["producer_number"] = int(data["producer_number"]) 
        data["screeplay_name"] = data["screeplay_name"]
        data["editor_name"] = data["editor_name"]
