from account import Account
from market import Market
from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def main():
    acc = Account("janek")
    market = Market()
    market.update()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    gui = Ui_MainWindow(acc, market)
    gui.setupUi(MainWindow)
    MainWindow.show()
    gui._account.addInvested(70000)
    gui._account.buyCurrency("BTC", 20139.54, 3)
    gui.update()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
