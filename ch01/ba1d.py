'''Find All Occurrences of a Pattern in a String'''

import sys


def find_all_occurrences(text, pattern):
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            occurrences.append(i)
    
    return occurrences


def main():
    with open(sys.argv[1], 'r') as f:
        pattern, text = f.read().strip().splitlines()
    
    result = find_all_occurrences(text, pattern)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
