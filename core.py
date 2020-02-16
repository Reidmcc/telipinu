import ui
import server_conn_utils as s_utils
import tkinter as tk
from tkinter import ttk, N, W, E, S

root = tk.Tk()
root.title('Telipinu')
home = ui.HomeForm(root)
home.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()

print('fin')
