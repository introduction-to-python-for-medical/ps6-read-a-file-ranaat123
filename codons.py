
def create_codon_dict(file_path):

    file_path = "data/codons.txt"
    file = open(file_path)
    rows = file.readlines()
    file.close()
    mapping_between_codons = {}
    
    for row in rows:
      cells = row.strip().split('\t')
      codon = cells[0]
      amino_acid = cells[2]
      mapping_between_codons[codon] = amino_acid

    return mapping_between_codons
