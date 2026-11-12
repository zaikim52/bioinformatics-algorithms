'''Generate the Frequency Array of a String'''

from utils import read_input


def pattern_to_number(pattern: str) -> int:
    num = 0
    for base in pattern:
        num = num * 4 + "ACGT".index(base)
    return num


def computing_frequencies(text: str, k: int) -> list[int]:
    frequency_array = [0] * (4 ** k)
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        frequency_array[pattern_to_number(kmer)] += 1
    return frequency_array


def main():
    text, k = read_input().strip().splitlines()
    result = computing_frequencies(text, int(k))
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
