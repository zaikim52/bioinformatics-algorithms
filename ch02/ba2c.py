'''Find a Profile-most Probable k-mer in a String'''

from utils import read_input, kmers


def profile_most_probable_kmer(text, k, profile):
    max_prob = -1
    most_probable_kmer = None
    
    for kmer in kmers(text, k):
        prob = 1
        for j, nucleotide in enumerate(kmer):
            prob *= profile[nucleotide][j]
        
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    
    return most_probable_kmer


def main():
    text, k, *profile_rows = read_input().strip().splitlines()
    k = int(k)
    profile = {nucleotide: [float(x) for x in row.split()] for nucleotide, row in zip("ACGT", profile_rows)}
    result = profile_most_probable_kmer(text, k, profile)
    print(result)

if __name__ == "__main__":
    main()
