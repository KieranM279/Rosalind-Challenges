from Bio import SeqIO

####    Step 1    ####    Import the data    ####

def Dictmaker(filename):

    # Parse the data
    records = SeqIO.parse(open(filename),'fasta')
    sequences = {}

    # Loop through the records
    for rec in records:

        # Isolate ID and sequence
        ID = str(rec.id)
        seq = str(rec.seq)

        # Create a dictionary of sequence, prefix and suffix
        data = {'seq':seq,
                'prefix':str(seq[0:3]),
                'suffix':str(seq[-3:-1])+str(seq[-1])}

        # add the dictonary to a dictionary of the IDs
        sequences[ID] = data

    return(sequences)

sequences = Dictmaker('sample_data2.fasta')

####    Step 2    ####    Main function    ####

def adjacencyMaker(sequences):

    # Isolate a list of the IDs
    ids = list(sequences.keys())

    # Loop through the suffixes
    for v in ids:
        suf = sequences[v]['suffix']

        # Loop through the prefixes
        for w in ids:
            pre = sequences[w]['prefix']

            # Skip if the prefix and suffix are from the same sequence
            if v == w:
                continue
            # If prefix and suffix match, print them
            elif str(suf) == str(pre):
                print(v + ' ' + w)

adjacencyMaker(sequences)
