# -*- coding: utf-8 -*-
import math

####    Step 1    ####    Import the data    ####

def Dictmaker(filename):

    # Initialise the dictionary and open the file
    file = open(filename,'r')
    data_dict = {'seq':0, 'pGC':0}
    line_counter = 0

    # Loop through the lines in the file
    for ln in file:
        ln = ln.strip()

        # The first line is the sequence
        if line_counter == 0:
            data_dict['seq'] = str(ln)
        # The second is the GC content probability array
        elif line_counter == 1:
            ln = ln.split()
            data_dict['pGC'] = ln

        line_counter += 1

    return(data_dict)


####    Step 2    ####    Calculate the probability as LOG    ####

def ProbCalc(data_dict):

    # Simple base counter
    bases_dict = {'A':0,'T':0,'G':0,'C':0}
    seq = data_dict['seq']
    for b in bases_dict:
        bases_dict[b] = seq.count(b)

    # Collate the respective contents
    GC_content = bases_dict['G'] + bases_dict['C']
    AT_content = bases_dict['A'] + bases_dict['T']

    probabilities = list()

    # Loop through each GC probability
    for p in data['pGC']:

        # Calculate probabilities of each base appearing
        p = float(p)
        pGC = p/2
        pAT = (1-p)/2

        # Calculate the Log of the overall probability to 3 d.p.
        prob = math.log10((pAT**AT_content)*(pGC**GC_content))
        probabilities.append('%0.3f' % prob)

        # print in required format
    print(*probabilities, sep = ' ')


####    Step 3    ####    Runs the functions    #####

# Import the data in dictionary format
data = Dictmaker('rosalind_prob.txt')

# Calculate the probabilities and print to terminal
ProbCalc(data)
