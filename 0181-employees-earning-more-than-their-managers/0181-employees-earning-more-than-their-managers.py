import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    data=employee.merge(right=employee,how='inner',left_on='managerId',right_on='id')
    s=data[data['salary_x']>data['salary_y']]['name_x']
    return pd.DataFrame({'Employee':s})