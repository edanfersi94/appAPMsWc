# -*- coding: utf-8 -*-
"""
    UNIVERSIDAD SIMON BOLIVAR
    Departamento de Computacion y Tecnologia de la Informacion.
    CI-3715 - Ingenieria de Software I (CI-3715)
    Abril - Julio 2015

    AUTORES:
        Nicolas Manan.      Carnet: 06-39883
        Edward Fernandez.   Carnet: 10-11121

	DESCRIPCION: Script que contiene los metodos requeridos para trabajar con la tabla
			     "User" de la base de datos dada.
	
"""

#-----------------------------------------------------------------------------------

import data.model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

model=data.model # por comodidad mas que todo
# Se realiza la conexion con la bases de datos para realizar cambios en ella.
DBSession = sessionmaker(bind=data.model.engine)
session = DBSession()

class clsUser():

    def insert_user(self, newFullname, newUsername, newPassword, newEmail):
        """
            @brief Funcion que permite insertar un nuevo usuario a la base de datos.
            
            @param newFullname: Nombre del usuario a insertar.
            @param newUsername: Username del usuario a insertar.
            @param newPassword: Password del usuario a insertar.
            @param newEmail: Email del usuario a insertar.

            @return True si se inserto el usuario dado. De lo contrario False.
        """	
         
        # Verificación de tipo.
        fullnameIsStr = type(newFullname) == str
        usernameIsStr = type(newUsername) == str
        emailIsStr    = type(newEmail) == str

        if (fullnameIsStr and usernameIsStr and emailIsStr):
            # Verificación los limites.
            usernameLenValid = 1 <= len(newUsername) <= 16
            fullnameLenValid = 1 <= len(newFullname) <= 50
            passwordLenValid = 1 <= len(newPassword) <= 16
            emailLenValid = 1 <= len(newFullname) <= 30

            if (usernameLenValid and fullnameLenValid and passwordLenValid and emailLenValid):
                query1 = self.find_username(newUsername)
                query2 = self.find_email(newEmail)

                if (query1 == [] and query2 == []):
                    newUser = model.User(newFullname, newUsername, newPassword, newEmail)
                    session.add(newUser)
                    session.commit()
                    return( True )

        return( False )

    #-----------------------------------------------------------------------
    
    def find_fullname(self, fullname):
        """
            @brief Funcion que realiza la busqueda de los usuarios cuyo nombre sea
                   "fullname"
            
            @param fullname: Nombre de los usuarios a buscar.
            
            @return lista con la consulta solicitada.
        """
        
        fullnameIsStr = type(fullname) == str
        if (fullnameIsStr):
            result = session.query(model.User).filter(model.User.fullname==fullname).all()
            return(result)
            
        return ([])
        
    #--------------------------------------------------------------------
    
    def find_username(self, username):
        """
            @brief Funcion que realiza la busqueda del usuario cuyo username sea
                   "username"
            
            @param username: Username del usuario a buscar.
            
            @return lista con la consulta solicitada.
        """        
        userIsStr = type(username) == str
        if(userIsStr):
            result = session.query(model.User).filter(model.User.username==username).all()
            return(result)
            
        return([])
        
    #--------------------------------------------------------------------
    
    def find_email(self, email):
        """
            @brief Funcion que realiza la busqueda del usuario cuyo email sea
                   "email"
            
            @param email: Correo del usuario a buscar.
            
            @return lista con la consulta solicitada.
        """
        emailIsStr = type(email) == str
        if(emailIsStr):
            result = session.query(model.User).filter(model.User.email==email).all()
            return(result)
            
        return([])
        
    #--------------------------------------------------------------------   

    def modify_fullname(self, username, newFullname):
        """
			@brief Funcion que modifica el nombre de un usuario dado 
                   por "newFullname".
			
			@param username	  : username del usuario a modificar.
			@param newFullname: nuevo nombre para el usuario.
			
			@return True si se modifico el rol dado. De lo contrario False.
		"""
        # Booleanos que indican si el tipo es el correcto.
        usernameIsStr = type(username) == str
        newFullnameIsStr = type(newFullname) == str        
        
        if ( usernameIsStr and  newFullnameIsStr ):
            # Booleanos que indican si cumplen con los limites.
            usernameLenValid = 1 <= len(username) <= 16
            newFullnameLenValid = 1 <= len(newFullname) <= 50

            if ( usernameLenValid and newFullnameLenValid ):
                query = self.find_username(username)
                
                if (query != []) :	
                    session.query(model.User).filter(model.User.username==username).\
                        update({'fullname':(newFullname)})
                    session.commit()
                    return( True )
                    
        return( False )     

    #--------------------------------------------------------------------

    def modify_username(self, oldUsername, newUsername):
        """
			@brief Funcion que modifica el username de un usuario dado 
                   por "newUsername".
			
			@param oldUsername	: username del usuario a modificar.
			@param newNameRole  : nuevo username para el usuario.
			
			@return True si se modifico el rol dado. De lo contrario False.
		"""
		# Booleanos que indican si el tipo es el correcto.
        usernameIsStr = type(username) == str
        newUsernameIsStr = type(newFullname) == str        
        
        if ( usernameIsStr and  newUsernameIsStr ):
            # Booleanos que indican si cumplen con los limites.
            usernameLenValid = 1 <= len(username) <= 16
            newUsernameLenValid = 1 <= len(newFullname) <= 16
            
            if ( usernameLenValid and newUsernameLenValid ):
                query = self.find_username(newUsername)
                
                if (query != []) :	
                    session.query(model.User).filter(model.User.username==oldUsername).\
                        update({'username':(newUsername)})
                    session.commit()
                    return( True )

        return( False )      

    #--------------------------------------------------------------------
        
    def modify_password(self, username, newPassword):
        """
			@brief Funcion que modifica el password de un usuario dado 
                   por "newPassword".
			
			@param username	  : username del usuario a modificar.
			@param newPassword: nueva contraseña para el usuario.
			
			@return True si se modifico el rol dado. De lo contrario False.
		"""
        # Booleanos que indican si el tipo es el correcto.
        usernameIsStr = type(username) == str
        newPasswordIsStr = type(newFullname) == str        
        
        if ( usernameIsStr and  newPasswordIsStr ):
            # Booleanos que indican si cumplen con los limites.
            usernameLenValid = 1 <= len(username) <= 16
            newPasswordLenValid = 1 <= len(newPassword) <= 16
            
            if ( usernameLenValid and newPasswordLenValid ):
                query = self.find_username(username)
                
                if (query != []) :	
                    session.query(model.User).filter(model.User.username==username).\
                        update({'password':(newPassword)})
                    session.commit()
                    return( True )
                    
        return( False )       

    #--------------------------------------------------------------------
    
    def modify_email(self, username, newEmail):
        """
			@brief Funcion que modifica el email de un usuario dado 
                   por "newEmail".
			
			@param username	: username del usuario a modificar.
			@param newEmail : nuevo email para el usuario.
			
			@return True si se modifico el rol dado. De lo contrario False.
		"""
		# Booleanos que indican si el tipo es el correcto.
        usernameIsStr = type(username) == str
        newEmailIsStr = type(newFullname) == str        
        
        if ( usernameIsStr and  newEmailIsStr ):
            # Booleanos que indican si cumplen con los limites.
            usernameLenValid = 1 <= len(username) <= 16
            newEmailLenValid = 1 <= len(newFullname) <= 30
            
            if ( usernameLenValid and newEmailLenValid ):
                query = self.find_email(newEmail)
                
                if (query != []) :	
                    session.query(model.User).filter(model.User.username==username).\
                        update({'email':(newEmail)})
                    session.commit()
                    return( True )

        return( False )     
        

    #--------------------------------------------------------------------    