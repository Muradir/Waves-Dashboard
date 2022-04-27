#import internal classes
from data_processing.crypto_details_processing import CryptoStatsDataProcessing
from data_processing.market_prices_processing import MarketPricesDataProcessing

class Main:

    #main method of backend service programm
    def main():
        print("Wir schaffen das!")
        MarketPricesDataProcessing().start()
        CryptoStatsDataProcessing().start()


    #invokes the main method
    if __name__ == "__main__":
        main()