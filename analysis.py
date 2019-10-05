#!/usr/bin/python
import os
import math
import mapping, cathode, flagger
import ROOT
from ROOT import TFile, TTree, TH1D, TH2D, TLorentzVector, TVector3, TCanvas
import argparse
parser = argparse.ArgumentParser(description='analysis.py...')
parser.add_argument('-s', metavar='site', required=True,  help='IL [IL, RU, CH, CL, CA]')
argus  = parser.parse_args()

### ROOT general
ROOT.gROOT.SetBatch(1)
ROOT.gStyle.SetOptFit(0);
ROOT.gStyle.SetOptStat(0);
ROOT.gStyle.SetPadBottomMargin(0.15)
ROOT.gStyle.SetPadLeftMargin(0.15)
ROOT.gStyle.SetPadRightMargin(0.15)

### layesrs measured are defined in sites' files
files = []
if(argus.s=="IL"): import IL; files = IL.files
if(argus.s=="RU"): import RU; files = RU.files
if(argus.s=="CH"): import CH; files = CH.files
if(argus.s=="CL"): import CL; files = CL.files
if(argus.s=="CA"): import CA; files = CA.files

### load pad areas from Benny's xlsx
allareas = cathode.get(argus.s)

### dictionaries
histos = {}
hbands = {}
ohistos = {}
o2histos = {}
h2histos = {}
o2hdummy = {}
h2hdummy = {}
h2hareas = {}
db = {}

### globals
suffix = "_final_histograms_pads.root"

### how much to trim (per site)
if(argus.s=="IL"): ftrim = IL.ftrim
if(argus.s=="RU"): ftrim = RU.ftrim
if(argus.s=="CH"): ftrim = CH.ftrim
if(argus.s=="CL"): ftrim = CL.ftrim
if(argus.s=="CA"): ftrim = CA.ftrim


### load database
for f in files:
   words = f.split("_")
   db.update({f:{"qname" : words[0],
                 "qid"   : int(words[1]),
                 "layer" : int(words[2].replace("L","")),
                 "HV"    : float(words[3].replace("kV","")),
                 "date"  : words[4]}
            })


### get histos
for f in files:
   quad  = db[f]["qname"]
   layer = db[f]["layer"]
   channels = mapping.read(quad,str(layer),"pad")
   nchannels = len(channels)
   fname = f+suffix
   hname = "Number_of_Hits"+str(layer)
   tfile = TFile("root/"+fname,"READ")
   print("Getting: %s from file: %s" % (hname,"root/"+fname))
   histos.update({f:tfile.Get(hname).Clone()})
   histos[f].SetDirectory(0)
   ### 2D binning depends on the cathode board
   nbinsx,nbinsy = cathode.getnbins(quad,nchannels)
   print("nbinsx=%g, nbinsy=%g" %(nbinsx,nbinsy))
   o2histos.update( { f:TH2D(f+"_2d_norm",         "Normalised, in board mapping (Alam);;;Hits/Area [mm^{-2}]", nbinsx,0.5,nbinsx+0.5, nbinsy,0.5,nbinsy+0.5) } )
   o2hdummy.update( { f:TH2D(f+"_2d_norm_dummy",   "Normalised, in board mapping (Alam);;;Hits/Area [mm^{-2}]", nbinsx,0.5,nbinsx+0.5, nbinsy,0.5,nbinsy+0.5) } )
   h2histos.update( { f:TH2D(f+"_2d_regular",      "Profile, in board mapping (Alam);;;Hits",                   nbinsx,0.5,nbinsx+0.5, nbinsy,0.5,nbinsy+0.5) } )
   h2hdummy.update( { f:TH2D(f+"_2d_reglar_dummy", "Profile, in board mapping (Alam);;;Hits",                   nbinsx,0.5,nbinsx+0.5, nbinsy,0.5,nbinsy+0.5) } )
   h2hareas.update( { f:TH2D(f+"_2d_areas", "Pads area, in board mapping (Alam);;;Pad Area [mm^{2}]", nbinsx,0.5,nbinsx+0.5, nbinsy,0.5,nbinsy+0.5) } )
   o2histos[f].SetDirectory(0) 
   h2histos[f].SetDirectory(0) 
   o2hdummy[f].SetDirectory(0) 
   h2hdummy[f].SetDirectory(0) 
   h2hareas[f].SetDirectory(0)


### loop over pads of all histograms
for f in files:
   h = histos[f]
   ohistos.update({f:h.Clone(f+"_normalised")})
   ohistos[f].Reset()
   ohistos[f].SetTitle("Normalised to pad area (Benoit)" )
   quad  = db[f]["qname"]
   layer = str(db[f]["layer"])
   channels = mapping.read(quad,layer,"pad")
   nchannels = len(channels)
   n12 = len(allareas[quad]["12"])
   areas = allareas[quad]["12"] if(nchannels==n12) else allareas[quad]["34"]
   for benoit_pad in range(1,h.GetNbinsX()+1):
      channel = mapping.get("Benoit",str(benoit_pad),channels)
      if(len(channel)==0):
         print("quad:%s, layer:%s, channel:%g for %s ???\nQuitting." % (quad,layer,benoit_pad,f))
         quit()
      vmm_id   = channel["VMMid"]
      vmm_ch   = channel["VMMch"]
      alam_pad = channel["Alam"]
      pad_area = areas[alam_pad]
      print("Benoit:%g --> Alam:%g --> VMM%g:%g, Area=%g mm2" % (benoit_pad,alam_pad,vmm_id,vmm_ch,pad_area))
      z = h.GetBinContent(benoit_pad)/pad_area
      ohistos[f].SetBinContent(benoit_pad,z)
      ohistos[f].GetYaxis().SetTitle("Number of Hits / Pad area [mm^{-2}]")
      ### 2d histos
      nx = o2histos[f].GetNbinsX()
      ny = o2histos[f].GetNbinsY()
      mod = alam_pad%nx
      x = (nx+1-mod) if(mod!=0) else (1-mod)
      y = ny+1-math.ceil(alam_pad/nx)
      binxy = o2histos[f].FindBin(x,y)
      o2histos[f].SetBinContent(binxy,z)
      h2histos[f].SetBinContent(binxy,h.GetBinContent(benoit_pad))
      o2hdummy[f].SetBinContent(binxy,alam_pad)
      h2hdummy[f].SetBinContent(binxy,alam_pad)
      h2hareas[f].SetBinContent(binxy,pad_area)


def txtsummary(f,h,avg,rms):
   summary = ""
   ftxt = open("txt/"+f+".txt","w")
   ftxt.write(f+"\n")
   ftxt.write("Mean and RMS calculated by trimming "+str(ftrim*100)+"% of the chanels with the highest normalised occupancy\n\n")
   quad  = db[f]["qname"]
   layer = str(db[f]["layer"])
   channels = mapping.read(quad,layer,"pad")
   known_channels = {}
   if(argus.s=="IL"): known_channels = IL.known_channels[quad]
   if(argus.s=="RU"): known_channels = RU.known_channels[quad]
   if(argus.s=="CH"): known_channels = CH.known_channels[quad]
   if(argus.s=="CL"): known_channels = CL.known_channels[quad]
   if(argus.s=="CA"): known_channels = CA.known_channels[quad]
   for b in range(1,h.GetNbinsX()+1):
      x = h.GetBinCenter(b)
      y = h.GetBinContent(b)
      if(((avg-2*rms)>0 and y<(avg-2*rms)) or ((avg-2*rms)<0 and y<(avg-1*rms)) or y<=0):
         channel = mapping.get("Benoit",str(b),channels)
         txt = str(channel)
         if({channel["VMMid"]:channel["VMMch"]} in known_channels): 
            txt += " --> dead VMM channel / GFZ problem / partial trigger coverage / high threshold / ..."
         ftxt.write(txt+"\n")
         summary += f+": "+txt+"\n"
   ftxt.close()
   return summary


### draw hit profiles
pdf = "pdf/"+argus.s+"_hitprofiles.pdf"
i=0
summary = ""
for f in files:
   cnv = TCanvas("cnv","",1000,1000)
   cnv.Divide(2,2)
   p1 = cnv.cd(1)
   p2 = cnv.cd(2)
   p3 = cnv.cd(3)
   p4 = cnv.cd(4)
   p1.cd()
   histos[f].SetTitle(f)
   histos[f].GetYaxis().SetTitleOffset(1.7)
   if(histos[f].GetMinimum()<0): histos[f].SetMinimum(-0.1*histos[f].GetMaximum())
   else:                         histos[f].SetMinimum(0)
   histos[f].Draw("hist")
   p2.cd()
   if(ohistos[f].GetMinimum()<0): ohistos[f].SetMinimum(-0.1*ohistos[f].GetMaximum())
   else:                          ohistos[f].SetMinimum(0)
   ohistos[f].GetYaxis().SetTitleOffset(1.7)
   ohistos[f].Draw("hist")
   avg,rms,h1sig,h2sig = flagger.get(ohistos[f],ftrim)
   h2sig.Draw("E3 same")
   h1sig.Draw("E3 same")
   h1sigc = h1sig.Clone()
   h1sigc.SetFillStyle(0)
   h1sigc.Draw("hist same")
   summary += txtsummary(f,ohistos[f],avg,rms)
   p3.cd()
   h2histos[f].GetZaxis().SetTitleOffset(1.5)
   h2hdummy[f].GetZaxis().SetTitleOffset(1.5)
   h2histos[f].SetMinimum(0)
   h2histos[f].Draw("colz")
   h2hdummy[f].Draw("text same")
   p4.cd()
   o2histos[f].GetZaxis().SetTitleOffset(1.5)
   o2hdummy[f].GetZaxis().SetTitleOffset(1.5)
   o2histos[f].SetMinimum(0)
   o2histos[f].Draw("colz")
   o2hdummy[f].Draw("text same")
   if(i==0):              cnv.SaveAs(pdf+"(")
   elif(i==len(files)-1): cnv.SaveAs(pdf+")")
   else:                  cnv.SaveAs(pdf)
   i+=1


### draw pad areas
exampleboards = []
if(argus.s=="IL"): exampleboards = IL.boards
if(argus.s=="RU"): exampleboards = RU.boards
if(argus.s=="CL"): exampleboards = CL.boards
if(argus.s=="CH"): exampleboards = CH.boards
if(argus.s=="CA"): exampleboards = CA.boards
pdf = "pdf/"+argus.s+"_areas.pdf"
n = 1
N = len(exampleboards)
for x in exampleboards:
   btype = x["board"]
   qname = x["fname"]
   cnv = TCanvas("cnv","",1000,500)
   cnv.Divide(2,1)
   p1 = cnv.cd(1)
   p2 = cnv.cd(2)
   p1.cd()
   h2hareas[qname].GetZaxis().SetTitleOffset(1.5)
   h2hareas[qname].SetTitle(btype)
   h2hareas[qname].Draw("colz")
   h2hareas[qname].Draw("text same")
   p2.cd()
   o2hdummy[qname].SetTitle(btype+", Alam's mapping")
   o2hdummy[qname].Draw("text")
   if(n==1):   cnv.SaveAs(pdf+"(")
   elif(n==N): cnv.SaveAs(pdf+")")
   else:       cnv.SaveAs(pdf)
   n+=1

# print("\n----------------------------------------------\n"+summary)