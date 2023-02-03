from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import defer
from database import db
from dao.basicDao import BasicDao
import bcrypt
from model.databaseModel import User , Token
import datetime
import jwt
import os

class AuthDao:

    def get_user(self, email):
        """
        Retrieve user from database based on email
        :param email: user email
        :return: User object or None if not found
        """
        user = User.query.filter(User.email == email).first()
        return user
    
    def check_password(self,user, password):
        """
        Check if the provided password matches the hashed password in the database
        :param user: User object
        :param password: plain text password
        :return: Boolean indicating match
        """
        # hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        # print(hashed_password)
        
        return bcrypt.checkpw(password.encode(), user.password.encode())
    
    def create_token(self, user):
        """
        Create a JWT token
        :param user: User object
        :return: JWT token
        """
        payload = {
            'sub': user.id,
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)
        }
        token = jwt.encode(payload, os.environ['JWT_SECRET'], algorithm='HS256')
        
        db.session.add(Token(user.id, token))
        BasicDao.safe_commit()
        return token

    def invalidate_token(self, token):
        """
        Invalidate JWT token
        :param token: JWT token
        :return: Boolean indicating success
        """
        try:
            jwt.decode(token, os.environ['JWT_SECRET'], algorithms=['HS256'])
            # Invalidate token in database
            db.session.query(Token).filter(Token.token == token).delete()
            BasicDao.safe_commit()
            return True
        except jwt.ExpiredSignatureError:
            return False
        except jwt.exceptions.DecodeError:
            return False