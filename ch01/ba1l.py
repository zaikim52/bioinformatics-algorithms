'''Implement PatternToNumber'''

from utils import read_input, pattern_to_number


def main():
    text = read_input().strip()
    result = pattern_to_number(text)
    print(result)

if __name__ == "__main__":
    main()
