import argparse
import bibtexparser
from bibtexparser.bibdatabase import BibDatabase
import os.path


def main():

    args = parse_arg()
    if not (os.path.isfile(args.bib[0]) and os.path.isfile(args.bib[1])):
        print("input file not found")
        exit(0)

    with open(args.bib[0]) as bibtex_file:
        database1 = bibtexparser.load(bibtex_file)

    with open(args.bib[1]) as bibtex_file:
        database2 = bibtexparser.load(bibtex_file)

    result = subtract(database1, database2)

    if args.output:
        with open(args.output, 'w') as bibtex_file:
            bibtexparser.dump(result, bibtex_file)
    else:
        print(bibtexparser.dumps(result))


def subtract(database1, database2):
    db = BibDatabase()
    for entry in database1.entries:
        if not contains(entry, database2):
            db.entries.append(entry)
    return db


def contains(entry, database):
    for ent in database.entries:
        if entry['ID'] == ent['ID']:
            return True
    return False


def parse_arg():
    parser = argparse.ArgumentParser(prog='bibdiff')
    parser.add_argument('bib', nargs=2 ,type=str, help='an integer for the accumulator')
    parser.add_argument('-o', '--output', nargs='?', help='bib target file')
    return parser.parse_args()


if __name__ == "__main__":
    main()