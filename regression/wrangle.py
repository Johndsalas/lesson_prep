from env import host, user, password
import pandas as pd
import numpy as np


#***************************Get Data From SQL******************************
def get_data_from_mysql(query, database):

    # create url string from user info and desired database
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'

    # return SQL query using read_sql
    return pd.read_sql(query, url)

#****************************Wrangle Telco Data*****************************

def wrangle_telco():

    query = """ 

        SELECT customer_id, monthly_charges, tenure, total_charges 
        FROM  customers 
            
        JOIN contract_types USING(contract_type_id)
        WHERE contract_type = 'Two Year'
            
        """ 

    # get query results by utilizing get_data_from_mysql function
    df = get_data_from_mysql(query, 'telco_churn')

    # replace space with nan
    df.replace(' ', np.nan, inplace=True)

    # drop rows containing nans in total_charges
    df.dropna(subset= ['total_charges'], inplace=True)

    # recast total charges as float
    df.total_charges = df.total_charges.astype(float)

    # drop customer_id
    df = df.drop(columns=['customer_id'])

    return df