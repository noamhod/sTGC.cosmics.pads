#!/usr/bin/python
import os
import math

def read(quad,layer,etype):
   fIn = open("mapping.txt",'r')
   channels = []
   for line in fIn:
      words = line.split()
      if(quad  not in words[0]): continue
      if(layer not in words[1]): continue
      if(etype not in words[2]): continue
      channels.append( {"VMMid":int(words[3]), "VMMch":int(words[4]), "Benoit":int(words[5]), "Alam":int(words[6])} )
   fIn.close()
   return channels

def get(mapping, channel, channels):
   c = []
   for chn in channels:
      if(mapping=="VMM"):
         if(channel != str(chn["VMMid"])+":"+str(chn["VMMch"])): continue
      else:
         if(channel != str(chn[mapping])): continue
      c = chn
      break
   return c


