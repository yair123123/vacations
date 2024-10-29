
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.models import Base


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    favorite_language = Column(String)
    favorite_framework = Column(String)

    vacations = relationship("StudentVacation", back_populates="students",lazy="joined")
