#!/usr/bin/python
import sys, getopt
from openmath import *

def simplify(inputfile, outputfile):
    with open(inputfile, "r") as f:
        data = f.read();
    with open(outputfile, "w") as f:
        f.write(OMstring(ParseOMfile(inputfile)));

def main(argv):
    inputfile  = ''
    outputfile = '' 
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    simplify(inputfile, outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])
