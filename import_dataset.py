#import_dataset

#funzioni per la lettura del Json e creazione del DataFrame

#importa moduli necessari
import pandas as pd

#inizializza il DataFrame vuoto
def initialize():
    return pd.DataFrame()


#legge il chunk (Json Reader) e lo inserisce in un DataFrame facendo uso del metodo pandas.json_normalize
#chunk=chunk del file Json
#data=chiave nell'oggetto Json da leggere
#recordpath=percorso in ogni oggetto Json per l'elenco dei record
#meta=campo da utilizzare come metadato incluso in ogni record del dataframe risultante
#metaprefix=prefisso per il campo meta
#recordprefix=prefisso per il campo record
def read_json_chunk (chunk, data, recordpath=None, meta=None, metaprefix=None, recordprefix=None):
    if (recordpath==None) and (meta==None) and (metaprefix==None) and (recordprefix==None):
        df=(pd.json_normalize(data=chunk[data])) #oggetti Json da serializzare
    else:
        df= (pd.json_normalize(data=chunk[data], record_path=[recordpath], meta=[meta], meta_prefix=metaprefix, record_prefix=recordprefix)) 
    return df


#legge il file Json linea per linea, itera sui chunks
#path_or_buf=percorso del file Json
#lines=legge il file come un oggetto Json per linea
#chunksize=dimensione dei chunk, restituisce un oggetto JsonReader iterabile
def read_json (df,path,data,columns_list):
    with open (path) as f:
        chunks=pd.read_json(path_or_buf=f, #
                      lines=True, #legge il file come un oggetto Json per linea
                      chunksize=10000) #
        for chunk in chunks:
            source_df=read_json_chunk(chunk,data)
            source_df.drop(columns=columns_list, inplace=True)
            df=pd.concat([df,source_df], ignore_index=True)
        return df
                
        

def read_json_flatten (df,path,data,recordpath,meta,metaprefix,recordprefix):
    with open (path) as f:
        chunks=pd.read_json(path_or_buf=f,lines=True,chunksize=10000) 
        for chunk in chunks:
            source_df=read_json_chunk(chunk,data,recordpath, meta,metaprefix,recordprefix)
            df=pd.concat([df,source_df], ignore_index=True)
        return df
                     

        
def read_json_flatten_from_dict (df,path,data,recordpath,meta,metaprefix,recordprefix):
#legge il json per chunk, itero sui chunk e chiamo la funzione read_json_chunk
    with open (path) as f:
        chunks=pd.read_json(f, lines=True, chunksize=10000)  
        for chunk in chunks:
            source_df=read_json_chunk(chunk,data)
            #mantiene solo le colonne necessarie
            source_df=source_df[[recordpath,meta]]
            #converte il dataframe in dict
            source_df = source_df.to_dict(orient='records')
            #memorizza gli elementi del dict in un dataframe temporaneo 
            df_tmp=pd.json_normalize(source_df, recordpath,meta,metaprefix,recordprefix)
            #concatena il dataframe temporaneo e quello inizialmente vuoto, alla fine del loop conterrà tutti gli elementi della chiave fos
            df=pd.concat([df,df_tmp])
        return df
        


        
        
        
        
        
        
        
        
