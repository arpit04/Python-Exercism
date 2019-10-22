def distance(strand_a, strand_b):
    assert len(strand_a) == len(strand_b)
    return sum(ch1 != ch2 for ch1, ch2 in zip(strand_a, strand_b))
 
if __name__=="__main__":
    strand_a = 'GAGCCTACTAACGGGAT'
    strand_b = 'CATCGTAATGACGGCCT'
    print (distance(strand_a, strand_b))

