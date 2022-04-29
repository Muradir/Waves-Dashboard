import pandas as pd
import numpy as np
from data_stores.database import Database


class CreateDataFrames:

    def getDataframeUSD():
        # Erzeuge eine leere Liste.
        usdSQL = []
        # Rufe Daten aus der SQL per Select Befehl ab.
        rows = Database().executeSelectQuery(tableName='report_marketPricesInUsd')
        # Übergebe die gesammelten Daten aus der SQL an die Liste.
        for row in rows:
            usdSQL.append(list(row))
            labels = ['Date', 'BTC', 'ETH', 'WAVES', 'SP500']
            # Übertrage die gesammelten Daten an den Dataframe.
            dfusd = pd.DataFrame.from_records(usdSQL, columns=labels)
        # Formatier den Dataframe entsprechend für die anschließende Nutzung im Graphen.
        dfusd['BTC'] = dfusd['BTC'].apply(pd.to_numeric)
        dfusd['ETH'] = dfusd['ETH'].apply(pd.to_numeric)
        dfusd['WAVES'] = dfusd['WAVES'].apply(pd.to_numeric)
        dfusd['SP500'] = dfusd['SP500'].apply(pd.to_numeric)
        dfusd['Date'] = dfusd['Date'].apply(pd.to_datetime)

        dfusd.to_pickle("./data_stores/dfusd")
        print("US-Dollar Data successfully saved to Dataframe: dfusd")

    def getDataframeWAVES():
        # Erzeuge eine leere Liste.
        wavesSQL = []
        # Rufe Daten aus der SQL per Select Befehl ab.
        rows = Database().executeSelectQuery(tableName='vw_report_waves_market_prices')
        # Übergebe die gesammelten Daten aus der SQL an die Liste.
        for row in rows:
            wavesSQL.append(list(row))
            labels = ['Datum', 'Wert']
            # Übertrage die gesammelten Daten an den Dataframe.
            dfwaves = pd.DataFrame.from_records(wavesSQL, columns=labels)
        # Formatier den Dataframe entsprechend für die anschließende Nutzung im Graphen.
        dfwaves['Wert'] = dfwaves['Wert'].apply(pd.to_numeric)
        dfwaves['Datum'] = dfwaves['Datum'].apply(pd.to_datetime)

        dfwaves.to_pickle("./data_stores/dfwaves")
        print("Waves Data successfully saved to Dataframe: dfwaves")

    def getDataframeBTC():
        # Erzeuge eine leere Liste.
        bitcoinSQL = []  # set an empty list
        # Rufe Daten aus der SQL per Select Befehl ab.
        rows = Database().executeSelectQuery(tableName='vw_report_waves_market_prices')
        # Übergebe die gesammelten Daten aus der SQL an die Liste.
        for row in rows:
            bitcoinSQL.append(list(row))
            labels = ['Datum', 'Wert']
            # Übertrage die gesammelten Daten an den Dataframe.
            dfbitcoin = pd.DataFrame.from_records(bitcoinSQL, columns=labels)
        # Formatier den Dataframe entsprechend für die anschließende Nutzung im Graphen.
        dfbitcoin['Wert'] = dfbitcoin['Wert'].apply(pd.to_numeric)
        dfbitcoin['Datum'] = dfbitcoin['Datum'].apply(pd.to_datetime)

        dfbitcoin.to_pickle("./data_stores/dfbitcoin")
        print("Bitcoin Data successfully saved to Dataframe: dfbitcoin")

    def getDataframeETH():
        # Erzeuge eine leere Liste.
        ethereumSQL = []  # set an empty list
        # Rufe Daten aus der SQL per Select Befehl ab.
        rows = Database().executeSelectQuery(tableName='vw_report_waves_market_prices')
        # Übergebe die gesammelten Daten aus der SQL an die Liste.
        for row in rows:
            ethereumSQL.append(list(row))
            labels = ['Datum', 'Wert']
            # Übertrage die gesammelten Daten an den Dataframe.
            dfethereum = pd.DataFrame.from_records(ethereumSQL, columns=labels)
        # Formatier den Dataframe entsprechend für die anschließende Nutzung im Graphen.
        dfethereum['Wert'] = dfethereum['Wert'].apply(pd.to_numeric)
        dfethereum['Datum'] = dfethereum['Datum'].apply(pd.to_datetime)

        dfethereum.to_pickle("./data_stores/dfethereum")
        print("Ethereum Data successfully saved to Dataframe: dfethereum")
