# -*- coding: utf-8 -*-

# Funci�n a importar.
import model

# Numero de acciones creados en la base de datos.
num_acciones   = 0

# Clase que tendra las diferentes funcionalidades de la tabla "Acciones".
class clsAccion():

    #-------------------------------------------------------------------------------
    
    def insert_Accion(self, newNameAccion,newDescripAccion):
        """
            @brief Funcion que permite insertar una nueva accion en la base de datos.
            
            @param newNameAccion     : Nombre de la accion a insertar.
            @param newDescripAccion     : Descripcion de la accion a insertar.

            @return True si se inserto la accion dada. De lo contrario False.
        """
        
        global num_acciones

        # Booleanos que indican si el tipo es el correcto.
        descripIsStr = type(newDescripAccion) == str
        nameIsStr = type(newNameAccion) == str
    
        if ( nameIsStr and descripIsStr):

            # Booleanos que indican si cumplen con los limites.
            nameLenValid = 1 <= len(newNameAccion) <= 50
            descripLenValid = 1 <= len(newDescripAccion) <= 500
        
            if (nameLenValid and descripLenValid):
                query = self.find_nameAccion(newNameAccion)

                if ( query == [] ):
                    num_acciones = num_acciones + 1
                    newActor = model.Acciones(num_acciones,newNameAccion, newDescripAccion)
                    model.db.session.add(newAccion)
                    model.db.session.commit()
                    return( True )
        
        return( False )
        
    #-------------------------------------------------------------------------------
    
    def find_idAccion(self, idAccion):
        """
            @brief Funcion que realiza la busqueda de la accion cuyo identificador
                   sea "idAccion".
            
            @param idAccion: Identificador de la accion a buscar.
            
            @return lista que contiene las tuplas obtenidas del subquery. De lo 
                    contrario retorna la lista vacia.
        """
        
        idIsInt = type(idAccion) == int
        
        if ( idIsInt ):
            accionesEsp = model.Acciones.idacciones == idAccion
            query = model.db.session.query(model.Acciones).filter(accionesEsp).all()
            return( query )
        return( [] )
    
    #-------------------------------------------------------------------------------

    def find_nameAccion(self, nameAccion):
        """
            @brief Funcion que realiza la busqueda de las acciones cuyo identificador
                   sea "nameAccion".
                   
            @param nameActor: Nombre del actor a buscar.
            
            @return lista que contiene las tuplas obtenidas del subquery. De lo 
                    contrario retorna la lista vacia.
        """

        nameIsStr = type(nameActor) == str
        
        if ( nameIsStr ):
            actoresEsp = model.Actores.nombre_actores == nameActor
            query = model.db.session.query(model.Acciones).filter(accionesEsp).all()
            return( query )
        return( [] )
        
    #-------------------------------------------------------------------------------

    def modify_Actor(self, idAccion, newNameAccion, newDescripAccion):
        """
            @brief Funcion que modifica los datos de la accion cuyo id sea "idAccion".
            
            @param idAccion         : id de la accion a modificar.
            @param newNameAcccion     : nuevo nombre para la accion dada.
            @param newDescripAccion  : nueva descripcion para la accion dada.
            
            @return True si se modifico la accion dada. De lo contrario False.
        """
        
        # Booleanos que indican si el tipo es el correcto.
        nameIsStr      = type(newNameAccion) == str
        descripIsStr = type(newDescripAccion) == str
        idIsInt      = type(idAccion) == int
        
        if ( nameIsStr and  idIsInt and descripIsStr ):
            # Booleanos que indican si se cumplen los limites.
            nameLenValid     = 1 <= len(newNameAccion) <= 50
            idIsPositive     = idAccion > 0
            descripLenValid = 1 <= len(newNameAccion) <= 500
            
            if ( nameLenValid and idIsPositive and descripLenValid ):
                query1 = self.find_idAccion(idAccion)
                query2 = self.find_nameAccion(newNameAccion)
                
                if (( query1 != [] ) and ( query2 == [])):
                    actores = model.Acciones.id_acciones == idAccion
                    model.db.session.query(model.Acciones).filter(acciones).\
                        update({'nombre_acciones':(newNameAccion),'descripcion_accciones':(newDescripAccion)})
                    model.db.session.commit()
                    return( True )
                    
        return( False )
    
    #--------------------------------------------------------------------------------    
