# importing the module
import sqlite3
import sys
from PyQt5.QtWidgets import * 

ROW_BATCH_COUNT = 10

class App(QWidget): 
    def __init__(self): 
        super().__init__() 
        self.title = 'sqlite_browser'
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 1000
   
        self.setWindowTitle(self.title) 
        self.setGeometry(self.left, self.top, self.width, self.height) 
   
        self.createTable() 
   
        self.layout = QVBoxLayout() 
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        self.show() 
   
    def createTable(self): 
        conn = sqlite3.connect("../data/hashes.sqlite")
        cursor = conn.cursor()
        self.tableWidget = QTableWidget() 
        result = cursor.execute('''SELECT * FROM safe_hashes''')
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2) 
        for row, form in enumerate(result):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
        conn.close()
   
        self.tableWidget.horizontalHeader().setStretchLastSection(True) 
        self.tableWidget.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch) 
   
if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    ex = App() 
    sys.exit(app.exec_()) 
