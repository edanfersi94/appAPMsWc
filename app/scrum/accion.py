# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
import model


accion = Blueprint('accion', __name__)


@accion.route('/accion/ACrearAccion', methods=['POST'])
def ACrearAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción creada']}, {'label':'/VCrearAccion', 'msg':['Error al crear acción']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    descripAcciones =  params['descripcion']

    descripAccionesStr = type(descripAcciones) == str
    
    if (descripAccionesStr):
        descripAccionesLenValido = 1<= len(descripAcciones) <=500

        if(descripAccionesLenValido):

            nuevaAccion = model.Acciones(descripAcciones)
            model.db.session.add(nuevaAccion)
            model.db.session.commit() 
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


@accion.route('/accion/AModifAccion', methods=['POST'])
def AModifAccion():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción actualizada']}, {'label':'/VAccion', 'msg':['Error al modificar acción']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    
    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)

    descripAccionesStr = type(descripAcciones) == str
    if (descripAccionesStr):
        descripAccionesLenValido = 1<= len(descripAcciones) <=500

        if(descripAccionesLenValido):

            db.session.query(Acciones).filter(Acciones.idacciones==idPila)
            update({'descripAcciones':(descripAcciones)})
            db.session.commit()
            res = results[0]

        else:
            res = results[1]

    else:
        res = results[1]  

    

    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)


@accion.route('/accion/VAccion')
def VAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure
    
    idacciones = int(request.args['idacciones'])
    acc = Acciones.query.filter_by(idacciones = idacciones).first()
    res['acciones'] = [{'idacciones':acc.idacciones, 'descripAcciones':acc.descripAcciones}
                    for acc in acc.DescripAcciones]
    res['fAccion'] = {'idacciones':idacciones, 'descripAcciones':'DescripAcciones'}
    
    res['idPila'] = 1 

    #Action code ends here
    return json.dumps(res)



@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']

    return json.dumps(res)
