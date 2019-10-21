DNA = {'adenine' : 'A','cytosine' : 'C','guanine' : 'G','thymine' : 'T'}
RNA = {'adenine' : 'A','cytosine' : 'C','guanine' : 'G','uracil' : 'U'}
def to_rna(dna_strand):
    if dna_strand not in DNA:
        return "Invalid Strand"
    elif DNA[dna_strand] == 'A':
        ls = list(RNA.keys())
        return ls[3]
    elif DNA[dna_strand] == 'C':
        ls = list(RNA.keys())
        return ls[2]
    elif DNA[dna_strand] == 'G':
        ls = list(RNA.keys())
        return ls[1]
    elif DNA[dna_strand] == 'T':
        ls = list(RNA.keys())
        return ls[0]
a=1
b=2
a!=b
dna_strand = input("Enter dna_strand : ")
print("RNA_strand :",to_rna(dna_strand))