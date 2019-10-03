#!/usr/bin/python
import os
import math
import mapping
import argparse

parser = argparse.ArgumentParser(description='cmdmapping.py...')
parser.add_argument('-q', metavar='quad', required=True,  help='Quad [QS1P/C, QS2P/C, QS3P/C, QL1P/C, QL2P/C, QL3P/C]')
parser.add_argument('-l', metavar='layer', required=True,  help='Layer number [1...4]')
parser.add_argument('-e', metavar='electrode', required=True,help='Electrode type [wire/pad/strip]')
parser.add_argument('-m', metavar='mapping', required=True,help='Mapping [VMM, Alam, Benoit]')
parser.add_argument('-c', metavar='channel', required=True,help='Channel number [... (for VMM, use e.g. 1:8)]')
argus  = parser.parse_args()

### do the work
channels = mapping.read(argus.q, argus.l, argus.e)
print("got %g channels" % len(channels))
# print(channels)
channel = mapping.get(argus.m, argus.c, channels)
print(channel)


