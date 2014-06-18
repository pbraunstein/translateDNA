#!/usr/bin/env python

#
# translateDNA.py
# Author: [YOUR_NAME_HERE]
# Date Created:
# Last Modified:
#
# Translates a DNA sequence provided on the command line into protein
# using a codon table from the command line. Only translates in the first
# frame. Exits if there are invalid characters in the DNA.
# Only A, C, T, G nucleotides allowed. The resulting transated sequence
# uses the one-letter amino acid codes (as opposed to the 3 letter codes).
# 
# GUIDELINES:
# You should write 3 helper functions for the main function: One to 
# Make sure the DNA sequence only has valid characters, one to read the
# codonTable.txt file into a dictionary, and one to translate the
# DNA sequence into a protein sequence using the codonTable dictionary that you
# created.
#
# When translating the DNA, use the one-letter amino acid codes, not the three-
# letter amino acid codes. For example, for phenylalanine, use F not Phe.
#
# Only translate the DNA in the first reading frame, don't worry about the
# other 5.
#
# Make a reasonable decision about what to do when the length of the inputted
# DNA sequence is not a multiple of 3.
#
# EG: Invoke the script using: ./translateDNA.py codonTable.txt TATACTT
#

from sys import argv
from sys import exit

def main():
        # Controls for number of arguments on the command line
        if len(argv) != 3:
                print "ERROR: Wrong Number of Arguments on the Command Line"
                usage()

        dnaSeq = argv[2].upper()  # Control for capitalization
        codonFile = argv[1]

        ####################### YOUR CODE HERE #########################

        # Check to make sure the DNA Sequence only has valid nucleotides
        #  exit nonzero with an error message if there are invalid nucs.


        # Read in the codons into a dictionary


        # Translate the DNA sequence into a protein sequence


        # Print the protein sequence

        ##############################################################
        
        exit(0)


# Prints the usage then exits nonzero
def usage():
        print "USAGE:", argv[0], "CODON_TABLE SEQUENCE_TO_TRANSLATE"
        exit(1)

if __name__ == '__main__':
        main()
