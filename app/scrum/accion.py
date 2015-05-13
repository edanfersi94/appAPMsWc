# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json

accion = Blueprint('accion', __name__)

from model import *
minIdAccion   = 0
maxDescripAcciones = 50

@accion.route('/accion/ACrearAccion', methods=['POST'])
def ACrearAccion(self,idacciones,descripAcciones):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Acción creada']}, {'label':'/VCrearAccion', 'msg':['Error al crear acción']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message
    id_accion = Acciones.query.filter_by(idacciones = idacciones).all()
    newAcciones = Acciones(idacciones = idacciones, descripAcciones = descripAcciones)
    if  type(idacciones) != int:
        return False
    if type(descripAcciones) != str:
        return False
    else:
        long_descriAcciones =len(newAcciones.descriAcciones)
        if (type(idacciones) == str or newAcciones.idacciones == None or newAccion.id_accion <= minIAccion or newAcciones.descriAcciones == '' or long_descriAcciones > maxDescripAcciones):
                    return False
        else:
                    db.session.add(newAcciones)
                    db.session.commit()
                    return True
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

    res['idPila'] = 1 

    #Action code ends here
    return json.dumps(res)



@accion.route('/accion/VCrearAccion')
def VCrearAccion():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here