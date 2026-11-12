'''Generate the d-Neighborhood of a String'''

from utils import read_input, neighbors


def main():
    pattern, d = read_input().strip().split()
    d = int(d)
    result = neighbors(pattern, d)
    print('\n'.join(result))

if __name__ == "__main__":
    main()
