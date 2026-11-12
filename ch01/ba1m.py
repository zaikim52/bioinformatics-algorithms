'''Implement NumberToPattern'''

from utils import read_input, number_to_pattern


def main():
    index, k = map(int, read_input().strip().split())
    result = number_to_pattern(index, k)
    print(result)

if __name__ == "__main__":
    main()
