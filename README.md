# Rosalind-Challenges
Scripts I have used to complete the tasks set out by Rosalind.info

## Finding a Protein Motif
### MotifFinder
Contains:
 - a script which takes a list of UniProt IDs and outputs the location of the N-glycosylation motif.
 - three text files containing example IDs.

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

## Calculate the Transition/Transversion Ratio
### TTRatio
Contains:
 - My script, which contains my solution to the Rosalind problem.
 - Two example test sets (FASTA format).

## Find all of the Open Reading Frames of a DNA sequence
### OpenReadingFrames
Contains:
 - ORFrames.py, a script containg my solution to the Rosoalind challenge.
 - genetic_code.tsv, a tab-delimited file contains the genetic code data.
 - Two example data sets.
