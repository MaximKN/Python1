#!/usr/bin/python
import sys, getopt, os.path
from openmath import *

"""
Simplifies OpenMath objects by reducing them down into Python types
before parsing them again back into OpenMath objects.
This has the effect of combining numbers together where possible.
"""
def simplify(inputfile, outputfile):
    if not os.path.isfile(inputfile):
        print "%s could not be opened because it doesn't exist, or due to permissions." % inputfile
    else:
        try:
            with open(outputfile, "w") as f:
                f.write(OMstring(ParseOMfile(inputfile)))
        except IOError:
            print "Error occurred while handlying files."
        
def main(argv):
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
            
    # check if user hasn't specified inputs
    if not 'inputfile' in locals()\
    or not 'outputfile' in locals():
        print usage
        sys.exit(2)
        
    simplify(inputfile, outputfile)

if __name__ == "__main__":
    main(sys.argv)
