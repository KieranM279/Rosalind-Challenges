import bio from SeqIO
import time

StartTime = time.time()

####    Preprocessing    ####

# Creating the Dicionary of sequences

def DictMaker():

    # Create a parsing object for the FASTA file
    record = SeqIO.parse('sequences.fasta','fasta')

    counter = 0
    dictionary = {}

    # Create a dictionary (of dictionaries) of the sequences
    for rec in record:
        counter += 1
        seq = ''

        # isolate each sequences as a string
        for b in rec.seq:
            seq += b

        # Create each entry and add it to the dictionary
        Entry = {'name':rec.name,
                 'seq':seq}
        dictionary[counter] = Entry

    return(dictionary)

Sequences = DictMaker()

# Finding the minimum length of the sequences
def MinMotifL():
    lengths = list()

    # Parse the data
    record = SeqIO.parse('test4_sequences.fasta', 'fasta')
    for fasta in record:

        length = len(fasta.seq)
        lengths.append(length)

    return(min(lengths))

# The maximum  length of the motif
MinMotif = MinMotifL()

####    Step 1    ####    Motif finding function    ####

def MotifF(motif, string):

    # Sets the length of the motif and string
    motif_length = len(motif)
    string_length = len(string)

    # Loops as a sliding window through the String
    for i in range(string_length):

        # Potential match to motif
        P_match = string[i:i+motif_length]

        # Conditional identifying the presence of the motif
        if len(P_match) < motif_length:
            break
        elif motif == P_match:
            Bool = True
            break
        else:
            Bool = False

    return(Bool)


####    Step 2    ####    Potential motif generation    ####

def MotifGen(seq):

    # List of bases
    bases = ['A','T','C','G']
    # Output list
    NewSeq = list()

    # Create all the sequences
    for i in bases:
        x = ''
        x = seq + i
        NewSeq.append(x)


    return(NewSeq)

####    Step 3    ####    See if motifs are present in the sequences    ####

# Remove Motifs that are not present in every sequence
def MotifUpdate(Potential_motifs):

    # Loop through the potential motifs
    for m in reversed(Potential_motifs):


        # Loop through the sequences
        for s in Sequences:

            Bool = MotifF(m, Sequences[s]['seq'])

            # If motif is not found remove it from the list
            if(Bool == True):
                continue
            elif(Bool == False):
                Potential_motifs.remove(m)
                break

    return(Potential_motifs)

####    Step 4    ####    Generate new list of potential motifs    ####

def Generation(Potential_motifs):

    New_Gen = []

    # Sequentially adds the next generation of motifs
    for i in Potential_motifs:
        New_Gen += MotifGen(i)

    return(New_Gen)

####    Step 5    ####    The Loop   ####

Potential_motifs = ['A','T','C','G']
MotifsTested = 0
for i in range(MinMotif):



    # Removes motifs that are not present in any of the sequences
    Updat_Start = time.time()
    MotifUpdate(Potential_motifs)
    Updat_End = time.time()
    u = Updat_End-Updat_Start

    print('Update time: ' + str(u))
    print('Number of potential motifs left: ' + str(len(Potential_motifs)))


    # Saves the previous generation of motifs
    if len(Potential_motifs) != 0:
        Save = Potential_motifs

    # If none of the new generation survive, the previous generation is printed
    if len(Potential_motifs) == 0:

        print('The longest shared motif(s) are:')
        if len(Save) == 1:
            print(''.join(Save))
        else:
            print(Save)
        break

    # makes the next generation
    Gen_Start = time.time()
    Potential_motifs = Generation(Potential_motifs)
    Gen_End = time.time()
    g = Gen_End-Gen_Start
    print('Gen Time: ' + str(g))
    print('Gen Size: ' + str(len(Potential_motifs)))
    MotifsTested += len(Potential_motifs)
    print('======================================================')


print('======================================================')
EndTime = time.time()
t = EndTime-StartTime
print('Total time elapsed: ' + str(t))
