import PySimpleGUI as sg
from main import User


class Gui:

    def __init__(self):
        self.user = User()

        sg.theme("darkgrey4")
        self.stk_name_txt = sg.Text("Stock Name")
        self.stk_code_txt = sg.Text("Stock Code")
        self.stk_price_txt = sg.Text("Stock Price")
        self.trade_type_txt = sg.Text("Trade Type")
        self.stk_quantity_txt = sg.Text("Stock Quantity")
        self.date_txt = sg.Text("Date of the trade")
        self.stk_name_input = sg.InputText(tooltip="Enter stock name bought or sold", key="stock_name", size=(10, 1))
        self.stk_code_input = sg.InputText(tooltip="Enter the stock code", key="stock_code", size=(10, 1))
        self.stk_price_input = sg.InputText(tooltip="Enter the price of the Stock at which you bought/sold for", key="stock_price", size=(10, 1))
        self.trade_type_input = sg.InputText(tooltip="Enter the Trade Type (Buy/Sell)", key="trade_type", size=(10, 1))
        self.stk_quantity_input = sg.InputText(tooltip="Enter the Quantity of the Stock bought/sold", key="stock_quantity", size=(10, 1))
        self.date_input = sg.InputText(tooltip="Date of the trade", key="date", size=(18, 1))
        self.info_box = sg.Listbox(values=self.user.read(), key='data_box', enable_events=True, size=(45, 10))
        self.add_button = sg.Button("Add to Journal", key="add_to_journal")
        self.delete_button = sg.Button("Delete", key="delete")
        self.show_data_button = sg.Button("Show Data Of Stock", tooltip="Show data of that stock name", key="related_data")
        self.buy_data_button = sg.Button("View Buy Trades", tooltip="Show all buy trades", key="buy_data")
        self.sell_data_button = sg.Button("View Sell Trades", tooltip="Show all sell trades", key="sell_data")
    def main_window(self):

        window1_layout = [[self.stk_name_txt, self.stk_code_txt, self.stk_price_txt, self.trade_type_txt, self.stk_quantity_txt, self.date_txt],
                         [self.stk_name_input, self.stk_code_input, self.stk_price_input, self.trade_type_input, self.stk_quantity_input, self.date_input],
                         [self.info_box, self.delete_button, self.show_data_button, self.add_button],
                         [self.buy_data_button, self.sell_data_button]]

        window1 = sg.Window("Stock Journal", layout=window1_layout,font=('Helvetica', 15))

        while True:
            event, values = window1.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "add_to_journal":
                self.user.write(values)
                # Updating the data in the data box in main gui
                window1['data_box'].update(values=self.user.read())
            if event == "delete":
                try:
                    self.user.delete(values)
                except:
                    sg.popup("Select one of the stock out of the shown data to delete it")
                window1['data_box'].update(values=self.user.read())
            if event == "related_data":
                try:
                    related_data = self.user.specific_read(event, values)
                    Gui.related_info_window(related_data)
                except:
                    sg.popup("Select one of the stock out of the shown data")
            if event == "buy_data":
                buy_data = self.user.specific_read(event, values)
                Gui.buy_trades_window(buy_data)
            if event == "sell_data":
                sell_data = self.user.specific_read(event, values)
                Gui.sell_trades_window(sell_data)

        window1.close()

    @staticmethod
    def related_info_window(related_data):
        related_info_box = sg.Listbox(values=related_data, key='related_box', enable_events=True, size=(45, 10))
        related_info_layout = [[related_info_box]]
        window2 = sg.Window("Related Data", layout=related_info_layout, font=('Helvetica', 15))
        while True:
            event, values = window2.read()
            if event == sg.WIN_CLOSED:
                break
            window2['related_box'].update(values=related_data)

        window2.close()

    @staticmethod
    def buy_trades_window(buy_data):
        buy_trades_box = sg.Listbox(values=buy_data, key='buy_data_box', enable_events=True, size=(45, 10))
        buy_trades_layout = [[buy_trades_box]]
        window3 = sg.Window("Buy Trades", layout=buy_trades_layout, font=('Helvetica', 15))
        while True:
            event, values = window3.read()
            if event == sg.WIN_CLOSED:
                break
            window3['buy_data_box'].update(values=buy_data)

        window3.close()

    @staticmethod
    def sell_trades_window(sell_data):
        sell_trades_box = sg.Listbox(values=sell_data, key='sell_data_box', enable_events=True, size=(45, 10))
        sell_trades_layout = [[sell_trades_box]]
        window4 = sg.Window("Sell Trades", layout=sell_trades_layout, font=('Helvetica', 15))
        while True:
            event, values = window4.read()
            if event == sg.WIN_CLOSED:
                break
            window4['sell_data_box'].update(values=sell_data)

        window4.close()




gui = Gui()
gui.main_window()



