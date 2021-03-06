
from Bio import SeqIO
def DictMaker(filename):

    Sequences = {}
    # Parse the data
    for record in SeqIO.parse(open(filename),'fasta'):

        # Isolate ID and sequence
        identity = str(record.id)
        sequence = str(record.seq)

        # Create a dictionary of sequences
        Sequences[identity] = sequence

    return(Sequences)

Sequences = DictMaker('rosalind_gc.txt')

def GCcalc(dictSeq):

    keys = dictSeq.keys()

    # Loop though each sequence ID
    for key in keys:

        # Isolate each sequence from the dictionary
        sequence = dictSeq[key]

        # Count the frequency of each base and add them to a dictionary
        bases = {'A':0,'T':0,'C':0,'G':0}
        for b in bases:
            bases[b] = sequence.count(b)

        # use the dictionary to calculate GC content
        GC = bases['G'] + bases['C']
        AT = bases['A'] + bases['T']
        content = (GC /(AT + GC)) * 100

        # Print ID and GC content to terminal
        print(key)
        print(content)

GCcalc(Sequences)
