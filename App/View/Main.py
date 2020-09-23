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

from App.View import Menu
from App.View import InitFunctions as Init



def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    dataReady = False
    catalogo = None

    while True:
        Menu.mainMenu() #imprimir el menu de opciones en consola
        inputs = input('Seleccione una opción para continuar\n') #leer opción ingresada
        
        if len(inputs)>0 and (dataReady or int(inputs[0])<=1):
            if int(inputs[0]) == 1:  #opcion 1
                del catalogo
                catalogo = Init.ejecutarLoadData()
                dataReady = True

            elif int(inputs[0]) == 2:  #opcion 2
                Init.ejecutarDescubrirProductoras(catalogo)
            
            elif int(inputs[0]) == 3:  #opcion 3
                Init.ejecutarDescubrirDirectores(catalogo)

            elif int(inputs[0]) == 4:  #opcion 4
                Init.ejecutarDescubrirActores(catalogo)
            
            elif int(inputs[0]) == 6:  #opcion 6
                Init.ejecutarDescubrirPaises(catalogo)
                
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)
                
        else:
            print("Porfavor, cargue datos")

if __name__ == "__main__":
    main()

