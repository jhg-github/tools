# https://realpython.com/qt-designer-python/
# 
# To convert gui from qt designer to a python file: "pyuic5 -x .\main_window_table.ui -o main_window_table.py"

from typing import Text
from PyQt5 import QtCore, QtGui, QtWidgets

from main_window_table import Ui_MainWindow
from lin_solver import LinSolver


class Solver():
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.ui.lineEdit_m.setText('#')
        self.ui.lineEdit_n.setText('#') 
        # self.ui.lineEdit_x0.textChanged.connect(lambda: self.update_field('x0'))    
        # self.ui.lineEdit_x1.textChanged.connect(lambda: self.update_field('x1'))
        # self.ui.lineEdit_y0.textChanged.connect(lambda: self.update_field('y0'))
        # self.ui.lineEdit_y1.textChanged.connect(lambda: self.update_field('y1'))
        self.ui.lineEdit_x.textChanged.connect(lambda: self.update_field('x'))
        self.ui.lineEdit_y.textChanged.connect(lambda: self.update_field('y'))
        self.ui.pushButton_create_table.clicked.connect(self.create_table)
        self.n_points = 0
        self.lin_solver = LinSolver()
    
    def update_field(self, field):
        # try:
        #     if field == 'x0':
        #         x0 = float(self.ui.lineEdit_x0.text())
        #         m,n = self.lin_solver.set_x0(x0)
        #         self.ui.lineEdit_m.setText(str(m))
        #         self.ui.lineEdit_n.setText(str(n))
        #     elif field == 'x1':
        #         x1 = float(self.ui.lineEdit_x1.text())
        #         m,n = self.lin_solver.set_x1(x1)
        #         self.ui.lineEdit_m.setText(str(m))
        #         self.ui.lineEdit_n.setText(str(n))
        #     elif field == 'y0':
        #         y0 = float(self.ui.lineEdit_y0.text())
        #         m,n = self.lin_solver.set_y0(y0)
        #         self.ui.lineEdit_m.setText(str(m))
        #         self.ui.lineEdit_n.setText(str(n))        
        #     elif field == 'y1':
        #         y1 = float(self.ui.lineEdit_y1.text())
        #         m,n = self.lin_solver.set_y1(y1)
        #         self.ui.lineEdit_m.setText(str(m))
        #         self.ui.lineEdit_n.setText(str(n))
        # except:
        #     self.ui.lineEdit_m.setText('#')
        #     self.ui.lineEdit_n.setText('#')  
        if field == 'x':
            try:
                x = float(self.ui.lineEdit_x.text())
                y = self.lin_solver.get_y(x)
                self.update_text_blocking_signals(self.ui.lineEdit_y, str(y))
            except:
                self.update_text_blocking_signals(self.ui.lineEdit_y, '#')
        elif field == 'y':
            try:
                y = float(self.ui.lineEdit_y.text())
                x = self.lin_solver.get_x(y)
                self.update_text_blocking_signals(self.ui.lineEdit_x, str(x))
            except:
                self.update_text_blocking_signals(self.ui.lineEdit_x, '#')
    
    def update_text_blocking_signals(self, ui_obj, text):
        ui_obj.blockSignals(True)
        ui_obj.setText(text)
        ui_obj.blockSignals(False)
    
    def create_table(self):
        try:
            self.n_points = int(self.ui.lineEdit_n_points.text())
            self.ui.tableWidget_points.setRowCount(self.n_points)
        except:
            return

       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    solver = Solver(ui)
    MainWindow.show()
    sys.exit(app.exec_())