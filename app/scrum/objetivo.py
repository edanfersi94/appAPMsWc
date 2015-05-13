# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from app.data.model import Objetivo, db
objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    #oObjetivo=Objetivo()
    #oObjetivo.add()
    
    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)
    
    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@objetivo.route('/objetivo/AModifObjetivo', methods=['POST'])
def AModifObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

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

# Librerias a utilizar.

import os

# PATH que permite utilizar al modulo "model.py"



#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker


class clsObjetivo():
    
    
    def insertar(self,idobjetivo,descripcionobjetivo):
        
        idobjetivoEsEntero = (type(idobjetivo) == int)
        if (idobjetivotEsEntero and idobjetivo >=0):
            if (self.buscar(idobjetivo) == []):
                try: # Si hay problema, retornamos False.
                    nuevoObjetivo=model.Objetivo(idobjetivo,idobjetivo)
                    session.add(nuevoObjetivo)
                    session.commit()           
                    return True
                except: 
                    return False
        
        return False
     
    
    def modificarDescripcion(self,idobjetivo,descripcionobjetivo):
        
        if (self.buscar(idobjetivo) == []):
           return False
       
        try: # Si hay problema, retornamos False.
            session.query(model.Objetivo).filter(model.Objetivo.idobjetivo==idobjetivo).\
            update({'descripcionobjetivo':(descripcionobjetivo)})
            session.commit()
            return True 
        except:
            return False
        
                     
    def buscar(self,idobjetivo):
         
        idobjetivoEsEntero = (type(idobjetivo) == int)
        
        if idobjetivoEsEntero:
            busqueda= session.query(model.Objetivo).filter(model.Objetivo.idobjetivo==idobjetivo).all()
            return busqueda

        return []
   
