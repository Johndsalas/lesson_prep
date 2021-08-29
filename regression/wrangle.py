from env import host, user, password
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns


#***************************Get Data From SQL******************************
def get_data_from_mysql(query, database):
    '''Takes in a SQL query and a database name
       Returns the results of the SQL query using the input database'''

    # create url string from user info and desired database
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'

    # return SQL query using read_sql
    return pd.read_sql(query, url)

#****************************Wrangle Telco Data*****************************

def wrangle_telco():
    ''' Acquires and cleans Telco data'''

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

#***************************Graphs*****************************

def histographs(df):
    '''Get histographs of preped Telco data'''

    plt.figure(figsize=(16, 3))

    # List of columns
    cols = df.columns

    for i, col in enumerate(cols):

        # i starts at 0, but plot should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1,4, plot_number)

        # Title with column name.
        plt.title(col)

        # Display histogram for column.
        df[col].hist(bins=5)

        # Hide gridlines.
        plt.grid(False)


def boxplots(df):
    '''Get boxplots of preped Telco data'''

    # List of columns
    cols = df.columns

    for i, col in enumerate(cols):

        # i starts at 0, but plot should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1,3, plot_number)

        # Title with column name.
        plt.title(col)

        # Display histogram for column.
        sns.boxplot(data=df[[col]])

        # Hide gridlines.
        plt.grid(False)
        
        # sets proper spacing between plots
        plt.tight_layout()