from env import host, user, password
import pandas as pd

def get_data_from_mysql(query, database):

    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'

    return pd.read_sql(query, url)


