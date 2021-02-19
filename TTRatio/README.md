# Finding the Transition/Transversion Ratio (tran)

## Usage
```python
# Import the sequences into a dictionary
sequences = Dictmaker('sequences.fasta')
# Calculate Transition/Transversion ratio
TTRatio(sequences)
```
## Prerequisites
```python
from bio import SeqIO
```
## Method

#### Step 1 - Import the data
Simple function to import the FASTA formatted sequences into the python environment. It utilises the SeqIO package to store the sequences as a dictionary
```python
def Dictmaker(filename):

    # Parse the data into environment
    record = SeqIO.parse(filename,'fasta')
    sequences = {}

    # Sequentially add data to a dictionary
    for rec in record:

        name = str(rec.name)
        seq = str(rec.seq)
        sequences[name] = seq

    return(sequences)
```
#### Step 2 - Calculate the TT Ratio
A function that loops through both sequences in the dictionary and tests whether each base is the same. If they are not it then checks if the different bases are of a different type (i.e. Purine vs Pyrimidine). This is done by referencing a dictionary initiated at the start of the function. The number of each are recorded and the ratio is calculated.
```python
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
```
