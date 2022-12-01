#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

import pandas as pd
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import scrolledtext
from pathlib import Path

from read_file import *
import read_file as rf
from converter import *
import converter as mn

# TODO Créer une fonction qui permet de choisir si on passe par le terminal ou si on passe par l'interface graphique
        # XXX Organiser des idées pour la partie terminal (par où on commence et par où on finir)
# TODO Create the interface completely and manage all the functions in (delete, save, open from file, etc)
# TODO finir dernière partie de gtf bouton function



def interface_tkinter():
    window = tk.Tk() 
    window.title("DNA converter")
    window.geometry("1000x800")
    window.iconbitmap("images\dna_icon.ico")
    window.config(bg = "lightblue")
    
    label_window = tk.Label(window, text = "DNA converter", font=("Arial", 22))
    label_window.grid(row=0, column=0, columnspan=4)

    label_choose = tk.Label(window, text = "Please enter your FASTA sequence here", font=("Arial", 15))
    label_choose.grid(row= 1, column= 0, columnspan=3)
    
    enter_fasta = tk.Text(window, width = 80, height = 20, font = ("Arial", 12))
    enter_fasta.grid(row = 2, column = 0, columnspan = 2, padx = 40)


    def select_file_fasta():
        file_name = filedialog.askopenfilename(title="Select a file", filetypes=(("fasta files", "*.fa"), ("all files", "*.*")))
        file = rf.fasta(file_name)
        enter_fasta.insert(INSERT, file)

    buttom_fasta_file = tk.Button(window, text = "Add a Fasta file", command = select_file_fasta)
    buttom_fasta_file.grid(row = 3, column = 0, pady = 20)   
    
    
    def select_gtf_gff_fasta(): 
        
        if enter_fasta.get("1.0", tk.END) != 0:
            file_name = enter_fasta.get("1.0", tk.END)
                
            file_gtf = filedialog.askopenfilename(title="Select a file", filetypes=(("gtf files", "*.gtf"), ("gff files", "*.gff3"), ("gff files", "*.gff"), ("all files", "*.*")))
            file_gtf_res = rf.split(file_gtf, file_name)
            
            enter_fasta.delete('1.0', tk.END)
            enter_fasta.insert(INSERT, file_gtf_res)
        # else:
            # make error label

    
        


    buttom_gtf_gff_file = tk.Button(window, text = "Add a GTF/GFF file", command = select_gtf_gff_fasta)
    buttom_gtf_gff_file.grid(row = 4, column = 0, pady = 20)
    
    label_result = scrolledtext.ScrolledText(window, width = 60, height = 8, font = ("Arial", 12))
    label_result.grid(row = 6, column = 0, columnspan = 3)
    
    
    def validate():
        if combobox_choices.get() == "ADN -> ARN":
            transcription_result = mn.transcription(enter_fasta.get("1.0",'end-1c'))
            label_result.insert(tk.INSERT, transcription_result)
        if combobox_choices.get() == "ARN -> Protein":
            traduction_result = mn.traduction(enter_fasta.get("1.0",'end-1c'))
            label_result.insert(tk.INSERT, traduction_result)
        if combobox_choices.get() == "ADN -> Protein":
            traduction_result_2 = mn.traduction(transcription(enter_fasta.get("1.0",'end-1c')))
            label_result.insert(tk.INSERT, traduction_result_2)
        
    
    def clean_text(): # TODO METTRE MESSAGEBOX
        if enter_fasta != 0:
            enter_fasta.delete('1.0', END)
        if label_result != 0:
            label_result.delete('0.0', END)
    
    combobox_choices = ttk.Combobox(window, values=["ADN -> ARN", 
                                                    "ARN -> Protein",
                                                    "ADN -> Protein"])
    combobox_choices.grid(row = 2, column = 2, padx = 10)
    

    button_clean = tk.Button(window, text = "Clean", width = 15, relief=tk.RAISED, command = clean_text) # TODO VOIR MISE EN FORME AVEC STICKY
    button_clean.grid(row = 5, column = 0, pady = 15, padx = 5)

    button_validate = tk.Button(window, text = "Validate", width = 15, relief=tk.RAISED, command = validate)
    button_validate.grid(row = 5, column = 1, pady = 15, padx = 5)

    button_quit = tk.Button(window, text = "Quit", width = 15, relief=tk.RAISED, command = window.destroy) # XXX Create a pop up to certify and maybe to ask if the user wants to save and quit
    button_quit.grid(row = 5, column = 2, pady = 15, padx = 5)
    
    def save_results():
        pass
    
    button_save = tk.Button(window, text = "Save", width = 15, relief=tk.RAISED, command = print("Hello")) # XXX Create a pop up to certify and maybe to ask if the user wants to save
    button_save.grid(row = 3, column = 2, pady = 15)
    
    

        



    window.mainloop()




if __name__ == '__main__':
    interface_tkinter()
    # file_name = input("Path fa :")
    # file_gtf = input("Path gtf : ")
    # file_gtf_res = rf.split(file_gtf, file_name)
    # print(file_gtf_res)
    
