#DB_connection

#funzioni per la connessione al db locale

#importa i moduli necessari
from sqlalchemy import *
import config as cfg
import pandas as pd
#import psycopg2


#formato della connection string:
#postgresql://[user[:password]@][netloc][:port][/dbname]

#recupera i parametri da config.py
user=cfg.postgres['user']
password=cfg.postgres['password']
host=cfg.postgres['host']
port=cfg.postgres['port']
dbname=cfg.postgres['dbname']

conn_str = f"""postgresql://{user}:{password}@{host}:{port}/{dbname}"""

#crea l'engine
def create_conn(conn_str):
    engine = create_engine(conn_str)
    connection = engine.connect()
    return connection

#crea la connessione+scrive i records del DataFrame nel db
def connect_db (df,table_name):
    connection=create_conn(conn_str)
    #metadata = MetaData()---->A COSA SERVE?
    nb_row=df.to_sql(table_name, con=connection,if_exists='append',method='multi',chunksize=10000,index=False)
    connection.close()
    return nb_row

#interroga il db e stampa il numero di righe affette dalla query
def count_row_from_db(df,table_name):
    connection = create_conn(conn_str)
    #connection.autocommit = True----->A COSA SERVE?
    print (f"""Tabella {table_name}:""")
    #print()
    try:
        for column in df.columns:
            sql_query=f"""SELECT COUNT({column}) FROM {table_name}"""
            results=connection.execute(sql_query)
            print (f"""Nr righe non nulle per {column} = {results.fetchall()[0][0]}
                    """) 
    except AttributeError:
        sql_query=f"""SELECT COUNT(*) FROM {table_name}"""
        results=connection.execute(sql_query)
        print (f"""Nr righe non nulle = {results.fetchall()[0][0]}""") 
    print()
    connection.close()
    
    
    
    
    
    
    
    
    
    
