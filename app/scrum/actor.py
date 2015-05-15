# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
import model


actor = Blueprint('actor', __name__)


@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    nombre_actores = params['nombre']

    # -- Insertar actor -- #
    # Booleanos que indican si el tipo es el correcto.
    nombreIsStr = type(nombre_actores) == str

    if (nombreIsStr):
        # Booleanos que indican si cumplen con los limites.
        nombreLenValid = 1 <= len(nombre_actores) <= 50
    
        if (nombreLenValid):

            query = model.db.session.query(model.Actores).filter(model.Actores.nombre_actores == nombre_actores).all()
            print(str(query))
            if (query == []):   
                actor = model.Actores(nombre_actores)
                model.db.session.add(actor)
                model.db.session.commit()
            else:
                res = results[1]
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




@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    # -- Modificar Actor -- #
    #if (id_actores == None):
    #    res = results[1]
    #else:
    nombre_nuevo = params['nombre']
    model.db.session.query(model.Actores).filter(model.Actores.id_actores == idPila).update({'nombre_actores':(nombre_nuevo)})
    model.db.session.commit()
    res = results[0]


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


    id_actores = int(request.args['id_actores'])
    query = model.db.session.query(model.Actores).filter_by(id_actores = id_actores).first()
    res['actor'] =  {'id_actores':query.id_actores, 'nombre_actores':query.nombre_actores}

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