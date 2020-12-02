# Finding the Transition/Transversion Ratio (tran)

## Contents

 - a script which takes in a FASTA formatted file of two sequences and calculates the ratio of transitions to transversions.
 - two example test sets

## Method

### Step 1 Dictmaker()

Import the FASTA formated sequences into a dictionary for later use.

### Step 2 TTRatio()

A function that loops through both sequences in the dictionary and tests whether each base is the same. If they are not it then checks if the different bases are of a different type (i.e. Purine vs Pyrimindine). This is done by referencing a dictionary initiated at the start of the function. The number of each are recorded and the ratio is calculated.
