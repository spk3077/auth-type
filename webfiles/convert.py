"""
File: convert.py
Assignment: Mini-Project 3
Lanuguage: python3
Author: Sean Kells <spk3077@rit.edu>
Purpose: Convert a file to a module acceptable format. Does not modify original, only creates new file.
Running: python3 convert.py <source_file> <index> <target_file>
Example Run: python3 convert.py ./original/top500Domains.csv ./formatted/top500_formatted.txt
"""
import sys
import csv

from pathlib import Path


def _check_input():
    """
    _check_input checks for input errors

    :return: Nothing
    """
    # Check invalid argument number (too few arguments)
    if len(sys.argv) < 4:
        print("Too few input arguments are present; three is necessary")
        print("EX: python3 convert.py <source_file> <index> <target_file>")
        print("EX: python3 convert.py ./original/top500Domains.csv 1 ./formatted/top500_formatted.txt")
        exit(1)
    
    # Check invalid argument number (too many arguments)
    elif len(sys.argv) > 4:
        print("Too many input arguments; three is necessary")
        print("EX: python3 convert.py <source_file> <index> <target_file>")
        print("EX: python3 convert.py ./original/top500Domains.csv 1 ./formatted/top500_formatted.txt")
        exit(1)

    # Check <index> Argument Validity
    elif not sys.argv[2].isdigit():
        print("The specified index must be an integer")
        print("EX: python3 convert.py <source_file> <index> <target_file>")
        print("EX: python3 convert.py ./original/top500Domains.csv 1 ./formatted/top500_formatted.txt")
        exit(1)


def csv_to_formatted(source_file, index, target_file):
    """
    csv_to_formatted creates a formatted file from a specified CSV

    :param source_file: the CSV file to format
    :param index: column to parse out
    :param target_file: the output formmated file name
    :return: Nothing
    """
    csv_sites: set = set()
    try:
        with open(source_file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                csv_sites.add("https://" + row[int(index)])
            
    except FileNotFoundError:
        print("The specified file, '%s', does not exist" % (sys.argv[1],), end='\n\n')
        exit(1)
    except (IOError, Exception):
        print("The specified file, '%s', could not open" % (sys.argv[1],), end='\n\n')
        exit(1)
    
    print(csv_sites)


def main():
    """
    main is the entry to execute conversion

    :return: Nothing
    """
    _check_input()
    csv_to_formatted(sys.argv[1], sys.argv[2], sys.argv[3])


if __name__ == '__main__':
    main()
