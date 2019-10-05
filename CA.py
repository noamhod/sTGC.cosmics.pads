import ROOT
from ROOT import TFile, TTree, TH1D, TH2D, TLorentzVector, TVector3, TCanvas

ftrim = 0.1

# files recorded (one per layer)
files = [
          "QS3P_6_L1_31kV_12182018", "QS3P_6_L2_31kV_12182018", "QS3P_6_L3_31kV_12182018", "QS3P_6_L4_31kV_12182018", 
          "QS3P_7_L1_31kV_03062019", "QS3P_7_L2_31kV_03062019", "QS3P_7_L3_31kV_03062019", "QS3P_7_L4_31kV_03062019",
          "QS3P_8_L1_31kV_03112019", "QS3P_8_L2_31kV_03112019", "QS3P_8_L3_31kV_03112019", "QS3P_8_L4_31kV_03112019", 
          "QS3P_9_L1_31kV_06052019", "QS3P_9_L2_31kV_06052019", "QS3P_9_L3_31kV_06052019", "QS3P_9_L4_31kV_06052019", 
          "QS3P_10_L1_31kV_05132019", "QS3P_10_L2_31kV_05132019", "QS3P_10_L3_31kV_05132019", "QS3P_10_L4_31kV_05132019",
          "QS3P_11_L1_31kV_05232019", "QS3P_11_L2_31kV_05232019", "QS3P_11_L3_31kV_05232019", "QS3P_11_L4_31kV_05232019",
          "QS3P_12_L1_31kV_05312019", "QS3P_12_L2_31kV_05312019", "QS3P_12_L3_31kV_05312019", "QS3P_12_L4_31kV_05312019",
]


# known_channels = {"QL2P":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...], "QL2C":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...], "QS3P":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...] }
known_channels = {"QL2P":[], "QL2C":[], "QS3P":[]}


# fnames should correspond to existing names found in the files array above
boards = [
          {"board":"QS3P12", "fname":"QS3P_6_L1_31kV_12182018"},
          {"board":"QS3P34", "fname":"QS3P_6_L3_31kV_12182018"},
          # {"board":"QL2P12", "fname":""},
          # {"board":"QL2P34", "fname":""},
          # {"board":"QL2C12", "fname":""},
          # {"board":"QL2C34", "fname":""},
]