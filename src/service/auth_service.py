from flask import (
    Blueprint,
    request,
    jsonify,
    abort,
    current_app,
    Response,
    redirect,
    url_for,
)

from dao.authDao import AuthDao

class AuthService:
    def __init__(self):
        self.auth_dao = AuthDao()
    
    def login(self, data) -> Response:
        """
        Check user an return login.
        :param data: JSON containing email and password
        :return: A response object for the POST API request.
        """
        email = data['email']
        user = self.auth_dao.get_user(email)
        if user is None:
            response = jsonify(
                {
                    "error": "Email o contraseña incorrectos"
                }
            )
            response.status_code = 401
            return response
        if not self.auth_dao.check_password(user, data['password']):
            response = jsonify(
                {
                    "error": "Email o contraseña incorrectos"
                }
            )
            response.status_code = 401
            return response
        
        token = self.auth_dao.create_token(user)
        response = jsonify(
            {
                "token": token
            }
        )
        response.status_code = 200
        return response
    
    def logout(self, data) -> Response:
        """
        Invalidate user token.
        :param data: JSON containing token
        :return: A response object for the POST API request.
        """
        if not self.auth_dao.invalidate_token(data['token']):
            response = jsonify(
                {
                    "error": "Failed to invalidate token"
                }
            )
            response.status_code = 401
            return response
        
        response = jsonify(
            {
                "message": "Successfully logged out"
            }
        )
        response.status_code = 200
        return response