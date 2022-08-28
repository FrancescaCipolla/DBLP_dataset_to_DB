#analyze_df

#funzioni per l'analisi del dataframe

#dato un DataFrame e una colonna, restituisce la percentuale di valori '' o NA:numpy.NaN o None per quella colonna 
def count_miss_value (df, column):
    i=0
    j=0
    i=df[column].isna().sum()
    j=df[df[column]==''][column].count() #uso di una maschera booleana per contare i valori ''
    return print(f'Percentuale di valori nulli per la colonna {column} = {((i+j)/len(df)*100)}%') 

#calcola la percentuale di valori mancanti (NaN o '') per ogni colonna, utile per determinare quali attibuti sono opzionali
def miss_percentage(df):
    for columns in df.columns:
        count_miss_value(df,columns)

# dato un Dataframe e una colonna, restituisce la percentuale di valori NA:numpy.NaN o None
def count_nan_value (df, column):
    i=0
    i=df[column].isna().sum() # conta il numero di NA,None o NaN nella serie
    return print(f'Percentuale di valori nulli per la colonna {column} = {(i/len(df)*100)}%') 

    
#calcola la percentuale di valori mancanti (NaN) per ogni colonna, controverifica: controlla che le percentuali di valori nulli non sia cambiata rispetto a prima di utilizzare fill_empty_values
def nan_percentage(df):
    for columns in df.columns:
        count_nan_value(df,columns)
    
#controlla quali sono le colonne che contengono una determinata stringa
def column_with_special_char (df,string):
    for column in df.columns:
        if df[column].dtype==object:
            df=df[df[column].str.contains(string,na=False)]
            print(f"""{df[column].head()}
            """)
            
#restituisce informazioni sul dataframe
def info(df):
    return df.info(verbose=True,show_counts=True)
    
#dato un DataFrame e una lista di colonne determina i duplicati su quel sottoinsieme di colonne e li ordina    
def check_duplicates (df,columns_list):
        return df[df.duplicated(subset=columns_list, keep=False)].sort_values(by=columns_list)

#controlla i valori massimi e minimi per le colonne del DataFrame con tipo di dato numerico
def check_max_min (df):
    for column in df.columns:
        if df[column].dtype!=object:
            print (f"""Colonna {column} : valore massimo {df[column].max()}, valore minimo {df[column].min()}""")


