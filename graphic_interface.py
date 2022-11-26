#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import scrolledtext

from read_file import *
import read_file as rf
from main import *
import main as mn

# TODO Créer une fonction qui permet de choisir si on passe par le terminal ou si on passe par l'interface graphique
        # XXX Organiser des idées pour la partie terminal (par où on commence et par où on finir)
# TODO Create the interface completely and manage all the functions in (delete, save, open from file, etc)
# TODO REVOIR FUNCTION POUR GTF FILE


def interface_tkinter():
    window = tk.Tk() 
    window.title("DNA converter")
    window.geometry("1000x700") # TODO revoir taille pour début
    window.iconbitmap("images\dna_icon.ico")
    
    label_window = tk.Label(window, text = "DNA converter", font=("Arial", 22))
    label_window.grid(row=0, column=0, columnspan=4)

    label_choose = tk.Label(window, text = "Please enter your FASTA sequence here", font=("Arial", 15))
    label_choose.grid(row= 1, column= 0, columnspan=2)
    
    enter_fasta = tk.Text(window, width = 80, height = 20, font = ("Arial", 12))
    enter_fasta.grid(row = 2, column = 0, columnspan = 2)

    def clear_text():
        if enter_fasta != 0:
            enter_fasta.delete('1.0', END)

    def select_file_fasta():
        file_name = filedialog.askopenfilename(title="Select a file", filetypes=(("fasta files", "*.fa"), ("all files", "*.*")))
        file = rf.fasta(file_name)
        enter_fasta.insert(INSERT, file)

    buttom_fasta_file = tk.Button(window, text = "Add a Fasta file", command = select_file_fasta)
    buttom_fasta_file.grid(row = 3, column = 0, pady = 20)   
    
    def select_gtf_gff_fasta(): # faire en sorte de détecter qu'on a selectionne le fasta file
        file_name_fasta = filedialog.askopenfilename(title="Select a file", filetypes=(("fasta files", "*.fa"), ("all files", "*.*")))
        file_name = rf.fasta(file_name_fasta)
        
        file_name_gtf_gff = filedialog.askopenfilename(title="Select a file", filetypes=(("gtf files", "*.gtf"), ("gff files", "*.gff3"), ("all files", "*.*")))
        file_read_gff_gtf = rf.split(file_name_gtf_gff, file_name)

        enter_fasta.insert(INSERT, file_read_gff_gtf)
        
        
    

            

    buttom_gtf_gff_file = tk.Button(window, text = "Add a GTF/GFF file", command = select_gtf_gff_fasta)
    buttom_gtf_gff_file.grid(row = 4, column = 0, pady = 20)
    
    button_clean = tk.Button(window, text = "clean", width = 15, command = clear_text)
    button_clean.grid(row = 5, column = 0, pady = 15)
    
    
    def validate():
        label_result = scrolledtext.ScrolledText(window, width = 60, height = 10, font = ("Arial", 12))
        label_result.grid(row = 6, column = 0, columnspan = 2)
        if combobox_choices.get() == "ADN -> ARN":
            transcription_result = mn.transcription(enter_fasta.get("1.0",'end-1c'))
            label_result.insert(tk.INSERT, transcription_result)
        if combobox_choices.get() == "ARN -> Protein":
            traduction_result = mn.traduction(enter_fasta.get("1.0",'end-1c'))
            label_result.insert(tk.INSERT, traduction_result)
        if combobox_choices.get() == "ADN -> Protein":
            traduction_result_2 = mn.traduction(transcription(enter_fasta.get("1.0",'end-1c')))
            label_result.insert(tk.INSERT, traduction_result_2)
        
    

    button_validate = tk.Button(window, text = "validate", width = 15, command = validate)
    button_validate.grid(row = 5, column = 1, pady = 15)

    button_quit = tk.Button(window, text = "quit", width = 15, relief=tk.RAISED, command = window.destroy) # XXX Create a pop up to certify and maybe to ask if the user wants to save
    button_quit.grid(row = 5, column = 2, pady = 15)
    
    
    def combobox_get(label_file): # choisir le type de traduction en fonction du combobox
        if buttom_fasta_file == TRUE:
            pass
    
    combobox_choices = ttk.Combobox(window, values=["ADN -> ARN", 
                                                    "ARN -> Protein",
                                                    "ADN -> Protein"])
    

    
    combobox_choices.grid(row = 2, column = 2, padx = 10)
        


    window.mainloop()




if __name__ == '__main__':
    interface_tkinter()