'''Find a Position in a Genome Minimizing the Skew'''

import sys


def find_min_skew_pos(text):
    skew = 0
    min_skew = 0
    pos_skew = []
    for nucleotide in text:
        pos_skew.append(skew)
        if nucleotide == 'G':
            skew += 1
        elif nucleotide == 'C':
            skew -= 1
        if skew < min_skew:
            min_skew = skew
    
    return [i for i, s in enumerate(pos_skew) if s == min_skew]


def main():
    with open(sys.argv[1], 'r') as f:
        text = f.read().strip()
    
    result = find_min_skew_pos(text)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
