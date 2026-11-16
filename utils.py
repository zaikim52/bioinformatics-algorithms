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


def pattern_to_number(pattern: str) -> int:
    num = 0
    for base in pattern:
        num = num * 4 + "ACGT".index(base)
    
    return num


def number_to_pattern(index: int, k: int) -> str:
    pattern = []
    for _ in range(k):
        index, r = divmod(index, 4)
        pattern.append("ACGT"[r])
    
    return ''.join(reversed(pattern))


def create_profile(motifs: list[str]) -> dict[str, list[float]]:
    k = len(motifs[0])
    profile = {nucleotide: [0] * k for nucleotide in NUCLEOTIDES}
    for motif in motifs:
        for j, nucleotide in enumerate(motif):
            profile[nucleotide][j] += 1
    
    t = len(motifs)
    for nucleotide in NUCLEOTIDES:
        profile[nucleotide] = [count / t for count in profile[nucleotide]]
    
    return profile


def create_profile_pseudocounts(motifs: list[str]) -> dict[str, list[float]]:
    k = len(motifs[0])
    profile = {nucleotide: [1] * k for nucleotide in NUCLEOTIDES}
    for motif in motifs:
        for j, nucleotide in enumerate(motif):
            profile[nucleotide][j] += 1
    
    t = len(motifs)
    for nucleotide in NUCLEOTIDES:
        profile[nucleotide] = [count / (t + 4) for count in profile[nucleotide]]
    
    return profile


def profile_most_probable_kmer(text: str, k: int, profile: dict[str, list[float]]) -> str:
    max_prob = -1
    most_probable_kmer = None
    for kmer in kmers(text, k):
        prob = 1
        for j, nucleotide in enumerate(kmer):
            prob *= profile[nucleotide][j]
        
        if prob > max_prob:
            max_prob = prob
            most_probable_kmer = kmer
    
    return most_probable_kmer


def score(motifs: list[str]) -> int:
    k = len(motifs[0])
    score = 0
    for j in range(k):
        counts = {nucleotide: 0 for nucleotide in NUCLEOTIDES}
        for motif in motifs:
            counts[motif[j]] += 1
        max_count = max(counts.values())
        score += len(motifs) - max_count
    
    return score