# Finding a Protein Motif (mprt)

This is my solution to the Rosalind challenge. It takes in a list of UniProt IDs and searches for the N-glycosylation motif in each sequence. Then outputs the locations in the format required by Rosalind.

## Usage
How to use the functions that I wrote to solve this Rosalind problem
```python
# Creates a list of the UniProt IDs in the text file.
id_list = IDlist('filename.txt')
# Creates a dictionary of the sequences, downloading them from UniProt.
sequences = DownloadSeq(id_list)
# Finds the coordinates of the N-glycosylation motif in each sequence
motif_dict = MotifFinder(sequences)
# Prints the motif coordianted and sequence IDs in the required format.
printer(motif_dict)
```
## Prerequisites
```python
# To download the sequences from Uniprot, in FASTA format
import requests
# Import the FASTA formatted file into the python environment
from Bio import SeqIO
```
## Methods
#### Step 1 - Importing the data
This function parses the text file and sequentially adds each UniProt ID, from the file, into a list in the global environment.
```python
def IDlist(filename):

    # Open text file containing UniProt IDs
    IDs = open(filename)
    id_list = list()

    # Loop through text wrapper and append ID to id_list
    for ln in IDs:

        ln = ln.strip()
        id_list.append(ln)

    # Return the list
    return(id_list)
```
#### Step 2 - Downloading the UniProt sequences
This is probably wasn't the best way of doing this, but it works. It downloads the sequences and saves it as a FASTA formatted file in the working directory. The function then utilizes the SeqIO packages to import the FASTA files into a dictionary (seq_dict). The dictionary can then be returned to the global environment.
```python
def DownloadSeq(id_list):

    seq_dict = {}

    for Ide in id_list:

        # Isolate URL name and request data
        url = 'https://www.uniprot.org/uniprot/' + Ide + '.fasta'
        r = requests.get(url, allow_redirects=True)

        # Isolate filename and write data to file
        filename = Ide + '.fasta'
        open(filename, 'wb').write(r.content)

        # Import data from file to python
        record = SeqIO.read(filename, 'fasta')

        # Add sequences to a dictionary
        seq = str(record.seq)
        seq_dict[Ide] = seq

    # Return the dictionary
    return(seq_dict)
```
#### Step 3 - Find the N-glycosylation motif coordinates
This function creates four Booleans, one for each base in the motif. It then loops through each sequences using a sliding window. When all four of the Booleans are true, the coordinates are recorded and stored in a dictionary of lists. The dictionary is then returned to the global environment
```python
def MotifFinder(seq_dict):

    motif_dict = {}

    # Loop through ID list
    for Ide in id_list:

        # Set up sequence and list
        seq = seq_dict[Ide]
        motif_list = list()

        # Loop through the sequence
        for i in enumerate(seq):

            if i[0]+4 == len(seq):
                break

            # Assign booleans for the motif
            bool_one = seq[i[0]] == 'N'
            bool_two = seq[i[0]+1] != 'P'
            bool_three = seq[i[0]+2] == 'S' or seq[i[0]+2] == 'T'
            bool_four =  seq[i[0]+3] != 'P'

            # If motif is recognised, the index is recorded
            if (bool_one == True and bool_two == True and
                bool_three == True and bool_four == True):

                motif_list.append(i[0]+1)

        # Skip any sequence that has no motifs
        if len(motif_list) == 0:
            continue
        else:
            motif_dict[Ide] = motif_list

    # Return the finished dictionary
    return(motif_dict)
```
#### Step 4 - Print the coordinates to the terminal, in the required format for Rosalind
This just makes it easy to copy and paste the solution from the terminal into the Rosalind solution box.
```python
def printer(motif_dict):

    keys = list(motif_dict.keys())

    # Loop through each sequence ID in the motif coordinates dictionary
    for i in keys:
        ind = ''
        indexes = motif_dict[i]

        # Create a string from the list of coordinates
        for n in indexes:
            ind += (str(n) + ' ')

        # Print the ID and then the coordinates
        print(i)
        print(ind)
```
