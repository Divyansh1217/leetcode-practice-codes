import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    data=logs
    data["num1"]=data["num"].shift(-1)
    data['num2']=data["num"].shift(-2)
    z=(data['num']==data['num1']) & (data['num']==data['num2'])
    z=data.loc[z,'num'].unique()
    return pd.DataFrame({"ConsecutiveNums":z})

