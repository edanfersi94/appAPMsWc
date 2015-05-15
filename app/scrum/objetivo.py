# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
from model import *


objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo(self,descripObjetivo):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[0]
    
    descripObjetivoStr = type(descripObjetivo) == str

    if (descripObjetivoStr):
    	descripObjetivoLenValido = 1<= len(descripObjetivo) <=500

    	if(descripObjetivoLenValido):

        	nuevoObjetivo=model.Objetivo(descripObjetivo)
        	session.add(nuevoObjetivo)
        	session.commit() 
        else:
        	res = results[1]       
    else: 
        res = results[1]
       
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
    descripObjetivoStr = type(descripObjetivo) == str
    if (descripObjetivoStr):
    	descripObjetivoLenValido = 1<= len(descripObjetivo) <=500

    	if(descripObjetivoLenValido):
    		query = session.query(model.Objetivo).filter(model.Objetivo.idObjetivo==idObjetivo).all()

    		if (query != []) :	
    		 	db.session.query(User).filter(User.idObjetivo==idObjetivo)
                update({'fullname':(newFullname)})
                db.session.commit()
                res = results[0]

            else:
            	res = results[1]

        else:
        	res = results[1]  

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