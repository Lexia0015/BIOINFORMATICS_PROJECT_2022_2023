#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'


# TODO split() function check with the tkinter part 
# TODO fasta() function to read multiple fastas

import pandas as pd
import numpy as np

# from graphic_interface import select_file_fasta




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
        if line.find(">") != 0:
            list_sequence.append(line)
    fasta_sequence = "".join(list_sequence)
    fasta_seq = fasta_sequence.upper()
    sequence = fasta_seq.replace("\n", "")
    return sequence




def split(file_gtf, file_name):
    """
        It will read the gtf or gff file
        Take the position of the gene and extract the portion of the gene in the fasta file
        
        Args:
        
    """
    gtf_file = open(file_gtf, "r")
    file_content = gtf_file.readlines()
    gtf_content = []
    for line in file_content:
        if line.find("#") != 0:
            gtf_content.append(line.split("\t"))
    
    # print(gtf_content)
    pandas_columns = ["chromosome", "source", "feature", "start", "end", "score", "strand", "frame", "attribute"]
    pandas_gtf = pd.DataFrame(gtf_content, columns=pandas_columns)
    # print(pandas_gtf)
    start_position = pandas_gtf.iloc[:,3]
    end_position = pandas_gtf.iloc[:,4] 
    # print(start_position)
    # print(end_position)
    start_position_list = start_position.values.tolist()
    end_position_list = end_position.values.tolist()
    # print(start_position_list[1])
    # print(end_position_list)
    
    # fasta part
    # global sequence_fasta
    sequence_fasta = fasta(file_name)
    # print(sequence_fasta, "\n")
    for i in range(1, 4):
        return sequence_fasta[int(start_position_list[i]):int(end_position_list[i])]
    






if __name__ == "__main__":
    file_name = input("Path file fasta: " )
    file_gtf = input("Path file gtf: ")
    print(fasta(file_name))
    print(split(file_gtf, file_name))
    
    
