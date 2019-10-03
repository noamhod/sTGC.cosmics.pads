#!/usr/bin/python
import os
import math
import pandas
import xlrd

bins = {}

### load pad areas from Benny's xlsx
def load(board,fname):
   df = pandas.read_excel(fname)
   # pads = df['Pad No.'].values
   pads = df['Alam'].values
   area = df['Area mm^2'].values
   print("===== reading %s =====" % board)
   print("Pads=",pads)
   print("Area=",area)
   n = len(pads)
   nbinsx = 0
   ### add board types as necessary
   ### IL
   if  ("QS3C12" in fname and board=="QS3C12"): nbinsx = 3
   elif("QS3C34" in fname and board=="QS3C34"): nbinsx = 3
   elif("QL1P12" in fname and board=="QL1P12"): nbinsx = 6
   elif("QL1P34" in fname and board=="QL1P34"): nbinsx = 7
   elif("QL1C12" in fname and board=="QL1C12"): nbinsx = 6
   elif("QL1C34" in fname and board=="QL1C34"): nbinsx = 6
   ### RU
   elif("QL3P12" in fname and board=="QL3P12"): nbinsx = 4
   elif("QL3P34" in fname and board=="QL3P34"): nbinsx = 5
   elif("QL3C12" in fname and board=="QL3C12"): nbinsx = 4
   elif("QL3C34" in fname and board=="QL3C34"): nbinsx = 4
   ### CL
   elif("QS1P12" in fname and board=="QS1P12"): nbinsx = 4
   elif("QS1P34" in fname and board=="QS1P34"): nbinsx = 3
   elif("QS1C12" in fname and board=="QS1C12"): nbinsx = 4
   elif("QS1C34" in fname and board=="QS1C34"): nbinsx = 4
   ### CA
   elif("QS3P12" in fname and board=="QS3P12"): nbinsx = 2
   elif("QS3P34" in fname and board=="QS3P34"): nbinsx = 3

   else:
      print("unknown cathode.\nQuitting")
      quit()
   nbinsy = int(n/nbinsx)
   bins.update( {board:{"npads":n, "nbinsx":nbinsx, "nbinsy":nbinsy}} )
   areas = dict(zip(pads,area))
   print("Board=%s: npads=%g, npadsx=%g, npadsy=%g" % (board,bins[board]["npads"],bins[board]["nbinsx"],bins[board]["nbinsy"]))
   return areas



def getnbins(quad,nchannels):
   nbinsx = -1
   nbinsy = -1
   n12 = bins[quad+"12"]["npads"]
   nbinsx = bins[quad+"12"]["nbinsx"] if(nchannels==n12) else bins[quad+"34"]["nbinsx"]
   nbinsy = bins[quad+"12"]["nbinsy"] if(nchannels==n12) else bins[quad+"34"]["nbinsy"]
   return nbinsx,nbinsy
   



