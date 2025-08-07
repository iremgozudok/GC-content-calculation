from structures import *


# DNA validation
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def gc_content(seq):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


# k karakterlik alt diziler oluşturur ve her biri için GC yüzdesini döndürür
def gc_content_subseq(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []
    # Loop through the sequence in steps of k to get non-overlapping subsequences
    for i in range(0, len(seq) - k + 1, k):
        # Extract a subsequence of length k starting at index i
        subseq = seq[i: i + k]

        # Calculate GC content of the subsequence and add it to the result list
        res.append(gc_content(subseq))

    # Return the list of GC content percentages for each subsequence
    return res
