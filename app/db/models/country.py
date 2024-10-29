from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.models import Base


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    region = Column(String)
    capital = Column(String)
    name = Column(String)

    vacations = relationship("StudentVacation", back_populates="countries",lazy="joined")
