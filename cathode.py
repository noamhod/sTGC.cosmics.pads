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
   elif("QL2P12" in fname and board=="QL2P12"): nbinsx = 4 
   elif("QL2P34" in fname and board=="QL2P34"): nbinsx = 5
   elif("QL2C12" in fname and board=="QL2C12"): nbinsx = 4
   elif("QL2C34" in fname and board=="QL2C34"): nbinsx = 4
   ### CH
   elif("QS2P12" in fname and board=="QS2P12"): nbinsx = 2
   elif("QS2P34" in fname and board=="QS2P34"): nbinsx = 3 
   elif("QS2C12" in fname and board=="QS2C12"): nbinsx = 3
   elif("QS2C34" in fname and board=="QS2C34"): nbinsx = 3
   else: print("unknown cathode.\nQuitting"); quit()
   nbinsy = int(n/nbinsx)
   bins.update( {board:{"npads":n, "nbinsx":nbinsx, "nbinsy":nbinsy}} )
   areas = dict(zip(pads,area))
   print("Board=%s: npads=%g, npadsx=%g, npadsy=%g" % (board,bins[board]["npads"],bins[board]["nbinsx"],bins[board]["nbinsy"]))
   return areas


def get(site):
   ### load pad areas from Benny's xlsx -- add here boards as necessary
   allareas = {}
   if(site=="IL"): 
      allareas.update( {"QS3C":{"12":load('QS3C12','cathodes/4931.10-14_QS3C12_Pads_Area.xlsx'), "34":load('QS3C34','cathodes/4931.10-51_QS3C34_Pads_Area.xlsx')} } )
      allareas.update( {"QL1P":{"12":load('QL1P12','cathodes/4921.00-14_QL1P12_Pads_Area.xlsx'), "34":load('QL1P34','cathodes/4921.00-51_QL1P34_Pads_Area.xlsx')} } )
      allareas.update( {"QL1C":{"12":load('QL1C12','cathodes/4921.10-14_QL1C12_Pads_Area.xlsx'), "34":load('QL1C34','cathodes/4921.10-51_QL1C34_Pads_Area.xlsx')} } )
   if(site=="RU"):                   
      allareas.update( {"QL3P":{"12":load('QL3P12','cathodes/4995.00-14_QL3P12_Pads_Area.xlsx'), "34":load('QL3P34','cathodes/4995.00-51_QL3P34_Pads_Area.xlsx')} } )
      allareas.update( {"QL3C":{"12":load('QL3C12','cathodes/4995.10-14_QL3C12_Pads_Area.xlsx'), "34":load('QL3C34','cathodes/4995.10-51_QL3C34_Pads_Area.xlsx')} } )
   if(site=="CL"):                   
      allareas.update( {"QS1P":{"12":load('QS1P12','cathodes/4963.00-14_QS1P12_Pads_Area.xlsx'), "34":load('QS1P34','cathodes/4963.00-51_QS1P34_Pads_Area.xlsx')} } )
      allareas.update( {"QS1C":{"12":load('QS1C12','cathodes/4963.10-14_QS1C12_Pads_Area.xlsx'), "34":load('QS1C34','cathodes/4963.10-51_QS1C34_Pads_Area.xlsx')} } )
   if(site=="CA"):                   
      allareas.update( {"QS3P":{"12":load('QS3P12','cathodes/4931.00-14_QS3P12_Pads_Area.xlsx'), "34":load('QS3P34','cathodes/4931.00-51_QS3P34_Pads_Area.xlsx')} } )
      allareas.update( {"QL2P":{"12":load('QL2P12','cathodes/5021.00-14_QL2P12_Pads_Area.xlsx'), "34":load('QL2P34','cathodes/5021.00-51_QL2P34_Pads_Area.xlsx')} } )
      allareas.update( {"QL2C":{"12":load('QL2C12','cathodes/5021.10-14_QL2C12_Pads_Area.xlsx'), "34":load('QL2C34','cathodes/5021.10-51_QL2C34_Pads_Area.xlsx')} } )
   if(site=="CH"):
      print("Not implemented yet, quitting."); quit()
      allareas.update( {"QS2P":{"12":load('QS2P12','cathodes/4748.00-14_QS2P12_Pads_Area.xlsx'), "34":load('QS2P34','cathodes/4748.00-51_QS2P34_Pads_Area.xlsx')} } )
      allareas.update( {"QS2C":{"12":load('QS2C12','cathodes/4748.10-14_QS2C12_Pads_Area.xlsx'), "34":load('QS2C34','cathodes/4748.10-51_QS2C34_Pads_Area.xlsx')} } )
   print(bins)
   return allareas


# def getnbins(quad,nchannels):
def getnbins(quad,gasvol):
   nbinsx = -1
   nbinsy = -1
   # n12 = bins[quad+"12"]["npads"]
   is12 = (gasvol==1 or gasvol==2)
   # nbinsx = bins[quad+"12"]["nbinsx"] if(nchannels==n12) else bins[quad+"34"]["nbinsx"]
   # nbinsy = bins[quad+"12"]["nbinsy"] if(nchannels==n12) else bins[quad+"34"]["nbinsy"]
   nbinsx = bins[quad+"12"]["nbinsx"] if(is12) else bins[quad+"34"]["nbinsx"]
   nbinsy = bins[quad+"12"]["nbinsy"] if(is12) else bins[quad+"34"]["nbinsy"]
   return nbinsx,nbinsy
   



