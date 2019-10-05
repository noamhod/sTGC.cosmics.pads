import ROOT
from ROOT import TFile, TTree, TH1D, TH2D, TLorentzVector, TVector3, TCanvas

ftrim = 0.1

# files recorded (one per layer)
files = [
         "QS1C_1_L1_31kV_06092019",   "QS1C_1_L2_31kV_06092019",   "QS1C_1_L3_31kV_06092019",   "QS1C_1_L4_31kV_06092019",
         "QS1C_1_L1_31kV_06092019r2", "QS1C_1_L2_31kV_06092019r2", "QS1C_1_L3_31kV_06092019r2", "QS1C_1_L4_31kV_06092019r2",
         "QS1C_3_L1_31kV_06092019",   "QS1C_3_L2_31kV_06092019",   "QS1C_3_L3_31kV_06092019",   "QS1C_3_L4_31kV_06092019",
         "QS1C_3_L1_31kV_06092019r2", "QS1C_3_L2_31kV_06092019r2", "QS1C_3_L3_31kV_06092019r2", "QS1C_3_L4_31kV_06092019r2",
         "QS1C_4_L1_31kV_080919",     "QS1C_4_L2_31kV_080919",     "QS1C_4_L3_31kV_080919",     "QS1C_4_L4_31kV_080919",
         "QS1C_4_L1_31kV_080919r2",   "QS1C_4_L2_31kV_080919r2",   "QS1C_4_L3_31kV_080919r2",   "QS1C_4_L4_31kV_080919r2",
         "QS1C_6_L1_31kV_06092019",   "QS1C_6_L2_31kV_06092019",   "QS1C_6_L3_31kV_06092019",   "QS1C_6_L4_31kV_06092019",
         "QS1C_6_L1_31kV_06092019r2", "QS1C_6_L2_31kV_06092019r2", "QS1C_6_L3_31kV_06092019r2", "QS1C_6_L4_31kV_06092019r2",

         "QS1P_7_L1_31kV_080919",     "QS1P_7_L2_31kV_080919",     "QS1P_7_L3_31kV_080919",     "QS1P_7_L4_31kV_080919",
         "QS1P_7_L1_31kV_080919r2",   "QS1P_7_L2_31kV_080919r2",   "QS1P_7_L3_31kV_080919r2",   "QS1P_7_L4_31kV_080919r2",
]


# known_channels = {"QS1P":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...], "QS1C":[{VMMid1:VMMch1}, {VMMid2:VMMch2},...]}
known_channels = {"QS1P":[], "QS1C":[{3:1}, {3:11}]}


# fnames should correspond to existing names found in the files array above
boards = [
          {"board":"QS1P12", "fname":"QS1P_7_L1_31kV_080919"},
          {"board":"QS1P34", "fname":"QS1P_7_L3_31kV_080919"},
          {"board":"QS1C12", "fname":"QS1C_6_L1_31kV_06092019"},
          {"board":"QS1C34", "fname":"QS1C_6_L3_31kV_06092019"},
]