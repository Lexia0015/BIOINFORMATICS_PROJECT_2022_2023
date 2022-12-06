# import numpy as np
# def fasta(file_name):
#     """
#         Function that will read the Fasta file
#         Args : Fasta file
#     """
#     with open(file_name, "r") as file_fasta_read:
#         fasta_content_file = file_fasta_read.readlines()
#         # print(fasta_content_file)
#         for line in fasta_content_file:
#             while line.find(">"):
#                 print(line.split("\n"))
#                 break
#         # fasta = "".join(fasta_content_file)
#         # liste_append = []
#         # for line in fasta_content_file:
#         #     if line.find(">"):
#         #         liste_append.append(np.array(line))
#         # print(liste_append)
#         # if line.startswith(">"):
#         #     line += "\n\n"
#         #     # print(line)

# if __name__ == "__main__":
#     file_name = input("Path file fasta: " )
#     file_gtf = input("Path file gtf: ")
#     # if control(file_name, file_gtf):
#     #     if erreur(file_name, file_gtf):
#     fasta_sequence = fasta(file_name)
#     print(fasta_sequence)


import io

FASTA='''\
>Rosetta_Example_1
THERECANBENOSPACE
>Rosetta_Example_2
THERECANBESEVERAL
LINESBUTTHEYALLMUST
BECONCATENATED'''

# infile = io.StringIO(FASTA)
# print(infile.read())

def fasta_parse():
    file_name = input("Path file fasta: " )
    with open(file_name, "r") as infile:
        # print(infile.read())
#         fasta_content_file = file_fasta_read.readlines()
        key = ''
        for line in infile:
            if line.startswith('>'):
                if key:
                    yield key, val
                key, val = line[1:].rstrip().split()[0], ''
            elif key:
                val += line.rstrip()
        if key:
            yield key, val

print('\n'.join('%s: %s' % keyval for keyval in fasta_parse()))

# print(fasta_parse())