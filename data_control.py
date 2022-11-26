#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

# TODO write control() function = see algorithm project (for Andreia)
# TODO write erreur() function

from read_file import *
import read_file as rf

def control(sequence):
    """
        Function that will verify is the input data is correct
        Args:
            Input data : TODO To specify
        Returns:
            Error_control (str) : an error message if the data is not correct or a simply message that says Correct ! 
            TODO simply message a voir
    """
    # if rf.fasta(sequence) 
    pass


def erreur(sequence):
    """
        Function that will show different error messages if the sequence doesn't correspond with the user choices.
        Args:
            Input data : DNA ou RNA sequence from the Fasta file, or from an Entry, or from the GTF/GFF file
        Returns:
            Error (str) : an error message if it doesn't match
    """
    # if the len of the sequence is None
    if len(sequence) == 0:
        # Raise an exception based on the class SequenceIncorrect with the following message
        raise Exception("La séquence rentrée est incorrecte (= 0)")

    # for each character on the sequence
    for c in sequence:
        # if the character is different thant A, and B, and C, and N, and T
        if c != 'A' and c != 'G' and c != 'C' and c != 'T' and c != "N":
            # Raise and exception based on the class SequenceIncorrect with the following message
            raise Exception("La sequence contient des autres lettres que A G C T")
