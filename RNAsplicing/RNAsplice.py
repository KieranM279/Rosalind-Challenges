# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:25:45 2020

@author: kiera
"""
from Bio import SeqIO

####    Step 1    ####    Put data into a usable format    ####

def Dictmaker():

    counter = 0
    sequences = {}

    # Parse the data
    record = SeqIO.parse('sequences.fasta','fasta')
    for rec in record:
        counter += 1

        # Add entries to dictionary
        if counter == 1:
            sequences['gene'] = str(rec.seq)
        else:
            name = 'intron' + str(counter-1)
            sequences[name] = str(rec.seq)

    # Output the dicionary
    return(sequences)

Sequences = Dictmaker()

####    Step 2    ####    Convert DNA to Pre-mRNA    ####

def DNA2RNA(Dict):

    # Loop through each sequence in the dictionary
    keys = Dict.keys()
    for i in keys:

        # Replaces any Thymine bases with Uracil
        Dict[i] = Dict[i].replace('T','U')

    return(Dict)

Sequences = DNA2RNA(Sequences)

####    Step 3    ####    Remove introns    ####

def spliceRNA(Dict):

    rna = Dict['gene']

    # Creates a dictionary of just the introns
    introns = list(Dict.keys())
    introns.remove('gene')

    # Replace the introns with an empty string
    for i in introns:
        rna = rna.replace(Dict[i],'')

    return(rna)

mRNA = spliceRNA(Sequences)

####    Step 4    ####    Genetic code dictionary    ####

def dmaker(genetic_code):

    # Open the genetic code file
    genetic_code_file = open(str(genetic_code))

    acids = {}

    # Parse the data in the genetic code file
    for ln in genetic_code_file.readlines():
        ln = ln.strip()
        ln = ln.split()

        # Builds the dictionary, entry by entry
        codon = {'1-letter':ln[1],
                 '3-letter':ln[2],
                 'amino acid':ln[3]}
        acids[ln[0]] = codon

    return(acids)

protein_map = dmaker('genetic_code.tsv')

####    Step 5    ####    Convert the mRNA to Protein    ####

def RNA2Protein(mrna):

    len_mrna = len(mrna)
    protein = ''

    # Loop through the RNA sequence in steps of three
    for codon in range(0,len_mrna,3):

        # Isolates the current codon of the RNA
        triplet = str(mrna[codon:codon+3])

        # Breaks the loop if it reaches a stop codon
        if protein_map[triplet]['1-letter'] == 'X':
            break

        # Builds the protein sequence
        protein += protein_map[triplet]['1-letter']

    return(protein)

Protein = RNA2Protein(mRNA)

# Prints the final protein string
print('The protein sequence is:')
print(Protein)
