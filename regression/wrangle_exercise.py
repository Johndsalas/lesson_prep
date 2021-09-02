##################################################Wrangle.py###################################################

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

from env import user, password, host

#**************************************************Acquire*******************************************************

def acquire_zillow():
    
    url = f"mysql+pymysql://{user}:{password}@{host}/zillow"
    
    query = """
            
    SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
    FROM properties_2017

    LEFT JOIN propertylandusetype USING(propertylandusetypeid)

    WHERE propertylandusedesc IN ("Single Family Residential",                       
                                  "Inferred Single Family Residential")"""

    # get dataframe of data
    df = pd.read_sql(query, url)
    
    
    # renaming column names to one's I like better
    df = df.rename(columns = {'bedroomcnt':'bedrooms', 
                              'bathroomcnt':'bathrooms', 
                              'calculatedfinishedsquarefeet':'area',
                              'taxvaluedollarcnt':'tax_value', 
                              'yearbuilt':'year_built',
                              'taxamount':'tax_amount'})
    return df

#**************************************************Distributions*******************************************************

def get_hist(df):
    
    plt.figure(figsize=(16, 3))

    # List of columns
    cols = [col for col in df.columns if col not in ['fips', 'year_built']]

    for i, col in enumerate(cols):

        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1, len(cols), plot_number)

        # Title with column name.
        plt.title(col)

        # Display histogram for column.
        df[col].hist(bins=5)

        # Hide gridlines.
        plt.grid(False)
        
        
def get_box(df):
    
    plt.figure(figsize=(8,4))

    sns.boxplot(data=df.drop(columns=['fips', 'year_built']))
    plt.show()
        
#**************************************************Prepare*******************************************************

def prepare_zillow(df):
    
    # drop rows that are nulls 
    df = df.dropna(subset = ['bedrooms','bathrooms', 'year_built', 'tax_value'])
    
    # drop taxamount
    df = df.drop(columns = 'tax_amount')
    
    # converting column datatypes
    df.fips = df.fips.astype(str)
    df.year_built = df.year_built.astype(str)
    df.bedrooms = df.bedrooms.astype(int)
    
    # train/validate/test split
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)
    
    # impute median value 
    imputer = SimpleImputer(strategy='median') 

    imputer.fit(train[['area']])

    train[['area']] = imputer.transform(train[['area']])        
    validate[['area']] = imputer.transform(validate[['area']])  
    test[['area']] = imputer.transform(test[['area']])          
    
    return train, validate, test    

#**************************************************Wrangle*******************************************************

def wrangle_zillow():
    
    train, validate, test = prepare_zillow(acquire_zillow())
    