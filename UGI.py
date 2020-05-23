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
root.title("GUI window")


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



#Edit Menu

edit_menu = Menu(menu_am)

#menu label
menu_am.add_cascade(label = "Edit",menu = edit_menu)



#search Menu

search_menu = Menu(menu_am)

#menu label
menu_am.add_cascade(label = "Search",menu = search_menu)

search_menu.add_cascade(label = "Find text")
search_menu.add_cascade(label = "Find Next")
search_menu.add_cascade(label ="Find Previous")
search_menu.add_cascade(label ="Replace")
search_menu.add_cascade(label ="Goto")


#tools Menu

tools_menu = Menu(menu_am)

#menu label
menu_am.add_cascade(label = "Tools",menu = tools_menu)


tools_menu.add_cascade(label = "New File")
tools_menu.add_cascade(label = "Save")
tools_menu.add_cascade(label ="Save As")
tools_menu.add_cascade(label ="Save All")
tools_menu.add_cascade(label ="print")
tools_menu.add_cascade(label = "Exit")

#View Menu

view_menu = Menu(menu_am)

#menu label
menu_am.add_cascade(label = "View",menu = view_menu)

view_menu.add_cascade(label = "New File")
view_menu.add_cascade(label = "Save")
view_menu.add_cascade(label ="Save As")
view_menu.add_cascade(label ="Save All")
view_menu.add_cascade(label ="print")
view_menu.add_cascade(label = "Exit")
#Help Menu

help_menu = Menu(menu_am)

#menu label
menu_am.add_cascade(label = "Help",menu = help_menu)


help_menu.add_cascade(label = "New File")
help_menu.add_cascade(label = "Save")
help_menu.add_cascade(label ="Save As")
help_menu.add_cascade(label ="Save All")
help_menu.add_cascade(label ="print")
help_menu.add_cascade(label = "Exit")

root.mainloop()