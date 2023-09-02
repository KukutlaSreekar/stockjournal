import PySimpleGUI as sg
import sqlite3
import os

path = "data.db"


class User:
    def __init__(self):
        if not os.path.exists(path):
            conn_1 = sqlite3.connect(path)
            cursor_1 = conn_1.cursor()

            cursor_1.execute("CREATE TABLE stocks_history(Stock_Name TEXT, Stock_Code TEXT, Stock_Price REAL,"
                             " Trade_Type TEXT, Quantity REAL, Date TEXT  )")
            conn_1.commit()
            conn_1.close()

        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

    def write(self, data_values):
        data_values = list(data_values.values())[:6]
        data_values
        self.cursor.execute("INSERT INTO stocks_history VALUES(?,?,?,?,?,?)", data_values)
        self.connection.commit()

    def read(self):
        # To read everything in the database
        self.cursor.execute("SELECT * FROM stocks_history")
        data = self.cursor.fetchall()
        return data

    def specific_read(self, event ,values):
        # To read something specific in the database
        if event == "related_data":
            stock_name = values["data_box"][0][0]
            stock_name = str(stock_name)
            self.cursor.execute("SELECT * FROM stocks_history WHERE Stock_Name=?", (stock_name,))
            related_data = self.cursor.fetchall()
            return related_data
        elif event == "buy_data":
            self.cursor.execute("SELECT * FROM stocks_history WHERE Trade_Type=? OR Trade_Type=? ", ("Buy", "buy"))
            buy_data = self.cursor.fetchall()
            return buy_data
        elif event == "sell_data":
            self.cursor.execute("SELECT * FROM stocks_history WHERE Trade_Type=? OR Trade_Type=? ", ("Sell", "sell"))
            sell_data = self.cursor.fetchall()
            return sell_data



    def delete(self, values):
        row_to_delete = values["data_box"][0]
        self.cursor.execute("DELETE FROM stocks_history WHERE Stock_Name=? AND Stock_Code=? AND Stock_Price=? AND "
                            "Trade_Type=? AND Quantity=? AND DATE=?", row_to_delete)
        self.connection.commit()







