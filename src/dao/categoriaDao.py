"""
"""

from typing import List

from sqlalchemy.orm import defer

from database import db
from dao.basicDao import BasicDao
from model.databaseModel import Categoria


class CategoriaDao:
    @staticmethod
    def get_categorias() -> List[Categoria]:
        """
        Get a list of all the users in the database.
        :return: A list containing User model objects.
        """
        return Categoria.query.all()
    
    @staticmethod
    def get_categoria_by_descripcion(descripcion: str) -> Categoria:
        """
        Get a single user from the database based on their username.
        :param username: Username which uniquely identifies the user.
        :return: The result of the database query.
        """
        return (
            Categoria.query.filter_by(descripcion=username)
            .filter(Categoria.deleted.is_(False))
            .first()
        )

  