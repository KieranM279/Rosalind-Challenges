
RNA = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'

####    Step 1    ####    Import the data    ####

def gCode(filename):

    genetic_code_file = open(str(filename))
    acids = {}

    # Parse the file containing the genetic code
    for ln in genetic_code_file.readlines():
        ln = ln.strip()
        ln = ln.split()

        # Create a dicionary of each codon
        codon = {'1-letter':ln[1],
                 '3-letter':ln[2],
                 'amino acid':ln[3]}
        # Compile the codon dictionaries
        acids[ln[0]] = codon

    return(acids)

protein_dict = gCode('genetic_code.tsv')

####    Step 2 - Translate the mRNA string to the protein string    ####

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

    print(protein)

RNA2Prot(RNA)
