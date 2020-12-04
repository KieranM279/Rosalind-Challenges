from Bio import SeqIO

####    Pre-processing    ####

def dictmaker(filename):

    # Open file
    genetic_code_file = open(str(filename))
    acids = {}

    # Loop through the lines of the .tsv file
    for ln in genetic_code_file.readlines():
        ln = ln.strip()
        ln = ln.split()

        # Build dictionary (of dictionaries) entry by entry
        codon = {'1-letter':ln[1],
                 '3-letter':ln[2],
                 'amino acid':ln[3]}
        acids[ln[0]] = codon

    return(acids)

protein_map = dictmaker('genetic_code.tsv')

####    Step 1    ####    Import sequence from FASTA file    ####

def seqF(filename):

    # Read FASTA file using SeqIO package
    record = SeqIO.read(filename,'fasta')
    seq = str(record.seq)

    return(seq)

sequence = seqF('sequence.fasta')

#### Step 2    ####    Create the reverse complement    ####

# First a simple reverse string function
def StringRev(string):
    rev = ''

    # Loop the sequence in reverse
    for i in range(len(string)):
        rev += string[-i-1]

    return(rev)

# A function to find the reverse complementary strand
# Uses StringRev()
def RevCompGen(dna):

    bases_dict = {'A':'T','T':'A','C':'G','G':'C'}

    comp_strand = ''
    # Goes through each base and replaces it with its partner
    for b in dna:
        comp_strand += bases_dict[b]

    # Reverse the new sequence
    rev_comp = StringRev(comp_strand)

    return(rev_comp)


####    Step 3    ####    Create a dictionary of the sequences    ####

def seqDict(seq):

    Dict = {'sequence':seq,
          'rev_comp':RevCompGen(seq)}

    return(Dict)

sequence_dict = seqDict(sequence)

####    Step 4    ####    Convert DNA to RNA    ####

def DNA2RNA(Dict):

    keys = list(Dict.keys())

    Dict2 = {'sequence':'',
             'rev_comp':''}

    # Loops through the dictionary entries and replaces Thymine with Uracil
    for key in keys:

        # Replace 'T' with 'U' in the sequence
        string = Dict[key]
        rna = string.replace('T','U')

        # Adds the new rna to a dictionary
        Dict2[key] = rna

    return(Dict2)

sequence_dict = DNA2RNA(sequence_dict)

####    Step 5    ####    Create a codon dictionary    ####

# A function to find all of the possible start codons in a sequence
def S_codon(seq):

    Slist = list()

    for i in range(len(seq)):
        triplet = seq[i:i+3]

        if triplet == 'AUG':
            Slist.append(i)

    return(Slist)

# A function to create a dictionary of the start codon indices
def codonDict(Dict):

    keys = list(Dict.keys())

    codon_dict = {'sequence':list(),
                  'rev_comp':list()}

    for key in keys:

        codon_dict[key] = S_codon(Dict[key])

    return(codon_dict)

codon_dict = codonDict(sequence_dict)

####    Step 7    ####    Convert RNA Open Reading Frames to Protein    ####

def RNA2Prot(seq_dict,codon_dict):

    keys = list(seq_dict.keys())
    proteins = list()

    # Loops through the keys
    for key in keys:

        # Loops though the list of codon coordinates
        for i in codon_dict[key]:
            prot = ''

            # Loops through each codon, starting from the start codon
            for b in range(i, len(seq_dict[key]), 3):

                sequence = seq_dict[key]
                triplet = sequence[b:b+3]

                # Break when the sequence ends
                if len(triplet) < 3:
                    break

                # Isolate amino acid from reference dictionary
                aa = protein_map[triplet]['1-letter']

                # Stop when a stop codon is reached
                if (aa == 'X'):
                    prot += aa
                    break

                prot += aa

            # Add protein to list if a complete open reading frame is found
            if prot[-1] == 'X':
                prot = prot.replace('X','')
                proteins.append(prot)

    # Remove duplicates
    proteins = list(dict.fromkeys(proteins))
    return(proteins)


proteins = RNA2Prot(sequence_dict,codon_dict)

####    Step 8    ####    Print to terminal for Rosalind    ####

def printer(lists):

    for i in lists:
        print(i)

printer(proteins)
