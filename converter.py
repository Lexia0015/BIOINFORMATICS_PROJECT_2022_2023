#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

from read_file import *
import read_file as rf



def transcription(sequence:str) -> str:
    """
        Function that translates the sequence of DNA into RNA
        Args:
            sequence (str): sequence of DNA
        Returns:
            sequence_RNA (str) : sequence translated into RNA
    """
    
    # if "T" is in the sequence
    if "T" in sequence:
        # replace the line break for nothing and keep it in a variable named sequence_DNA
        sequence_DNA = sequence.replace("\n", "")
        # replace "T" into "A" and return the result
        return sequence_DNA.upper().replace("T", "U")


def traduction(sequence_rna:str, protein_sequence=""):
    """Function that traducts the RNA sequence into protein sequence

    Args:
        sequence_rna (str): sequence of RNA
        protein_sequence (str, optional): protein sequence

    Raises:
        Exception: If the length of the RNA is not a multiple of 3

    Returns:
        protein_sequence(str) : RNA sequence traducted into amino acids
    """
    # create a dictionary with the codons as key and the corresponding amino acids as value
    list_amino_acids = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
           'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
           'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
           'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
           'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A', 
           'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A', 
           'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A', 
           'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A', 
           'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D', 
           'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D', 
           'UAA':'*', 'CAA':'Q', 'AAA':'K', 'GAA':'E', 
           'UAG':'*', 'CAG':'Q', 'AAG':'K', 'GAG':'E', 
           'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G', 
           'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G', 
           'UGA':'*', 'CGA':'R', 'AGA':'R', 'GGA':'G', 
           'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}
    
    # put the rows of the RNA sequence into one long string by replacing the line break with an empty string
    sequence_rna.replace("\n", "")
    # find the AUG codon in the RNA sequence and keep it in a start variable
    start = sequence_rna.find('AUG')
    # for each third letter in the sequence 
    for letter in range(start, len(sequence_rna)-1, 3):
        # take the nucleotide and the following two and keep it in a variable codon
        codon = sequence_rna[letter:letter+3]
        # print(codon)
        # if the value in the dictionary of the codon key equals to "*" (which means STOP)
        if list_amino_acids[codon] == '*':
            # print(protein_sequence)
            # break the loop
            break
        # add the amino acid values of the codon keys to a variable 
        protein_sequence += list_amino_acids[codon]
    
    # return the protein sequence    
    return protein_sequence
    
        
       
# def main():
#     """
#         Function that provides a choice to the User
#         Args:
#             user_choice (str): the User has to choose a number between 1 and 3
#         Returns:
#             The previous functions according to the choice of the User
#     """
#     file_name = input("Path file fasta: " )
#     sequence_fasta = rf.fasta(file_name)
    
#     # create a variable that asks the user what to choose between different options
#     user_choice = input("""Chose what you want to do : \n
#                     1 = Transcription
#                     2 = Traduction
#                     3 = Transcription et Traduction\n""")
    
#     # if the user chooses "1"
#     if user_choice == "1":
#         # return the transcription of the DNA
#         print(transcription(sequence_fasta))
#     else:
#         # if the user chooses "2"
#         if user_choice == "2":
#             sys.setrecursionlimit(1000)
#             # return the traduction of the RNA
#             transcription_seq = transcription(sequence_fasta)
#             print(traduction(transcription_seq))
            
#         else:
#             # if the user chooses "3"
#             if user_choice == "3":
#                 # return the transcription and the traduction of the DNA
#                 transcripion_seq = transcription(sequence_fasta)
#                 print(transcripion_seq)
#                 print(traduction(transcripion_seq))
#             else:
#                 # if the user chooses 0 or nothing
#                 if user_choice == "0" or user_choice== "" :
#                     # return an error phrase
#                     print("You must choose a number between 1 and 3")
#                 # ask the user again what he wants to choose
#                 return main()
 
                
            
        


# if __name__ == '__main__':
#     main()

