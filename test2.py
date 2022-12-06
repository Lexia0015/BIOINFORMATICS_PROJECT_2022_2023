import numpy as np
def fasta(file_name):
    """
        Function that will read the Fasta file
        Args : Fasta file
    """
    with open(file_name, "r") as file_fasta_read:
        fasta_content_file = np.array(file_fasta_read.readlines())
        print(fasta_content_file)
        
        if ">" in fasta_content_file:
            # print(np.array(fasta_content_file))
            pass
        list_sequence = []
        for line in fasta_content_file:
            # if line.startswith(">"):
            #     line += "\n\n"
            #     # print(line)
            # if line.find(">") != 0:
            
            if line.startswith(">") == 0 :
                fasta = np.array(list_sequence.append(line))
        print(fasta)
        # fasta_sequence = "".join(list_sequence)
        # fasta_seq = fasta_sequence.upper().replace("\n", "")
        # return fasta_seq
    
    
if __name__ == "__main__":
    file_name = input("Path file fasta: " )
    file_gtf = input("Path file gtf: ")
    # if control(file_name, file_gtf):
    #     if erreur(file_name, file_gtf):
    fasta_sequence = fasta(file_name)
    print(fasta_sequence)