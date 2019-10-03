import ROOT
from ROOT import TFile, TTree, TH1D, TH2D, TLorentzVector, TVector3, TCanvas

ftrim = 0.1


# files recorded (one per layer)
files = [
          "", "", "", "",
]

# known_channels = {"QS2P":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...], "QS2C":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...]}
known_channels = {"QS2P":[], "QS2C":[]}


# fnames should correspond to existing names found in the files array above
boards = [
          # {"board":"QS2P12", "fname":""},
          # {"board":"QS2P34", "fname":""},
          # {"board":"QS2C12", "fname":""},
          # {"board":"QS2C34", "fname":""},
]