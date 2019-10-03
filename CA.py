import ROOT
from ROOT import TFile, TTree, TH1D, TH2D, TLorentzVector, TVector3, TCanvas

ftrim = 0.1

# files recorded (one per layer)
files = [
          "", "", "", "",
]


# known_channels = {"QL2P":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...], "QL2C":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...], "QS3P":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...] }
known_channels = {"QL2P":[], "QL2C":[], "QS3P":[]}


# fnames should correspond to existing names found in the files array above
boards = [
          # {"board":"QS3P12", "fname":""},
          # {"board":"QS3P34", "fname":""},
          # {"board":"QL2P12", "fname":""},
          # {"board":"QL2P34", "fname":""},
          # {"board":"QL2C12", "fname":""},
          # {"board":"QL2C34", "fname":""},
]