from sqlalchemy import Column, Date, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class StudentVacation(Base):
    __tablename__ = "studentVacation"
    id = Column(Integer, primary_key=True, autoincrement=True)
    start_vacation = Column(Date, nullable=False)
    end_vacation = Column(Date, nullable=False)
    student_id = Column(Integer, ForeignKey("students.id"))
    country_id = Column(Integer, ForeignKey("countries.id"))

    students = relationship("Student", back_populates="vacations",lazy="joined")
    countries = relationship("Country", back_populates="vacations",lazy="joined")
