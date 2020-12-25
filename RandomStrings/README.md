# Introduction to Random Strings (A Rosalind problem)
## Contents
 - Python script containing my solution for the Rosalind problem
 - Two test data sets

## Usage
```Python
# Import the data
data = Dictmaker(filename)
# Calculate the probabilities
ProbCalc(data)
```
### Prerequisites
```Python
import math
```
## Methods
#### Importing the data as a dictionary
```Python
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
```
#### Calculate the probabilities (ProbCalc())
This function has a simple base counter, which stores the output as a dictionary. The relative GC and AT contents are then calculated from that dictionary.
```Python
# Simple base counter
bases_dict = {'A':0,'T':0,'G':0,'C':0}
seq = data_dict['seq']
for b in bases_dict:
    bases_dict[b] = seq.count(b)

# Collate the respective contents
GC_content = bases_dict['G'] + bases_dict['C']
AT_content = bases_dict['A'] + bases_dict['T']
```
Then the log of the probability of getting an equivalent string, randomly, is calculated. The results are then printed as a list in the format required for the Rosalind challenge
```Python
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
```
