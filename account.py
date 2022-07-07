class Account:
    def __init__(self, username):
        self._username = username
        self._invested = 0  # Wplacone pieniadze na konto
        self._funds = 0     # Dostępne srodki na koncie
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
        self._invested += round(amount, 2)
        self.addFunds(amount)
        self.addBalance(amount)

    def getInvested(self):
        return self._invested

    def addFunds(self, amount):
        self._funds += round(amount, 2)

    def getFunds(self):
        return self._funds

    def addBalance(self, amount):
        self._balance += round(amount, 2)

    def getBalance(self):
        return self._balance

    def getWallet(self):
        return self._wallet

    def buyCurrency(self, name, price, quantity):
        curr = {"name": name,
                "price": price,
                "quantity": int(quantity),
                "currentPrice": price,
                "value": price*quantity}
        if self.getFunds() < curr["value"]:
            raise Exception("Currency too expensive to buy. Not enough funds!")
        self._wallet.append(curr)
        self.addFunds(-curr["value"])
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
        self.updateBallance()

    def updatePrices(self, livePrices):
        for curr in self._wallet:
            curr["currentPrice"] = livePrices[curr["name"]]
            curr["value"] = curr["quantity"] * curr["currentPrice"]
        self.updateBallance()

    def updateBallance(self):
        ballance = 0
        for curr in self._wallet:
            ballance += curr["value"]
        self._balance = round(ballance + self.getFunds(), 2)
