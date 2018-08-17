#!/usr/bin/python
import sys
import string
import re

sdn = []
dpl = []
with open("data/sdnlist.txt") as infile:
    sdn = infile.read().split("\n\n")
with open("data/dpl.txt") as infile:
    dpl = infile.readlines()

punctuation = re.sub('@','',string.punctuation) # keep email addresses intact
def format_input(s):
    '''
    Takes a string, replaces punctuation with spaces (except @), then returns
    list of tokens (aka words).
    '''
    for c in punctuation:
        s=s.replace(c," ")
    s = s.lower().strip()
    s = re.sub('\s+', ' ', s)
    return s.split(' ')


searchinput = []
with open(sys.argv[1]) as infile:
    searchinput = infile.readlines()

for srec in searchinput:
    srec = srec.strip()
    #print(format_input(srec))
    for sdnrec in sdn:
        sdnrecL = sdnrec.lower()
        present = 1
        for token in format_input(srec):
            if token not in sdnrecL:
                present = 0
        if present:
            print(srec + " is in the SDN")
            break
    for dplrec in dpl:
        dplrecL = dplrec.lower()
        present = 1
        for token in format_input(srec):
            if token not in dplrecL:
                present = 0
        if present:
            print(srec + " is in the DPL")
            break
