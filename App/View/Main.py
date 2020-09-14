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
import sys

from App.Controller import LoadData as Load
from App.View import Menu 
from App import Const


def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    data = False

    while True:
        Menu.mainMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        
        if len(inputs)>0 and (data or int(inputs[0])<=1):
            if int(inputs[0])==1: #opcion 1
                catalogo = Load.newCatalogo()
                Load.loadData(Const.LINKS_DIR,catalogo)

            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
        else:
            print("Porfavor, cargue datos")

if __name__ == "__main__":
    main()