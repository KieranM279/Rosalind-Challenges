
from Bio import SeqIO

# parse over the fasta file
for seq_record in SeqIO.parse(open('rosalind_gc.txt'),'fasta'):

    # isolate the sequence and its respective ID
    identity = str(seq_record.id)
    sequence = str(seq_record.seq)

    # create a dictionary to store the base counts
    bases = {'A':0, 'T':0, 'G':0, 'C':0}
    for b in bases:
        bases[b] = sequence.count(b)

    # calculate GC content
    GC = bases['G'] + bases['C']
    AT = bases['A'] + bases['T']
    content = (GC /(AT + GC)) * 100

    #print the results
    print(identity)
    print(content)
