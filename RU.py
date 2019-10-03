import ROOT
from ROOT import TFile, TTree, TH1D, TH2D, TLorentzVector, TVector3, TCanvas

ftrim = 0.1

# files recorded (one per layer)
files = [
          "QL3P_1_L1_31kV_090719", "QL3P_1_L2_31kV_090719", "QL3P_1_L3_31kV_090719", "QL3P_1_L4_31kV_090719",
          "QL3P_2_L1_31kV_090719", "QL3P_2_L2_31kV_090719", "QL3P_2_L3_31kV_090719", "QL3P_2_L4_31kV_090719",
          "QL3P_3_L1_31kV_090719", "QL3P_3_L2_31kV_090719", "QL3P_3_L3_31kV_090719", "QL3P_3_L4_31kV_090719",
          "QL3P_4_L1_31kV_090719", "QL3P_4_L2_31kV_090719", "QL3P_4_L3_31kV_090719", "QL3P_4_L4_31kV_090719",
]


# known_channels = {"QL3P":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...], "QL3C":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...]}
known_channels = {"QL3P":[{3:0}, {3:4}, {3:8}, {3:15}, {3:17}, {3:21}, {3:36}, {3:38}, {2:32}, {2:34}, {2:38}, {2:39}, {2:43}, {2:46}, ],
                  "QL3C":[]}


# fnames should correspond to existing names found in the files array above
boards = [{"board":"QL3P12", "fname":"QL3P_4_L1_31kV_090719"},
          {"board":"QL3P34", "fname":"QL3P_4_L3_31kV_090719"},
          # {"board":"QL3C12", "fname":""},
          # {"board":"QL3C34", "fname":""},
]