# -*- coding: utf-8 -*-

# Librerias a importar.
from flask import request, session, Blueprint, json
from app.scrum.funcAccion import clsAccion

pag_actual = 0


accion = Blueprint('accion', __name__)

#.----------------------------------------------------------------------------------------.

@actor.route('/accion/ACrearAcccion', methods=['POST'])
def ACrearAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Accion creada']}, {'label':'/VCrearAccion', 'msg':['Error al crear acccion']}, ]
    res = results[0]

    nuevo_nombre_acciones      = params['nombre']
    nueva_descripcion_acciones = params['descripcion']
    
    nuevaAccion   = clsAccion()
    resultInsert = nuevaAccion.insert_Accion(nombre_acciones, nueva_descripcion_acciones)

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

@actor.route('/accion/AModifAccion', methods=['POST'])
def AModifAccion():
    #POST/PUT parameters
    params = request.get_json()
    print(params)
    results = [{'label':'/VProducto', 'msg':['Accion actualizada']}, {'label':'/VAccion', 'msg':['Error al modificar accion']}, ]
    res = results[0]

    print(str(request.url_rule))

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)


    idaccion = idPila
    nuevo_nombre_acciones = params['nombre']
    nueva_descripcion_acciones= params['descripcion']

    accionModif = clsAccion()
    resultsModif = acccion.Modif.modify_Accion(idaccion, nuevo_nombre_acciones, nueva_descripcion_acciones)

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



@actor.route('/accion/VAccion')
def VAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['idPila'] = 1 

    global pag_actual
    idacciones = int(request.args['idacciones'])
    pag_actual = idacciones
    query = model.db.session.query(model.Acciones).filter_by(idacciones = idacciones).first()
    res['acciones'] =  {'id_acciones':query.idacciones, 'nombre_acciones':query.nombre_acciones}

    #Action code ends here
    return json.dumps(res)


@actor.route('/accion/VCrearAccion')
def VCrearAccion():
    res = {}
    if "accion" in session:
        res['accion']=session['accion']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



#Use case code starts here

