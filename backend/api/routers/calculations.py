
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from api.schemas.calculation import CalculationCreate, CalculationResult
from api.db.repository.calculations import create_new_calculation, get_all_calculations
from api.db.session import get_db
from api.utils.csv import write_csv_file

router = APIRouter()


@router.post("/calculate", response_model=CalculationResult)
def create_calculation(
    calculation: CalculationCreate, session: Session = Depends(get_db)
):
    calculation = create_new_calculation(session, calculation)
    return {"result": calculation.result}

@router.get("/export", response_class=FileResponse)
async def export_calculations(session: Session = Depends(get_db)):
    calculations = get_all_calculations(session)

    write_csv_file(calculations,"./calculations.csv")
    return FileResponse("./calculations.csv", media_type="text/csv", filename="calculations.csv")
