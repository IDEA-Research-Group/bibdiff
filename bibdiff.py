import argparse


def main():
    print(parse_arg())


def parse_arg():
    parser = argparse.ArgumentParser(prog='bibdiff')
    parser.add_argument('bib', nargs=2 ,type=str, help='an integer for the accumulator')
    parser.add_argument('-o', '--output', nargs='?', help='bib target file', default='stdout')
    return parser.parse_args()

if __name__ == "__main__":
    main()