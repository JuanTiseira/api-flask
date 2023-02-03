"""
"""

import functools
import asyncio
from typing import List, Optional
import aiohttp
from flask import abort, current_app, request
import jwt
from flask import request, jsonify
import os
from utils.literals import HTTPMethod
from model.databaseModel import User , Token
import datetime


def protected(func):
    def wrapper(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            
        if not token:
            
            return jsonify({'error': 'Token is missing'}), 401
        
        try:
            payload = jwt.decode(token, os.environ['JWT_SECRET'], algorithms=['HS256'])
            expires = payload.get("exp")
            print(expires)
            token_record = Token.query.filter_by(token=token).first()
            if not token_record:
                return jsonify({'error': 'Token is invalid'}), 401
            
            user = User.query.filter_by(id=token_record.user_id).first()
            
            if not user:
                return jsonify({'error': 'Token is invalid user'}), 401
            
            if expires is None:
                raise credentials_exception
            # if datetime.datetime.utcnow() > expires:
            #     raise credentials_exception
            
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired'}), 401
        
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token is invalid'}), 401
        # Continue with the endpoint logic
        
        return func(*args, **kwargs)
    return wrapper
