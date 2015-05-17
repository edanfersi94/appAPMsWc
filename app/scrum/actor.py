# -*- coding: utf-8 -*-

# Librerias a importar.
from flask import request, session, Blueprint, json
from app.scrum.funActor import clsActor

pag_actual = 0


actor = Blueprint('actor', __name__)

#.----------------------------------------------------------------------------------------.

@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[0]

    nuevo_nombre_actores      = params['nombre']
    nueva_descripcion_actores = params['descripcion']
    
    nuevoActor   = clsActor()
    resultInsert = nuevoActor.insert_Actor(nombre_actores, nueva_descripcion_actores)

    if ( resultInsert ):
        res = results[0]
    else:
        res = results[1]

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)

#.----------------------------------------------------------------------------------------.

@actor.route('/actor/AModifActor', methods=['POST'])
def AModifActor():
    #POST/PUT parameters
    params = request.get_json()
    print(params)
    results = [{'label':'/VProducto', 'msg':['Actor actualizado']}, {'label':'/VActor', 'msg':['Error al modificar actor']}, ]
    res = results[0]

    print(str(request.url_rule))

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    print(pag_actual)

    id_actor = idPila
    nuevo_nombre_actores = params['nombre']
    nueva_descripcion_actores = params['descripcion']

    actorModif = clsActor()
    resultsModif = actorModif.modify_Actor(id_actor, nuevo_nombre_actores, nueva_descripcion_actores)

    if ( resultsModif ):
        res = results[0]
    else:
        res = results[1]

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

    global pag_actual
    id_actores = int(request.args['id_actores'])
    pag_actual = id_actores
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

