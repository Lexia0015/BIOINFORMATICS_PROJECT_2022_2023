def cdna_longura():
    dict_longura = {}
    with open("example.gtf", "r") as file_nx_tx:
        for line in file_nx_tx:
            line_split_transcript = line.split("transcript_id")[-1]
            line_split_sep = line_split_transcript.split(";")[:1]
            str_ens = "".join(line_split_sep)
            print(str_ens)
            str_ens.replace("' ", "")
            # line_split_start = line.split("\t")[3]
            # line_split_end = line.split("\t")[4]
            # longura_cdna = (int(line_split_end) - int(line_split_start))
            # dict_longura[str_ens] = longura_cdna
        return dict_longura
    
print(cdna_longura())