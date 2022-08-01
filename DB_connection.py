#DB_connection

#funzioni per la connessione al db locale

#importa i moduli necessari
from sqlalchemy import *
import config as cfg
import pandas as pd
import psycopg2


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
def connect_db (df,dfname):
    connection=create_conn(conn_str)
    #metadata = MetaData()---->A COSA SERVE?
    nb_row=df.to_sql(dfname, con=connection,if_exists='append',method='multi',chunksize=10000,index=False)
    connection.close()
    return nb_row


#interroga il db e stampa il numero di righe affette dalla query
def count_row_from_db(df,table_name):
    connection = psycopg2.connect(conn_str)
    #connection.autocommit = True----->A COSA SERVE?
    print (f"""Tabella {table_name}:""")
    for column in df.columns:
        sql_query=f"""SELECT {column} FROM {table_name} WHERE {column} IS NOT NULL"""
        cursor = connection.cursor()
        cursor.execute(sql_query)
        print (f"""Nr righe non nulle per {column} = {cursor.rowcount}""")
    cursor.close()
    connection.close()


 
#interroga il db e stampa il numero di righe affette dalla query
def count_row_from_db3(df,table_name):
    connection = create_conn(conn_str)
    #connection.autocommit = True----->A COSA SERVE?
    print (f"""Tabella {table_name}:""")
    for column in df.columns:
        sql_query=f"""SELECT {column} FROM {table_name} WHERE {column} IS NOT NULL"""
        results=connection.execute(sql_query)
        print (f"""Nr righe non nulle per {column} = {results.rowcount}""") 
    connection.close()   
    
    
    
    
    
    
    
    
    
    
def count_row_from_db2(df,table_name):
    connection = psycopg2.connect(conn_str)
    #connection.autocommit = True----->A COSA SERVE?
    print (f"""Tabella {table_name}:""")
    for column in df.columns:
        sql_query=f"""SELECT COUNT({column}) FROM {table_name}"""
        cursor = connection.cursor()
        cursor.execute(sql_query)
        print (f"""Nr righe non nulle per {column} = {cursor.fetchone()}""")
    cursor.close()
    connection.close()

#interroga il db e scrive il risultato in un DataFrame
def query_db(sql):
    connection=create_conn(conn_str)
    table=pd.read_sql_query(sql,connection)
    connection.close()
    return table


#query
sql_queries=['select * from paper',
             'select * from alias_id',
             'select * from with_alias',
             'select * from reference',
             'select * from venue',
             'select * from author',
             'select * from who',
             'select * from author_extended',
             'select * from fos',
             'select * from what']

#esegue una serie di query sul db
def check_nb_records(sql_queries):
    for query in sql_queries:
        df=query_db(query)
        df.info()
        print()