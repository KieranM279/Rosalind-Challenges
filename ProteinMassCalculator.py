# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:41:31 2020

@author: kiera
"""
# enter you directory
import os
os.chdir("")

sequence = 'AWALCCVFLRYPKACQLRNHSTSKCWRLPPAFNLDITADMENFLFAYNGKKWAREPGKCPRNACFFCLGEDALFPCYAQKVPCKWLMPESFHWAHVDTGNYQMAYQRTSWMPTSNVMIVSCLHCGLAQCNSECWEHVHRRLVLCTIFALKMVFSRGERIADSTEFTVCTYWNPAFNMFNFLNRYGAYIEALPFWMRMRMPLQWWNDTRYRDVMLHEHHYGLLLDPKAIRNKHTKVSMAPLADESAMTGQRWPYKAKYDAVAPDSSWQRVGWEHIVHLFEMIKSLSFNMPGYLWCKRANLRSIKTEGRYYFHLESAMAETAWSLYSLKYSDPVHEVRIEWPGCKAGPGYQSRCTGPHHQFHHPHPGHNSCTDCKDYQCASPHQICCNYWIAIWRYIGCHWVLKWMCEAGQFFEFIVVEWMWAHAQKQVCCRCECQGEDSDGLIDCTMHVTPLVRDTCPVFMSSMIMIVTMELYPTSDHDHMPWIIMWMTYFLHFSNSGMYANMVPHWTQSNTHTTKYQWIENTTFCLIQQWAAEDVEINPFMKHGYAEVGCLKEDINAKACRMPHGYAVPELRSFWWDTYKWVFASNVCFFTARVCRLDNQSMMHCNETRKLPWFPPVPMAPVGKAYSWMPSMNNQCITAYEYCDQEYDLMCEEVYHAMMPIVSTQRWMKWCNTFAILKEPWKQWQPCYYFYVFTTKYQRMPDKPRFDLEFEWWCCHLNNRGSDRETEVHKWFMDAKNGSSNQYHRLCYACRVPGGVPELFFWASDHSHYVKQIYRCADLITPWKFKDPASYDHMDDFEDHNNYLADTGMMLGYTTGPEMEMMPICDWECMTEQRQHVSAKIKTTKNYFQCERTIWWVNMICSVESSI'

def AAcounter(sequence):
    
    # Initiate the dicionary and final mass
    MassDict = {}
    TotalMass = 0
    
    # Opens a text file which contains individual AA mass data
    masses = open('mass.txt')
    
    # Creates a dictionary of dictionaries of the data in the mass data
    for ln in masses:
        ln = ln.strip()
        ln = ln.split()
        
        temp = {'freq':0,'mass':ln[1]}
        MassDict[ln[0]] = temp
    
    # Loops through the Dictionary and adds the frequencies of each amino acid in the sequence
    for aa in MassDict:
        
        weightedMass = 0
        
        MassDict[aa]['freq'] = sequence.count(aa)
        
        # Calculates the weighted mass of the amino acids in the sequence
        frequency = int(MassDict[aa]['freq'])
        daltons = float(MassDict[aa]['mass'])
        weightedMass = float(frequency*daltons)
        
        # Creates a cumulative mass of the protein sequence
        TotalMass += weightedMass
    
    return(TotalMass)
    
ProteinMass = AAcounter(sequence)

    
    
