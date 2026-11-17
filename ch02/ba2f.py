'''Implement RandomizedMotifSearch'''

import random
from utils import read_input, kmers, create_profile_pseudocounts, profile_most_probable_kmer, score


def randomized_motif_search(dnas, k, t):
    motifs = []
    for dna in dnas:
        random_pos = random.randint(0, len(dna) - k)
        motifs.append(dna[random_pos:random_pos + k])
    
    best_motifs = motifs[:]
    while True:
        profile = create_profile_pseudocounts(motifs)
        motifs = [profile_most_probable_kmer(dna, k, profile) for dna in dnas]
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
        else:
            break
    
    return best_motifs


def n_times_randomized_motif_search(dnas, k, t, n):
    best_motifs = randomized_motif_search(dnas, k, t)
    for _ in range(n - 1):
        motifs = randomized_motif_search(dnas, k, t)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    
    return best_motifs


def main():
    k, t, *dnas = read_input().strip().split()
    k = int(k)
    t = int(t)
    result = n_times_randomized_motif_search(dnas, k, t, 1000)
    for motif in result:
        print(motif)

if __name__ == "__main__":
    main()
