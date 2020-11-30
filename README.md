# Rosalind-Challenges
Scripts I have used to complete the tasks set out by Rosalind.info

## Calculate the GC content of DNA
### CalculateGC
Contains a script which takes a FASTA formatted which contains a DNA sequence and calculates the relative amount of Guanine and Cytosine in the sequence.

## Calculate Protein mass
### ProteinMassCalc
Contains:
 - a function which takes in a protein sequence and calculates the mass of the protein.
 - a text file containing the mass of each amino acid, required to run the function.

## Convert an RNA string to Protein
### RNAtoProt
Contains:
- a script which takes a mRNA sequence (already spliced) and returns the resulted protein sequence.

## Splice RNA and output Protein sequence
### RNAsplicing
Contains:
 - My script, which contains the Python code solution (RNAsplice.py).
 - A dependent file which contains the genetic code for RNA sequences (genetic_code.tsv).
 - Two example FASTA files. The first sequence in each file is the sequence that is to be spliced and the remaining sequences are all introns.
