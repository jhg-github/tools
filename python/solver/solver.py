# https://realpython.com/qt-designer-python/
# 
# To convert gui from qt designer to a python file: "pyuic5 -x .\main_window.ui -o main_window.py"

from PyQt5 import QtCore, QtGui, QtWidgets
from main_window import Ui_MainWindow

class LinSolver():
    def __init__(self):
        self.x0 = 0
        self.x1 = 0
        self.y0 = 0
        self.y1 = 0
        self.m = 0
        self.n = 0
    
    def update_m_n(self):
        try:
            self.m = (self.y1-self.y0) / (self.x1-self.x0)
            self.n = self.y0 - (self.m*self.x0)
        except:
            self.m = 0
            self.n = 0
        return self.m, self.n
    
    def set_x0(self, x0):
        self.x0 = x0
        return self.update_m_n()

    def set_x1(self, x1):
        self.x1 = x1
        return self.update_m_n()

    def set_y0(self, y0):
        self.y0 = y0
        return self.update_m_n()

    def set_y1(self, y1):
        self.y1 = y1
        return self.update_m_n()
    
    def get_y(self, x):
        y = (self.m*x)+self.n
        return y
    
    def get_x(self, y):
        x = (y-self.n)/self.m
        return x



class Solver():
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.ui.lineEdit_m.setText('#')
        self.ui.lineEdit_n.setText('#') 
        self.ui.lineEdit_x0.textChanged.connect(lambda: self.update_field('x0'))    
        self.ui.lineEdit_x1.textChanged.connect(lambda: self.update_field('x1'))
        self.ui.lineEdit_y0.textChanged.connect(lambda: self.update_field('y0'))
        self.ui.lineEdit_y1.textChanged.connect(lambda: self.update_field('y1'))
        self.ui.lineEdit_x.textChanged.connect(lambda: self.update_field('x'))
        self.ui.lineEdit_y.textChanged.connect(lambda: self.update_field('y'))
        self.lin_solver = LinSolver()
    
    def update_field(self, field):
        try:
            if field == 'x0':
                x0 = float(self.ui.lineEdit_x0.text())
                m,n = self.lin_solver.set_x0(x0)
                self.ui.lineEdit_m.setText(str(m))
                self.ui.lineEdit_n.setText(str(n))
            elif field == 'x1':
                x1 = float(self.ui.lineEdit_x1.text())
                m,n = self.lin_solver.set_x1(x1)
                self.ui.lineEdit_m.setText(str(m))
                self.ui.lineEdit_n.setText(str(n))
            elif field == 'y0':
                y0 = float(self.ui.lineEdit_y0.text())
                m,n = self.lin_solver.set_y0(y0)
                self.ui.lineEdit_m.setText(str(m))
                self.ui.lineEdit_n.setText(str(n))        
            elif field == 'y1':
                y1 = float(self.ui.lineEdit_y1.text())
                m,n = self.lin_solver.set_y1(y1)
                self.ui.lineEdit_m.setText(str(m))
                self.ui.lineEdit_n.setText(str(n))
        except:
            self.ui.lineEdit_m.setText('#')
            self.ui.lineEdit_n.setText('#')  
        if field == 'x':
            try:
                x = float(self.ui.lineEdit_x.text())
                y = self.lin_solver.get_y(x)
                self.ui.lineEdit_y.blockSignals(True)
                self.ui.lineEdit_y.setText(str(y))
                self.ui.lineEdit_y.blockSignals(False)
            except:
                self.ui.lineEdit_y.blockSignals(True)
                self.ui.lineEdit_y.setText('#')
                self.ui.lineEdit_y.blockSignals(False)
        elif field == 'y':
            try:
                y = float(self.ui.lineEdit_y.text())
                x = self.lin_solver.get_x(y)
                self.ui.lineEdit_x.blockSignals(True)
                self.ui.lineEdit_x.setText(str(x))
                self.ui.lineEdit_x.blockSignals(False)
            except:
                self.ui.lineEdit_x.blockSignals(True)
                self.ui.lineEdit_x.setText('#')
                self.ui.lineEdit_x.blockSignals(False)
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    solver = Solver(ui)
    MainWindow.show()
    sys.exit(app.exec_())