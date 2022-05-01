#import internal classes
from data_processing.crypto_details_processing import CryptoStatsDataProcessing
from data_processing.market_prices_processing import MarketPricesDataProcessing
#from data_processing.create_dataframes import CreateDataFrames



class Main:

    #main method of backend service programm
    def main():
        print("Wir schaffen das!")
<<<<<<< HEAD
        MarketPricesDataProcessing().start()
        CryptoStatsDataProcessing().start()
        #CreateDataFrames.getDataframeUSD()
        #CreateDataFrames.getDataframeBTC()
        #CreateDataFrames.getDataframeETH()
        #CreateDataFrames.getDataframeWAVES()
=======
        #MarketPricesDataProcessing().start()
        #CryptoStatsDataProcessing().start()
        CreateDataFrames.getDataframeUSD()
        CreateDataFrames.getDataframeBTC()
        CreateDataFrames.getDataframeETH()
        CreateDataFrames.getDataframeWAVES()
        CreateDataFrames.getDataframeCurrency()
>>>>>>> 68e4b7cdf16e9e2eee89b9b79726f3bce4a31247

    #invokes the main method
    if __name__ == "__main__":
        main()