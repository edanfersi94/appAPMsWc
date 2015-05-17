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
    #----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # FUNCION INSERTAR
    
    # ------------------- Casos Validos ----------------------------
    
    #Test 2:
    #Inserto palabras en minusculas
    def test2ObjInsertMinusValid(self):
        
        newDescripObj = 'hola'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
        
    #Test 3:
    #Inserto palabras en Mayusculas
    def test3ObjInsertMayusValid(self):    
        
        newDescripObj = 'HOLA'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
        
    #Test 4:
    #Inserto palabras mayusculas y minusculas
    def test4ObjInsertMayusMinusValid(self):
        
        newDescripObj = 'HOLAsoyYo'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
        
    #Test 5:
    #Inserto palabras mayusculas y minusculas
    def test5ObjInsertMayusMinusValid(self):
        
        newDescripObj = 'HOLAsoyYo'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
        
    #Test 6:
    #Inserto palabras mayusculas y numeros
    def test6ObjInsertMayusNumValid(self):
        
        newDescripObj = 'HOLA1223'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
        
    #Test 7:
    #Inserto palabras minusculas y numeros
    def test7ObjInsertMinusNumValid(self):
        
        newDescripObj = 'hola1223'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
        
    #Test 8:   
    #Inserto una palabra de tamanio 1
    def test8ObjInsertLen1Valid(self):
        
        newDescripObj = 'h'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
    
    #Test 9:
    #Inserto una palabra de tamanio 1
    def test9ObjInsertLen250Valid(self):
        
        newDescripObj = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
        
    # ---------------------- Casos Fronteras --------------------------------------------
        
    #Test 10:
    #Inserto una palabra de tamanio 1
    def test_10_ObjInsertLen500Valid(self):
        
        newDescripObj = 'h'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
        
    #Test 11:
    #Inserto una palabra de tamanio 500
    def test_11_ObjInsertLen500Valid(self):
        
        newDescripObj = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. Praesent turpis. Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Donec elit libero, sodales nec, volutpat a, suscipit non, turpis. Nullam sagittis. Suspendisse pulvinar, augue ac venenatis condimentum, sem libero volutpat nibh, nec pellentesque velit pede quis nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis'
        result = insert_Objetivo(newDescripObj)
        self.assertTrue( result )
        
        
    
    # -------------------------------------- Casos invalidos ------------------------------------------------------------
    
    #Test 12: 
    #Inserto una palabra nula
    def test_12_ObjInsertLeNNoneInvalid(self):
        
        newDescripObj = ''
        result = insert_Objetivo(newDescripObj)
        self.assertFalse(result)  
        
    #Test 13: 
    #Inserto una palabra de tamanio 501
    def test_13_ObjInsertLeN501Invalid(self):
        
        newDescripObj = 'Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Fusce vulputate eleifend sapien. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Nullam accumsan lorem in dui. Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer lacinia. Nam pretium turpis et arcu. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Sed aliquam ultrices mauris. Integer ante arcu, accumsan a, consectetuer eget, posuere ut, mauris. Praesent adipiscing. Phasellus ullamcorper ipsum rutrum nunc. Nunc nonummy metus. Vestibulum volutpat pretium libero. Cras id dui. Aenean ut eros et nisl sagittis vestibulum. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede. Sed lectus. Donec mollis hendrerit risus. Phasellus nec sem in justo pellentesque facilisis. Etiam imperdiet imperdiet orci. Nunc nec neque. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Maecenas malesuada. Praesent congue erat at massa. Sed cursus turpis vitae tortor. Donec posuere vulputate arcu. Phasellus accumsan cursus velit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed aliquam, nisi quis porttitor congue, elit erat euismod orci, ac placerat dolor lectus quis orci. Phasellus consectetuer vestibulum elit. Aenean tellus metus, bibendum sed, posuere ac, mattis non, nunc. Vestibulum fringilla pede sit amet augue. In turpis. Pellentesque posuere. Praesent turpis. Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Donec elit libero, sodales nec, volutpat a, suscipit non, turpis. Nullam sagittis. Suspendisse pulvinar, augue ac venenatis condimentum, sem libero volutpat nibh, nec pellentesque velit pede quis nunc. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Fusce id purus. Ut varius tincidunt libero. Phasellus dolor. Maecenas vestibulum mollis diam.'
        result = insert_Objetivo(newDescripObj)
        self.assertFalse(result)
        
    #Test 14: 
    #Inserto un numero
    def test_14_ObjInsertNumInvalid(self):
        
        newDescripObj = 1234343
        result = insert_Objetivo(newDescripObj)
        self.assertFalse(result)  
    
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # FUNCION BUSCAR.
    
    #-------------------------- Casos validos ----------------------------------
    
    #Test 15: 
    
    def test_15_ObjFindValid(self):
    # Se inserta un elemento en la base. Dicha insercion se asegura
    # que es valida. 
    
        newDescripObj = 'holasoyYO1'
        newObjecto = model.Objecto(newDescripObj)
        session.add(newDpt)
        session.commit()  
        
        tempObj = clsObjetivo()
        idObjetivo = 1
        query = tempObj.find_idObjetivo(idObjetivo)
        
        boolR = True
        
        for element in query:
            if element.idObjetivo != idObjetivo:
                boolR = False
        self.assertTrue( boolR )
        
    
    # Test 16: Buscar un idObjetivo que no exista en la base de 
    #          datos.
    
    def test_16_ObjFindiDNoExistInvalid(self):
        
        tempObj = clsObjetivo()
        idObjetivo = 100
        query = tempObj.find_idObjetivo(idObjetivo)
        self.assertEqual( query, [] )
        
    ### CASOS INVALIDOS( Casos Maliciosos ).
    
    # Test 17: Buscar un STRING como idObjetivo.
    
    def test_17_Objfind_idObjInvalid(self):
        tempObj = clsUser()
        idObjetivo = "Holaa"
        query = tempObj.find_idObjetivo(idObjetivo)
        self.assertEqual( query, [] )
        
    # Test 18: Buscar el string vacio como idObjetivo.
    def test_18_Objfind_idObjInvalid(self):
        tempObj = clsObjetivo()
        idObjetivo = ''
        query = tempObj.find_idObjetivo( idObjetivo )
        self.assertEqual( query, [] )
        
    # Test 19: Buscar None como idObjetivo.
    def test_19_Objfind_idObjInvalid(self):
        tempObj = clsObjetivo()
        idObjetivo = None
        query = tempObj.find_idObjetivo( idObjetivo )
        self.assertEqual( query, [] )
        
    #-------------------------------------------------------------------------------------
    
    
    # FUNCION MODIFICAR
    
    
    
    
    
    
    
    
     
        
        
    
        
    ## 
    
    
    
    
    
    
    
    
    
        
        
    
        
    
        
        
        
    
    
        
        
    
    
        
        
    

