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
    
    
    def select_multi_fasta():
        # allow the user to select a file of different type (fasta type) from the local server and keep it in a variable
        file_name = filedialog.askopenfilename(title="Select a multiple fasta", filetypes=(("fasta files", "*.fa"), ("all files", "*.*")))
        # extract the sequence from the selected file by using the fasta() function in the read_file.py and keep it in a variable
        file = rf.fasta(file_name)
        # insert the sequence in the text window
        enter_fasta.insert(INSERT, file)
        
    # create a button with the request to add a fasta file, use the select_multi_fasta() function as a command when pressing the button and keep it in a variable
    buttom_fasta_file_multiple = tk.Button(window, text = "Add a Multiple Fasta file", command = select_multi_fasta)
    # set the position of the button within the interface window
    buttom_fasta_file_multiple.grid(row = 3, column = 2)   
    
    
    # create a label for start
    entry_start_label = tk.Label(window, text = "Start index of the GTF")
    # show the label of start in tkinter according to the positions
    entry_start_label.grid(row = 4, column = 0)
    # create a label for start
    entry_end_label = tk.Label(window, text = "End index of the GTF")
    # show the label of end in tkinter according to the positions
    entry_end_label.grid(row = 4, column = 1)
    
    # create a start entry
    entry_start = tk.Entry(window)
    # show the start entry in the tkinter window according to the positions
    entry_start.grid(row = 5, column = 0)
    # create a start entry
    entry_end = tk.Entry(window)
    # show the end entry in the tkinter window according to the positions
    entry_end.grid(row = 5, column=1)
    
    
    
    def select_gtf_gff_fasta(): 
        """
            Function that allows the user to insert a wanted gtf/gff file and that extracts the sequence in the fasta file at the positions taken from the gtf file with the split() function from the read_fle.py4
            Returns :
                Sequence fasta with the positions start and end from the gtf file.
        """
        # if the text window is empty
        if enter_fasta.get("1.0",'end-1c') == "" :
            # add a label error with the following message
            label_error["text"] = "You must firstly choose a fasta file or enter a sequence"
            
        # if the text window is not empty
        if enter_fasta.get("1.0",'end-1c') != 0 and entry_start.get() != 0 and entry_end.get() != 0:
            # put the sequence from the text window into a variable
            file_name = enter_fasta.get("1.0",'end-1c')
            # allow the user to select a gtf, gff or different type file from the local server and keep it in a variable    
            file_gtf = filedialog.askopenfilename(title="Select a file", filetypes=(("gtf files", "*.gtf"), ("gff files", "*.gff3"), ("gff files", "*.gff"), ("all files", "*.*")))
            # extract the wanted sequence from the fasta sequence at the positions written in the gtf file by using the split() function from the read_file.py and keep it in a variable
            file_gtf_res = rf.split(file_gtf, file_name, int(entry_start.get()), int(entry_end.get()))
            
            # delete the text in the text field
            enter_fasta.delete('1.0', tk.END)
            # insert the wanted sequence into the text field
            enter_fasta.insert(INSERT, file_gtf_res)

        
            
    
    
        

    # create a button which tells the user to add a gtf/gff file, use the select_gft_gff_fasta() function as a command when pressing the button and keep it in a variable
    buttom_gtf_gff_file = tk.Button(window, text = "Add a GTF/GFF file", command = select_gtf_gff_fasta)
    # set the position of the button within the interface window
    buttom_gtf_gff_file.grid(row = 3, column = 1, pady = 20)
    
    # create a results label and set the font and fontsize
    label_resulttext = tk.Label(window, text = "Result:", font=("Arial", 15))
    # set the position of the results label
    label_resulttext.grid(row= 7, column= 0, columnspan=1)
    # set the background color of the results label to light blue
    label_resulttext.config(bg = "lightblue")
    
    # create a scrolled text field, set the size, font and fontsize and keep it in a variable
    label_result = scrolledtext.ScrolledText(window, width = 75, height = 8, font = ("Arial", 12))
    # set the position of the scrolled text field wihtin the interface window
    label_result.grid(row = 8, column = 0, columnspan = 3)
    
    
    def validate():
        """
            Function that converts the sequence from the text window into the wanted RNA or proteine sequence according to the selected combobox command.
            Returns :
                The sequence transcripted or translated depending on what the user wants.
        """
        # if the user the text window is empty: 
        if  enter_fasta.get("1.0",'end-1c') == "":
            # show an error with the following message
            label_error["text"] = "You must write a sequence on the scrolledtext or take a file"
        else:
            # if the combobox is not selected:
            if combobox_choices.get() == "" :
                # show an error with the following message
                label_error["text"] = "Make sure you choose a way to convert the sequence in the combobox !"
            else:
                # if the user chooses to transcript DNA into RNA
                if combobox_choices.get() == "ADN -> ARN":
                    # for every character in the text window:
                    for char in enter_fasta.get("1.0",'end-1c'):
                        # if the character is different than A, T, G and C:
                        if  char != "A" and char != "T" and char != "G" and char != "C":
                            # show an error with the following message
                            label_error["text"] = "The sequence can only contain A, T, G, C"
                            # break the loop
                            break
                        else:
                            # continue the loop
                            continue
                    # transcribe the sequence in the text window with the transcription() function from the converter.py and keep it in a variable
                    transcription_result = mn.transcription(enter_fasta.get("1.0",'end-1c'))
                    # insert the result from the variable into the result scrolled text field 
                    label_result.insert(tk.INSERT, transcription_result)
                # if the user selected the traduction from RNA to protein in the combobox    
                if combobox_choices.get() == "ARN -> Protein":
                    # if the length of the sequence that can be translated into protein is different than 0
                    if ((len(enter_fasta.get("1.0",'end-1c')))-1)%3 !=0:
                        # show an error label with the following message
                        label_error["text"] = "The length of the sequece must be a multiple of 3 ! Please remove 1 or 2 nucleotides !"
                    # for character in the text field:
                    for char in enter_fasta.get("1.0",'end-1c'):
                        # if the character is different than A, U, G, and C:
                        if  char != "A" and char != "U" and char != "G" and char != "C":
                            # show an error label with the following message
                            label_error["text"] = "The sequence can only contain A, U, G, C"
                            # break the loop
                            break
                        else:
                            # continue the following codes
                            continue
                    # traduct the sequence in the text window with the traduction() function from the converter.py and keep it in a variable
                    traduction_result = mn.traduction(enter_fasta.get("1.0",'end-1c'))
                    # put the result from the variable into the result scrolled text field
                    label_result.insert(tk.INSERT, traduction_result)
                # if the user selected the traduction from DNA to protein in the combobox
                if combobox_choices.get() == "ADN -> Protein":
                    # for character in the text field:
                    for char in enter_fasta.get("1.0",'end-1c'):
                        # if the length of the sequence that can be translated into proteins is different than 0:
                        if ((len(enter_fasta.get("1.0",'end-1c')))-1)%3 !=0:
                            # show an error label with the following text
                            label_error["text"] = "The length of the sequece must be a multiple of 3 ! Please remove 1 or 2 nucleotides !"
                        # if character is different than A, T, G and G:
                        if  char != "A" and char != "T" and char != "G" and char != "C":
                            # show an error label with the following text
                            label_error["text"] = "The sequence can only contain A, T, G, C"
                    
                    # translate and then traduct the sequence in the text window with both the translation() and the traducted() function from the converter.py and keep it in a variable    
                    traduction_result_2 = mn.traduction(transcription(enter_fasta.get("1.0",'end-1c')))
                    # put the result from the variable into the result scrolled text field
                    label_result.insert(tk.INSERT, traduction_result_2)
                    # erase all the error label
                    label_error.config(text = "")
            

    # create a combobox with the three choices what to convert into what and keep it in a variable
    combobox_choices = ttk.Combobox(window, values=["ADN -> ARN", 
                                                    "ARN -> Protein",
                                                    "ADN -> Protein"])
    # set the position of the combobox
    combobox_choices.grid(row = 2, column = 2, padx = 10)
    
    # create a validation button, set the width, use the validate() function as a command when pressing the button and keep it in a variable
    button_validate = tk.Button(window, text = "Validate", width = 15, relief=tk.RAISED, command = validate)
    # set the position of the validation button
    button_validate.grid(row = 6, column = 1, pady = 15, padx = 5)
    
    
    def clean_text(): 
        """
            Function that deletes the content of the sequence and results text fields, and label errors
        """
        # show the warning if the user is sure he wants to clean the fields with a clean button to validate and keep it in a variable
        message_warning = messagebox.showwarning("Clean", "Are you sure you want to clean the fields ?")
        # if the user is sure to clean the text fields
        if message_warning:
            # if the sequence text field is not empty
            if enter_fasta != 0:
                # delete the text field content
                enter_fasta.delete('1.0', END)
            # if the result scrolled text field is not empty
            if label_result != 0:
                # delete thescrolled text field content
                label_result.delete('0.0', END)
        # erase label error
        label_error["text"] = ""

    # create a clean button, set its width, use the clean_text() function as a command when pressing the button and keep it in a variable
    button_clean = tk.Button(window, text = "Clean", width = 15, relief=tk.RAISED, command = clean_text) 
    # set the position of the clean button in the interface window 
    button_clean.grid(row = 6, column = 0, pady = 15, padx = 5)


    def quit():
        """
            Function that quits the graphic interface and destroys the interface window
        """
        # show the warning if the user is sure he wants to quit with a quit button to validate and keep it in a variable
        message_quit = messagebox.showwarning("Quit", "Are you sure you want to quit ?")
        # if the user validates he wants to quit
        if message_quit:
            # destroy the interface window
            window.destroy()

    # create a quit button, set its width, use the quit() function as a command when pressing the button and keep it in a variable
    button_quit = tk.Button(window, text = "Quit", width = 15, relief=tk.RAISED, command = quit) 
    # set the position of the quit button within the interface window
    button_quit.grid(row = 6, column = 2, pady = 15, padx = 5)
    
    def save_results():
        """
            Function that saves the results from the scrolled text field as a text file
        """
        # if the result text field is not empty
        if label_result != 0:
            # show the warning if the user is sure he wants to save with a save button to validate and keep it in a variable
            message_save = messagebox.showwarning("Save", "Are you sure you want to save the results ?")
            # if the user validates he wants to save the results
            if message_save:
                # with opening a new text file in writing mode and keeping it in a variable
                with open("results.txt", 'w') as file_result:
                    # write the sequence from the result text field into the opened text file
                    file_result.write(label_result.get('1.0', tk.END))
    # create a save button, set the width, use the save_result() function as a command when pressing the button and keep it in a variable
    button_save = tk.Button(window, text = "Save", width = 15, relief=tk.RAISED, command = save_results) 
    # set the position of the save button within the interface window
    button_save.grid(row = 4, column = 2, pady = 15)
    
    

        


    # set the end of the interface window 
    window.mainloop()

    
