

def read_gtf_file(gtf_file):
    """ Reads gene, transcript, and edge information from a GTF file.
        Args:
            gtf_file: Path to the GTF file
        Returns:
            genes: A dictionary mapping gene IDs to corresponding gene objects
            transcripts: A dictionary mapping gene IDs to corresponding 
                   transcript objects
            exons: A dictionary mapping exon IDs to corresponding edge objects
    """
    genes = {}
    transcripts = {}
    exons = {}

    with open(gtf_file) as gtf:
        for line in gtf:
            line = line.strip()

            # Ignore header
            if line.startswith("#"):
                continue

            # Split into constitutive fields on tab
            tab_fields = line.split("\t")
            chrom = tab_fields[0]
            entry_type = tab_fields[2]

            # Entry is a gene
            if entry_type == "gene":
                gene = Gene.get_gene_from_gtf(tab_fields)
                native_id = gene.identifier
                genes[native_id] = gene

            # Entry is a transcript
            elif entry_type == "transcript":
                transcript = Transcript.get_transcript_from_gtf(tab_fields)
                gene_id = transcript.gene_id
                if gene_id in genes:
                    genes[gene_id].add_transcript(transcript)
                native_id = transcript.identifier
                transcripts[native_id] = transcript
                
            # Entry is an edge
            elif entry_type == "exon":
                exon = Edge.create_edge_from_gtf(tab_fields)
                # This ID is used because of a rare GENCODE bug
                location_exon_id = exon.identifier
                exons[location_exon_id] = exon 

                transcript_id = list(exon.transcript_ids)[0]
                gene_id = exon.annotations["gene_id"]
                
                if location_exon_id not in exons:
                    # Add the new edge to the data structure
                    exons[location_exon_id] = exon
                else:
                    # Update existing exon entry, including its transcript set
                    exon = exons[location_exon_id]
                    exon.transcript_ids.add(transcript_id)
           
                if transcript_id in transcripts:         
                    currTranscript = transcripts[transcript_id]
                    currTranscript.add_exon(exon)

    return genes, transcripts, exons 


print(read_gtf_file("example.gtf"))