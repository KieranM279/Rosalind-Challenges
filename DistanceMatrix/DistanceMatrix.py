
from Bio import SeqIO

####    Step 1    ####    Import the data    ####

def Dictmaker(filename):

    # Parse the FASTA formatted text file given by Rosalind
    record = SeqIO.parse(filename,'fasta')
    sequences = {}

    # Loop through each record and add to a dictionary
    for rec in record:
        sequences[rec.id] = str(rec.seq)

    return(sequences)

sequenceDict = Dictmaker('rosalind_pdst.txt')

####    Step 2    ####    Calculate distance between two strings    ####

def DistCalc(string1, string2):

    index = range(0,len(string1))
    differenceDict = {'same':0,'diff':0}

    # Loops through the length of the string(s)
    for i in index:

        # Counts the bases which are the same and different between strings
        if string1[i] == string2[i]:
            differenceDict['same'] += 1

        elif string1[i] != string2[i]:
            differenceDict['diff'] += 1

    # Calculates the distance between the strings
    distance = differenceDict['diff']/len(string1)

    return(format(distance, '.5f'))

####    Step 3    ####    Distance Matrix printer    ####

def DistMatrix(sequences):
    # Create a list of the IDs in the dictionary
    ids = list(sequences.keys())

    # Compare each sequence to every other sequence, inclusive
    for ID in ids:

        distances = list()
        for ID2 in ids:

            # Calculate distance and add it to a list
            distance = DistCalc(sequences[ID], sequences[ID2])
            distances.append(distance)

            # Print each list in the format required by Rosalind
        print(' '.join(distances))

DistMatrix(sequenceDict)
