import pandas as pd
import numpy as np
import sys,os

pathToDataStoresDir = os.path.join(os.path.dirname(__file__), '../data_stores')
sys.path.append(pathToDataStoresDir)

from database import Database

#Authors: Pascal Hildebrandt, Genar Yildiran
#Description: This class is responsible for creating and saving Dataframes.
#             The start method is creating one dataframe for each purpose
#             or rather currency. The Dataframes are later on used for the 
#             dashboard to create the graphs and the converter.

class CreateDataFrames:

    def start(self):
        self.getDataframeByChoice('Bitcoin')
        self.getDataframeByChoice('Ethereum')
        self.getDataframeByChoice('Waves')
        self.getDataframeByChoice('Usd')
        self.getDataframeByChoice('Converter')

    def __getDataframeByChoice(self, currency: str):
        # Creating empty list.
        SQL = []  # set an empty list
        # Get data from SQL database.
        rows = Database().executeSelectQuery(
            tableName=self.getTableName(currency=currency))
        # Pass the collected data from SQL database to the list.
        for row in rows:
            SQL.append(list(row))
            labels = self.getLabelsByChoice(currency=currency)
            # Transfer the collected data to the dataframe.
            df = pd.DataFrame.from_records(SQL, columns=labels)
        # Format the dataframe accordingly for subsequent use in the graph.
        if(currency == 'Converter'):
            df['USD'] = df['USD'].apply(pd.to_numeric)
            df['Fee'] = df['Fee'].apply(pd.to_numeric)
            df['Date'] = df['Date'].apply(pd.to_datetime)
        elif currency == 'Usd':
            df['BTC'] = df['BTC'].apply(pd.to_numeric)
            df['ETH'] = df['ETH'].apply(pd.to_numeric)
            df['WAVES'] = df['WAVES'].apply(pd.to_numeric)
            df['SP500'] = df['SP500'].apply(pd.to_numeric)
            df['Date'] = df['Date'].apply(pd.to_datetime)
        else:
            df[labels[2]] = df[labels[2]].apply(pd.to_numeric)
            df[labels[1]] = df[labels[1]].apply(pd.to_numeric)
            df[labels[0]] = df[labels[0]].apply(pd.to_datetime)

        df.to_pickle("./backend_app/data_stores/df" + str(currency.lower()))
        print(str(currency) +
              " Data successfully saved to Dataframe: df" + str(currency.lower()))

    def __getLabelsByChoice(self, currency):
        allLabels = ['Date', 'BTC', 'ETH', 'WAVES',
                     'SP500', 'USD', 'Fee', 'Currency']
        specLabel = []
        if currency == 'Bitcoin':
            specLabel.append(allLabels[0])
            specLabel.append(allLabels[2])
            specLabel.append(allLabels[3])
        elif currency == 'Ethereum':
            specLabel.append(allLabels[0])
            specLabel.append(allLabels[1])
            specLabel.append(allLabels[3])
        elif currency == 'Waves':
            specLabel.append(allLabels[0])
            specLabel.append(allLabels[1])
            specLabel.append(allLabels[2])
        elif currency == 'Usd':
            specLabel.append(allLabels[0])
            specLabel.append(allLabels[1])
            specLabel.append(allLabels[2])
            specLabel.append(allLabels[3])
            specLabel.append(allLabels[4])
        elif currency == 'Converter':
            specLabel.append(allLabels[0])
            specLabel.append(allLabels[5])
            specLabel.append(allLabels[6])
            specLabel.append(allLabels[7])
        return specLabel

    def __getTableName(self, currency: str):
        if currency == 'Converter':
            return 'report_currencyConverter'
        else:
            return 'report_marketPricesIn' + currency
