# importing the module
import sqlite3
import sys
from PyQt5.QtWidgets import *

ROW_BATCH_COUNT = 10


class SqliteBrowser(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'sqlite_browser'
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 1000

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.fetch_data()
        self.create_table()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.show()


    def fetch_data(self):
        self.conn = sqlite3.connect("../data/hashes.sqlite")
        cursor = self.conn.cursor()
        self.data_fetched = cursor.execute('''SELECT * FROM safe_hashes''')

    def create_table(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)        
        for row, form in enumerate(self.data_fetched):
            self.tableWidget.insertRow(row)
            for column, item in enumerate(form):
                self.tableWidget.setItem(
                    row, column, QTableWidgetItem(str(item)))
                self.tableWidget.setItem(
                    row, column, QTableWidgetItem(str(item)))
        self.conn.close()

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SqliteBrowser()
    sys.exit(app.exec_())
