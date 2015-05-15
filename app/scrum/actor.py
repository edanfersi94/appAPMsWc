# -*- coding: utf-8 -*-
import model
from flask import request, session, Blueprint, json

actor = Blueprint('actor', __name__)

print("inicial")

@actor.route('/actor/ACrearActor', methods=['POST'])
def ACrearActor(self, nombre_actores):
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Actor creado']}, {'label':'/VCrearActor', 'msg':['Error al crear actor']}, ]
    res = results[0]
    #Action code goes here, res should be a list with a label and a message

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
        model.db.session.query(model.Actores).filter(model.Actores.id_actores == id_actores).update({'nombre_actores':(nombre_nuevo)})
        model.db.session.commit()
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

'''@art.route('/art/VArticulos')
def VArticulos():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure

    articulos = Articulo.query.all()
    if len(articulos)==0:
      art1 = Articulo('El pasado', 'Ya se fué, ya no importa.', 'Leo')
      art2 = Articulo('El presente', '¿Ya fue, es ahora o será pronto?', 'Leo')
      db.session.add(art1)
      db.session.add(art2)
      db.session.commit()
      articulos = Articulo.query.all()
    res['data0'] = [
      {'idArticulo':art.idArticulo, 'titulo':art.titulo, 'autor':art.autor}
      for art in articulos]
  

    #Action code ends here
    return json.dumps(res)
'''


@actor.route('/actor/VCrearActor')
def VCrearActor():
    res = {}
    if "actor" in session:
        res['actor']=session['actor']
    #Action code goes here, res should be a JSON structure


    #Action code ends here
    return json.dumps(res)