#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:02:24 2020

@author: hossain
"""


# GUI on python


# import module for GUI and messagebox


from tkinter import *






root = Tk()
root.geometry("800x600")
menu_am = Menu(root)
root.config(menu = menu_am)


#File Menu

file_menu = Menu(menu_am)

#Add label
menu_am.add_cascade(label = "File",menu = file_menu)

file_menu.add_cascade(label = "New File")
file_menu.add_cascade(label = "Save")
file_menu.add_cascade(label ="Save As")
file_menu.add_cascade(label ="Save All")
file_menu.add_cascade(label ="print")
file_menu.add_cascade(label = "Exit")


root.mainloop()