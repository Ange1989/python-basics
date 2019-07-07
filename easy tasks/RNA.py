"""
transcribe to RNA
"""

transcription = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',

}


def transcribe_rna(dna):
    """Transcribe RNA
    """
    rna = ''
    for letter in dna:
        rna += transcription[letter]

    return rna

def validate_dna(dna):
    return set(dna).issubset(set('GCTA'))


if __name__ == '__main__':
    input_dna = input("Provide DNA: ")
    print(transcribe_rna(input_dna))