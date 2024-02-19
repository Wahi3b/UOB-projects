def complimentDNAsequence(sequence):
    '''
    (str) -> str

    Take in a string input of a DNA sequence and return its compliment 
    >>> complimentDNAsequence('ATTCG')
    'TAAGC'
    >>> complimentDNAsequence('AATTGCCGT')
    'TTAACGGCA'
    >>> complimentDNAsequence('ATATGGCATA')
    'TATACCGTAT'

    '''
    comDNAseq = ''
    for char in sequence:
        if char == 'A': comDNAseq += 'T'
        elif char == 'T': comDNAseq += 'A'
        elif char == 'G': comDNAseq += 'C'
        else: comDNAseq += 'G'
    return comDNAseq 
if __name__ == "__main__":
    
    import doctest
    doctest.testmod(verbose=True)
