# Open Reading Frames (orf)

My solution to the Rosalind challenge in which all the possible open reading frames from a single FASTA formatted sequence.

## Contents

Contains:
 - My script, python code which finds all the valid open reading frames and translates them to proteins.
 - A tab-delimited file which contains the genetic code ('genetic_code.tsv').
 - Two test sequences for the script.

## Methods

### Dictmaker()
A function which takes the filename of the genetic code data ('genetic_code.tsv') and parses it into a dictionary to reference later.

### seqF()
A function to import the FASTA formatted sequence into the global environment. This uses the SeqIO package.

### StringRev()
A function which takes a string and returns the reverse.

### RevCompGen()
A function which takes in a DNA sequence and produces the reverse complement strand. This uses a dictionary of base pairs for reference and utilises the StringRev function.

### seqDict()
Puts the DNA sequence and reverse complement in a dictionary.

### DNA2RNA()
A function which takes in a dictionary of DNA sequences and replaces them with their RNA counterparts.

### S_codon()
A function which loops through and RNA string and returns all of the possible start codons in list form.

### codonDict()
A function which takes in a dictionary of RNA sequences and returns a dictionary of the respective Start codons. This function conserves the sequence dictionary keys.

### RNA2Prot()
This is a function takes in the sequences dictionary and codon dictionary made previously. For each sequence, the function loops through each sequence in steps of 3, starting at the previously generated codon indices. All possible protein sequences are saved, however any that do not contain a stop codon are removed (along with any duplicate sequences). The remaining sequences are then output in a list.

### printer()
A small function to print the sequences to the terminal in the correct format.
