import json
import urllib.request

class Market:
    def __init__(self):
        self._key = "efa54c05253d0bf4edaeee0fc4d576dc84b34b8a"
        self._url = f"https://api.nomics.com/v1/currencies/ticker?key={self._key}&ids=%s"
        self._currencies = "BTC,ETH,USDT,BNB,XRP,ADA,SOL,DOGE,ETC"
        self._market = []

    def updateMarket(self):
        self._market = []
        data = urllib.request.urlopen(self._url %self._currencies).read()
        jsonData = json.loads(data)
        for curr in jsonData:
            tmpCurr = {"id": curr["id"],
                "name:": curr["name"],
                "price": curr["price"],
                "volume": curr["1d"]["volume"],
                "1d": curr["1d"]["price_change_pct"],
                "7d": curr["7d"]["price_change_pct"],
                "30d": curr["30d"]["price_change_pct"]}
            self._market.append(tmpCurr)

    def getMarket(self):
        return self._market

    def getLivePrices(self):
        livePrices = {}
        for curr in self._market:
            livePrices[curr["id"]] = curr["price"]
        return livePrices

    def get30dGraph(self, id):
        pass
