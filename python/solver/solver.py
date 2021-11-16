# https://realpython.com/qt-designer-python/
# 
# To convert gui from qt designer to a python file: "pyuic5 -x .\main_window.ui -o main_window.py"

from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import Ui_MainWindow

class Solver():
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.ui.pushButton.clicked.connect(lambda: self.change('ojojoj'))
    
    def change(self, text):
        self.ui.label.setText(text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    solver = Solver(ui)
    MainWindow.show()
    sys.exit(app.exec_())