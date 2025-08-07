from DNAToolkit import *
from utilities import colored
import random

# Creating a random DNA sequence for testing:
randDNASeq = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNASeq)

print(f"\nSequence: {colored(DNAStr)}\n")
print(f"Sequence Lenght: {len(DNAStr)}\n")
print(f"GC Content: {gc_content(DNAStr)}%\n")
print(f"GC Content in Subsection k=5: {gc_content_subseq(DNAStr, k=5)}\n")
