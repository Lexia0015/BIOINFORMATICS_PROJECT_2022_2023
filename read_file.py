#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

# TODO fasta() function to multiple files
# TODO split() function with pandas and try it

import pandas as pd


def split(file_gtf):
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
            gtf_content.append(line)
            
    pandas_columns = ["chromosome", "from", "type", "start", "end", ".", "strand", ".", "gene_id", "ens", "transcript_id"]
    pandas_gtf = pd.DataFrame (gtf_content)
    print(pandas_gtf)
    # return gtf_content


def fasta(file_fasta):
    """
        Function that will read the Fasta file
        Args : Fasta file
    """

    file_fasta_read = open(file_fasta, "r") 
    fasta_content_file = file_fasta_read.readlines()
    # fasta_seq_line = fasta_content_file.split("\n")
    list_sequence = []
    for line in fasta_content_file:
        if line.find(">") != 0:
            list_sequence.append(line)
    fasta_sequence = "".join(list_sequence)
    sequence = fasta_sequence.replace("\n", "")
    return sequence


if __name__ == "__main__":
    # split()
    # file_fasta = input("Path file : ")
    file_gtf = input("Path file gtf: ")
    # print(fasta(file_fasta))
    print(split(file_gtf))
    
    
