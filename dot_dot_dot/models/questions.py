from .meta import Base
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime
)


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(Text, nullable=False)
    asked_on = Column(DateTime, nullable=False)
