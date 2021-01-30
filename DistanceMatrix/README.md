# Creating a Distance Matrix

## Prerequisites
```Python
# To import the FASTA formatted data
from Bio import SeqIO
```
## Usage
```Python
# Imports the sequences into a dictionary
sequenceDict = Dictmaker('filename')
# Creates a distance matrix of the sequences from the dictionary
DistMatrix(sequenceDict)
```
## Methods
#### Step 1 - Import the data
```Python
def Dictmaker(filename):

    # Parse the FASTA formatted text file given by Rosalind
    record = SeqIO.parse(filename,'fasta')
    sequences = {}

    # Loop through each record and add to a dictionary
    for rec in record:
        sequences[rec.id] = str(rec.seq)

    return(sequences)
```
#### Step 2 - DistCalc()
I initiated a function that takes in two equal length strings as arguments (string1 and string2). Then it outputs the distance between the strings to 5 significant figures.
```Python
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
```
#### Step 3 - Create and Print the Distance Matrix
This function takes in the dictionary of sequences from step 1.Then, using the function initiated in step 2, inputs every combination of the sequences in the dictionary as string1 and string2 and then outputs the distances in a matrix to the terminal.
```Python
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
```
