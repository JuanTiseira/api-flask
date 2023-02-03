"""
User routes in the SaintsXCTF API.  Used for retrieving and updating application users.
So much love for you here <3
Author: Andrew Jarombek
Date: 6/16/2019
"""
import re
from datetime import datetime
from typing import List, Optional

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

from sqlalchemy.engine.row import Row
from sqlalchemy.engine.cursor import ResultProxy
from sqlalchemy.exc import SQLAlchemyError

from service.categoria_service import CategoriaService
from dao.categoriaDao import CategoriaDao
 
from decorators import protected

categoria_route = Blueprint("user_route", __name__, url_prefix="/v1/categoria")
categoria_service = CategoriaService()


@categoria_route.route("/", methods=["GET", "POST"])
@protected
def categoria() -> Response:
    """
    Endpoints for searching all the users or creating a uleser
    :return: JSON representation of a list of users and revant metadata
    """
    if request.method == "GET":
        """[GET] /v1/categoria/"""
        response = categoria_service.get_categorias()
        
        return response

    return abort(404)


