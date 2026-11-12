'''Compute the Hamming Distance Between Two Strings'''

import sys


def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))


def main():
    with open(sys.argv[1], 'r') as f:
        str1, str2 = f.read().strip().splitlines()

    result = hamming_distance(str1, str2)
    print(result)

if __name__ == "__main__":
    main()
