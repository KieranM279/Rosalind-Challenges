# Calculating the GC content of DNA strings

## Usage
```python
# Imports the FASTA formatted data into a dictionary
Sequences = DictMaker('filename.txt')
# Prints the Sequence ID and respective GC content to the terminal
GCcalc(Sequences)
```
## Prerequisites
```python
# For reading the FASTA formatted data
from Bio import SeqIO
```
## Methods
#### Step 1 - Importing the data
Simply parses the data in the FASTA formatted text file into a dictionary, which it then returns to the global environment
```python
def DictMaker(filename):

    Sequences = {}

    # Parse the data
    for record in SeqIO.parse(open(filename),'fasta'):

        # Isolate the ID ad the sequence
        identity = str(record.id)
        sequence = str(record.seq)

        # Create a dictionary of sequences
        Sequences[identity] = sequence

    return(Sequences)
```
#### Step 2 - Calculate GC content
This function uses a simple base counter to calculate the frequency of each base in the sequence. Then is calculates the overall GC content of the sequence and prints it, along with the sequences respective ID, to the terminal in the format required by Rosalind.
```python
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
```
