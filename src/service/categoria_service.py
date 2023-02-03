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
from dao.categoriaDao import CategoriaDao




class CategoriaService:
    def __init__(self):
        self.categoria_dao = CategoriaDao()
    
    def get_categorias(self) -> Response:
        """
        Retrieve all the categories in the database.
        :return: A response object for the GET API request.
        """
        all_categorias = self.categoria_dao.get_categorias()
        if all_categorias is None:
            response = jsonify(
                {
                    "self": "/v1/categoria",
                    "categorias": None,
                    "error": "ocurrio un error al retornar las categorias",
                }
            )
            response.status_code = 500
            return response

        categoria_dicts = []
        for categoria_data in all_categorias:
            d = {
                "id": categoria_data.id,
                "codigo": categoria_data.codigo,
                "nombre": categoria_data.descripcion
            }
            categoria_dicts.append(d)            
        response = jsonify(categorias=categoria_dicts)
        response.status_code = 200
        return response
    