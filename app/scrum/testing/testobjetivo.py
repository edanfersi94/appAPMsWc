"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        Equipo SoftDev
        
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo 
                 "objetivo.py"
    
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.

import os
import sys

from app.scrum import *
import model

import unittest

class TestObjetivo(unittest.TestCase):
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsUser.
    def test1ObjectExist(self):
        tempObjetivo = clsObjetivo()
        self.assertIsNotNone( tempObjetivo )
        session.query( model.Objetivo ).delete()  # Se limpia la base de datos.
        
    
    
        
        
    

