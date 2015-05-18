# -*- coding: utf-8 -*-

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
#----------------------------------------------------------
# Librerias a importar 

from flask import request, session, Blueprint, json

dev = Blueprint('dev', __name__)


@dev.route('/dev/VDesarrollador')
def VDesarrollador():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here