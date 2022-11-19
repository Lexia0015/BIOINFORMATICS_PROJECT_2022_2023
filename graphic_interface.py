#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

from tkinter import *
import tkinter as tk

# TODO Créer une fonction qui permet de choisir si on passe par le terminal ou si on passe par l'interface graphique
        # XXX Organiser des idées pour la partie terminal (par où on commence et par où on finir)
# TODO Create the interface completely and manage all the functions in (delete, save, open from file, etc)


def interface_tkinter():
    window = tk.Tk()
    window.title("Traducteur d'éléments du génome")
    window.geometry("1900x1400")
    
    label_window = tk.Label(window, text = "Traducteur d'Éléments du Génome")
    
    
    
    
    label_window.grid(row = 0, column=0, columnspan=4)
    
    
    
    
    
    window.mainloop()


if __name__ == '__main__':
    interface_tkinter()