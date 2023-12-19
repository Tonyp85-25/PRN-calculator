from typing import List
import csv

from api.schemas.calculation import CalculationFull

def write_csv_file(calculations:List[CalculationFull] ,file:str): 

    with open(file, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Expression', 'Result'])
        for calculation in calculations:
            filewriter.writerow([calculation.expression, calculation.result])
  
   