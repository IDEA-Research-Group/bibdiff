# -*- coding: utf-8 -*-
"""
The result is the first database, removing the entities existing in the second database, based on his IDs
This script remove from database1 (first parameter) the entities in database2 (second parameter)

José Miguel Pérez-Álvarez <josemi@us.es>
A. M. Reina Quintero <reinaqu@us.es>

"""
import argparse
from bibtexparser.bibdatabase import BibDatabase
import bibtexparser
from bibtexparser.bparser import BibTexParser
import os.path


def main():

    args = parse_arg()
    if not (os.path.isfile(args.bib[0]) and os.path.isfile(args.bib[1])):
        print("input file not found")
        exit(0)

    with open(args.bib[0]) as bibtex_file:
        database1 = bibtexparser.load(bibtex_file, BibTexParser(common_strings=True))

    with open(args.bib[1]) as bibtex_file:
        database2 = bibtexparser.load(bibtex_file, BibTexParser(common_strings=True))

    result = subtract(database1, database2)

    if args.output:
        with open(args.output, 'w') as bibtex_file:
            bibtexparser.dump(result, bibtex_file)
    else:
        print(bibtexparser.dumps(result))


def subtract(database1, database2):
    """
    The result of the operation is a database2 - database1.
    The result is the database2 without the entities of database1
    """
    db = BibDatabase()
    for entry in database1.entries:
        if not contains(entry, database2):
            db.entries.append(entry)
    return db


def contains(entry, database):
    """
    check if entry exits in the database, based on his ID
    """
    for ent in database.entries:
        if entry['ID'] == ent['ID']:
            return True
    return False


def parse_arg():
    parser = argparse.ArgumentParser(prog='bibdiff', description='The result is the first database, removing the '
                                                                 'entities existing in the second database, based on '
                                                                 'his IDs')
    parser.add_argument('bib', nargs=2, type=str)
    parser.add_argument('-o', '--output', nargs='?', help='file')
    return parser.parse_args()


if __name__ == "__main__":
    main()