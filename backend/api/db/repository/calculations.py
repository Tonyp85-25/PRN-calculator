from sqlalchemy.orm import Session

from api.core.calculator import Calculator
from api.db.models.calculation import Calculation
from api.schemas.calculation import CalculationCreate


def create_new_calculation(session: Session, calculation: CalculationCreate):
    calculation = Calculation(
        expression=calculation.expression,
        result=Calculator.calculate(calculation.expression),
    )
    session.add(calculation)
    session.commit()
    session.refresh(calculation)
    return calculation

def get_all_calculations(session: Session):
    calculations = session.query(Calculation).all()
    return calculations
