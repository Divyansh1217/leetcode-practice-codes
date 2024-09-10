import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    cus=pd.merge(customers,orders,left_on='id',right_on='customerId',how='left')
    cus=cus[cus['customerId'].isna()]
    return pd.DataFrame({"Customers":cus['name']})