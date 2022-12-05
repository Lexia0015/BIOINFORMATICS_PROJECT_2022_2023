#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

from graphic_interface import *
import graphic_interface as gi
def main(): 
    """
        Function that provides a choice to the User
        Args:
            user_choice (str): the User has to choose a number between 1 and 3
        Returns:
            The previous functions according to the choice of the User
    """
    users_choice_envs = input("""Choose where you want to work: \n
                        1 = Terminal
                        2 = Interface\n
    Your choice: """)
    #if the user chooses 1
    if users_choice_envs == "1":
        user_choice_args = input("""\nWhat do you want to choose?\n
                            1 = Fasta file 
                            2 = Text\n

        Your choice: """)
        if user_choice_args == "1":
            file_name = input("\nChoose your Fasta file: ")
            fasta_file = rf.fasta(file_name)
            
            user_choice_file_gtf = input("""\nDo you want to use a gtf file?\n
                                    y = Yes
                                    n = No\n
            Your choice: """)


            if user_choice_file_gtf == "y":
                gtf_file_name = input("\nChoose your gtf file: ")
                gtf_file = rf.split(gtf_file_name, fasta_file)
                print(gtf_file)
                
                user_choice_conversion = input("""\nWhat do you want to convert?\n
                                            1 = ADN -> ARN
                                            2 = ARN -> Protein
                                            3 = ADN -> Protein\n
                Your choice: """)
                
                if user_choice_conversion == "1":
                    print(mn.transcription(gtf_file))

                if user_choice_conversion == "2":
                    print(mn.traduction(gtf_file))

                if user_choice_conversion == "3" :
                    print(mn.traduction(transcription(gtf_file)))
                                
            if user_choice_file_gtf == "n":
                print(fasta_file)

                user_choice_conversion = input("""\nWhat do you want to convert?\n
                                            1 = ADN -> ARN
                                            2 = ARN -> Protein
                                            3 = ADN -> Protein\n
                Your choice: """)
                
                if user_choice_conversion == "1":
                    print(mn.transcription(fasta_file))

                if user_choice_conversion == "2":
                    print(mn.traduction(fasta_file))

                if user_choice_conversion == "3" :
                    print(mn.traduction(transcription(fasta_file)))
                    
        if user_choice_args == "2":
            pass      


    if users_choice_envs == "2" :
        gi.interface_tkinter()


if __name__ =='__main__':
    main()
    