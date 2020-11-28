# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:50:50 2020

@author: kiera
"""
import os
os.chdir('C:/Users/kiera/Desktop/Rosalind/RNAtoProtein')

RNA = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

#### Create a dictionary of dictionaries for the genetic code ####

def dmaker(genetic_code):
    
    # Open file
    genetic_code_file = open(str(genetic_code))
    
    acids = {}
    
    # Parse the file containing the genetic code
    for ln in genetic_code_file.readlines():
        ln = ln.strip()
        ln = ln.split()
        print(ln)
        
        # Create a dicionary of each codon
        codon = {'1-letter':ln[1],
                 '3-letter':ln[2],
                 'amino acid':ln[3]}
        # Compile the codon dictionaries
        acids[ln[0]] = codon
        
    return(acids)

# Save protein dictionary to the variable Protein_dict
protein_dict = dmaker('genetic_code.tsv')

#### Translate the mRNA string to the protein string ####

def RNA2Prot(mRNA):
    
    protein = ''

    # Iterate over the RNA string in steps of three
    for i in range(0,len(RNA),3):
        
        # Isolate the amino acid translated by the codon
        codon = mRNA[i:i+3]
        amino_acid = protein_dict[codon]['1-letter']
        
        # Check whether to end the translation
        if amino_acid == 'X':
            break
        
        # Iteratively builds the protein
        protein += amino_acid
    
    return(protein)

# Saves the protein string to variable 'protein'
protein = RNA2Prot(RNA)
    
    
    
    
