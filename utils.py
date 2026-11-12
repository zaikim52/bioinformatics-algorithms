import sys

NUCLEOTIDES = "ACGT"
_COMPLEMENT = str.maketrans("ACGT", "TGCA")


def read_input() -> str:
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            return f.read()
    
    return sys.stdin.read() # EOF(Window: ctrl+Z, macOS/Linux: ctrl+D)


def kmers(text: str, k: int) -> list[str]:
    return [text[i:i + k] for i in range(len(text) - k + 1)]


def reverse_complement(text: str) -> str:
    return text.translate(_COMPLEMENT)[::-1]


def hamming_distance(str1: str, str2: str) -> int:
    return sum(a != b for a, b in zip(str1, str2))


def neighbors(pattern: str, d: int) -> set[str]:
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return set(NUCLEOTIDES)

    result = set()
    for suffix in neighbors(pattern[1:], d):
        if hamming_distance(pattern[1:], suffix) < d:
            result.update(base + suffix for base in NUCLEOTIDES)
        else:
            result.add(pattern[0] + suffix)
    return result