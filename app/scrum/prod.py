# -*- coding: utf-8 -*-
from flask import request, session, Blueprint, json
import model

prod = Blueprint('prod', __name__)


@prod.route('/prod/ACrearProducto', methods=['POST'])
def ACrearProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto creado']}, {'label':'/VCrearProducto', 'msg':['Error al crear producto']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/AModifProducto', methods=['POST'])
def AModifProducto():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProductos', 'msg':['Producto actualizado']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message


    #Action code ends here
    if "actor" in res:
        if res['actor'] is None:
            session.pop("actor", None)
        else:
            session['actor'] = res['actor']
    return json.dumps(res)



@prod.route('/prod/VCrearProducto')
def VCrearProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)



@prod.route('/prod/VProducto')
def VProducto():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    actores = model.Actores.query.all()
    acciones = model.Acciones.query.all()
    objetivos = model.Objetivo.query.all()
    idPila = int(request.args.get('idPila', 1))
    pilas = [{'idPila':1, 'nombre':'Pagos en línea', 'descripcion':'Pagos usando tarjeta de débito'}, {'idPila':2, 'nombre':'Recomendaciones de playas', 'descripcion':'Red social para playeros consumados'}, {'idPila':3, 'nombre':'Tu taxi seguro', 'descripcion':'Toma un taxi privado de forma segura'}, ]
    res['fPila'] = pilas[idPila-1]
    res['data3'] = [
        {'idActor':act.id_actores, 'descripcion':act.nombre_actores}
        for act in actores]
    res['data5'] = [
        {'idAccion':acc.idacciones, 'descripcion':acc.descripAcciones}
         for acc in acciones]
    res['data7'] = [
        {'idObjetivo':obj.idObjetivo, 'descripcion':obj.descripObjetivo}
         for obj in objetivos]
    res['idPila'] = idPila    

    #Action code ends here
    return json.dumps(res)



@prod.route('/prod/VProductos')
def VProductos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    res['data0'] = [{'idPila':1, 'nombre':'Pagos en línea'}, {'idPila':2, 'nombre':'Recomendaciones de playas'}, {'idPila':3, 'nombre':'Tu taxi seguro'}, ]

    #Action code ends here
    return json.dumps(res)





#Use case code starts here


#Use case code ends here