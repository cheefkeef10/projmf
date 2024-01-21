from tkinter import *
from turtle import width
import customtkinter 
from tkinter import messagebox
from tkinter import ttk
from config import *


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


window = customtkinter.CTk()
window.title('Импорт xml в СУБД')

window.geometry("300x200+800+400")
window.resizable(width=False, height=False)


btnmain = customtkinter.CTkButton(window,text='Загрузить',command=load)
btnmain.place(x=80,y=110)

btnmain = customtkinter.CTkButton(window,text='Очистить',command=clear)
btnmain.place(x=80,y=50)




window.mainloop()