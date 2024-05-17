from database import Base
from sqlalchemy import Column, String, Integer, BigInteger


class Student(Base):
    __tablename__ = "student"

    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    clas = Column(Integer)
