'''Find the Most Frequent Words in a String'''

import sys


def most_frequent_words(text, length):
    freq = {}
    for i in range(len(text) - length + 1):
        word = text[i:i + length]
        freq[word] = freq.get(word, 0) + 1
    
    max_freq = max(freq.values())
    
    return [word for word, f in freq.items() if f == max_freq]


def main():
    with open(sys.argv[1], 'r') as f:
        text, length = f.read().strip().splitlines()
    
    result = most_frequent_words(text, int(length))
    print(' '.join(result))


if __name__ == "__main__":
    main()
