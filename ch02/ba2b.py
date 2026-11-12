'''Find a Median String'''

from utils import read_input, hamming_distance, number_to_pattern


def find_median_string(dnas, k):
    min_distance = float('inf')
    median = None
    for i in range(4 ** k):
        pattern = number_to_pattern(i, k)
        distance = sum(min(hamming_distance(pattern, dna[j:j + k]) for j in range(len(dna) - k + 1)) for dna in dnas)
        if distance <= min_distance:
            min_distance = distance
            median = pattern
    
    return median


def main():
    k, texts = read_input().strip().split('\n', 1)
    k = int(k)
    dnas = texts.splitlines()
    result = find_median_string(dnas, k)
    print(result)

if __name__ == "__main__":
    main()
