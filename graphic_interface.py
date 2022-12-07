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
from tkinter import messagebox

from read_file import *
import read_file as rf
from converter import *
import converter as mn


def interface_tkinter():
    """
        Function that creates an interface of the traductor
        Args:
            
        Returns: 
            Tkinter window of the graphic interface
    
    """
    # create a tkinter window and keep it in a variable
    window = tk.Tk() 
    # give the window a title
    window.title("DNA converter")
    # set the size of the window
    window.geometry("1000x800")
    # set the icon picture of the window by choosing a picture by path
    window.iconbitmap("images\dna_icon.ico")
    # set the background color of the window to light blue
    window.config(bg = "lightblue")
    
    # create a label for the title "DNA converter" in the interface window, set the font and font size and keep it in a variable
    label_window = tk.Label(window, text = "DNA converter\n", font=("Arial", 22))
    # set the position of the label within the interface window
    label_window.grid(row=0, column=0, columnspan=4)
    # set the background color of the label to light blue
    label_window.config(bg = "lightblue")

    # create a label to show the content of the fasta file, set the font and font size and keep it in a variable
    label_choose = tk.Label(window, text = "Please enter your FASTA sequence here", font=("Arial", 15))
    # set the position of the label within the interface window
    label_choose.grid(row= 1, column= 0, columnspan=1)
    # set the background color of the label to light blue
    label_choose.config(bg = "lightblue")
    
    # create a text window for the fasta file or to entry text, set the size, font and fontsize and keep it in a variable
    enter_fasta = tk.Text(window, width = 80, height = 15, font = ("Arial", 12))
    # set the position of the text window within the interface window  
    enter_fasta.grid(row = 2, column = 0, columnspan = 2, padx = 40)

    # create a label error that will show an error if the content is not correct for analysis
    label_error = tk.Label(window, text = "", font =("Arial", 12))
    # set the position of the label whithin the interface
    label_error.grid(row = 6, column = 1)
    # set the backgroung color of the label to light blue
    label_error.config(bg = "lightblue")


    def select_file_fasta():
        """
            Function that allows the user to insert a wanted fasta file and that extracts the sequence returned from the fasta() function from the read_fle.py
            Returns :
                Sequence fasta inserted in the text label.
        """
        # allow the user to select a file of different type (fasta type) from the local server and keep it in a variable
        file_name = filedialog.askopenfilename(title="Select a file", filetypes=(("fasta files", "*.fa"), ("all files", "*.*")))
        # extract the sequence from the selected file by using the fasta() function in the read_file.py and keep it in a variable
        file = rf.fasta(file_name)
        # insert the sequence in the text window
        enter_fasta.insert(INSERT, file)

    # create a button with the request to add a fasta file, use the select_file_fasta() function as a command when pressing the button and keep it in a variable
    buttom_fasta_file = tk.Button(window, text = "Add a Fasta file", command = select_file_fasta)
    # set the position of the button within the interface window
    buttom_fasta_file.grid(row = 3, column = 0, pady = 20)   
    
    
    
    def select_gtf_gff_fasta(): 
        """
            Function that allows the user to insert a wanted gtf/gff file and that extracts the sequence in the fasta file at the positions taken from the gtf file with the split() function from the read_fle.py4
            Returns :
                Sequence fasta with the positions start and end from the gtf file.
        """
        # if the text window is empty
        if enter_fasta.get("1.0",'end-1c') == "":
            # add a label error
            label_error["text"] = "You must firstly choose a fasta file or enter a sequence"
            
        if enter_fasta.get("1.0",'end-1c') != 0:
            file_name = enter_fasta.get("1.0",'end-1c')
                
            file_gtf = filedialog.askopenfilename(title="Select a file", filetypes=(("gtf files", "*.gtf"), ("gff files", "*.gff3"), ("gff files", "*.gff"), ("all files", "*.*")))
            file_gtf_res = rf.split(file_gtf, file_name)
            
            enter_fasta.delete('1.0', tk.END)
            enter_fasta.insert(INSERT, file_gtf_res)

        
            

    
        


    buttom_gtf_gff_file = tk.Button(window, text = "Add a GTF/GFF file", command = select_gtf_gff_fasta)
    buttom_gtf_gff_file.grid(row = 4, column = 0, pady = 20)
    
    label_resulttext = tk.Label(window, text = "Result:", font=("Arial", 15))
    label_resulttext.grid(row= 6, column= 0, columnspan=1)
    label_resulttext.config(bg = "lightblue")
    
    label_result = scrolledtext.ScrolledText(window, width = 75, height = 8, font = ("Arial", 12))
    label_result.grid(row = 7, column = 0, columnspan = 3)
    
    
    def validate():
        if  enter_fasta.get("1.0",'end-1c') == "":
            label_error["text"] = "You must write a sequence on the scrolledtext or take a file"
        else:

            if combobox_choices.get() == "" :
                label_error["text"] = "Make sure you choose a way to convert the sequence in the combobox !"
            else:
                if combobox_choices.get() == "ADN -> ARN":
                    for char in enter_fasta.get("1.0",'end-1c'):
                        if  char != "A" and char != "T" and char != "G" and char != "C":
                            label_error["text"] = "The sequence can only contain A, T, G, C"
                            break
                        else:
                            continue
                    transcription_result = mn.transcription(enter_fasta.get("1.0",'end-1c'))
                    label_result.insert(tk.INSERT, transcription_result)
                if combobox_choices.get() == "ARN -> Protein":
                    if ((len(enter_fasta.get("1.0",'end-1c')))-1)%3 !=0:
                        label_error["text"] = "The length of the sequece must be a multiple of 3 ! Please remove 1 or 2 nucleotides !"
                    for char in enter_fasta.get("1.0",'end-1c'):
                        if  char != "A" and char != "U" and char != "G" and char != "C":
                            label_error["text"] = "The sequence can only contain A, U, G, C"
                            break
                        else:
                            continue
                    traduction_result = mn.traduction(enter_fasta.get("1.0",'end-1c'))
                    label_result.insert(tk.INSERT, traduction_result)
                if combobox_choices.get() == "ADN -> Protein":
                    for char in enter_fasta.get("1.0",'end-1c'):
                        if ((len(enter_fasta.get("1.0",'end-1c')))-1)%3 !=0:
                            label_error["text"] = "The length of the sequece must be a multiple of 3 ! Please remove 1 or 2 nucleotides !"
                        
                        if  char != "A" and char != "T" and char != "G" and char != "C":
                            label_error["text"] = "The sequence can only contain A, T, G, C"
                        
                    traduction_result_2 = mn.traduction(transcription(enter_fasta.get("1.0",'end-1c')))
                    label_result.insert(tk.INSERT, traduction_result_2)
                    label_error.config(text = "")
            

    
    combobox_choices = ttk.Combobox(window, values=["ADN -> ARN", 
                                                    "ARN -> Protein",
                                                    "ADN -> Protein"])
    combobox_choices.grid(row = 2, column = 2, padx = 10)
    
    button_validate = tk.Button(window, text = "Validate", width = 15, relief=tk.RAISED, command = validate)
    button_validate.grid(row = 5, column = 1, pady = 15, padx = 5)
    
    
    def clean_text(): 
        message_warning = messagebox.showwarning("Clean", "Are you sure you want to clean the fields ?")
        if message_warning:
            if enter_fasta != 0:
                enter_fasta.delete('1.0', END)
            if label_result != 0:
                label_result.delete('0.0', END)
        label_error["text"] = ""

    button_clean = tk.Button(window, text = "Clean", width = 15, relief=tk.RAISED, command = clean_text) 
    button_clean.grid(row = 5, column = 0, pady = 15, padx = 5)


    def quit():
        message_quit = messagebox.showwarning("Quit", "Are you sure you want to quit ?")
        if message_quit:
            window.destroy()


    button_quit = tk.Button(window, text = "Quit", width = 15, relief=tk.RAISED, command = quit) 
    button_quit.grid(row = 5, column = 2, pady = 15, padx = 5)
    
    def save_results():
        if label_result != 0:
            message_save = messagebox.showwarning("Save", "Are you sure you want to save the results ?")
            if message_save:
                with open("results.txt", 'w') as file_result:
                    file_result.write(label_result.get('1.0', tk.END))
    
    button_save = tk.Button(window, text = "Save", width = 15, relief=tk.RAISED, command = save_results) 
    button_save.grid(row = 3, column = 2, pady = 15)
    
    

        



    window.mainloop()




if __name__ == '__main__':
    interface_tkinter()
    # file_name = input("Path fa :")
    # file_gtf = input("Path gtf : ")
    # file_gtf_res = rf.split(file_gtf, file_name)
    # print(file_gtf_res)
    
