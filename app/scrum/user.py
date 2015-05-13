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

#------------------------------------------------------------------------------------

# Librerias a utilizar.

from model import *

#-------------------------------------------------------------------------------

# Se realiza la conexion con la bases de datos para realizar cambios en ella.

class clsUser():

    def insert_user(self, newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole):
        """
            @brief Funcion que permite insertar un nuevo usuario a la base de datos.
            
            @param newFullname: Nombre del usuario a insertar.
            @param newUsername: Username del usuario a insertar.
            @param newPassword: Password del usuario a insertar.
            @param newEmail: Email del usuario a insertar.
            @param newIdRole: Id del rol del usuario a insertar.
            @param newIdDpt: Id del departamento del usuario a insertar.
            
            @return True si se inserto el usuario dado. De lo contrario False.
        """	
            
        newUser = User(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
        db.session.add(newUser)
        db.session.commit()

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
            result = db.session.query(User).filter(User.fullname==fullname).all()
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
            result = db.session.query(User).filter(User.username==username).all()
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
            result = db.session.query(User).filter(User.email==email).all()
            return(result)
            
        return([])
        
    #--------------------------------------------------------------------   
        
    def find_idDpt(self, idDpt):
        """
            @brief Funcion que realiza la busqueda de los usuarios cuyo id del dpt sea
                   "idDpt"
            
            @param idDpt: Id del departamento de los usuarios a buscar.
            
            @return lista con la consulta solicitada.
        """        
        idDptIsInt = type(idDpt) == int
        if(idDptIsInt):
            result = db.session.query(User).filter(User.iddpt==idDpt).all()
            return(result)
            
        return([])
        
    #--------------------------------------------------------------------
        
    def find_idRole(self, idRole):
        """
            @brief Funcion que realiza la busqueda de los usuarios cuyo id del rol sea
                   "idRol"
            
            @param idRol: Id del rol de los usuarios a buscar.
            
            @return lista con la consulta solicitada.
        """     
                   
        idRoleIsInt = type(idRole) == int
        if(idRoleIsInt):
            result = db.session.query(User).filter(User.idrole==idRole).all()
            return(result)
            
        return ([])
        
    #--------------------------------------------------------------------
    
    def find_listFullname(self):
        """
            @brief Funcion que devuelve los nombres de los diferentes 
            usuarios que se encuentran almacenados en la base de 
            datos.
            
            @param no admite parametros.
            
            @return lista con la consulta solicitada.
        """
     
        result = db.session.query(User.fullname.label('name')).all()
        return(result)

    #--------------------------------------------------------------------
    
    def find_listUsername(self):
        """
        @brief Funcion que devuelve los usernames de los diferentes 
            usuarios que se encuentran almacenados en la base de 
            datos.
            
            @param no admite parametros.
            
            @return lista con la consulta solicitada.
        """
        result = db.session.query(User.username.label('user')).all()
        return(result)

    #--------------------------------------------------------------------
       
    def find_listEmail(self):
        """
            @brief Funcion que devuelve los emails de los diferentes 
            usuarios que se encuentran almacenados en la base de 
            datos.
            
            @param no admite parametros.
            
            @return lista con la consulta solicitada.
        """
        result = db.session.query(User.email.label('email')).all()
        return(result)

    #--------------------------------------------------------------------

    def find_listIdDpt(self):
        """
            @brief Funcion que devuelve los id de los diferentes 
            departamentos almacenados en la base de datos.
            
            @param no admite parametros.
            
            @return lista con la consulta solicitada.
        """
        result = db.session.query(User.iddpt.label('dpt')).all()
        return(result)

    #--------------------------------------------------------------------
    
    def find_listIdRole(self):
        """
            @brief Funcion que devuelve los id de los diferentes 
            roles almacenados en la base de datos.
            
            @param no admite parametros.
            
            @return lista con la consulta solicitada.
        """
        result = db.session.query(User.idrole.label('role')).all()
        return(result)

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
                query1 = self.find_username(username)
                
                if (query1 != []) :	
                    db.session.query(User).filter(User.username==username).\
                    update({'fullname':(newFullname)})
                    db.session.commit()
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
                query1 = self.find_username(username)
                
                if (query1 != []) :	
                    db.session.query(User).filter(User.username==oldUsername).\
                    update({'username':(newUsername)})
                    db.session.commit()
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
                query1 = self.find_username(username)
                
                if (query1 != []) :	
                    db.session.query(User).filter(User.username==username).\
                    update({'password':(newPassword)})
                    db.session.commit()
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
                query1 = self.find_username(username)
                
                if (query1 != []) :	
                    db.session.query(User).filter(User.username==username).\
                    update({'email':(newEmail)})
                    db.session.commit()
                    return( True )

        return( False )     
        
    #--------------------------------------------------------------------                       
    
    def modify_idDpt(self, username, newIdDpt):
        """
			@brief Funcion que modifica el id del dpt de un usuario dado 
                   por "newIdDpt".
			
			@param username	  : username del usuario a modificar.
			@param newIdDpt   : nuevo id del dpt para el usuario.
			
			@return True si se modifico el rol dado. De lo contrario False.
		"""
		# Booleanos que indican si el tipo es el correcto.
        usernameIsStr = type(username) == str
        newIdDptIsInt = type(newFullname) == int        
        
        if ( usernameIsStr and  newFullnameIsStr ):
            # Booleanos que indican si cumplen con los limites.
            usernameLenValid = 1 <= len(username) <= 16
            newIdDptIsPositive = newIdDpt > 0
            
            if ( usernameLenValid and newIdDptIsPositive ):
                query1 = self.find_username(username)
                query2 = self.find_idDpt(newIdDpt)
                
                if (query1 != [] and query2 != []) :	
                    db.session.query(User).filter(User.username==username).\
                    update({'iddpt':(newIdDpt)})
                    db.session.commit()
                    return( True )

        return( False )                         
        
    #--------------------------------------------------------------------    
    
    def modify_idRole(self, username, newIdRole):
        """
			@brief Funcion que modifica el id del role de un usuario dado 
                   por "newIdRole".
			
			@param username	  : username del usuario a modificar.
			@param newIdRole  : nuevo id del rol para el usuario.
			
			@return True si se modifico el rol dado. De lo contrario False.
		"""
 		# Booleanos que indican si el tipo es el correcto.
        usernameIsStr = type(username) == str
        newIdRoleIsInt = type(newFullname) == int        
        
        if ( usernameIsStr and  newFullnameIsStr ):
            # Booleanos que indican si cumplen con los limites.
            usernameLenValid = 1 <= len(username) <= 16
            newIdRoleIsPositive = newIdRole > 0
            
            if ( usernameLenValid and newIdRoleIsPositive ):
                query1 = self.find_username(username)
                query2 = self.find_idDpt(newIdRole)
                
                if (query1 != [] and query2 != []) :	
                    db.session.query(User).filter(User.username==username).\
                    update({'idrole':(newIdRole)})
                    db.session.commit()
                    return( True )
        
        return( False )                    

    #--------------------------------------------------------------------

    def delete_username(self, username):
        """
            @brief Funcion que elimina el usuario cuyo nombre de usuario 
            sea "username".
            
            @param username: Identificador del usuario a eliminar.
            
            @return True si elimina el usuario dado. De lo contrario False.
        """       
        usernameIsString = type(username) == str
        
        if( usernameIsString ):
            query = self.find_username( username ) 
        
        if ( query != []):
            db.session.query(User).filter(User.username==username).delete()
            db.session.commit()
            return( True )
        
        return( False )

    #--------------------------------------------------------------------