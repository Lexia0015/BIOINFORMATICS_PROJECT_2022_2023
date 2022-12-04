#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

# TODO voir comment ça s'encadre avec Tkinter

import pathlib

from read_file import *
import read_file as rf


def control():
    """
        Function that will verify is the input data is correct
        Args:
            Input data : files data
        Returns:
            Error_control (str) : an error message if the data is not correct or a simply message that says Correct ! 
            TODO simply message a voir
    """
    file_name = input("Path fa file : ")
    file_gtf = input("Path gtf file : ")
    if pathlib.Path(file_name).suffix != ".fa":
        raise Exception("You have to take a fasta file")
    if pathlib.Path(file_gtf).suffix not in [".gtf",".gff",".gff3"]:
        raise Exception("You have to take a gtf or a gff file") 


def erreur(): # TODO HAVE TO MAKE FOR GTF FILE / SEE WHY IT DOESN'T WORK
    """
        Function that will show different error messages if the sequence doesn't correspond with the user choices.
        Args:
            Input data : DNA ou RNA sequence from the Fasta file, or from an Entry, or from the GTF/GFF file
        Returns:
            Error (str) : an error message if it doesn't match
    """
    fasta_file = input("Path fa file : ")
    file_gtf = input("Path gtf file : ")
    
    file_open_fasta = open(fasta_file, "r")
    file_content_fasta = file_open_fasta.readlines()

    fasta_sequence = rf.fasta(fasta_file)
    # print(fasta_sequence)
    # if the len of the sequence is None
    if len(file_content_fasta) == 0:
        # Raise an exception based on the class SequenceIncorrect with the following message
        raise Exception("La séquence rentrée est incorrecte (= 0)")
    
    for line in file_content_fasta:
        if ">" in line:
            raise Exception ("The ID hasn't been cut ! Make sure you cut the ID")
        
    # # for each character on the sequence
    # for c in fasta_sequence:
    #     # if the character is different thant A, and B, and C, and N, and T
    #     if c != 'A' and c != 'G' and c != 'C' and c != 'T' and c != "N":
    #         # Raise and exception based on the class SequenceIncorrect with the following message
    #         raise Exception("La sequence contient des autres lettres que A G C T")
        
    
        
    


# print(control())
print(erreur())

