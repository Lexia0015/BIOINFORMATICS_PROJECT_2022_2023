#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

from graphic_interface import *
import graphic_interface as gi
from read_file import *
import read_file as rf
from converter import *
import converter as mn

def main(): 
    """
        Function that provides a choice to the User
        Args:
            user_choice (str): the User has to choose a number between 1 and 3
        Returns:
            The previous functions according to the choice of the User
    """
    # Ask the user which environment he wants to use
    users_choice_envs = input("""Choose where you want to work: \n
                        1 = Terminal
                        2 = Interface\n
    Your choice: """)
    # if the user wants to use the Terminal
    if users_choice_envs == "1":
        # Ask the user what file format he wants to use
        user_choice_args = input("""\nWhat do you want to choose?\n
                            1 = Fasta file 
                            2 = Text\n

        Your choice: """)
        # if the user chooses a fasta file
        if user_choice_args == "1":
            # Ask the user to write the path of the fasta file he wants to use and keep it in a variable
            file_name = input("\nChoose your Fasta file: ")
            # Get the sequence from the result of the fasta function and keep it in a variable
            fasta_file = rf.fasta(file_name)
            # Ask the user if he wants to add a gtf file
            user_choice_file_gtf = input("""\nDo you want to use a gtf file?\n
                                    y = Yes
                                    n = No\n
            Your choice: """)

            # if the user wants to add a gtf file
            if user_choice_file_gtf == "y":
                # Ask the user to write the path of the gtf file he wants to use and keep it in a variable
                gtf_file_name = input("\nChoose your gtf file: ")
                # Get the sequence from the fasta file with the positions from the gtf file and keep it in a variable by using the split function in the read_file.py
                gtf_file = rf.split(gtf_file_name, fasta_file)
                # Print the sequence result of the split function 
                print(gtf_file)
                
                # Ask the user what he wants to convert into what : DNA to RNA, RNA to Protein, or DNA to protein
                user_choice_conversion = input("""\nWhat do you want to convert?\n
                                            1 = DNA -> RNA
                                            2 = RNA -> Protein
                                            3 = DNA -> Protein\n
                Your choice: """)
                
                # if the user wants to convert the DNA sequence into RNA sequence
                if user_choice_conversion == "1":
                    # print the transcripted RNA by using the transcription function from the converter.py file
                    print(mn.transcription(gtf_file))

                # if the user wants to convert the RNA sequence into Protein sequence
                if user_choice_conversion == "2":
                    # print the traducted amino acids by using the traduction function from the converter.py file
                    print(mn.traduction(gtf_file))

                # if the user wants to convert the DNA sequence into Protein sequence
                if user_choice_conversion == "3" :
                    # print the amino acids which has been translated into RNA before by using first the translation function and then the traduction function from the converter.py file
                    print(mn.traduction(transcription(gtf_file)))
                    
            # if the user does not want to add a gtf file            
            if user_choice_file_gtf == "n":
                # print the sequence from the fasta file by using the variable where it has been kept
                print(fasta_file)

                # Ask the user what he wants to convert into what : DNA to RNA, RNA to Protein, or DNA to protein
                user_choice_conversion = input("""\nWhat do you want to convert?\n
                                            1 = DNA -> RNA
                                            2 = RNA -> Protein
                                            3 = DNA -> Protein\n
                Your choice: """)
                
                # if the user wants to convert the DNA sequence into RNA sequence
                if user_choice_conversion == "1":
                    # print the transcripted RNA by using the transcription function from the converter.py file
                    print(mn.transcription(fasta_file))
                
                # if the user wants to convert the RNA sequence into Protein sequence
                if user_choice_conversion == "2":
                    # print the traducted amino acids by using the traduction function from the converter.py file
                    print(mn.traduction(fasta_file))

                # if the user wants to convert the DNA sequence into Protein sequence
                if user_choice_conversion == "3" :
                    # print the amino acids which has been translated into RNA before by using first the translation function and then the traduction function from the converter.py file
                    print(mn.traduction(transcription(fasta_file)))
        
        # if the user wants to use a text file            
        if user_choice_args == "2":
            user_input_text = input("Write your fasta sequence :\n")

            # Ask the user what he wants to convert into what : DNA to RNA, RNA to Protein, or DNA to protein
            user_choice_conversion = input("""\nWhat do you want to convert?\n
                                            1 = DNA -> RNA
                                            2 = RNA -> Protein
                                            3 = DNA -> Protein\n
                Your choice: """)
            
            
            # if the user wants to convert the DNA sequence into RNA sequence
            if user_choice_conversion == "1":
                if user_input_text != "A" and user_input_text != "G" and user_input_text != "T" and user_input_text != "C":
                    raise Exception("The text must contain A, T, C and G")
                else:
                # print the transcripted RNA by using the transcription function from the converter.py file
                    print(mn.transcription(user_input_text))
            
            # if the user wants to convert the RNA sequence into Protein sequence
            if user_choice_conversion == "2":
                if user_input_text != "A" and user_input_text != "G" and user_input_text != "U" and user_input_text != "C":
                    raise Exception("The text must contain A, U, C and G")
                else:
                # print the traducted amino acids by using the traduction function from the converter.py file
                    print(mn.traduction(user_input_text))

            # if the user wants to convert the DNA sequence into Protein sequence
            if user_choice_conversion == "3" :
                if user_input_text != "A" and user_input_text != "G" and user_input_text != "T" and user_input_text != "C":
                    raise Exception("The text must contain A, T, C and G")
                else:
                # print the amino acids which has been translated into RNA before by using first the translation function and then the traduction function from the converter.py file
                    print(mn.traduction(transcription(user_input_text)))
                
    # if the user wants to use the Interface
    if users_choice_envs == "2" :
        # Excecute graphic_interface.py
        gi.interface_tkinter()


if __name__ =='__main__':
    main()
    