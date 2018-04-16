from .meta import Base
from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from cryptacular import bcrypt
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime
)

manager = bcrypt.BCRYPTPasswordManager()


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String)
    registered_on = Column(DateTime, nullable=False)
    admin = Column(Boolean, nullable=False, default=False)

    def __init__(self, username, password, email, admin=False):
        self.username = username
        self.password = manager.encode(password, 10)
        self.email = email
        self.registered_on = dt.now()
        self.admin = admin
