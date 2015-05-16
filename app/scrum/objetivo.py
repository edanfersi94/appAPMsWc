# -*- coding: utf-8 -*-

# Librerias a importar.
from flask import request, session, Blueprint, json
from app.scrum.funcObjetivo import clsObjetivo

pag_actual = 0


objetivo = Blueprint('objetivo', __name__)


@objetivo.route('/objetivo/ACrearObjetivo', methods=['POST'])
def ACrearObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo creado']}, {'label':'/VCrearObjetivo', 'msg':['Error al crear objetivo']}, ]
    res = results[0]
    
    descripObjetivo = params['descripcion']
    
    nuevoObjetivo   = clsObjetivo()
    resultInsert = nuevoObjetivo.insert_Objetivo(nombre_objetivos, nueva_descripcion_objetivos)

    if ( resultInsert ):
        res = results[0]
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
def AModifObjetivo():
    #POST/PUT parameters
    params = request.get_json()
    results = [{'label':'/VProducto', 'msg':['Objetivo actualizado']}, {'label':'/VObjetivo', 'msg':['Error al modificar objetivo']}, ]
    res = results[0]
    
    #Action code goes here, res should be a list with a label and a message
     

    idPila = 1
    res['label'] = res['label'] + '/' + str(idPila)
    
    id_Objetivo = idPila
    nueva_descripcion_Objetivos = params['descripcion']
    
    objModif = clsObjetivo()
    
    resultsModif = objModif.modify_Objetivo(id_Objetivo, nueva_descripcion_Objetivos)

    if ( resultsModif ):
        res = results[0]
    else:
        res = results[1]

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
        
    res['idPila'] = 1
    #Action code goes here, res should be a JSON structure
    global pag_actual
    id_objetivos = int(request.args['id_objetivos'])
    pag_actual = id_objetivos
    query = model.db.session.query(model.Objetivo).filter_by(id_objetivos = id_objetivos).first()
    res['objetivo'] =  {'id_objetivos':query.id_objetivos, 'nueva_descripcion_Objetivos':query.nueva_descripciones_Objetivos}
    

    #Action code ends here
    return json.dumps(res)


#Use case code starts here

#Use case code ends here