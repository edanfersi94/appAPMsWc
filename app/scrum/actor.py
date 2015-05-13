# -*- coding: utf-8 -*-
from model import *
from flask import request, session, Blueprint, json

actor = Blueprint('actor', __name__)


@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor(self, id_actores, nombre_actores):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    # -- Insertar actor -- #
    actor = model.Actores(id_actores, nombre_actores)
    session.add(actor)
    session.commit()

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor(self, id_actores, nombre_actores):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    # -- Modificar Rol -- #
    def modify_id_actores(self, id_actores, new):
        if (id_actores != None):
            session.query(model.Actores).filter(model.Actores.id_actores == id_actores).update({'id_actores':(new)})
            session.commit()
            return True
        return None
    
    def modify_nombre_actores(self, nombre_actores, new):
        if (nombre_actores != None):
            session.query(model.Actores).filter(model.Actores.nombre_actores == nombre_actores).update({'nombre_actores':(new)})
            session.commit()
            return True
        return None

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/VActor')
def VActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idPila'] = 1 

    #Action code ends here
    return json.dumps(res)



@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here