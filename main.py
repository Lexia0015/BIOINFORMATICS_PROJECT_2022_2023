#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'


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
        # replace "T" into "A" and keep the changment in a variable named sequence_RNA
        sequence_RNA = sequence.replace("T", "U")
    # return the RNA sequence
    return sequence_RNA

def traduction(sequence_RNA):
    list_amino_acids = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
                        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
                        "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
                        "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
                        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
                        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
                        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
                        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}


def main():
    user_choice = input("""Chose what you want to do : \n
                    1 = Transcription
                    2 = Traduction
                    3 = Transcription et Traduction\n""")
    
    if user_choice == "1":
        print(transcription("ATCGACGTAGC"))
    else:
        if user_choice == "2":
            print(traduction)
        else:
            if user_choice == "3":
                print(transcription("ATCGACGTAGC"))
                print(traduction)
            else:
                if user_choice == 0 or user_choice== "" :
                    print("You must choose a number !")
                    return main()
                else:
                    print("You must choose between transcription or translation")
                    return main()
                
            
        


if __name__ == '__main__':
    main()