# Translating an mRNA sequence into a protein
My solution to the Rosalind Challenge of turning any given mRNA string into its protein counterpart. It achieves this by importing the genetic code, contained within a '.tsv', into a usable dictionary. A second function then translates the mRNA string into a protein sting and then prints the output to the terminal.
## Usage
```python
# Set a variable as a mRNA sequence in string format
RNA = "mRNA_string"
# Import the genetic code data into a usable dictionary
protein_dict = gcode('genetic_code.tsv')
# Translate the mRNA into a protein string
RNA2Prot(RNA)
```
## Methods
#### Step 1 - Import the genetic code into a usable format
This function parses the '.tsv' file and imports the data as a dictionary of dictionaries. This means that for each codon, I could easily store the corresponding amino acid and the amino acid's single and triple letter code.
```python
def gCode(filename):

    genetic_code_file = open(str(filename))
    acids = {}

    # Parse the file containing the genetic code
    for ln in genetic_code_file.readlines():
        ln = ln.strip()
        ln = ln.split()

        # Create a dictionary of each codon
        codon = {'1-letter':ln[1],
                 '3-letter':ln[2],
                 'amino acid':ln[3]}
        # Compile the codon dictionaries
        acids[ln[0]] = codon

    return(acids)
```
#### Step 2 - Translate the mRNA sting into a protein
This function takes in the mRNA string and loops over the length of the sequences in steps of three. This forms a sliding window and shows each codon in the mRNA sequence. Then, using the genetic code dictionary of dictionaries, it translates each codon to its respective single letter amino acid code. The function then prints the output to the terminal.
```python
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
```
