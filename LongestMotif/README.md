# Finding the Longest Shared Motif
## Contents
- My solution for the Rosalind Challenge to find the longest shared motif between a list of DNA sequences.
- Six test datasets in which to practice. The datasets have 100 sequences, each being 1000 bases in length.

## Prerequisites
```python
import bio from SeqIO
import time
```
The SeqIO package is used to parse the data in an the 'time' package, although not shown below, is used to measure the computation times of differnt section of the script.
## Method
### The main script
This is script uses several functions, which have been outlined below, to search for the longest shared motif among a FASTA formatted list of DNA sequences. It uses a semi-brute force method in which the shortest possible motifs are tested first and then the next longest are tested (i.e. A, T, C, G -> AA, AT, AC, AG,...etc). This, however, is sped up by the removal of any motif that has not been found in any of the sequences in the dataset (e.g. if A is not found AT, AG, AC, AA, will not be generated), thus saving computation time.
```python
Potential_motifs = ['A','T','C','G']
MotifsTested = 0
for i in range(MinMotif):

    # Removes motifs that are not present in any of the sequences
    MotifUpdate(Potential_motifs)

    # Saves the previous generation of motifs
    if len(Potential_motifs) != 0:
        Save = Potential_motifs

    # Prints the Longest shared motif if only one is left
    # If none survive the the previous generation is printed
    if len(Potential_motifs) == 0:

        print('The longest shared motif(s) are:')
        if len(Save) == 1:
            print(''.join(Save))
        else:
            print(Save)
        break

    # makes the next generation
    Potential_motifs = Generation(Potential_motifs)
```
The slowest part of this solution is the MotifUpdate function. To speed this up in subsequent version I will try to utilise multiprocessing
### Importing the data (Dictmaker())
This is how parsed the FASTA formatted data, straight from the Rosalind download, and placed in a dictionary (of dictionaries) for use in the main script.
```python
def DictMaker():

    record = SeqIO.parse('sequences.fasta','fasta')
    counter = 0
    dictionary = {}

    # Create a dictionary (of dictionaries) of the sequences
    for rec in record:
        counter += 1
        seq = ''

        # isolate each sequences as a string
        for b in rec.seq:
            seq += b

        # Create each entry and add it to the dictionary
        Entry = {'name':rec.name,
                 'seq':seq}
        dictionary[counter] = Entry

    return(dictionary)
```
This isn't the most elegant solution but since it only needs to be run once it does the job.

### Motif finding function (MotifF())
This is the heart of the script. I simple motif matching function that takes in the motif that is being searched for and the sequence being searched. A sliding windows, the length of the motif, is created along the sequence until a match is found. The result is returned as a boolean.
```python
def MotifF(motif, string):

    # Sets the length of the motif and string
    motif_length = len(motif)
    string_length = len(string)

    # Loops as a sliding window through the String
    for i in range(string_length):

        # Potential match to motif
        P_match = string[i:i+motif_length]

        # Conditional identifying the presence of the motif
        if len(P_match) < motif_length:
            break
        elif motif == P_match:
            Bool = True
            break
        else:
            Bool = False

    return(Bool)
```
### Motif generation (in two parts)
 The first function, MotifGen(), takes in a single sequences and then creates a list of four 'daughter' sequences. Each containing one additional base (i.e. A, T, C or G).

 ```python
 def MotifGen(seq):

    # List of bases
    bases = ['A','T','C','G']
    # Output list
    NewSeq = list()

    # Create all the sequences
    for i in bases:
        x = ''
        x = seq + i
        NewSeq.append(x)

    return(NewSeq)
```
The second function, Generation(), utilises the previous function (MotifGen()) to produce the entire generation of sequences that are to be tested against the test datasets.

```python
def Generation(Potential_motifs):
    New_Gen = []

    # Sequentially adds the next generation of motifs
    for i in Potential_motifs:
        New_Gen += MotifGen(i)

    return(New_Gen)
```
