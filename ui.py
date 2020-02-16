import tkinter as tk
from tkinter import N, W, E, S
from tkinter import ttk
import glob
import server_conn_utils as s_utils

class HomeForm(ttk.Frame):
    def __init__(self, parent):
        super(HomeForm, self).__init__()
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        data_dir = 'C:\\Users\\Rominus\\test_data\\'
        dir_dbs = glob.glob('{}*.db'.format(data_dir))
        try:
            if len(dir_dbs) == 1:
                engine = s_utils.connect_extant(dir_dbs[0])
            if len(dir_dbs) == 0:
                s_utils.create_sqlite('{}\\telipinu_default.db'.format(data_dir))
                engine = engine = s_utils.connect_extant('{}\\telipinu_default.db'.format(data_dir))
        except Exception as e:
            parent.lower()
            err = ErrorBox(self, e, plus_txt= """
                Database connection failed:
                """
                )
            

        self.person_list = ttk.Button(self, text='Open Person List')
        self.person_list.grid(column=0, row=0, sticky = (N,W,E,S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)
        for child in self.winfo_children(): child.grid_configure(padx=5, pady=5)

class ErrorBox(tk.Toplevel):
    def __init__(self, parent, my_error, plus_txt=None):
        super(ErrorBox, self).__init__()

        if plus_txt:
            self.plus_display = ttk.Label(self, text=plus_txt)
            self.plus_display.grid(column=0, row=0)

        self.error_display = ttk.Label(self, text=my_error.with_traceback)
        self.error_display.grid(column=1, row=1, sticky=(W))
        
        self.btn_close = ttk.Button(self, text='Close', command=self.close_me)
        self.btn_close.grid(column=0, row=2, sticky=(W))

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.lift()

    def close_me(self):
        self.destroy()
        
