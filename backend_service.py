#import internal classes
from data_processing.crypto_details_processing import CryptoStatsDataProcessing
from data_processing.market_prices_processing import MarketPricesDataProcessing

class Main:

    def main():
        print("Wir schaffen das!")
        MarketPricesDataProcessing().start()
        CryptoStatsDataProcessing().start()


    if __name__ == "__main__":
        main()