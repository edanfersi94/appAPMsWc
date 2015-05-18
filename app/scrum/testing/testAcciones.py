# -*- coding: utf-8 -*-. 

"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015
    AUTORES:
        
    DESCRIPCION: Script que contiene los casos de prueba del modulo "funcAccion.py"
    
"""

#------------------------------------------------------------------------------------

# Librerias a utilizar.
import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../../')
import model

# PATH que permite utilizar al modulo "dpt.py"
sys.path.append('../')
from funcAccion import clsAccion



import unittest


class TestAccion(unittest.TestCase):
    
    #.-------------------------------------------------------------------.  
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsAccions.
    def test1ObjectExist(self):
        tempAccion = clsAccion()
        self.assertIsNotNone( tempAccion )
        model.db.session.query( model.Acciones ).delete()  # Se limpia la base de datos.
    
    #.-------------------------------------------------------------------.  
    # FUNCION BUSCAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 2: Buscar el id de una acción que exista. 
    def test2find_idAcccionExist(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba'
        newAccion = model.Acciones( newIdAccion, newDescripAccion ) 
        model.db.session.add(newAccion)
        model.db.session.commit()   
        
        tempAccion = clsAccion()
        idAccion = 1
        query = tempAccion.find_idAccion( idAccion )
        self.assertIsNotNone( query[0] )
    
    # Test 3: Buscar el id de una acción que no exista.
    def test3find_idAccionNotExist(self):
        tempAccion = clsAccion()
        idAccion = 1000
        query = tempAccion.find_idAccion( idAccion )
        self.assertEqual(query,[])
    
    ### CASOS INVALIDOS( Casos Malicia )
    # Test 4: El id de la acción a buscar es un string.
    def test4find_idAccionString(self):
        tempAccion = clsAccion()
        idAccion = '1'
        query = tempAccion.find_idAccion( idAccion )
        self.assertEqual(query,[])
    
    # Test 5: El id de la acción a buscar es de tipo float.
    def test5find_idAccionFloat(self):
        tempAccion = clsAccion()
        idAccion = 1.01
        query = tempAccion.find_idAccion( idAccion )
        self.assertEqual(query,[])  

    # Test 6: El id de la acción a buscar es nulo.
    def test6find_idAccionNone(self):
        tempAccion = clsAccion()
        idAccion = None
        query = tempAccion.find_idAccion( idAccion )
        self.assertEqual(query,[])  
    
    #.-------------------------------------------------------------------.  
    # FUNCION INSERTAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 7: Insertar una acción
    def test_7insert_accion(self):
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
        tempAccion = clsAccion()
        newDescripAccion = 'Accion 2.0'
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertTrue(result)
           
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 8: Se insertara una acción cuyo tamaño es igual a 1.
    def test_8insert_accionLen1(self):
        tempAccion = clsAccion()
        newDescripAccion = '1'
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertTrue(result)

    # Test 9: Se insertara una acción cuyo tamaño es igual a 500.
    def test_9insert_accionLen500(self):
        tempAccion = clsAccion()
        newDescripAccion = 'r'*500
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertTrue(result)
                
    ### CASOS INVALIDOS( Casos Malicia ):    
    # Test 10: Se insertara una accion cuyo tamaño es 0 (Cadena Vacía).
    def test_10insert_accionLen0(self):
        tempAccion = clsAccion()
        newDescripAccion = ''
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertFalse(result)

    # Test 11: Se insertara una accion cuyo tamaño es de 501.
    def test_11insert_accionLen501(self):
        tempAccion = clsAccion()
        newDescripAccion = 'r'*501
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertFalse(result)

    # Test 12: Se insertara una accion cuya descripcion es un numero.
    def test_12insert_accionNumber(self):
        tempAccion = clsAccion()
        newDescripAccion = 501
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertFalse(result)

    # Test 13: Se insertara una accion cuya descripcion dada es None.
    def test_13insert_accionNone(self):
        tempAccion = clsAccion()
        newDescripAccion = None
        result = tempAccion.insert_Accion( newDescripAccion )
        self.assertFalse(result)

    #.-------------------------------------------------------------------.  
    # FUNCION MODIFICAR.
    
    ### CASOS VALIDOS( Casos Interiores ).
    # Test 14: El id de la acción a modificar existe en la base de datos.
    def test_14modify_accionExist(self):
        model.db.session.query(model.Acciones).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdAccion = 1
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'AccionX'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result )         

    # Test 15: El id de la acción a modificar no existe en la base de datos.
    def test_15modify_accionNoExist(self):
        tempAccion = clsAccion()
        idAccion = 20
        newDescripAccion = 'Esto sigue siendo una prueba'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result ) 
    
    ### CASOS VALIDOS( Casos Fronteras )
    # Test 16: El id de la acción a modificar existe en la base de datos y su
    #          valor es igual a 1. 
    def test_16modify_accionIdExistIqual1(self):

        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'esto sigue siendo una prueva V2'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result ) 

    
    # Test 17: El id de la acción a modificar existe en la base de datos. La nueva 
    #          descripción es de largo 1.
    def test_17modify_accionIdExistNewDescripLen1(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdAccion = 2
        newDescripAccion = 'Esto es una prueba.'
        newAccion = model.Acciones( newIdAccion, newDescripAccion) 
        model.db.session.add(newAccion)
        model.db.session.commit() 
        
        tempAccion = clsAccion()
        idAccion = 2
        newDescripAccion = '1'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result )  
    
    # Test 18: El id de la acción a modificar existe en la base de datos. La nueva 
    #          descripción es de largo 500.
    def test_18modify_accionIdExistNewDescripLen500(self):
        tempAccion = clsAccion()
        idAccion = 2
        newDescripAccion = 'x'*500
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result )  
    
    ### CASOS VALIDOS( Casos Esquinas )
    # Test 19: El id de la acción a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripción es de longitud igual a 1.
    def test_19modify_accionIdExistIqual1NewDescripLen1(self):
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'z'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result ) 
    
    # Test 20: El id de la acción a modificar existe en la base de datos y su valor es
    #          igual a 1. La nueva descripción es de longitud igual a 500.
    def test_20modify_accionIdExistIqual1NewDescripLen500(self):
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'z'*500
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertTrue( result ) 

    ### CASOS INVALIDOS( Casos Malicia )
    # Test 21: El id dado de la acción a modificar es un string.
    def test_21modify_accionIdString(self):        
        tempAccion = clsAccion()
        idAccion = '1'
        newDescripAccion = 'Axx'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )    
        
    # Test 22: El id dado de la acción a modificar es un numero negativo.    
    def test_22modify_accionIdNegative(self):        
        tempAccion = clsAccion()
        idAccion = -1
        newDescripAccion = 'accion de prueba'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )   

    # Test 23: El id dado de la acción a modificar es un float.
    def test_23modify_accionIdFloat(self):        
        tempAccion = clsAccion()
        idAccion = 1.0
        newDescripAccion = 'accion de prueba'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )   
        
    # Test 24: El id dado de la acción a modificar es None.         
    def test_24modify_accionIdNone(self):        
        tempAccion = clsAccion()
        idAccion = None
        newDescripAccion = 'accionPrueba'
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )   
    
    # Test 25: La nueva descripción para la acción a modificar es un string vacio.
    def test_25modify_accionDescripIsEmpty(self):        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = ''
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )    
        
    # Test 26: La nueva descripción para la acción a modificar es de longitud 501.    
    def test_26modify_accionDescripLen501(self):        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 'r'*501
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )   

    # Test 27: La nueva descripción para la acción a modificar es un numero.
    def test_27modify_accionDescripIsNumber(self):        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = 12345
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )   
        
    # Test 28: La nueva descripción para la acción a modificar es None. 
    def test_28modify_accionDescripNone(self):        
        tempAccion = clsAccion()
        idAccion = 1
        newDescripAccion = None
        result = tempAccion.modify_Accion( idAccion, newDescripAccion )
        self.assertFalse( result )   

    #.-------------------------------------------------------------------.  