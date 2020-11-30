# RNA Splicing (splc)

My solution to the RNA splicing problem (splc) from the Rosalind challenges.

## Contents

 - My script, which contains the Python code solution (RNAsplice.py).
 - A dependent file which contains the genetic code for RNA sequences (genetic_code.tsv).
 - Two example FASTA files. The first sequence in each file is the sequence that is to be spliced and the remaining sequences are all introns.

## Method

### Step 1 Dictmaker()

A function which utlises the SeqIO package to parse the FASTA formated data into a dictionary. This dictionary can then be used later in the script. The FASTA formatted file must be compliant with the description in Contents

### Step 2 DNA2RNA()

A function which takes in the dictionary of DNA sequences and replaces them with their pre-mRNA counterpart.

### Step 3 spliceRNA()

A function which replaces the introns in the pre-mRNA sequence with an empty string, effectively removing them. This function returns the mRNA sequence as a string.

### Step 4 dmaker()

A second dictionary creating function which parses the 'genetic_code.tsv' file into a dictionary which can be used by the following function.

### Step 5 RNA2Protein()

A final function to loop through the mRNA sequence (post-splicing) in steps of three. It isolates each triplet codon and references the genetic code dictionary (Step 4) to build the final protein sequence. The final sequence is returned as a string.
