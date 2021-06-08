
def get_db_url(db):

    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'


def get_data_from_mysql(database, query):

    return pd.read_sql(query, get_db_url(f'{database}'))

get_data_from_mysql('employees','select * from employees')
