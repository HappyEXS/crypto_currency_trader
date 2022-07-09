import json

class Account:
    def __init__(self, username):
        self._username = username
        self._invested = 0  # Wplacone pieniadze na konto
        self._funds = 0     # Dostępne srodki na koncie
        self._wallet_v = 0  # Wartoć portfela kryptowalut
        self._balance = 0   # Wartosc calego konta
        self._wallet = []

    def __str__(self):
        return (f"Username: {self._username}\t\t\tInvested: {self._invested}\n" +
                f"Available funds: {self._funds}\tAccount balance: {self._balance}")

    def setUsername(self, newUsername):
        self._username = newUsername

    def getUsername(self):
        return self._username

    def addInvested(self, amount):
        self._invested += amount
        self.addFunds(amount)
        self.addBalance(amount)

    def getInvested(self):
        return round(self._invested, 2)

    def addFunds(self, amount):
        self._funds += amount

    def getFunds(self):
        return round(self._funds, 2)

    def getWalletValue(self):
        return round(self._wallet_v, 2)

    def addBalance(self, amount):
        self._balance += amount

    def getBalance(self):
        return round(self._balance, 2)

    def getWallet(self):
        return self._wallet

    def buyCurrency(self, name, price, quantity):
        curr = {"name": name,
                "price": float(price),
                "quantity": int(quantity),
                "currentPrice": float(price),
                "value": price*quantity}
        if self.getFunds() < curr["value"]:
            raise Exception("Currency too expensive to buy. Not enough funds!")
        self._wallet.append(curr)
        self.addFunds(-curr["value"])
        self.updateWalletValue()
        self.updateBallance()

    def sellCurrency(self, name, quantity):
        for curr in self._wallet:
            if curr["name"] == name:
                if curr["quantity"] < quantity :
                    raise Exception("Too many quantity to sell!")
                self.addFunds(curr["currentPrice"]*quantity)
                if curr["quantity"] == quantity:
                    self._wallet.remove(curr)
                else:
                    curr["quantity"] -= quantity
                    curr["value"] = curr["quantity"] * curr["currentPrice"]
        self.updateWalletValue()
        self.updateBallance()

    def updatePrices(self, livePrices):
        for curr in self._wallet:
            curr["currentPrice"] = float(livePrices[curr["name"]])
            curr["value"] = curr["quantity"] * curr["currentPrice"]

    def updateWalletValue(self):
        wallet_value = 0
        for curr in self._wallet:
            wallet_value += curr["value"]
        self._wallet_v = wallet_value

    def updateBallance(self):
        self._balance = self.getWalletValue() + self.getFunds()

    def saveToJson(self):
        data = {
            "username": self.getUsername(),
            "invested": self.getInvested(),
            "funds": self.getFunds(),
            "wallet_value": self.getWalletValue(),
            "balance": self.getBalance(),
            "wallet": self.getWallet()
        }
        with open(f"acc_data/data_{self.getUsername()}.json", 'w') as f:
            json.dump(data, f)

    def readFromJson(self):
        with open(f"acc_data/data_{self.getUsername()}.json") as f:
            data = json.load(f)
        self._invested = data["invested"]
        self._funds = data["funds"]
        self._wallet_v = data["wallet_value"]
        self._balance = data["balance"]
        self._wallet = data["wallet"]

    def update(self):
        self.updateWalletValue()
        self.updateBallance()
        self.saveToJson()
