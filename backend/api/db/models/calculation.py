from api.db.base_class import Base
from sqlalchemy import Column, String, Integer


class Calculation(Base):
    id = Column(Integer, primary_key=True)
    expression = Column(String, nullable=False)
    result = Column(String, nullable=False)
