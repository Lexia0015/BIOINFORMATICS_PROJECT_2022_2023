def nome():
    name = input('Poderia nos dizer seu nome? ')
    return name

def intro(name):
    print('Olá {}, seja bem vindo!'.format(name))

name = nome()
intro(name)


file_name = input("Path file fasta: " )
file_gtf = input("Path file gtf: ")
fasta_sequence = fasta(file_name)
# print(fasta(file_name))
gtf_analysis = split(file_gtf, fasta_sequence)
print(gtf_analysis)