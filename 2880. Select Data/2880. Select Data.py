import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[["name","age"]].where(students["student_id"]==101).dropna()
