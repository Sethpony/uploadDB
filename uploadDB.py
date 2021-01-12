
'''
    Notes left for next time to pick up:
    https://chrisalbon.com/python/data_wrangling/pandas_dataframe_load_xls/
    https://www.fullstackpython.com/blog/export-pandas-dataframes-sqlite-sqlalchemy.html

    Need to define the data in the tables. So need to look at the columns of the excel sheet and define the data

    use pandas to import the excel file and load as a dataframe with pandas
    And then export the pandas dataframe into sqlite with sqlalchemy

    Might need to possibly set up the developer environment for this

    Idea to use the sneaker API - use Jvscript to download the API data as a CSV then use pandas to upload that csv data into a data frame and then export that pandas dataframe into sqlite using sqlalchemy
'''
import pandas as pd
from pandas import Series, DataFrame
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql://postgres:passy123@localhost:5432/sneaker_app')
df = pd.read_csv('C:/Users/spbac/Documents/dataframetoSQL/stockX.csv', header = 0)

#make dataframe have data types that correlate to the data attributes

#df.to_sql('ShoesSuper', engine)


df.to_sql(name = 'sneaker_model', schema = 'public', con = engine, if_exists = 'append', index = False,
          dtype={
               'Index_ID': sqlalchemy.types.Integer(),
               'Order_Date': sqlalchemy.types.DateTime(),
               'Brand': sqlalchemy.types.String(length = 255),
               'Sneaker_Name': sqlalchemy.types.String(length=255),
               'Sale_Price': sqlalchemy.types.Float(precision = 2, asdecimal=True),
               'Retail_Price': sqlalchemy.types.Float(precision = 2, asdecimal=True),
               'Release_Date': sqlalchemy.types.DateTime(),
               'Shoe_Size': sqlalchemy.types.Float(asdecimal=True),
               'Buyer_Region': sqlalchemy.types.String(length=255)}
        )

print(df.dtypes)
'''
	Index_ID = db.Column(db.Integer, primary_key = True)
	Order_Date = db.Column(db.Date, nullable = False)
	Brand = db.Column(db.String(255), nullable = False)
	Sneaker_Name = db.Column(db.String(255), nullable = False)
	Sale_Price = db.Column(db.Float, nullable = False)
	Retail_Price = db.Column(db.Float, nullable = False)
	Release_Date = db.Column(db.Date, nullable = False)
	Shoe_Size = db.Column(db.Float, nullable = False)
	Buyer_Region = db.Column(db.String(255))
'''

#df.to_sql('ShoesSuper', engine)

#'postgresql://postgres:passy123@localhost:5432/sneaker_app'
conn = psycopg2.connect(host="localhost", database="sneaker_app", user ="postgres", password = "passy123")

#engine.execute("SELECT * FROM ShoesSuper").fetchall()




#Connect and create if DNE? to sqlite3 db
#conn = sqlite3.connect('C:/Users/spbac/Documents/dataframetoSQL/db.sqlite3')

#dframe.to_sql('ShoesSuper', conn, if_exists='replace', index = False)

#pd.read_sql('select * from ShoesSuper', conn)

#PRAGMA table_info(table_name); CHECK TABLE INFO