'''Find Patterns Forming Clumps in a String'''

import sys


def find_clumps(text, k, l, t):
    clumps = set()
    for i in range(len(text) - l + 1):
        window = text[i:i + l]
        for j in range(len(window) - k + 1):
            pattern = window[j:j + k]
            if window.count(pattern) >= t:
                clumps.add(pattern)
    
    return list(clumps)


def main():
    with open(sys.argv[1], 'r') as f:
        text, nums = f.read().strip().splitlines()
        k, l, t = nums.split()
    
    result = find_clumps(text, int(k), int(l), int(t))
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
