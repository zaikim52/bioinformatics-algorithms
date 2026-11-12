'''Compute the Number of Times a Pattern Appears in a Text'''

import sys


def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    
    return count


def main():
    with open(sys.argv[1], 'r') as f:
        text, pattern = f.read().strip().splitlines()
    
    result = pattern_count(text, pattern)
    print(result)


if __name__ == "__main__":
    main()
