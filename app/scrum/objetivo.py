# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.scrum.model import *


objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo(self, idObjetivo, descripObjetivo):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[0]
    
     # -- Insertar Objetivo -- #
    
    if (descripObjetivo==None):
        return False 

    idObjetivoEsEntero = (type(idObjetivo) == int)
    
    if (idObjetivoEsEntero and idObjetivo >=0):
        try: # Preguntamos si hay problemas con claves foraneas, claves primarias o dominios.
            nuevoObjetivo=model.Objetivo(idObjetivo,descripObjetivo)
            session.add(nuevoObjetivo)
            session.commit()           
            return True
        except: 
            return False
    
    return False
     
    
    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila) # falta agregar el id de la pila
    
    #Action code ends here
    
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@objetivo.route('/objetivo/AModifObjetivo', methods=['POST'])
def AModifObjetivo(self, idObjetivo, descripObjetivo):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message
    
    # -- Modificar Objetivo -- #
    
    if (descripObjetivo==None):
        return False
    
    try: # Preguntamos si hay algun problema buscando el idObjetivo.        
        session.query(model.Objetivo).filter(model.Objetivo.idObjetivo==idObjetivo).\
        update({'descripObjetivo':(descripObjetivo)})
        session.commit()
        return True 
    
    except:
       return False    

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@objetivo.route('/objetivo/VCrearObjetivo')
def VCrearObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@objetivo.route('/objetivo/VObjetivo')
def VObjetivo():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idPila'] = 1 

    #Action code ends here
    return json.dumps(res)



#Use case code starts here

#Use case code ends here
