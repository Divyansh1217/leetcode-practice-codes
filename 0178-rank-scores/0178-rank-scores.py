import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    data=scores
    data=data.sort_values(by='score',ascending=False)
    data["rank"]=data["score"].rank(method='dense',ascending=False).astype('int')
    return pd.DataFrame({"score":data["score"],"rank":data["rank"]})