'''Implement DistanceBetweenPatternAndStrings'''

import random
from utils import read_input, kmers, hamming_distance


def distance_between_pattern_and_strings(pattern, dnas):
    k = len(pattern)
    distance = 0
    for dna in dnas:
        min_distance = float('inf')
        for kmer in kmers(dna, k):
            min_distance = min(min_distance, hamming_distance(pattern, kmer))
        distance += min_distance
    
    return distance


def main():
    pattern, *dnas = read_input().strip().split()
    result = distance_between_pattern_and_strings(pattern, dnas)
    print(result)

if __name__ == "__main__":
    main()
