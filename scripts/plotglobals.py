# plotglobals.py
# Holds the global variables needed for ploting, 
# used by HistogramMaker.py and plotfunctions.py
# Helen Persson 


#==================================================
#
# Imports
#
#==================================================

from configurate_samples import configurate_samples


# Imports - end
#==================================================




#==================================================
#
# Functions
#
#==================================================

def init():
    """
    Function called for setting up gobal variables.
    """
    
    #******************************
    # Defining global variables
    #******************************
    
    global d_hist                     # Nested dict holding each background + data histogram for each variable
    global d_MC                       # Dict of elements THStack() to hold all background histograms stacked for each variable
    global d_data                     # Dict for holding data histograms for each variable
    global d_signal                   # Dict for holding signal histograms for each variable
    global d_basesignal               # Dict for holding the 2D plot of nbase VS nsignal leptons 
    
    global d_sample                   # Dict for holding configuration info about samples from configurate_samples.py
    global d_title                    # Dict for holding titles used in plots
    global d_xaxis                    # Dict for holding labels used for xaxis in plots
    global l_leg                      # List used to check if lable as been added before

    global l_sample_bkg               # List of all background samples
    global l_sample_data              # List of all data samples
    global l_sample_signal            # List of all signal samples 
    global l_sample                   # List combining background + data + signal samples

    global d_zExp                     # Nested dict to hold significance values for different signals and different regions
    global d_significance             # Nested dict to hold significance values sorted by type of signal


    #******************************
    # Initilizing global variables 
    # with values
    #******************************
    
    d_hist = {}                      
    d_MC = {}                         
    d_data = {}                       
    d_signal ={}   
    d_basesignal = {}

    d_zExp = {}
    d_significance = {}

    d_sample = configurate_samples()  

    d_title = {"lepPt" : "Lepton Pt",                
               "mll": "Diboson invariant mass", 
               "met_Et" : "Missing transverse energy",
               "mT2" : "mT2",
              }
    
    d_xaxis = {"lepPt"      : "Lep Pt", 
               "mll"        : "m_{ll}", 
               "met_Et"     : "E_{T}^{miss}",
               "mT2"        : "m_{T2}",
               "nJetB"      : "nJetB", 
               "nJetLight"  : "nJetLight", 
               "nLepSignal" : "nLepSignal",
               "nLepBase"   : "nLepBase",
              }
    
   
    l_leg = []          
    
    l_sample_bkg = ['higgs',    
                    'Vgamma',     
                    'triboson',     
                    'diboson',     
                    'Wjets',     
                    'Zjets',     
                    'lowMassDY',     
                    'topOther',     
                    'singleTop',     
                    'ttbar'
                   ]
    
    l_sample_data = ["data15-16", 
                     "data17",
                     "data18",
                     #"data15-17",
                     #"data15-18", 
                    ]
    
    l_sample_signal = ["C1C1_SlepSnu_200p0_50p0",
                       "C1C1_SlepSnu_800p0_400p0", 
                       "C1C1_SlepSnu_950p0_50p0", 
                       "C1C1_WW_200p0_75p0", 
                       "C1C1_WW_350p0_100p0",
                       "C1C1_WW_425p0_1p0",
                       "SlepSlep_direct_200p0_150p0",
                       "SlepSlep_direct_550p0_300p0", 
                       "SlepSlep_direct_650p0_1p0", 
                       "all",
                       ]


    l_sample = l_sample_bkg + l_sample_data + l_sample_signal

# Functions - end
#==================================================




#==================================================
#
# If run as a main program, not called upon by
# HistogramMaker.py
#
#==================================================


if __name__ == "__main__":
    
    print " "
    print "Error in use:"
    print "This program is used to initilaze global variables used by HistogramMaker.py and plotfunctions.py."
    print "Use HistogramMaker.py to initialize these variables."
    print " "

# If run as a main program - end
#==================================================
