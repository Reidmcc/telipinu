import tkinter as tk
from tkinter import N, W, E, S, messagebox
from tkinter import ttk
import glob
import server_conn_utils as s_utils
import db_ops


class TeliApp(tk.Tk):
    def __init__(self, **kwargs):
        super(TeliApp, self).__init__()

        self.title('Telipinu')
        self.home = HomeForm(self)
        self.home.grid(column=0, row=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        data_dir = 'C:\\Users\\Rominus\\test_data\\'
        dir_dbs = glob.glob('{}*.db'.format(data_dir))

        if len(dir_dbs) == 1:
            self.engine = s_utils.connect_extant(data_dir, dir_dbs[0])
        if len(dir_dbs) == 0:
            s_utils.create_sqlite(data_dir, 'telipinu_default.db')
            self.engine = s_utils.connect_extant(data_dir, 'telipinu_default.db')
        else:
            self.engine = s_utils.connect_extant(data_dir, 'telipinu_default.db')
        db_ops.check_core_tbls(self.engine)
        
    def report_callback_exception(self, exc, val, tb):
        messagebox.showerror("Error", message=str(val))


class HomeForm(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super(HomeForm, self).__init__()
        self.grid(column=0, row=0, sticky=(N, W, E, S))
        self.configure(width=100, height=50)

        data_dir = 'C:\\Users\\Rominus\\test_data\\'
        dir_dbs = glob.glob('{}*.db'.format(data_dir))
        
        self.person_list = ttk.Button(self, text='Open Person List')
        self.person_list.grid(column=0, row=0, sticky = (N,W,E,S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)
        for child in self.winfo_children(): child.grid_configure(padx=200, pady=50)


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
        
        
if __name__ == '__main__':
    app = TeliApp()
    app.lift()
    app.mainloop()
