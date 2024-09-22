import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter



customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
window = customtkinter.CTk()
window.title("Document Scanner")
window.geometry("1080x720")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')
lbl1 = Label(tab1, text= 'label1')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text= 'label2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')

scrollable_frame = customtkinter.CTkScrollableFrame(window, width=200, height=200)


sample_data = ["Plan A", "Plan B", "Plan C"]
combobox = customtkinter.CTkComboBox(window, values=sample_data)
combobox.pack()
combobox.set("Select a Plan")
# w = Label(window, text="Document Scanner")
# w.pack()
 
button = customtkinter.CTkButton(window, text="Import Image", width=25, command=window.destroy)
button.place(relx = 0.5, rely= 0.5, anchor=CENTER)


window.mainloop()