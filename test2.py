# # import numpy as np
# # def fasta(file_name):
# #     """
# #         Function that will read the Fasta file
# #         Args : Fasta file
# #     """
# #     with open(file_name, "r") as file_fasta_read:
# #         fasta_content_file = file_fasta_read.readlines()
# #         # print(fasta_content_file)
# #         for line in fasta_content_file:
# #             while line.find(">"):
# #                 print(line.split("\n"))
# #                 break
# #         # fasta = "".join(fasta_content_file)
# #         # liste_append = []
# #         # for line in fasta_content_file:
# #         #     if line.find(">"):
# #         #         liste_append.append(np.array(line))
# #         # print(liste_append)
# #         # if line.startswith(">"):
# #         #     line += "\n\n"
# #         #     # print(line)

# # if __name__ == "__main__":
# #     file_name = input("Path file fasta: " )
# #     file_gtf = input("Path file gtf: ")
# #     # if control(file_name, file_gtf):
# #     #     if erreur(file_name, file_gtf):
# #     fasta_sequence = fasta(file_name)
# #     print(fasta_sequence)


# # import io

# # FASTA='''\
# # >Rosetta_Example_1
# # THERECANBENOSPACE
# # >Rosetta_Example_2
# # THERECANBESEVERAL
# # LINESBUTTHEYALLMUST
# # BECONCATENATED'''

# # infile = io.StringIO(FASTA)
# # print(infile.read())

# # def fasta_parse():
# #     file_name = input("Path file fasta: " )
# #     with open(file_name, "r") as infile:
# #         # print(infile.read())
# # #         fasta_content_file = file_fasta_read.readlines()
# #         key = ''
# #         for line in infile:
# #             if line.startswith('>'):
# #                 if key:
# #                     yield key, val
# #                 key, val = line[1:].rstrip().split()[0], ''
# #             elif key:
# #                 val += line.rstrip()
# #         if key:
# #             yield  key, val
# #         print(key, "\n", val)

# # print('\n'.join('%s: %s' % keyval for keyval in fasta_parse()))

# # print(fasta_parse())


# # # Project Bioinformatiques Python Programmation

# # ## Use the code in the terminal

# # ## Use the code in the graphic interface Tkinter

# # ## About file main.py
# # Write the list of the functions and how do tey serve

# # notes about validate function 
# # The first part, "1.0" means that the input should be read from line one, character zero.

# # The end-1c is divided in 2 parts:

# #     end: Read until the end of the text.
# #     1c: Remove 1 character starting from the end.

# # It deletes the last character to remove that last \n so your e-mail doesn't end with an extra line.


# # suprim gitignore

# def fasta2dict(fil):
#     """
#     Read fasta-format file fil, return dict of form scaffold:sequence.
#     Note: Uses only the unique identifier of each sequence, rather than the 
#     entire header, for dict keys. 
#     """
#     dic = {}
#     cur_scaf = ''
#     cur_seq = []
#     for line in open(fil):
#         if line.startswith(">") and cur_scaf == '':
#             cur_scaf = line.split(' ')[0]
#         elif line.startswith(">") and cur_scaf != '':
#             dic[cur_scaf] = ''.join(cur_seq)
#             cur_scaf = line.split(' ')[0]
#             cur_seq = []
#         else:
#             cur_seq.append(line.rstrip())
#     dic[cur_scaf] = ''.join(cur_seq)
#     return dic

# fil = input("fasta : ")
# print(fasta2dict(fil))


def swap_dna(dnastring):
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
        }
    protein = []
    end = len(dnastring) - (len(dnastring) %3) - 1
    start = dnastring.find('ATG')
    # for each third letter in the sequence 
    for i in range(start,end,3):
        codon = dnastring[i:i+3]
        if codon in table:
            aminoacid = table[codon]
            protein.append(aminoacid)
            
        else:
            protein.append("N")
        if table[codon] == '*':
            # print(protein_sequence)
            # break the loop
            break
    return "".join(protein)

