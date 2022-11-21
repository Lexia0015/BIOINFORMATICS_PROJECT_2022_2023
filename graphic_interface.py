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
    window.geometry("1400x900") # TODO revoir taille pour début
    window.iconbitmap("data\images\dna_icon.ico")
    
    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    label_window = tk.Label(main_frame, text = "Traducteur d'Éléments du Génome", font=("Arial", 22))
    label_window.pack()
    
    label_choose = tk.Label(main_frame, text = "What do you want to choose ?", font=("Arial", 15))
    label_choose.pack(pady=50)
    
    
    def go_page_2_sequence():
        top_page_2_sequence = Toplevel()
        top_page_2_sequence.geometry("900x1200")
        top_page_2_sequence.title("Sequence Page")
        page_2_sequence_label = tk.Label(top_page_2_sequence, text="Write a DNA/RNA sequence", font = ("Arial", 22))
        page_2_sequence_label.pack()
        top_page_2_sequence.mainloop()
        
        
        # Mettre soit des boutons soit des radiobutons
        
        
    def go_page_2_files():
        top_page_2_files = Toplevel()
        top_page_2_files.geometry("900x1200")
        top_page_2_files.title("Files Page")
        page_2_sequence_label = tk.Label(top_page_2_files, text="Select the Files", font = ("Arial", 22))
        page_2_sequence_label.pack()
        top_page_2_files.mainloop()
    
    

    button_files = tk.Button(main_frame, text="Select the Files", command = go_page_2_files)
    button_files.pack(pady = 30)
    
    button_sequence = tk.Button(main_frame, text="Write a DNA/RNA sequence", command = go_page_2_sequence)
    button_sequence.pack(pady = 30)

    
    buttom_frame = tk.Frame(window)
    buttom_frame.pack(side=tk.BOTTOM, padx=10)
    
    buttom_quit = tk.Button(buttom_frame, text = "Quit", relief=tk.RAISED, command = window.destroy)
    buttom_quit.pack(side = tk.BOTTOM, padx = 10)
    
    


    window.mainloop()


if __name__ == '__main__':
    interface_tkinter()