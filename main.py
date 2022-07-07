from account import Account
from market import Market

def main():
    acc = Account("janek")
    print(acc)
    market = Market()
    market.update()
    print(market)
    print(market.getLivePrices())

if __name__ == '__main__':
    main()
