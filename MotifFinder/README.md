# Finding a Protein Motif (mprt)

This is my solution to the Rosalind challenge. It takes in a list of UniProt IDs and searches for the N-glycosylation motif in each sequence. Then outputs the locations in the format required by Rosalind. This script uses the SeqIO and request packages.

## Content

 - My script, which contains the solution (FindingMotif.py)
 - Three test files containing example IDs.

## Method

### Step 1 IDlist()

A function which takes a text file containing a list of UniProt IDs and inputs them into a usable list format

### Step 2 DownloadSeq()

A function which uses the request package to download the sequence from the UniProt database and write the output to a FASTA file in the working directory. Then uses the SeqIO package to read the FASTA file into a dictionary for later use. It never removes the FASTA files from the directory to they build up fast. I chose to leave them in as they often come in useful later on in projects that require them.

### Step 3 MotifFinder()

A function which loops through each sequence, in the dictionary made previously in step 2, and searches for the N-glycosylation motif. In traverses each sequence in a 4 residue sliding window and assigns four booleans (one per residue). If all four a true it records its current index, along with the respective ID in a dictionary.

### Step 4 printer()

A function which simple outputs the data in the format required by Rosalind, so I could just copy and paste the terminal output.
