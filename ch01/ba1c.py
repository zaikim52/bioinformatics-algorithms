'''Find the Reverse Complement of a String'''

import sys


def reverse_complement(text):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    return ''.join(complement[base] for base in text[::-1])


def main():
    with open(sys.argv[1], 'r') as f:
        text = f.read().strip()
    
    result = reverse_complement(text)
    print(result)

if __name__ == "__main__":
    main()
