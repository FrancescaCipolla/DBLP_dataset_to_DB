# DBLP_dataset_to_DB

Il progetto DBLP_dataset_to_DB si occupa di estrarre, analizzare ed elaborare i dati del dataset messo a disposizione dal lab SimpleText, attraverso gli strumenti offerti dalla libreria Pandas

## Struttura

1. **import_dataset.py**: script che raccoglie funzioni atte ad importare i dati del file dblp1.json nei diversi DataFrame
1. **analize_df.py**: script con funzioni che analizzano i DataFrame creati
1. **manipulate_df.py**; script contenente funzioni che manipolano i DataFrame creati
1. **DB_connection**: script che si occupa di creare la connessione ad un database esistente, scrivere gli elementi dei DataFrame nelle tabelle del database ed interrogarlo al fine di verificare la corretta importazione di tutti i records
1. **Json_Parser_DBLP_Dataset**: file di esecuzione principale, dove vengono eseguite le funzioni contenute negli scripts, con l’aggiunta di qualche raro utilizzo diretto dei metodi di Pandas
1. **DBLP_db**: file contenente lo schema del database (nella cartella SQL)

Il file **config.py** (volutamente tralasciato) contiene i parametri di connessione al database sotto forma di dict

Il database è stato creato tramite il Query Tool di pgAdmin4.
