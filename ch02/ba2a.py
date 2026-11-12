'''Implement MotifEnumeration'''

from utils import read_input, neighbors, hamming_distance, kmers


def motif_enumeration(dnas, k, d):
    patterns = set()
    first_dna = dnas[0]
    for kmer in kmers(first_dna, k):
        for neighbor in neighbors(kmer, d):
            if all(any(hamming_distance(neighbor, dna[j:j + k]) <= d for j in range(len(dna) - k + 1)) for dna in dnas):
                patterns.add(neighbor)
    return sorted(patterns)


def main():
    nums, texts = read_input().strip().split('\n', 1)
    k, d = map(int, nums.split())
    dnas = texts.splitlines()
    result = motif_enumeration(dnas, k, d)
    print(' '.join(result))

if __name__ == "__main__":
    main()
