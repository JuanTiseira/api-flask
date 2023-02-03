from flask import Blueprint, request, jsonify
from service.auth_service import AuthService
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

auth_route = Blueprint("auth_route", __name__)

@auth_route.route("/login", methods=["POST"])
def login() -> Response:
    """
    Endpoint for user login
    :return: JSON representation of a token and relevant metadata
    """
    
    auth_service = AuthService()
    if request.method == "POST":
        """ [POST] /v1/auth/login """
        request_data = request.get_json()
        
        return auth_service.login(request_data)
    return abort(404)


@auth_route.route("/logout", methods=["POST"])
def logout() -> Response:
    """
    Endpoint for user logout
    :return: JSON representation of a message
    """
    auth_service = AuthService()
    if request.method == "POST":
        """ [POST] /v1/auth/logout """
        data = request.get_json()
        # print(data)
        return auth_service.logout(data)
        
    return abort(404)