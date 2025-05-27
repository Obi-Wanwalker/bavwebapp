def r_todos(filee='todos.txt'):
    with open('todos.txt','r') as a:
        c=a.readlines()
    return c

def w_todos(tl,filee='todos.txt'):
    with open('todos.txt','w') as b :
        b.writelines(tl)
'''
import FreeSimpleGUI as sg

sg.theme_previewer()'''