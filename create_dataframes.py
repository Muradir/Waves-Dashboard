import pandas as pd
from database_depr import Database

##Erzeuge eine leere Liste.
usdSQL = []
##Rufe Daten aus der SQL per Select Befehl ab.    
rows = Database().executeSelectQuery(tableName = 'vw_report_waves_market_prices')
##Übergebe die gesammelten Daten aus der SQL an die Liste.
for row in rows:
    usdSQL.append(list(row))
    labels = ['Datum','Wert']
    ##Übertrage die gesammelten Daten an den Dataframe.
    dfusd = pd.DataFrame.from_records(usdSQL, columns=labels)
    ##Formatier den Dataframe entsprechend für die anschließende Nutzung im Graphen.
    dfusd['Wert'] = dfusd['Wert'].apply(pd.to_numeric)
    dfusd['Datum'] = dfusd['Datum'].apply(pd.to_datetime)

dfusd.to_pickle("./DataFrames/dfusd")
print("US-Dollar Data successfully saved to Dataframe: dfusd")

##Erzeuge eine leere Liste.
wavesSQL = []
##Rufe Daten aus der SQL per Select Befehl ab.    
rows = Database().executeSelectQuery(tableName = 'vw_report_waves_market_prices')
##Übergebe die gesammelten Daten aus der SQL an die Liste.
for row in rows:
    wavesSQL.append(list(row))
    labels = ['Datum','Wert']
    ##Übertrage die gesammelten Daten an den Dataframe.
    dfwaves = pd.DataFrame.from_records(wavesSQL, columns=labels)
    ##Formatier den Dataframe entsprechend für die anschließende Nutzung im Graphen.
    dfwaves['Wert'] = dfwaves['Wert'].apply(pd.to_numeric)
    dfwaves['Datum'] = dfwaves['Datum'].apply(pd.to_datetime)

dfwaves.to_pickle("./DataFrames/dfwaves")
print("Waves Data successfully saved to Dataframe: dfwaves")

bitcoinSQL = [] #set an empty list
    
rows = Database().executeSelectQuery(tableName = 'vw_report_waves_market_prices')
for row in rows:
    bitcoinSQL.append(list(row))
    labels = ['Datum','Wert']
    dfbitcoin = pd.DataFrame.from_records(bitcoinSQL, columns=labels)
    dfbitcoin['Wert'] = dfbitcoin['Wert'].apply(pd.to_numeric)
    dfbitcoin['Datum'] = dfbitcoin['Datum'].apply(pd.to_datetime)

dfbitcoin.to_pickle("./DataFrames/dfbitcoin")
print("Bitcoin Data successfully saved to Dataframe: dfbitcoin")

ethereumSQL = [] #set an empty list
    
rows = Database().executeSelectQuery(tableName = 'vw_report_waves_market_prices')
for row in rows:
    ethereumSQL.append(list(row))
    labels = ['Datum','Wert']
    dfethereum = pd.DataFrame.from_records(ethereumSQL, columns=labels)
    dfethereum['Wert'] = dfethereum['Wert'].apply(pd.to_numeric)
    dfethereum['Datum'] = dfethereum['Datum'].apply(pd.to_datetime)

dfethereum.to_pickle("./DataFrames/dfethereum")
print("Ethereum Data successfully saved to Dataframe: dfethereum")