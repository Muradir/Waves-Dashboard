#Author: Lars Brebeck
#Description: This file starts the backend_service app

#import internal classes
from data_processing.crypto_details_processing import CryptoStatsDataProcessing
from data_processing.market_prices_processing import MarketPricesDataProcessing
#from data_processing.create_dataframes import CreateDataFrames

class Main:

    #main method of backend service program
    def main():
        print("Wir schaffen das!")
        MarketPricesDataProcessing().start()
        CryptoStatsDataProcessing().start()
        #CreateDataFrames.getDataframeUSD()
        #CreateDataFrames.getDataframeBTC()
        #CreateDataFrames.getDataframeETH()
        #CreateDataFrames.getDataframeWAVES()

        #MarketPricesDataProcessing().start()
        #CryptoStatsDataProcessing().start()
        #CreateDataFrames.getDataframeUSD()
        #CreateDataFrames.getDataframeBTC()
        #CreateDataFrames.getDataframeETH()
        #CreateDataFrames.getDataframeWAVES()
        #CreateDataFrames.getDataframeCurrency()

    #invokes the main method
    if __name__ == "__main__":
        main()