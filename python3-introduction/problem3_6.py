# -problem3_6.py *- coding: utf-8 -*-

import sys

inputFile = open(sys.argv[1])
outputFile = open(sys.argv[2],'w')

for line in inputFile:
    line = line.strip("\n")
    outputFile.write(str(len(line)))
    outputFile.write("\n")
    
outputFile.close()
inputFile.close()