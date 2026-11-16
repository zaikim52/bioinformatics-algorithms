'''Implement GreedyMotifSearch'''

from utils import read_input, kmers, create_profile, profile_most_probable_kmer, score


def greedy_motif_search(dnas, k, t):
    best_motifs = [dna[:k] for dna in dnas]
    for kmer in kmers(dnas[0], k):
        motifs = [kmer]
        for i in range(1, t):
            profile = create_profile(motifs)
            next_kmer = profile_most_probable_kmer(dnas[i], k, profile)
            motifs.append(next_kmer)
        
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    
    return best_motifs


def main():
    k, t, *dnas = read_input().strip().split()
    k = int(k)
    t = int(t)
    result = greedy_motif_search(dnas, k, t)
    for motif in result:
        print(motif)

if __name__ == "__main__":
    main()
