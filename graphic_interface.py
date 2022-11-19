#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'

from tkinter import *
import tkinter as tk

def interface_tkinter():
    window = tk.Tk()
    window.title("Traducteur d'éléments du génome")
    window.geometry("1900x1400")
    
    label_window = tk.Label(window, text = "Traducteur d'Éléments du Génome")
    
    
    
    
    label_window.grid(row = 0, column=0, columnspan=4)
    
    
    
    
    
    window.mainloop()


if __name__ == '__main__':
    interface_tkinter()