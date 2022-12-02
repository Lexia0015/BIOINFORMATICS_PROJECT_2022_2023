#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'



# TODO fasta() function to read multiple fastas
# TODO VOIR S'IL FAUT PAS SAUTER DE LIGNES POUR RESULTAT DANS TKINTER

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




def split(file_gtf, fasta_sequence): 
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

    # print(start_position_list[1])
    # print(end_position_list)
    
    # fasta part
    liste = []
    # print(sequence_fasta, "\n")
    for i in range(1, 4):
        liste.append(fasta_sequence[int(start_position_list[i]):int(end_position_list[i])])
    fasta_sequence_gtf = "".join(liste)
    return fasta_sequence_gtf






if __name__ == "__main__":
    file_name = input("Path file fasta: " )
    file_gtf = input("Path file gtf: ")
    fasta_sequence = fasta(file_name)
    print(fasta(file_name))
    # gtf_analysis = split(file_gtf, fasta_sequence)
    # print(gtf_analysis)
    
    
