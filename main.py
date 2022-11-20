#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Andreia CAMPOS FERREIRA'
__author__ = 'Franziska NICOLAUS'

# TODO améliorer les fonctions (voir si besoin de mettre lettres minuscules)
# TODO finir de mettre des commentaires
# TODO Améliorer fichier (mais dans l'ensemble partie 3 et 4 fait)

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
        sequence_DNA = sequence.replace("\n", "")
        sequence_RNA = sequence_DNA.replace("T", "U")
    # return the RNA sequence
    return sequence_RNA

def traduction(sequence_test:str):
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

    protein_string = ""
    # protein = ""
    for letter in range(0, len(sequence_test), 3):
        if len(sequence_test)%3 != 0:
            return "The length of the sequence must be a multiple of 3"
        codon = sequence_test[letter:letter+3]
        protein = list_amino_acids[codon]
        if protein == "STOP":
            break
        protein_string += list_amino_acids[codon]
        
    print(protein_string)
    
    
    
def main():
    """
        Function that provides a choice to the User
        Args:
            user_choice (str): the User has to choose a number between 1 and 3
        Returns:
            The previous functions according to the choice of the User
    """
    # create a variable that asks the user what to choose between different options
    user_choice = input("""Chose what you want to do : \n
                    1 = Transcription
                    2 = Traduction
                    3 = Transcription et Traduction\n""")
    
    # if the user chooses "1"
    if user_choice == "1":
        # return the transcription of the DNA
        print(transcription("ATCGACGTAGC"))
    else:
        # if the user chooses "2"
        if user_choice == "2":
            # return the traduction of the RNA
            transcripion_seq = transcription("ATGTACTCATTCGTTTCGGAAGAGACAGGTACGTTAATAGTTAATAGCGTACTTCTTTTTCTTGCTTTCGTGGTATTCTTGCTAGTTACACTAGCCATCCTTACTGCGCTTCGATTGTGTGCGTACTGCTGCAATATTGTTAACGTGAGTCTTGTAAAACCTTCTTTTTACGTTTACTCTCGTGTTAAAAATCTGAATTCTTCTAGAGTTCCTGATCTTCTGGTCTAA")
            print(traduction(transcripion_seq))
        else:
            # if the user chooses "3"
            if user_choice == "3":
                # return the transcription and the traduction of the DNA
                transcripion_seq = transcription("ATGTACTCATTCGTTTCGGAAGAGACAGGTACG")
                print(transcripion_seq)
                print(traduction(transcripion_seq))
            else:
                # if the user chooses 0 or nothing
                if user_choice == "0" or user_choice== "" :
                    # return an error phrase
                    print("You must choose a number between 1 and 3")
                # ask the user again what he wants to choose
                return main()
                
            
        


if __name__ == '__main__':
    main()