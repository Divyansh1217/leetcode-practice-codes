import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person=person.groupby('email').filter(lambda x : len(x)>1).drop_duplicates(subset=['email'])
    return pd.DataFrame({"Email":person['email']})