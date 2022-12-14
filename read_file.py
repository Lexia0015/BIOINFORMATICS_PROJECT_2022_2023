#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'


import pandas as pd
import numpy as np
import pathlib

from read_file import *
import read_file as rf
from converter import *
import converter as ct


def control_fasta(file_name):
    """
        Function that will verify is the input data is correct
        Args:
            Input data : files data
        Returns:
            Error_control (str) : an error message if the data is not correct or a simply message that says Correct ! 
            TODO simply message a voir
    """
    # if user inserts a file which has not a fasta extension
    if pathlib.Path(file_name).suffix != ".fa":
        # raise an exception to tell the user he has to insert a fasta file
        raise Exception("You have to take a fasta file")
    # else return True
    else:
        return True

def control_gtf(file_gtf):
    """
        Function that will verify is the input data is correct
        Args:
            Input data : files data
        Returns:
            Error_control (str) : an error message if the data is not correct or a simply message that says Correct ! 
            TODO simply message a voir
    """
    # else if the user inserts a file which is not in a gtf, gff or gff3 format
    if pathlib.Path(file_gtf).suffix not in [".gtf",".gff",".gff3"]:
        # raise an exception to tell the user he has to insert a gtf or gff file
        raise Exception("You have to take a gtf or a gff file") 
    # else return True
    else:
        return True



def fasta(file_name):
    """
        Function that will read the Fasta file
        Args : 
            Fasta file
        Returns :
            Fasta sequence without the >ID
    """
    # open the fasta file in read mode and keep it in a variable
    with open(file_name, "r") as file_fasta_read:
        # read each line of the opened fasta file and keep it in a variable
        fasta_content_file = file_fasta_read.readlines()
        # fasta_seq_line = fasta_content_file.split("\n")
        
        # create an empty list named list_sequence
        list_sequence = []
        # for each line in the fasta file:
        for line in fasta_content_file:
            # if line doesn't contain ">"
            if line.find(">") != 0:
                # add line to list sequence
                list_sequence.append(line)
        # convert the list_sequence into a string and keep it in a variabme
        fasta_sequence = "".join(list_sequence)
        # transform all the letters in the sequence in upper mode  and replace line breaks for nothing
        fasta_seq = fasta_sequence.upper().replace("\n", "")
        # return the fasta sequence
        return fasta_seq




def split(file_gtf, fasta_sequence, start, end): 
    """
        It will read the gtf or gff file
        Take the position of the gene and extract the portion of the gene in the fasta file    
    Args:
        file_gtf : gtf file containing the positions start and end
        fasta_sequence : the return of the function fasta() containing the fasta sequence

    Returns:
        fasta_sequence_gtf : the fasta sequence that begans with the start and ends with the end collected from the gtf file
    """
    # open the gtf file in read mode and keep it in a variable named gtf_file
    with open(file_gtf, "r") as gtf_file:
        # give every column in the gtf file a name
        pandas_columns = ["chromosome", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]
        # read the gtf file, convert it into a table and keep it in a variable
        pandas_gtf = pd.read_csv(gtf_file, header=None, sep="\t", comment="#", dtype=str, names=pandas_columns)
        # select the third column "feature" and keep it in a variable
        column_feature = pandas_gtf.iloc[:,2]
        # print(column_feature)
        
        # select the rows where the "feature" column is like "gene" an keep it in a variable
        pandas_gene = pandas_gtf.loc[pandas_gtf["feature"] == "gene"]
        # select the fourth column "start" and keep it in a variable
        start_position = pandas_gene.iloc[:,3]
        # select the fifth column "end" and keep it in a variable
        end_position = pandas_gene.iloc[:,4] 
        # print(start_position)
        # print(end_position)
        # convert the values of every start position in the table into a list and keep it in a variable
        start_position_list = start_position.values.tolist()
        # convert the values of every end position in the table into a list and keep it in a variable
        end_position_list = end_position.values.tolist()
        print(start_position_list)
        
        # this part begins the analysis of the fasta sequence with the gtf file
        # create an empty list
        liste = []
        
        # append to a list the fasta sequence that begins with the start and ends with the end
        liste.append(fasta_sequence[int(start_position_list[start]):int(end_position_list[end])])
        # convert the list into a string and keep it in a variable
        fasta_sequence_gtf = "".join(liste)
        # return the fasta sequence
        return fasta_sequence_gtf

def erreur_fasta(fasta_file): 
    """
        Function that will show different error messages if the sequence doesn't correspond with the user choices.
        Args:
            Input data : DNA ou RNA sequence from the Fasta file, or from an Entry
        Returns:
            Error (str) : an error message if it doesn't match
    """
    # open the fasta file in read mode and keep it in a variable
    file_open_fasta = open(fasta_file, "r")
    # read each line of the opened fasta file and keep it in a variable
    file_content_fasta = file_open_fasta.readlines()

    # print(fasta_sequence)
    # if the len of the sequence is zero
    if len(file_content_fasta) == 0:
        # Raise an exception based on the following message
        raise Exception("The sequence is empty !")
    # else if the first line starts with ">":
    elif file_content_fasta[0].startswith(">"):
        # everything is okay and how it should be
        pass
    # else which means if the first line does not start with ">"
    else:
        # Raise an exception and tell the user the file does not have an ID
        raise Exception("This file doesn't have an ID. Make sure you're fasta file begins with '>' !")
    
    # use the fasta function with the fasta file as the argument and keep it in a variable    
    fasta_sequence = fasta(fasta_file)
    # for each character on the sequence
    for char in fasta_sequence:
        # if the character is different thant A, and B, and C, and N, and T
        if char != "A" and char != "G" and char != "C" and char != "T" and char != "N":
            # Raise and exception based on the following message
            raise Exception("The sequence contains letters others than A G C T N")
    # close the fasta file
    file_open_fasta.close()
    return True


def erreur_gtf(gtf_file):
    """
        Function that will show different error messages if the sequence doesn't correspond with the user choices.
        Args:
            Input data : GTF file
        Returns:
            Error (str) : an error message if it doesn't match
    """
    # give every column in the gtf file a name
    pandas_columns = ["chromosome", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]
    # read the gtf file, convert it into a table and keep it in a variable
    pandas_gtf = pd.read_csv(gtf_file, header=None, sep="\t", comment="#", names=pandas_columns)
    
    # print(pandas_gtf.dtypes)
    print(pandas_gtf)
    
    # if the table is empty
    if pandas_gtf.empty == True:
        # Raise an exception telling the user the table is empty
        raise Exception("The Dataframe is empty !!!")
    # for every ID in the first "chromosome" column
    for id in pandas_gtf.iloc[:,0]:
        # if the ID is not in string format
        if type(id) is not str:
            # Raise an exception telling the user that it must be in string format
            raise Exception("The first column of the GTF/GFF/GFF3 file must be in string format !")
    # for every entry in the fourth "start" column
    for start in pandas_gtf.iloc[:,3]:
        # when the start is not in integer format
        if type(start) is not int:
            # Raise an exception telling the user that it must be in integer format
            raise Exception("The column start must have integer data !")
    # for every entry in the fifth "end" column
    for end in pandas_gtf.iloc[:,4]:
        # when the end is not in integer format
        if type(end) is not int:
            # Raise an exception telling the user that it must be in integer format
            raise Exception("The column end must have integer data !")
    # for every score in the sixth "score" column
    for ltr in pandas_gtf.iloc[:, 6]:
        # if the score is not +, - or .
        if ltr != "+" and ltr != "-" and ltr != ".": 
            # Raise an exception telling the user that the column can only contain +,- and . symbols
            raise Exception("The Strand column can only contain the + and - symbols")
    # for every entry in the eighth "frame" column    
    for frame in pandas_gtf.iloc[:, 7]:
        # if the row entry is not in the range 0-2 or .
        if frame not in ["0", "1", "2"] and frame != ".":
            # Raise an exception that the frame value is not correct
            raise Exception("The frame value is not correct !")
    # for score in the sixth "frame" column
    for score in pandas_gtf.iloc[:, 5]:
        # if score is different than ".", 0 and 1 :
        if score != "." and score != "0" and score != "1":
            # Raise an exception that the score value is not correct
            raise Exception("The score is not a numeric value !")
    for start, end in zip(pandas_gtf.iloc[:,3], pandas_gtf.iloc[:,4]) : 
            # if the start is bigger than the end
        if start>end:
            # raise an exception with the following message
            raise Exception("The start must be smaller than the end !")
        if end<start:
            # raise an exception with the following message
            raise Exception("The end must be bigger than the start !")
            

    
    return True
        
    
def read_multiple_fasta(fasta_file:str):
    """
        Function that reads a multiple fasta file
        Args:
            fasta_file (str): fasta file containing different sequences separated by ">"
        Returns: sequences without the sequence ID
    """
    # open the multiple fasta file and keep it in a variable named multiple_fasta
    with open(fasta_file) as multiple_fasta:
        # create an empty dictionnary
        fasta = {}
        # create an empty string
        sequence_id = ''
        # create an empty list
        sequence_fasta = []
        #for line in the multiple fasta file
        for line in multiple_fasta:
            # if the line starts with ">" and the string sequence_id is empty
            if line.startswith(">") and sequence_id == '':
                # take the ID of the sequence
                sequence_id = line.split(' ')[0]
            # else if line starts with ">" and the string of the sequence_id is not empty
            elif line.startswith(">") and sequence_id != '':
                # add the ID in the fasta as a key, and the sequence as a value
                fasta[sequence_id] = ''.join(sequence_fasta)
                # takes another ID of another sequence
                sequence_id = line.split(' ')[0]
                # creates an empty list
                sequence_fasta = []
            else:
                # add the line in the empty list
                sequence_fasta.append(line.rstrip())
        # add the ID in the fasta as a key, and the sequence as a value     
        fasta[sequence_id] = ''.join(sequence_fasta)
        # create an empty string
        list_sequence = ""
        # for values in the fasta dictionnary values:
        for v in fasta.values():
            # add values to the dictionnary
            list_sequence = list_sequence + "\n" + v
        # return the sequences of the multiple fasta
        return list_sequence

    
