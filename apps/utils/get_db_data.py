from sqlalchemy import create_engine
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from apps.config.constants import POSTGRES_USER,POSTGRES_PASSWD,POSTGRES_HOST,POSTGRES_PORT,POSTGRES_DB


def run_sql_query(query):
    print(POSTGRES_PORT)
    engine = create_engine(f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")
    with engine.connect() as conn:
        print(query)
        df = pd.read_sql(query,conn)
        return df.to_markdown(index=False)
        ##print(df)


def main():
    query = 'select * from incentive_plans'
    df=run_sql_query(query)
    print(df)

if __name__ == '__main__':
    main()