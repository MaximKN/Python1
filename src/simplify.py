#!/usr/bin/python
import sys, getopt, os.path
from openmath import *

def simplify(inputfile, outputfile):
    if os.path.isfile(inputfile):
        with open(inputfile, "r") as f:
            data = f.read()
        with open(outputfile, "w") as f:
            f.write(OMstring(ParseOMfile(inputfile)))
    else:
        print "%s could not be opened because it doesn't exist" % inputfile

def main(argv):
    inputfile  = ''
    outputfile = ''
    usage = "usage: %s -i <inputfile> -o <outputfile>" % argv[0]
    try:
        opts, args = getopt.getopt(argv[1:],"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print usage
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if (inputfile == '') or (outputfile == ''):
        print usage
        sys.exit()
    simplify(inputfile, outputfile)

if __name__ == "__main__":
    main(sys.argv)
