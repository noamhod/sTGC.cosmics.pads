# sTGC cmd mapping query
1. setup python3
2. to convert from one mapping to the other for one channel, run `python cmdmapping.py -h`
3. this is using mapping.txt [and columns.txt for reference] from Benoit's git:
   https://gitlab.cern.ch/McGill-sTGC/NSW_sTGC_Channel_Mapping
   make sure to update this file whenever a change is done upstram

# sTGC.cosmics.pads analysis
1. setup python3 and ROOT
2. get the data from /eos/user/h/hod/sTGC/root/ (or add new files) into root/
3. the code expects one file per layer in this format:
   QS3C_6_L4_31kV_080919_final_histograms_pads.root
4. if new files have been added, this should be reflected in the site-specific .py file
   - same thing for dead/masked/... channels
   - same thing for new types of boards that have not been used
5. run with `python analysis.py -s IL` [site option can be: IL, RU, CL, CA, CH]
6. look at the output in pdf/ and txt/
