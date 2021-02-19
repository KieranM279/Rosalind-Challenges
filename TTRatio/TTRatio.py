
from Bio import SeqIO

####    Step 1    ####    Import the data    ####
def Dictmaker(filename):

    # Parse the data into environment
    record = SeqIO.parse(filename,'fasta')
    sequences = {}

    # Add data to a dictionary
    for rec in record:

        name = str(rec.name)
        seq = str(rec.seq)
        sequences[name] = seq

    return(sequences)

sequences = Dictmaker('sequences.fasta')

####    Step 2    ####    Calculate the Transition/Transversion ratio    ####

def TTRatio(Dict):

    # Creates a dictionary of base types
    Bases = {'C':'pyrimidine',
             'T':'pyrimidine',
             'A':'purine',
             'G':'purine'}

    # initialises necessary variables
    keys = list(Dict.keys())
    transitions = 0
    transversions = 0

    # Loop through the length of the sequences
    for b in range(len(str(Dict[keys[0]]))):

        seqA = str(Dict[keys[0]])
        seqB = str(Dict[keys[1]])

        # Checks if the bases are the same
        if seqA[b] == seqB[b]:
            continue
        elif seqA[b] != seqB[b]:

            # Isolates the type of base
            base1_type = Bases[seqA[b]]
            base2_type = Bases[seqB[b]]

            # Checks if bases types are the same
            if base1_type == base2_type:
                transitions += 1
            elif base1_type != base2_type:
                transversions += 1

    # Calculates the ratio
    ratio = transitions/transversions

    print(ratio)

TTRatio(sequences)
