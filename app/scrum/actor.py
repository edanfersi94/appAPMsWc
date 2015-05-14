# -*- coding: utf-8 -*-
#from base import *
from flask import request, session, Blueprint, json

actor = Blueprint('actor', __name__)


@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor(self, nombre_actores):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    # -- Insertar actor -- #
    actor = base.Actores(nombre_actores)
    db.session.add(actor)
    db.session.commit()

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor(self, id_actores, nombre_nuevo):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    # -- Modificar Actor -- #
    
    if (id_actores == None):
        return False
    else:
        db.session.query(base.Actores).filter(base.Actores.id_actores == id_actores).update({'nombre_actores':(nombre_nuevo)})
        db.session.commit()
        return True


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