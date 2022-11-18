#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'

def split():
    """
        It will read the gtf or gff file
        Take the position of the gene and extract the portion of the gene in the fasta file
        
        Args:
        
    """
    pass


def fasta(file_fasta):
    """
        Function that will read the Fasta file
        Args : Fasta file
    """
    
    file_fasta_read = open(file_fasta, "r")
    for line in file_fasta_read.readlines():
        print(line)


if __name__ == "__main__":
    # split()
    file_fasta = input("Path file : ")
    fasta(file_fasta)
    