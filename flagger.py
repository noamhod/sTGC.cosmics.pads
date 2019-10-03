import ROOT
from ROOT import TH1D
import numpy as np

def getlist(h,ignore):
   lst = []
   for b in range(1,h.GetNbinsX()+1):
      x = h.GetBinCenter(b)
      y = h.GetBinContent(b)
      if(x in ignore): continue
      if(y<=0):        continue
      lst.append(y)
   return lst

def trimspikes(lst,ftrim):
   lst.sort()
   n = len(lst)
   nmax = int(n*(1-ftrim))
   trimmed = lst[1:nmax]
   return trimmed   

def meanrms(lst):
   avg = np.mean(lst)
   rms = np.std(lst)
   return avg,rms

def get(h,ftrim,ignore=[]):
   lst = getlist(h,ignore)
   srt = trimspikes(lst,ftrim)
   avg,rms = meanrms(srt)
   h1sig = TH1D(h.GetName()+"_1sig","", h.GetNbinsX(),h.GetXaxis().GetXmin(),h.GetXaxis().GetXmax())
   h2sig = TH1D(h.GetName()+"_2sig","", h.GetNbinsX(),h.GetXaxis().GetXmin(),h.GetXaxis().GetXmax())
   h1sig.SetLineColor(ROOT.kBlack)
   h1sig.SetFillColorAlpha(ROOT.kGreen,0.50)
   h2sig.SetFillColorAlpha(ROOT.kYellow,0.60)
   for b in range(1,h.GetNbinsX()+1):
      h1sig.SetBinContent(b,avg)
      h2sig.SetBinContent(b,avg)
      h1sig.SetBinError(b,rms)
      h2sig.SetBinError(b,2*rms)
   return avg,rms,h1sig,h2sig