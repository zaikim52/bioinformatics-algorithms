'''Find the Most Frequent Words with Mismatches in a String'''

import sys


def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


def find_approx_occurrences(pattern, text, d):
    occurrences = []
    pattern_length = len(pattern)
    for i in range(len(text) - pattern_length + 1):
        substring = text[i:i + pattern_length]
        if hamming_distance(pattern, substring) <= d:
            occurrences.append(i)
    return occurrences


def main():
    with open(sys.argv[1], 'r') as f:
        pattern, text, d = f.read().strip().splitlines()
        d = int(d)

    result = find_approx_occurrences(pattern, text, d)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
