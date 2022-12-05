#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'



# TODO fasta() function to read multiple fastas
# TODO VOIR S'IL FAUT PAS SAUTER DE LIGNES POUR RESULTAT DANS TKINTER

import pandas as pd
import numpy as np


# from graphic_interface import select_file_fasta


import pathlib

from read_file import *
import read_file as rf


def control(file_name, file_gtf):
    """
        Function that will verify is the input data is correct
        Args:
            Input data : files data
        Returns:
            Error_control (str) : an error message if the data is not correct or a simply message that says Correct ! 
            TODO simply message a voir
    """
    if pathlib.Path(file_name).suffix != ".fa":
        raise Exception("You have to take a fasta file")
    elif pathlib.Path(file_gtf).suffix not in [".gtf",".gff",".gff3"]:
        raise Exception("You have to take a gtf or a gff file") 
    else:
        return True



def fasta(file_name):
    """
        Function that will read the Fasta file
        Args : Fasta file
    """
    file_fasta_read = open(file_name, "r") 
    fasta_content_file = file_fasta_read.readlines()
    # fasta_seq_line = fasta_content_file.split("\n")
    list_sequence = []
    for line in fasta_content_file:
        # if line.startswith(">"):
        #     line += "\n\n"
        #     # print(line)
        if line.find(">") != 0:
            list_sequence.append(line)
    # print(list_sequence)
    fasta_sequence = "".join(list_sequence)
    fasta_seq = fasta_sequence.upper().replace("\n", "")
    return fasta_seq




def split(file_gtf, fasta_sequence): 
    """
        It will read the gtf or gff file
        Take the position of the gene and extract the portion of the gene in the fasta file
        
        Args:
        
    """
    gtf_file = open(file_gtf, "r")
    pandas_columns = ["chromosome", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]
    pandas_gtf = pd.read_csv(gtf_file, header=None, sep="\t", comment="#", dtype=str, names=pandas_columns)
    column_feature = pandas_gtf.iloc[:,2]
    # print(column_feature)
    pandas_gene = pandas_gtf.loc[pandas_gtf["feature"] == "gene"]
    start_position = pandas_gene.iloc[:,3]
    # print(start_position)
    end_position = pandas_gene.iloc[:,4] 
    # print(start_position)
    # print(end_position)
    start_position_list = start_position.values.tolist()
    end_position_list = end_position.values.tolist()

    # print(start_position_list[0])
    # print(end_position_list)
    
    # fasta part
    liste = []
    # print(sequence_fasta, "\n")
    for i in range(1, 4):
        liste.append(fasta_sequence[int(start_position_list[i]):int(end_position_list[i])])
    fasta_sequence_gtf = "".join(liste)
    return fasta_sequence_gtf



def erreur(fasta_file, file_gtf): # TODO HAVE TO MAKE FOR GTF FILE / SEE WHY IT DOESN'T WORK
    """
        Function that will show different error messages if the sequence doesn't correspond with the user choices.
        Args:
            Input data : DNA ou RNA sequence from the Fasta file, or from an Entry, or from the GTF/GFF file
        Returns:
            Error (str) : an error message if it doesn't match
    """
    
    file_open_fasta = open(fasta_file, "r")
    file_content_fasta = file_open_fasta.readlines()

    # print(fasta_sequence)
    # if the len of the sequence is None
    if len(file_content_fasta) == 0:
        # Raise an exception based on the class SequenceIncorrect with the following message
        raise Exception("La séquence rentrée est incorrecte (= 0)")

    elif file_content_fasta[0].startswith(">"):
        # raise Exception ("The ID hasn't been cut ! Make sure you cut the ID")
        pass
    else:
        raise Exception("This file doesn't have an ID. Make sure you're fasta file begins with '>' !")
        
    fasta_sequence = fasta(fasta_file)
    # for each character on the sequence
    for char in fasta_sequence:
        # if the character is different thant A, and B, and C, and N, and T
        if char != "A" and char != "G" and char != "C" and char != "T" and char != "N":
            # Raise and exception based on the class SequenceIncorrect with the following message
            raise Exception("La sequence contient des autres lettres que A G C T N")
    
    # gtf/gff/gff3 part
    gtf_file = open(file_gtf, "r")
    
    pandas_columns = ["chromosome", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]
    pandas_gtf = pd.read_csv(gtf_file, header=None, sep="\t", comment="#", names=pandas_columns)
    print(pandas_gtf.dtypes)
    if pandas_gtf.empty == True:
        raise Exception("The Dataframe is empty !!!")
    for id in pandas_gtf.iloc[:,0]:
        if type(id) is not str:
            raise Exception("The first column of the GTF/GFF/GFF3 file must be in string format !")
        # elif id.startswith("NZ") == 0:
        #     raise Exception("The first column must contain the ID of the chromosome")
    for source in pandas_gtf.iloc[:, 0]:  # A REVOIR
        if type(source) is not str:
            raise Exception("The second column of the GTF/GFF/GFF3 file must be in string format !")
    for start in pandas_gtf.iloc[:,3]:
        if type(start) is not int:
            raise Exception("The column start must have integer data !")
    for end in pandas_gtf.iloc[:,3]:
        if type(end) is not int:
            raise Exception("The column end must have integer data !")
    for ltr in pandas_gtf.iloc[:, 6]:
        if ltr != "+" and ltr != "-": 
            raise Exception("The Strand column can only contain the + and - symbols")
        
        
    return True
        
    
        


if __name__ == "__main__":
    file_name = input("Path file fasta: " )
    file_gtf = input("Path file gtf: ")
    if control(file_name, file_gtf):
        if erreur(file_name, file_gtf):
            fasta_sequence = fasta(file_name)
            print(fasta_sequence)
        # gtf_split = split(file_gtf, fasta_sequence)
        # print(gtf_split)
    
        # print(fasta(file_name))
        # print("NO")
    
    # print(control())
    # print(erreur())

    # gtf_analysis = split(file_gtf, fasta_sequence)
    # print(gtf_analysis)
    
    
