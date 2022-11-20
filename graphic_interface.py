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
    window.geometry("1900x1400") # TODO revoir taille pour début
    window.iconbitmap("data\images\dna_icon.ico")
    
    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    label_window = tk.Label(main_frame, text = "Traducteur d'Éléments du Génome", font=("Arial", 22))
    label_window.pack()
    
    label_choose = tk.Label(main_frame, text = "What do you want to choose ?", font=("Arial", 15))
    label_choose.pack(pady=50)
    
    var = tk.StringVar(main_frame, "1")
    radiobutton_files = tk.Radiobutton(main_frame, text="Select the Files", value="Files", variable=var)
    radiobutton_files.pack(pady = 30)
    
    radiobutton_sequence = tk.Radiobutton(main_frame, text="Write a DNA/RNA sequence", value="Sequence", variable=var)
    radiobutton_sequence.pack(pady = 30)

    
    buttom_frame = tk.Frame(window)
    buttom_frame.pack(side=tk.BOTTOM, padx=10)
    
    back_buttom = tk.Button(buttom_frame, text = "Back", relief=tk.RAISED)
    back_buttom.pack(side = tk.LEFT, padx = 10)
    
    next_button = tk.Button(buttom_frame, text = "Next", relief=tk.RAISED, command=lambda:page_2())
    next_button.pack(side = tk.RIGHT, pady=10)
    
    page_2_sequence = tk.Frame(main_frame)
    page_2_sequence_label = tk.Label(page_2_sequence, text="Write a DNA/RNA sequence", font = ("Arial", 22))
    page_2_sequence_label.pack()
    
    page_2_files = tk.Frame(main_frame)
    page_2_files = tk.Label(page_2_files, text="Select the Fasta and GTF/GFF files", font = ("Arial", 22))
    page_2_files.pack()
    
    pages = [page_2_files, page_2_sequence]
    count = 0
    
    def page_2():
        global count
        if not var.get():
            page = page_2_sequence
            page.pack(pady = 100)
        else:
            page = page_2_files
            page.pack(pady = 100)

    window.mainloop()


if __name__ == '__main__':
    interface_tkinter()