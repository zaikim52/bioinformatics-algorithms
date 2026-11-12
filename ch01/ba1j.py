'''Find Frequent Words with Mismatches and Reverse Complements'''

import sys


def reverse_complement(text):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    return ''.join(complement[base] for base in text[::-1])


def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


def find_neighbors(word, d):
    if d == 0:
        return {word}
    if len(word) == 1:
        return {'A', 'C', 'G', 'T'}

    neighbors = set()
    suffix_neighbors = find_neighbors(word[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(word[1:], text) < d:
            for nucleotide in 'ACGT':
                neighbors.add(nucleotide + text)
        else:
            neighbors.add(word[0] + text)

    return neighbors


def most_frequent_words(text, k, d):
    freq = {}
    for seq in (text, reverse_complement(text)):
        for i in range(len(seq) - k + 1):
            for neighbor in find_neighbors(seq[i:i + k], d):
                freq[neighbor] = freq.get(neighbor, 0) + 1
    
    max_freq = max(freq.values())
    
    return [word for word, f in freq.items() if f == max_freq]


def read_input():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            return f.read()
    
    return sys.stdin.read() # EOF(Window: ctrl+Z, macOS/Linux: ctrl+D)


def main():
    text, nums = read_input().strip().splitlines()
    k, d = map(int, nums.split())

    result = most_frequent_words(text, k, d)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
