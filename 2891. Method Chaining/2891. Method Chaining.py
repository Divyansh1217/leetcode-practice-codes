import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    df=animals.where(animals['weight']>100).dropna().sort_values(by='weight',ascending=False)
    return df[['name']]
