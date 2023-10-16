#!/usr/bin/python3
"""
Defines the User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
    
        first_name (str): first name
        last_name (str): last name
        email (str): user email
        password (str): user password
       

    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
