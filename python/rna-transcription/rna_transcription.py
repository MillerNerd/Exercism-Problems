def to_rna(dna):
    rna = ""
    for i in dna:
        dna.replace("G", "C")
        dna.replace("C", "G")
        dna.replace("T", "A")
        dna.replace("A", "U")
    return dna
