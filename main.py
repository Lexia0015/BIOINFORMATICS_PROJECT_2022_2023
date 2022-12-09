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
                        2 = Multi Fasta Analysis
                        3 = Interface\n
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
            # Ask the user if he wants to add a gtf file
            user_choice_file_gtf = input("""\nDo you want to use a gtf file?\n
                                    y = Yes
                                    n = No\n
            Your choice: """)
            
            

            # if the user wants to add a gtf file
            if user_choice_file_gtf == "y":
                # Ask the user to write the path of the gtf file he wants to use and keep it in a variable
                gtf_file_name = input("\nChoose your gtf file: ")
                # create a start where the user can choose a number
                start = int(input("Choose an index fort start :"))
                # create an end where the user can choose a number
                end = int(input("Choose an index for the end : "))
                if rf.control_fasta(file_name):
                    if rf.control_gtf(gtf_file_name):
                        if rf.erreur_fasta(file_name):
                            if rf.erreur_gtf(gtf_file_name):

                                # Get the sequence from the result of the fasta function and keep it in a variable
                                fasta_file = rf.fasta(file_name)
                                # Get the sequence from the fasta file with the positions from the gtf file and keep it in a variable by using the split function in the read_file.py
                                gtf_file = rf.split(gtf_file_name, fasta_file, start, end)
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
                                else:
                                    if user_choice_conversion != "1" and user_choice_conversion != "2" and user_choice_conversion != "3":
                                        # return an error phrase
                                        print("You must choose a number between 1 and 2")
                                        # ask the user again what he wants to choose
                                        return main()
                    
            # if the user does not want to add a gtf file            
            if user_choice_file_gtf == "n":
                if rf.control_fasta(file_name):
                    if rf.erreur_fasta(file_name):
                    # Get the sequence from the result of the fasta function and keep it in a variable
                        fasta_file = rf.fasta(file_name)
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
                else:
                    if user_choice_conversion != "1" and user_choice_conversion != "2" and user_choice_conversion != "3":
                        # return an error phrase
                        print("You must choose a number between 1 and 2")
                        # ask the user again what he wants to choose
                        return main()
            else:
                if user_choice_file_gtf != "y" and user_choice_file_gtf != "n" :
                    # return an error phrase
                    print("You must write 'y' or 'n'. Please mind to write it in lowercase.")
                    # ask the user again what he wants to choose
                    return main()
    
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
                # for letter in user_input_text:
                for ltr in user_input_text:
                    # if letter is different than A, G, T, and C:
                    if ltr != "A" and ltr != "G" and ltr != "T" and ltr != "C":
                        # raise an exception error with the following message
                        raise Exception("The text must contain A, T, C and G")   
                # print the transcripted RNA by using the transcription function from the converter.py file
                print(mn.transcription(user_input_text))
                        
            
            # if the user wants to convert the RNA sequence into Protein sequence
            if user_choice_conversion == "2":
                # for letter in user_input_text:
                for ltr in user_input_text:
                    # if letter is different than A, G, U, and C:
                    if ltr != "A" and ltr != "G" and ltr != "U" and ltr != "C":
                        # raise an exception error with the following message
                        raise Exception("The text must contain A, U, C and G")   
                
                # print the traducted amino acids by using the traduction function from the converter.py file
                print(mn.traduction(user_input_text))

            # if the user wants to convert the DNA sequence into Protein sequence
            if user_choice_conversion == "3" :
                # for letter in user_input_text:
                for ltr in user_input_text:
                    # if letter is different than A, G, T, and C:
                    if ltr != "A" and ltr != "G" and ltr != "T" and ltr != "C":
                        # raise an exception error with the following message
                        raise Exception("The text must contain A, T, C and G")
                # print the amino acids which has been translated into RNA before by using first the translation function and then the traduction function from the converter.py file
                print(mn.traduction(transcription(user_input_text)))
            
            else:
                if user_choice_conversion != "1" and user_choice_conversion != "2" and user_choice_conversion != "3":
                    # return an error phrase
                    print("You must choose a number between 1 and 3")
                    # ask the user again what he wants to choose
                    return main()  
        else:
            if user_choice_args != "1" and user_choice_args != "2" :
                # return an error phrase
                print("You must choose a number between 1 and 2")
                # ask the user again what he wants to choose
                return main()
                
   
    
    if users_choice_envs == "2" :
        file_name = input("\nChoose your Fasta file: ")
        if rf.control_fasta(file_name):
            if rf.erreur_fasta(file_name):
                multiple_fasta = rf.read_multiple_fasta(file_name)
                print(multiple_fasta)
                
                # Ask the user what he wants to convert into what : DNA to RNA, RNA to Protein, or DNA to protein
                user_choice_conversion = input("""\nWhat do you want to convert?\n
                                            1 = DNA -> RNA
                                            2 = RNA -> Protein
                                            3 = DNA -> Protein\n
                Your choice: """)
                
                # if the user wants to convert the DNA sequence into RNA sequence
                if user_choice_conversion == "1":
                    # print the transcripted RNA by using the transcription function from the converter.py file
                    print(mn.transcription(multiple_fasta))

                # if the user wants to convert the RNA sequence into Protein sequence
                if user_choice_conversion == "2":
                    # print the traducted amino acids by using the traduction function from the converter.py file
                    print(mn.traduction(multiple_fasta))

                # if the user wants to convert the DNA sequence into Protein sequence
                if user_choice_conversion == "3" :
                    # print the amino acids which has been translated into RNA before by using first the translation function and then the traduction function from the converter.py file
                    print(mn.traduction(transcription(multiple_fasta)))

    
    
     # if the user wants to use the Interface
    if users_choice_envs == "3" :
        # Excecute graphic_interface.py
        gi.interface_tkinter()
    
    else:
        if users_choice_envs != "1" and users_choice_envs != "2" and users_choice_envs != "3":
            # return an error phrase
            print("You must choose a number between 1, 2 and 3")
            # ask the user again what he wants to choose
            return main()
        
        
        
if __name__ =='__main__':
    main()
    