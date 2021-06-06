from KrakenRequests import KrakenRequests as kr

if __name__ == "__main__":
    print("OK")
    print("Server time: ", kr.GetServerTime())
    print("Bitcoin Prices: ", kr.GetPrices('XXBTZUSD', interval=240, since=None))