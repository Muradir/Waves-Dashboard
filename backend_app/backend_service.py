# import internal classes
from data_processing.crypto_details_processing import CryptoStatsDataProcessing
from data_processing.market_prices_processing import MarketPricesDataProcessing
from data_processing.create_dataframes import CreateDataFrames
<<<<<<< HEAD

=======
>>>>>>> e1a71ce3712230ff80e09a78121c0d8a1850dae3


class Main:

    # main method of backend service programm
    def main():
        print("Wir schaffen das!")
<<<<<<< HEAD
        MarketPricesDataProcessing().start()
        CryptoStatsDataProcessing().start()
        CreateDataFrames.getDataframeUSD()
        CreateDataFrames.getDataframeBTC()
        CreateDataFrames.getDataframeETH()
        CreateDataFrames.getDataframeWAVES()
        CreateDataFrames.getDataframeCurrency()
        CreateDataFrames.getDataframeDetails()
=======
        # MarketPricesDataProcessing().start()
        # CryptoStatsDataProcessing().start()
        # CreateDataFrames.getDataframeUSD()
        # CreateDataFrames.getDataframeBTC()
        # CreateDataFrames.getDataframeETH()
        # CreateDataFrames.getDataframeWAVES()

        # MarketPricesDataProcessing().start()
        # CryptoStatsDataProcessing().start()
        # CreateDataFrames.getDataframeUSD()
        # CreateDataFrames.getDataframeBTC()
        # CreateDataFrames.getDataframeETH()
        # CreateDataFrames.getDataframeWAVES()
        # CreateDataFrames().start()
>>>>>>> e1a71ce3712230ff80e09a78121c0d8a1850dae3

    # invokes the main method
    if __name__ == "__main__":
        main()
