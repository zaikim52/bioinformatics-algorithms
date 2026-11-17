'''Implement GibbsSampler'''

import random
from utils import read_input, create_profile_pseudocounts, profile_randomly_generated_kmer, score


def gibbs_sampler(dnas, k, t, N):
    motifs = []
    for dna in dnas:
        random_pos = random.randint(0, len(dna) - k)
        motifs.append(dna[random_pos:random_pos + k])
    
    best_motifs = motifs[:]
    for _ in range(N):
        i = random.randint(0, t - 1)
        profile = create_profile_pseudocounts(motifs[:i] + motifs[i + 1:])
        motifs[i] = profile_randomly_generated_kmer(dnas[i], k, profile)
        
        if score(motifs) < score(best_motifs):
            best_motifs = motifs[:]
    
    return best_motifs


def n_times_gibbs_sampler(dnas, k, t, N, n):
    best_motifs = gibbs_sampler(dnas, k, t, N)
    for _ in range(n - 1):
        motifs = gibbs_sampler(dnas, k, t, N)
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    
    return best_motifs


def main():
    k, t, N, *dnas = read_input().strip().split()
    k = int(k)
    t = int(t)
    N = int(N)
    result = n_times_gibbs_sampler(dnas, k, t, N, 20)
    for motif in result:
        print(motif)

if __name__ == "__main__":
    main()
