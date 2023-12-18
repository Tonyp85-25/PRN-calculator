from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.schemas.calculation import CalculationCreate, CalculationResult
from api.db.repository.calculations import create_new_calculation
from api.db.session import get_db

router = APIRouter()


@router.post("/calculate", response_model=CalculationResult)
def create_calculation(
    calculation: CalculationCreate, session: Session = Depends(get_db)
):
    calculation = create_new_calculation(session, calculation)
    return {"result": calculation.result}
