# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:58:43 2020

@author: kiera
"""

from Bio import SeqIO
import requests

####    Step 1    ####    Create the list of IDs    ####

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

id_list = IDlist('id.txt')

####    Step 2    ####    Download the list of sequences    ####

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

sequences = DownloadSeq(id_list)

####    Step 3    ####    Look for the N-glycosylation motif    ####

# N-glycosylation motif = N{P}[ST]{P}
# N = asparagine
# {P} = Not proline
# [ST] = serine or threonine

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

motif_dict = MotifFinder(sequences)

####    Step 4    ####    Print dictionary in the required form     ####

def printer(motif_dict):

    keys = list(motif_dict.keys())

    for i in keys:
        ind = ''
        indexes = motif_dict[i]

        for n in indexes:
            ind += (str(n) + ' ')

        print(i)
        print(ind)

printer(motif_dict)
