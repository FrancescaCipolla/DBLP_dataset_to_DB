#manipulate_dataframe

#funzioni per la manipolazione del dataframe

#importa moduli necessari
import pandas as pd
import numpy as np
import html

#dato un DataFrame elimina le righe completamente nulle e duplicate
def del_null_duplicates(df):
    df.dropna(axis='index', #effettua l'eliminazione lungo l'asse degli indici
                   how='all', #elimina la riga se tutti i valori sono NaN
                   inplace=True) #effettua l'operazione sul dataframe anzichè restituire una copia
    df.drop_duplicates(inplace=True, #effettua l'operazione sul dataframe anzichè restituire una copia
                            ignore_index=True) #affinchè gli assi risultanti siano da 0 a n-1
    return df.info(verbose=True,show_counts=True)


#dato un DataFrame e una stringa rimpiazza tutti i valori che contengono la stringa con NaN
def fill_with_nan (df,string):
    df.replace(to_replace=string, #valore da sostituire
                    value=np.nan, #valore con cui sostituire
                    inplace=True) #effettua l'operazione sul dataframe anzichè restituire una copia
    return df.info(verbose=True,show_counts=True)


#decodifica le sequenze di escape dei caratteri speciali html (entità numerica html) per quelle colonne di tipo object
def unescape_special_char (df):
    for column in df.columns:
        if df[column].dtype==object:
            df[column]=df[column].map(html.unescape, #mappa le righe nella loro versione decodificata
                                      na_action='ignore') #mantiene i valori NaN senza passarli alla funzione map
    
    
#rinomina le colonne del DataFrame in base al dict passato
def rename_columns(df, columns_dict):
    df.rename(columns=columns_dict, inplace=True)

#elimina le colonne del DataFrame passate come argomento
def del_columns(df, columns_list):
    df.drop(columns_list, axis='columns',inplace=True)
        
    
#effettua il cast di una colonna al tipo di dato passato    
def cast_to(df,column,dtype):
    df[column]=(df[column]).astype(dtype,copy=False)

#esegue una funzione di hash sul DataFrame, convertendo il risultato al tipo di dato passato
def hash_df(df,dtype):
    return abs((pd.util.hash_pandas_object(df, index=False)).astype(dtype,copy=False))

#trasforma ogni elemento di una lista in una riga
def expand_column(df,column):
    return df.explode(column,ignore_index=True) #indici risultanti da 0 a n-1

    