from typing_extensions import Annotated
from pydantic import BaseModel, Field, BeforeValidator

operators_map = {"+": 1, "-": 1, "*": 1, "/": 1, "^": 1}


def check_expression_length(expression: str):
    if len(expression) < 4:
        raise ValueError("Expression is too short")
    return expression


def check_symbols_presence(expression: str):
    split_expression = expression.split()
    operators = 0
    numbers = 0
    for symbol in split_expression:
        if operators_map.get(symbol):
            operators += 1
        if symbol.isdigit():
            numbers += 1
    if numbers - operators != 1:
        raise ValueError("Expression is invalid")
    return expression


CalculationExpression = Annotated[
    str,
    BeforeValidator(check_expression_length),
    BeforeValidator(check_symbols_presence),
]


class CalculationCreate(BaseModel):
    expression: CalculationExpression


class CalculationResult(BaseModel):
    result: str = Field(example="4")

class CalculationFull(BaseModel):
    expression: CalculationExpression
    result: CalculationResult
