##
## Simple example of the usage of the KrakenRequests
##
## Simia-Tech (example version)

from KrakenRequests.KrakenRequests import KrakenRequests as kr

if __name__ == "__main__":
    print("Server Time: ", kr.GetServerTime())
    print("System Status: ", kr.GetSystemStatus())
    print("Asset Pairs Info: ", kr.GetAssetPairsInfo())
    print("Bitcoin Prices: ", kr.GetPrices('XXBTZUSD', interval=240, since=None))