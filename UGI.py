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


tools_menu.add_cascade(label = "Referance")
tools_menu.add_cascade(label = "Install")
tools_menu.add_cascade(label ="Update")
tools_menu.add_cascade(label ="Account")

#View Menu

view_menu = Menu(menu_am)

#menu label
menu_am.add_cascade(label = "View",menu = view_menu)

view_menu.add_cascade(label = "Toolbar")
view_menu.add_cascade(label = "Hide Toolbar")
view_menu.add_cascade(label ="User Layouts")
view_menu.add_cascade(label ="Window Layout")


help_menu = Menu(menu_am)

#menu label
menu_am.add_cascade(label = "Help",menu = help_menu)


help_menu.add_cascade(label = "Documentation")
help_menu.add_cascade(label = "Tutarial")
help_menu.add_cascade(label ="Report")
help_menu.add_cascade(label ="About")


root.mainloop()