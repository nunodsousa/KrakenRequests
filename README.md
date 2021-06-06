# Kraken Requests methods

Very simple library with the following four functions:

- GetAssetPairInfo
- GetPrices
- GetServerTime
- GetSystemStatus

The main file contains examples of how to call each static method.
Prices are given in a pandas dataframe.

How to install the library:

- pip install git+https://github.com/nunodsousa/KrakenRequest.git

### Very Short but complete documentation 

    Kraken Request methods
    ---------------------

    GetAssetPairInfo()
    args:
        No arguments
    return:
        Information of the each pair.
        The information is the following:

        <pair_name> = pair name
        altname = alternate pair name
        wsname = WebSocket pair name (if available)
        aclass_base = asset class of base component
        base = asset id of base component
        aclass_quote = asset class of quote component
        quote = asset id of quote component
        lot = volume lot size
        pair_decimals = scaling decimal places for pair
        lot_decimals = scaling decimal places for volume
        lot_multiplier = amount to multiply lot volume by to get currency volume
        leverage_buy = array of leverage amounts available when buying
        leverage_sell = array of leverage amounts available when selling
        fees = fee schedule array in [volume, percent fee] tuples
        fees_maker = maker fee schedule array in [volume, percent fee] tuples (if on maker/taker)
        fee_volume_currency = volume discount currency
        margin_call = margin call level
        margin_stop = stop-out/liquidation margin level
        ordermin = minimum order volume for pair


    GetPrices()
    args:
        pair = asset pair to get OHLC data for
        interval = time frame interval in minutes (optional):
        1 (default), 5, 15, 30, 60, 240, 1440, 10080, 21600
        since = return committed OHLC data since given id (optional. in timestamp)
    return:
        A pandas dataframe with 'time', 'open', 'high', 'low', 'close', 'vwap', 'volume', 'count'


    GetServerTime()
    args:
        No arguments
    return:
        Server time in several formats.
        Example: {'unixtime': 1622828722, 'rfc1123': 'Fri,  4 Jun 21 17:45:22 +0000'}


    GetSystemStatus()
    args:
        No arguments
    return:
        System Status and timestamp:
        Example: {'status': 'online', 'timestamp': '2021-06-04T17:47:35Z'}

