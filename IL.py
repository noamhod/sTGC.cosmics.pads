import ROOT
from ROOT import TFile, TTree, TH1D, TH2D, TLorentzVector, TVector3, TCanvas

ftrim = 0.1

# files recorded (one per layer)
files = [
          "QL1P_9_L1_31kV_241019", "QL1P_9_L2_31kV_281019", "QL1P_9_L3_31kV_271019", "QL1P_9_L4_31kV_271019",
          "QL1P_10_L1_31kV_180919", "QL1P_10_L2_31kV_180919", "QL1P_10_L3_31kV_160919", "QL1P_10_L4_31kV_180919",
          "QL1P_7_L1_31kV_100919",  "QL1P_7_L2_31kV_120919",  "QL1P_7_L3_31kV_110919",  "QL1P_7_L4_31kV_120919",
          ### "QL1P_7_L1_29kV_090919",  "QL1P_7_L2_29kV_110919",  "QL1P_7_L3_29kV_110919",  "QL1P_7_L4_29kV_150919",
          "QS3C_6_L1_31kV_050919",  "QS3C_6_L2_31kV_080919",  "QS3C_6_L3_31kV_080919",  "QS3C_6_L4_31kV_080919",
          "QS3C_10_L1_31kV_120819", "QS3C_10_L2_31kV_140819", "QS3C_10_L3_31kV_130819", "QS3C_10_L4_31kV_130819", 
          ### "QS3C_10_L1_29kV_130819", "QS3C_10_L2_29kV_140819", "QS3C_10_L3_29kV_130819", "QS3C_10_L4_29kV_130819",
          "QS3C_11_L1_31kV_010819", "QS3C_11_L2_31kV_070819", "QS3C_11_L3_31kV_060819", "QS3C_11_L4_31kV_060819",
          "QS3C_13_L1_31kV_290719", "QS3C_13_L2_31kV_080819", "QS3C_13_L3_31kV_080819", "QS3C_13_L4_31kV_310719",
          "QS3C_2_L1_31kV_280519",   "QS3C_2_L2_31kV_280519",   "QS3C_2_L3_31kV_280519",   "QS3C_2_L4_31kV_280519",
          "QS3C_3_L1_31kV_20190410", "QS3C_3_L2_31kV_20190410", "QS3C_3_L3_31kV_20190410", "QS3C_3_L4_31kV_20190410",
          "QS3C_3_L1_31kV_17041805", "QS3C_3_L2_31kV_17041805", "QS3C_3_L3_31kV_17041805", "QS3C_3_L4_31kV_17041805",
]


# known_channels = {"QL1P":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...], "QL1C":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...], "QS3C":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...]}
known_channels = {"QL1P":[{2:34}, {3:10}, {3:0}], "QL1C":[], "QS3C":[{2:29},]}


# fnames should correspond to existing names found in the files array above
boards = [{"board":"QL1P12", "fname":"QL1P_7_L1_31kV_100919"},
          {"board":"QL1P34", "fname":"QL1P_7_L3_31kV_110919"},
          # {"board":"QL1C12", "fname":""},
          # {"board":"QL1C34", "fname":""},
          {"board":"QS3C12", "fname":"QS3C_10_L1_31kV_120819"},
          {"board":"QS3C34", "fname":"QS3C_10_L3_31kV_130819"}
]