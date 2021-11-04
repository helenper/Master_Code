# RunSelector
# Run the selector used for analysis
# Helen Persson 



#==================================================
#
# Import statements
#
#==================================================


import sys    # To give arguments from commandline    
from time import localtime, strftime
import os 
import argparse 
import json

# Import statements - end
#==================================================




#==================================================
#
# Reading command line arguments
#
#==================================================

possible_cuts = ["Preselection",
                 "SR-SF-0J", 
                 "SR-SF-1J", 
                 "SR-SF-0J-ee",
                 "SR-SF-1J-ee",
                 "SR-SF-0J-mumu",
                 "SR-SF-1J-mumu",
                 "SR-DF-0J",
                 "SR-DF-1J",
                 "VR-WW-0J",
                 "VR-WW-1J",
                 #"VR-VZ",
                 #"VR-top-low",
                 #"VR-top-high",
                 #"VR-top-WW",
                 "all",
                 ]

possible_data = ["data15-16", 
                 "data17",
                 "data18",
                ]

possible_backgrounds = [ "mc16a",
                         "mc16cd",
                         "mc16e",
                       ]


possible_signal_samples =["C1C1_SlepSnu_1000p0_100p0",
                          "C1C1_SlepSnu_1000p0_1p0",
                          "C1C1_SlepSnu_1000p0_200p0",
                          "C1C1_SlepSnu_1000p0_300p0",
                          "C1C1_SlepSnu_1000p0_400p0",
                          "C1C1_SlepSnu_1000p0_500p0",
                          "C1C1_SlepSnu_1050p0_150p0",
                          "C1C1_SlepSnu_1050p0_250p0",
                          "C1C1_SlepSnu_1050p0_350p0",
                          "C1C1_SlepSnu_1050p0_450p0",
                          "C1C1_SlepSnu_1050p0_50p0",
                          "C1C1_SlepSnu_1100p0_100p0",
                          "C1C1_SlepSnu_1100p0_1p0",
                          "C1C1_SlepSnu_1100p0_200p0",
                          "C1C1_SlepSnu_1100p0_300p0",
                          "C1C1_SlepSnu_1200p0_100p0",
                          "C1C1_SlepSnu_1200p0_1p0",
                          "C1C1_SlepSnu_1200p0_200p0",
                          "C1C1_SlepSnu_1200p0_300p0",
                          "C1C1_SlepSnu_1300p0_100p0",
                          "C1C1_SlepSnu_1300p0_1p0",
                          "C1C1_SlepSnu_1300p0_200p0",
                          "C1C1_SlepSnu_1300p0_300p0",
                          "C1C1_SlepSnu_150p0_1p0",
                          "C1C1_SlepSnu_150p0_50p0",
                          "C1C1_SlepSnu_200p0_100p0",
                          "C1C1_SlepSnu_200p0_150p0",
                          "C1C1_SlepSnu_200p0_50p0",
                          "C1C1_SlepSnu_250p0_100p0",
                          "C1C1_SlepSnu_250p0_150p0",
                          "C1C1_SlepSnu_300p0_100p0",
                          "C1C1_SlepSnu_300p0_150p0",
                          "C1C1_SlepSnu_300p0_200p0",
                          "C1C1_SlepSnu_300p0_250p0",
                          "C1C1_SlepSnu_350p0_200p0",
                          "C1C1_SlepSnu_350p0_250p0",
                          "C1C1_SlepSnu_400p0_100p0",
                          "C1C1_SlepSnu_400p0_200p0",
                          "C1C1_SlepSnu_400p0_250p0",
                          "C1C1_SlepSnu_400p0_300p0",
                          "C1C1_SlepSnu_450p0_250p0",
                          "C1C1_SlepSnu_450p0_350p0",
                          "C1C1_SlepSnu_500p0_100p0",
                          "C1C1_SlepSnu_500p0_1p0",
                          "C1C1_SlepSnu_500p0_200p0",
                          "C1C1_SlepSnu_500p0_300p0",
                          "C1C1_SlepSnu_500p0_400p0",
                          "C1C1_SlepSnu_550p0_350p0",
                          "C1C1_SlepSnu_550p0_450p0",
                          "C1C1_SlepSnu_600p0_100p0",
                          "C1C1_SlepSnu_600p0_1p0",
                          "C1C1_SlepSnu_600p0_200p0",
                          "C1C1_SlepSnu_600p0_300p0",
                          "C1C1_SlepSnu_600p0_400p0",
                          "C1C1_SlepSnu_600p0_500p0",
                          "C1C1_SlepSnu_650p0_450p0",
                          "C1C1_SlepSnu_700p0_100p0",
                          "C1C1_SlepSnu_700p0_1p0",
                          "C1C1_SlepSnu_700p0_200p0",
                          "C1C1_SlepSnu_700p0_300p0",
                          "C1C1_SlepSnu_700p0_400p0",
                          "C1C1_SlepSnu_700p0_500p0",
                          "C1C1_SlepSnu_750p0_450p0",
                          "C1C1_SlepSnu_800p0_100p0",
                          "C1C1_SlepSnu_800p0_1p0",
                          "C1C1_SlepSnu_800p0_200p0",
                          "C1C1_SlepSnu_800p0_300p0",
                          "C1C1_SlepSnu_800p0_400p0",
                          "C1C1_SlepSnu_800p0_500p0",
                          "C1C1_SlepSnu_850p0_150p0",
                          "C1C1_SlepSnu_850p0_250p0",
                          "C1C1_SlepSnu_850p0_350p0",
                          "C1C1_SlepSnu_850p0_450p0",
                          "C1C1_SlepSnu_850p0_50p0",
                          "C1C1_SlepSnu_900p0_100p0",
                          "C1C1_SlepSnu_900p0_1p0",
                          "C1C1_SlepSnu_900p0_200p0",
                          "C1C1_SlepSnu_900p0_300p0",
                          "C1C1_SlepSnu_900p0_400p0",
                          "C1C1_SlepSnu_900p0_500p0",
                          "C1C1_SlepSnu_950p0_150p0",
                          "C1C1_SlepSnu_950p0_250p0",
                          "C1C1_SlepSnu_950p0_350p0",
                          "C1C1_SlepSnu_950p0_450p0",
                          "C1C1_SlepSnu_950p0_50p0",
                          "C1C1_WW_100p0_1p0",
                          "C1C1_WW_125p0_1p0",
                          "C1C1_WW_125p0_25p0",
                          "C1C1_WW_150p0_1p0",
                          "C1C1_WW_150p0_25p0",
                          "C1C1_WW_150p0_50p0",
                          "C1C1_WW_175p0_1p0",
                          "C1C1_WW_175p0_25p0",
                          "C1C1_WW_175p0_50p0",
                          "C1C1_WW_175p0_75p0",
                          "C1C1_WW_200p0_100p0",
                          "C1C1_WW_200p0_1p0",
                          "C1C1_WW_200p0_25p0",
                          "C1C1_WW_200p0_50p0",
                          "C1C1_WW_200p0_75p0",
                          "C1C1_WW_225p0_100p0",
                          "C1C1_WW_225p0_1p0",
                          "C1C1_WW_225p0_25p0",
                          "C1C1_WW_225p0_50p0",
                          "C1C1_WW_225p0_75p0",
                          "C1C1_WW_250p0_100p0",
                          "C1C1_WW_250p0_150p0",
                          "C1C1_WW_250p0_1p0",
                          "C1C1_WW_250p0_25p0",
                          "C1C1_WW_250p0_50p0",
                          "C1C1_WW_250p0_75p0",
                          "C1C1_WW_275p0_100p0",
                          "C1C1_WW_275p0_1p0",
                          "C1C1_WW_275p0_25p0",
                          "C1C1_WW_275p0_50p0",
                          "C1C1_WW_300p0_100p0",
                          "C1C1_WW_300p0_125p0",
                          "C1C1_WW_300p0_150p0",
                          "C1C1_WW_300p0_1p0",
                          "C1C1_WW_300p0_200p0",
                          "C1C1_WW_300p0_25p0",
                          "C1C1_WW_300p0_50p0",
                          "C1C1_WW_300p0_75p0",
                          "C1C1_WW_325p0_100p0",
                          "C1C1_WW_325p0_1p0",
                          "C1C1_WW_325p0_25p0",
                          "C1C1_WW_325p0_50p0",
                          "C1C1_WW_350p0_100p0",
                          "C1C1_WW_350p0_1p0",
                          "C1C1_WW_350p0_25p0",
                          "C1C1_WW_350p0_50p0",
                          "C1C1_WW_350p0_75p0",
                          "C1C1_WW_375p0_1p0",
                          "C1C1_WW_375p0_25p0",
                          "C1C1_WW_375p0_75p0",
                          "C1C1_WW_400p0_100p0",
                          "C1C1_WW_400p0_150p0",
                          "C1C1_WW_400p0_1p0",
                          "C1C1_WW_400p0_50p0",
                          "C1C1_WW_425p0_1p0",
                          "C1C1_WW_425p0_25p0",
                          "C1C1_WW_450p0_1p0",
                          "C1C1_WW_450p0_50p0",
                          "C1C1_WW_475p0_1p0",
                          "C1C1_WW_500p0_100p0",
                          "C1C1_WW_500p0_1p0",
                          "SlepSlep_direct_100p0_1p0",
                          "SlepSlep_direct_100p0_40p0",
                          "SlepSlep_direct_100p0_50p0",
                          #"SlepSlep_direct_100p0_70p0",
                          #"SlepSlep_direct_125p0_105p0",
                          #"SlepSlep_direct_125p0_115p0",
                          "SlepSlep_direct_125p0_75p0",
                          #"SlepSlep_direct_125p0_95p0",
                          "SlepSlep_direct_150p0_100p0",
                          #"SlepSlep_direct_150p0_110p0",
                          #"SlepSlep_direct_150p0_140p0",
                          "SlepSlep_direct_150p0_90p0",
                          #"SlepSlep_direct_175p0_135p0",
                          #"SlepSlep_direct_175p0_145p0",
                          #"SlepSlep_direct_175p0_155p0",
                          #"SlepSlep_direct_175p0_165p0",
                          #"SlepSlep_direct_200p0_100p0",
                          "SlepSlep_direct_200p0_140p0",
                          "SlepSlep_direct_200p0_150p0",
                          #"SlepSlep_direct_200p0_170p0",
                          "SlepSlep_direct_200p0_1p0",
                          "SlepSlep_direct_250p0_100p0",
                          "SlepSlep_direct_250p0_150p0",
                          "SlepSlep_direct_250p0_1p0",
                          "SlepSlep_direct_250p0_200p0",
                          #"SlepSlep_direct_250p0_240p0",
                          "SlepSlep_direct_300p0_100p0",
                          "SlepSlep_direct_300p0_150p0",
                          "SlepSlep_direct_300p0_1p0",
                          "SlepSlep_direct_300p0_200p0",
                          "SlepSlep_direct_300p0_250p0",
                          "SlepSlep_direct_300p0_280p0",
                          #"SlepSlep_direct_300p0_290p0",
                          "SlepSlep_direct_350p0_100p0",
                          "SlepSlep_direct_350p0_150p0",
                          #"SlepSlep_direct_350p0_1p0",
                          "SlepSlep_direct_350p0_200p0",
                          "SlepSlep_direct_350p0_250p0",
                          "SlepSlep_direct_350p0_300p0",
                          "SlepSlep_direct_350p0_330p0",
                          "SlepSlep_direct_400p0_100p0",
                          "SlepSlep_direct_400p0_1p0",
                          "SlepSlep_direct_400p0_200p0",
                          "SlepSlep_direct_400p0_250p0",
                          "SlepSlep_direct_400p0_300p0",
                          "SlepSlep_direct_400p0_350p0",
                          "SlepSlep_direct_400p0_380p0",
                          "SlepSlep_direct_450p0_100p0",
                          "SlepSlep_direct_450p0_1p0",
                          "SlepSlep_direct_450p0_200p0",
                          "SlepSlep_direct_450p0_250p0",
                          "SlepSlep_direct_450p0_300p0",
                          "SlepSlep_direct_450p0_350p0",
                          "SlepSlep_direct_450p0_400p0",
                          "SlepSlep_direct_500p0_100p0",
                          "SlepSlep_direct_500p0_1p0",
                          "SlepSlep_direct_500p0_200p0",
                          "SlepSlep_direct_500p0_300p0",
                          "SlepSlep_direct_500p0_350p0",
                          "SlepSlep_direct_500p0_400p0",
                          "SlepSlep_direct_500p0_450p0",
                          "SlepSlep_direct_550p0_100p0",
                          "SlepSlep_direct_550p0_1p0",
                          "SlepSlep_direct_550p0_200p0",
                          "SlepSlep_direct_550p0_300p0",
                          "SlepSlep_direct_550p0_350p0",
                          "SlepSlep_direct_550p0_400p0",
                          "SlepSlep_direct_550p0_450p0",
                          "SlepSlep_direct_550p0_500p0",
                          "SlepSlep_direct_600p0_100p0",
                          "SlepSlep_direct_600p0_1p0",
                          "SlepSlep_direct_600p0_200p0",
                          "SlepSlep_direct_600p0_300p0",
                          "SlepSlep_direct_600p0_400p0",
                          "SlepSlep_direct_600p0_450p0",
                          "SlepSlep_direct_600p0_500p0",
                          "SlepSlep_direct_650p0_100p0",
                          "SlepSlep_direct_650p0_1p0",
                          "SlepSlep_direct_650p0_200p0",
                          "SlepSlep_direct_650p0_300p0",
                          "SlepSlep_direct_650p0_400p0",
                          "SlepSlep_direct_650p0_450p0",
                          "SlepSlep_direct_650p0_500p0",
                          "SlepSlep_direct_650p0_550p0",
                          "SlepSlep_direct_700p0_100p0",
                          "SlepSlep_direct_700p0_1p0",
                          "SlepSlep_direct_700p0_200p0",
                          "SlepSlep_direct_700p0_300p0",
                          "SlepSlep_direct_700p0_400p0",
                          "SlepSlep_direct_700p0_500p0",
                          "SlepSlep_direct_700p0_550p0",
                          #"SlepSlep_direct_700p0_600p0",
                          "SlepSlep_direct_800p0_100p0",
                          "SlepSlep_direct_800p0_1p0",
                          "SlepSlep_direct_800p0_200p0",
                          "SlepSlep_direct_800p0_300p0",
                          "SlepSlep_direct_800p0_400p0",
                          "SlepSlep_direct_800p0_500p0",
                          "SlepSlep_direct_800p0_600p0",
                          "SlepSlep_direct_800p0_700p0",
                          "SlepSlep_direct_90p0_1p0",
                          "SlepSlep_direct_90p0_30p0",
                          "all",
                      ]




possible_periods = ["15-16", 
                    "17",
                    "18",
                    "all"
                   ]


possible_isolation_points = ["0",   # BL: medium ID, SG: Tight ID + ISO: FCL + FCHPT
                            "1",   # BL: ingenting, SG: Mediun ID + ISO: FCL + FCHPT
                            "2",   # BL: medium ID, SG: tight ID + ISO: FCT
                            "3",   # BL: ingenting, SG: medium ID + ISO: FCT
                           ]


parser = argparse.ArgumentParser(description="Code to analyse data/signal/background TTrees")

parser.add_argument("-p" , "--period",
                    type=str,
                    nargs="+",
                    choices=possible_periods,
                    help="Set time period to run over. Allowed values are: "+", ".join(possible_periods),
                    metavar="",
                   )

parser.add_argument("-b" , "--background", 
                    action="store_true", 
                    default=False, 
                    help="Bool to determin if to run background.",
                   )

parser.add_argument("-d" , "--data", 
                    action="store_true", 
                    default=False, 
                    help="Bool to determin if to run data.",
                   )


parser.add_argument("-s" , "--signal", 
                    action="store_true", 
                    default=False, 
                    help="Bool to determin if to run signal.",
                   )

parser.add_argument("-f" , "--fakes",
                    action="store_true",
                    default=False, 
                    help="Bool to determin if to run over fakes.",
                   )

parser.add_argument("-s_samps" , "--signal_samples", 
                    type=str,
                    nargs="+",
                    default=["all"], 
                    help="Determin witch signal samples to run over. Allowed values are: "+", ".join(possible_signal_samples),
                   )


parser.add_argument("-c", "--cuts", 
                    type=str, 
                    default="all",
                    choices=possible_cuts,
                    help="Define cut region if NOT to run over all regions. Then only one region can be chosen. Allowed values are: "+", ".join(possible_cuts),
                    metavar=""
                   )

parser.add_argument("-iso" , "--isolation_point", 
                    type=str, 
                    required=True,
                    choices=possible_isolation_points, 
                    help="Chose which isolation points to run on. Allowed values are: "+", ".join(possible_isolation_points),
                    metavar="",
                   )

args = parser.parse_args()

""" For checking what comes in from command line
print " "
print args
print " "
"""

if args.period[0] == "all": 
    possible_periods.remove("all")
    period = possible_periods
else:
    period = args.period

if args.signal_samples[0] == "all":
    possible_signal_samples.remove("all")
    signal = possible_signal_samples
else:
    signal = args.signal_samples

if args.cuts: 
    cut_string = args.cuts

if args.isolation_point:
    iso_point = args.isolation_point

#print period, signal, cut_string




#==================================================
#
# Create folder for saving of results
#
#==================================================

timestamp = strftime("%Y-%m-%d_%H-%M-%S", localtime())


main_path = "/uio/hume/student-u10/helenper/Master/Analyse/Output_files/"
#save_path_PDF = save_path + "PDF/" 
save_path_ROOT = main_path +"ROOT/" + timestamp
save_path_logfile = save_path_ROOT + "/Logfile"


try:  
    #os.makedirs(save_path_PDF)
    os.makedirs(save_path_ROOT)
    os.makedirs(save_path_logfile)
except OSError:  
    print " "
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    print " "
    #print ("Creation of the directory %s failed" % save_path_PDF)
    print ("Creation of the directory %s failed" % save_path_ROOT)
    print ("Creation of the directory %s failed" % save_path_logfile)
    print " "
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    print " "
    sys.exit(1)
else:  
    print " "
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    print " "
    #print ("Successfully created the directory %s" % save_path_PDF)
    print ("Successfully created the directory %s" % save_path_ROOT)
    print ("Successfully created the directory %s" % save_path_logfile)
    print " "
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    print " "





#==================================================
#
# Create logfile
#
#==================================================

log = open(save_path_logfile + "/logfile.txt", "w+")
log.write("{Timestamp: %s} \n" % timestamp)
dict_args = vars(args)
dict_as_string = json.dumps(dict_args)
log.write(dict_as_string)
log.close()

# Create logfile - end
#==================================================




#==================================================
#
# Import ROOT stuff not to interfere with argparse
#
#==================================================

from ROOT import TFile 
from ROOT import gROOT, gPad, gSystem

# Import ROOT stuff not to interfere with argparse - end
#
#==================================================




#==================================================
#
# Loading necessary files
#
#==================================================

gROOT.ProcessLine(".L /uio/hume/student-u10/helenper/Master/Analyse/scripts/MySelector.C+")

# Loading necessary files - end
#==================================================


#==================================================
#
# Running selector
#
#==================================================

for timeperiod in period: 

    print " "
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    print " " 
    print "Running on timeperiod: ", timeperiod
    print " "
    print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    print " "
    
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    # Background
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    if args.background and not args.fakes:
    
        background = [line.strip() for line in open("text_files/background.txt", "r")]  
        #background = ["lowMassDY"]

        for elm in background:
            print " "
            print "Running on background sample: ", elm
            print " "

            # timeperiod 15-16: background is given by mc16a"
            if timeperiod == "15-16":
                path = "/scratch2/Eirik/SUSY_Bkgs/mc16a/240919/"  + elm + "_merged_processed.root"

            # timeperiod 17: background is given by mc16cd"
            if timeperiod == "17":
                path = "/scratch2/Eirik/SUSY_Bkgs/mc16cd/240919/" + elm + "_merged_processed.root"
           

            # timeperiod 18: background is given by mc16e"
            if timeperiod == "18":
                path = "/scratch2/Eirik/SUSY_Bkgs/mc16e/240919/"  + elm + "_merged_processed.root"
        

            myFile = TFile.Open(path, "READ") 
            treename = elm  + "_NoSys" 
            myTree = myFile.Get(treename) 

            options = timestamp + " " + save_path_ROOT + " " + "bkg" + " " + cut_string + " " + timeperiod + " " + iso_point +" " +  elm 

            if not myTree:
                print "Failed to get tree from file"
                sys.exit (1)
                
            myTree.Process("MySelector", options) #Processing the tree n TSelector
            
            myFile.Close() # Close file


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    # Fakes
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

    if args.fakes: # and not args.background and not args.data and not args.signal:
        if timeperiod == "15-16":
            path = "/scratch2/Eirik/SUSY_Fakes/110220/data" + timeperiod + "_merged_processed_MY_0_0.root"
        if timeperiod == "17":
            path = "/scratch2/Eirik/SUSY_Fakes/110220/data" + timeperiod + "_merged_processed_MY_0_0.root"
       
        if timeperiod == "18":
            path = "/scratch2/Eirik/SUSY_Fakes/110220/data" + timeperiod + "_merged_processed_MY_0_0.root"

        myFile = TFile.Open(path, "READ") 
        treename = "MM_CENTRAL"
        myTree = myFile.Get(treename) 

        option = timestamp + " " + save_path_ROOT + " " + "fakes" + " " + cut_string + " " + timeperiod + " " +  iso_point
    

        if not myTree:
            print "Failed to get tree from file"
            sys.exit (1)

        myTree.Process("MySelector", option) #Processing the tree in TSelector
        
        myFile.Close() # Close file




    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    # Data
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

    if args.data and not args.fakes:
        print " "
        print "Running on data "
        print " "

        if timeperiod == "15-16":
            path = "/scratch2/Eirik/SUSY_Data/240919/data" + timeperiod + "_merged_processed.root"
        if timeperiod == "17":
            path = "/scratch2/Eirik/SUSY_Data/240919/data" + timeperiod + "_merged_processed.root"
        if timeperiod == "18":
            path = "/scratch2/Eirik/SUSY_Data/240919/data" + timeperiod + "_merged_processed.root"

        myFile = TFile.Open(path, "READ") 
        treename = "data" + timeperiod
        myTree = myFile.Get(treename) 

        option = timestamp + " " + save_path_ROOT + " " + "data" + " " + cut_string + " " + timeperiod + " " +  iso_point

        if not myTree:
            print "Failed to get tree from file"
            sys.exit (1)

        myTree.Process("MySelector", option) #Processing the tree in TSelector
        
        myFile.Close() # Close file


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
    # Signal 
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

    if args.signal and not args.fakes:
        for elm in signal:
            print " "
            print "Running on signal sample: ", elm
            print " "


            if timeperiod == "15-16":
                path = "/scratch2/Eirik/SUSY_Signal/mc16a/011119/"  + elm + "_2L8_merged_processed.root"
            if timeperiod == "17":
                path = "/scratch2/Eirik/SUSY_Signal/mc16cd/011119/" + elm + "_2L8_merged_processed.root"
            if timeperiod == "18":
                path = "/scratch2/Eirik/SUSY_Signal/mc16e/011119/"  + elm + "_2L8_merged_processed.root"

        
            myFile = TFile.Open(path, "READ") 
            treename = elm + "_2L8_NoSys"
            myTree = myFile.Get(treename) 
        
            option = timestamp + " " + save_path_ROOT + " " + "signal" + " " + cut_string + " " + timeperiod + " " + iso_point + " " +  elm
        
            if not myTree:
                print "Failed to get tree from file"
                sys.exit (1)
            
            myTree.Process("MySelector", option) #Processing the tree in TSelector
            
            myFile.Close() # Close file



#==================================================
#
# Mark end of program in terminal
#
#==================================================

print("-------------------------------------------")
print(" ") 
print("Done!")
print(" ") 
print("-------------------------------------------")

# Main program - end
#==================================================






