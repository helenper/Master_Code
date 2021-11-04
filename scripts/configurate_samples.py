# Configurate_samples
# Cotains a function that creates a dictionary that holds sample configurations
# Helen Persson 


from ROOT import TColor 
from ROOT import kBlack,kWhite,kGray,kRed,kPink,kMagenta,kViolet,kBlue,kAzure,kCyan,kTeal,kGreen,kSpring,kYellow,kOrange, kFullCircle


def configurate_samples():

    # Blues   
    #myLighterBlue=TColor.GetColor('#deebf7')   
    myLighterBlue=kAzure-2   
    myLightBlue  =TColor.GetColor('#9ecae1')   
    myMediumBlue =TColor.GetColor('#0868ac')   
    myDarkBlue   =TColor.GetColor('#08306b')   

    # Greens  
    myLightGreen   =TColor.GetColor('#c7e9c0')   
    myMediumGreen  =TColor.GetColor('#41ab5d')   
    myDarkGreen    =TColor.GetColor('#006d2c')   

    # Oranges  
    myLighterOrange=TColor.GetColor('#ffeda0')   
    myLightOrange  =TColor.GetColor('#fec49f')   
    myMediumOrange =TColor.GetColor('#fe9929')   

    # Greys   
    myLightestGrey=TColor.GetColor('#f0f0f0')   
    myLighterGrey=TColor.GetColor('#e3e3e3')   
    myLightGrey  =TColor.GetColor('#969696')   

    # Pinks  
    myLightPink = TColor.GetColor('#fde0dd')   
    myMediumPink = TColor.GetColor('#fcc5c0')   
    myDarkPink = TColor.GetColor('#dd3497')   

    # Purples  
    myLightPurple   = TColor.GetColor('#dadaeb')   
    myMediumPurple  = TColor.GetColor('#9e9ac8')   
    myDarkPurple    = TColor.GetColor('#6a51a3')


    d_sample = {

        # Background
        "diboson"   : {"type":"bkg",    "leg":"Diboson",     "fill_color":myMediumOrange,  "line_color":myMediumOrange  }, 
        "triboson"  : {"type":"bkg",    "leg":"Triboson",    "fill_color":myLightOrange,   "line_color":myLightOrange   },
        "higgs"     : {"type":"bkg",    "leg":"Higgs",       "fill_color":myDarkPink,      "line_color":myDarkPink      },
        "lowMassDY" : {"type":"bkg",    "leg":"Low mass DY", "fill_color":myLightGrey,     "line_color":myLightGrey     }, 
        "singleTop" : {"type":"bkg",    "leg":"Single top",  "fill_color":myMediumBlue,    "line_color":myMediumBlue    }, 
        "topOther"  : {"type":"bkg",    "leg":"Top other",   "fill_color":myLightBlue,     "line_color":myLightBlue     },
        "ttbar"     : {"type":"bkg",    "leg":"t#bar{t}",    "fill_color":myDarkBlue,      "line_color":myDarkBlue      },
        "Vgamma"    : {"type":"bkg",    "leg":"V+gamma",     "fill_color":myLighterOrange, "line_color":myLighterOrange },
        "Wjets"     : {"type":"bkg",    "leg":"W+jets",      "fill_color":myLightGreen,    "line_color":myLightGreen    },
        "Zjets"     : {"type":"bkg",    "leg":"Z+jets",      "fill_color":myMediumGreen,   "line_color":myMediumGreen   },

        
        # Fakes
        "fakes"     : {"type":"fakes",    "leg":"Fakes",     "fill_color":kAzure+8,   "line_color":kAzure+8           },
 
        # Data
        "data"      : {"type":"data",   "leg":"Data",        "fill_color":kBlack, "line_color":kBlack, 'marker_style':kFullCircle },
        "data15-16" : {"type":"data",   "leg":"Data15-16",   "fill_color":kBlack, "line_color":kBlack, 'marker_style':kFullCircle },
        "data15-17" : {"type":"data",   "leg":"Data15-17",   "fill_color":kBlack, "line_color":kBlack, 'marker_style':kFullCircle },
        "data15-18" : {"type":"data",   "leg":"Data15-18",   "fill_color":kBlack, "line_color":kBlack, 'marker_style':kFullCircle },
        "data17"    : {"type":"data",   "leg":"Data17",      "fill_color":kBlack, "line_color":kBlack, 'marker_style':kFullCircle },
        "data18"    : {"type":"data",   "leg":"Data18",      "fill_color":kBlack, "line_color":kBlack, 'marker_style':kFullCircle },
    
        #Signal

        # C1C1_Slep_snu
        "C1C1_SlepSnu_1000p0_100p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1000, 100]",                 "fill_color":kRed,        "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_1000p0_1p0"      : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1000, 1]",                   "fill_color":kCyan-1,     "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_1000p0_200p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1000, 200]",                 "fill_color":kGreen,      "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_1000p0_300p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1000, 300]",                 "fill_color":kMagenta+2,        "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_SlepSnu_1000p0_400p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1000, 400]",                 "fill_color":kRed,        "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_1000p0_500p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1000, 500]",                 "fill_color":kMagenta-3,        "line_color":kMagenta-3,       "line_style":4   },

        "C1C1_SlepSnu_1050p0_150p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1050, 150]",                  "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_1050p0_250p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1050, 250]",                  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_1050p0_350p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1050, 350]",                  "fill_color":kGreen,     "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_1050p0_450p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1050, 450]",                  "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_SlepSnu_1050p0_50p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1050, 50]",                   "fill_color":kRed,       "line_color":kRed,       "line_style":4   },

        "C1C1_SlepSnu_1100p0_100p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1100, 100]",                 "fill_color":kRed,        "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_1100p0_1p0"      : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1100, 1]",                   "fill_color":kCyan-1,     "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_1100p0_200p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1100, 200]",                 "fill_color":kGreen,      "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_1100p0_300p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1100, 300]",                  "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },

        "C1C1_SlepSnu_1200p0_100p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1200, 100]",                 "fill_color":kRed,        "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_1200p0_1p0"      : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1200, 1]",                   "fill_color":kCyan-1,     "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_1200p0_200p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1200, 200]",                 "fill_color":kGreen,      "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_1200p0_300p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1200, 300]",                 "fill_color":kMagenta+2,        "line_color":kMagenta+2,       "line_style":4   },

        "C1C1_SlepSnu_1300p0_100p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1300, 100]",                 "fill_color":kRed,        "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_1300p0_1p0"      : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1300, 1]",                   "fill_color":kCyan-1,     "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_1300p0_200p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1300, 200]",                 "fill_color":kGreen,      "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_1300p0_300p0"    : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [1300, 300]",                 "fill_color":kMagenta+2,        "line_color":kMagenta+2,       "line_style":4   },

        "C1C1_SlepSnu_150p0_1p0"       : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [150, 1]",                    "fill_color":kRed,        "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_150p0_50p0"      : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [150, 50]",                   "fill_color":kCyan-1,     "line_color":kCyan-1,    "line_style":6   },

        "C1C1_SlepSnu_200p0_100p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [200, 100]",                 "fill_color":kGreen,       "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_200p0_150p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [200, 150]",                 "fill_color":kCyan-1,      "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_200p0_50p0"      : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [200, 50]",                  "fill_color":kRed,         "line_color":kRed,       "line_style":4   },

        "C1C1_SlepSnu_250p0_100p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [250, 100]",                 "fill_color":kRed,         "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_250p0_150p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [250, 150]",                 "fill_color":kCyan-1,      "line_color":kCyan-1,    "line_style":6   },

        "C1C1_SlepSnu_300p0_100p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [300, 100]",                 "fill_color":kRed,         "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_300p0_150p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [300, 150]",                 "fill_color":kCyan-1,      "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_300p0_200p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [300, 200]",                 "fill_color":kGreen,       "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_300p0_250p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [300, 250]",                 "fill_color":kMagenta+2,         "line_color":kMagenta+2,       "line_style":4   },

        "C1C1_SlepSnu_350p0_200p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [350, 200]",                 "fill_color":kRed,         "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_350p0_250p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [350, 250]",                "fill_color":kCyan-1,      "line_color":kCyan-1,    "line_style":6   },

        "C1C1_SlepSnu_400p0_100p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [400, 100]",                 "fill_color":kRed,         "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_400p0_200p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [400, 200]",                 "fill_color":kCyan-1,      "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_400p0_250p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [400, 250]",                 "fill_color":kGreen,       "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_400p0_300p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [400, 300]",                 "fill_color":kMagenta+2,         "line_color":kMagenta+2,       "line_style":4   },

        "C1C1_SlepSnu_450p0_250p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [450, 250]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_450p0_350p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [450, 350]",                "fill_color":kCyan-1,       "line_color":kCyan-1,    "line_style":6   },

        "C1C1_SlepSnu_500p0_100p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [500, 100]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_500p0_1p0"       : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [500, 1]",                  "fill_color":kCyan-1,       "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_500p0_200p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [500, 200]",                "fill_color":kGreen,        "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_500p0_300p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [500, 300]",                "fill_color":kMagenta+2,          "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_SlepSnu_500p0_400p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [500, 400]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },

        "C1C1_SlepSnu_550p0_350p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [550, 350]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_550p0_450p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [550, 450]",                "fill_color":kCyan-1,       "line_color":kCyan-1,    "line_style":6   },

        "C1C1_SlepSnu_600p0_100p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [600, 100]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_600p0_1p0"       : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [600, 1]",                  "fill_color":kCyan-1,       "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_600p0_200p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [600, 200]",                "fill_color":kGreen,        "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_600p0_300p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [600, 300]",                "fill_color":kMagenta+2,          "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_SlepSnu_600p0_400p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [600, 400]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_600p0_500p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [600, 500]",                "fill_color":kMagenta-3,          "line_color":kMagenta-3,       "line_style":4   }, 

        "C1C1_SlepSnu_650p0_450p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [650, 450]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },

        "C1C1_SlepSnu_700p0_100p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [700, 100]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_700p0_1p0"       : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [700, 1]",                  "fill_color":kCyan-1,       "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_700p0_200p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [700, 200]",                "fill_color":kGreen,        "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_700p0_300p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [700, 300]",                "fill_color":kMagenta+2,          "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_SlepSnu_700p0_400p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [700, 400]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_700p0_500p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [700, 500]",                "fill_color":kMagenta-3,          "line_color":kMagenta-3,       "line_style":4   },

        "C1C1_SlepSnu_750p0_450p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [750, 450]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },

        "C1C1_SlepSnu_800p0_100p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [800, 100]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_800p0_1p0"       : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [800, 1]",                  "fill_color":kCyan-1,       "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_800p0_200p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [800, 200]",                "fill_color":kGreen,        "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_800p0_300p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [800, 300]",                "fill_color":kMagenta-3,          "line_color":kMagenta-3,       "line_style":4   },
        "C1C1_SlepSnu_800p0_400p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [800, 400]",                "fill_color":kMagenta+2,    "line_color":kMagenta+2, "line_style":4   },
        "C1C1_SlepSnu_800p0_500p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [800, 500]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },

        "C1C1_SlepSnu_850p0_150p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [850, 150]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_850p0_250p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [850, 250]",                "fill_color":kCyan-1,       "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_850p0_350p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [850, 350]",                "fill_color":kGreen,        "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_850p0_450p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [850, 450]",                "fill_color":kMagenta+2,          "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_SlepSnu_850p0_50p0"      : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [850, 50]",                 "fill_color":kRed,          "line_color":kRed,       "line_style":4   },

        "C1C1_SlepSnu_900p0_100p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [900, 100]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_900p0_1p0"       : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [900, 1]",                  "fill_color":kCyan-1,       "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_900p0_200p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [900, 200]",                "fill_color":kGreen,        "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_900p0_300p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [900, 300]",                "fill_color":kMagenta+2,          "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_SlepSnu_900p0_400p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [900, 400]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_900p0_500p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [900, 500]",                "fill_color":kMagenta-3,          "line_color":kMagenta-3,       "line_style":4   },

        "C1C1_SlepSnu_950p0_150p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [950, 150]",                "fill_color":kRed,          "line_color":kRed,       "line_style":4   },
        "C1C1_SlepSnu_950p0_250p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [950, 250]",                "fill_color":kCyan-1,       "line_color":kCyan-1,    "line_style":6   },
        "C1C1_SlepSnu_950p0_350p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [950, 350]",                "fill_color":kGreen,        "line_color":kGreen,     "line_style":7   },
        "C1C1_SlepSnu_950p0_450p0"     : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [950, 450]",                "fill_color":kMagenta-3,          "line_color":kMagenta-3,       "line_style":4   },
        "C1C1_SlepSnu_950p0_50p0"      : {"type":"signal", "leg":"#tilde{#font[12]{CC->SlepSnu}} [950, 50]",                "fill_color":kMagenta+2,    "line_color":kMagenta+2, "line_style":4   },

         
        # C1C1_WW
        "C1C1_WW_100p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [100, 1]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
       
        "C1C1_WW_125p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [125, 1]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_125p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [125, 25]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        
        "C1C1_WW_150p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [150, 1]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_150p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [150, 25]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_150p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [150, 50]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        
        "C1C1_WW_175p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [175, 1]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_175p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [175, 25]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_175p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [175, 50]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        "C1C1_WW_175p0_75p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [175, 75]",                      "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },
        
        "C1C1_WW_200p0_100p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [200, 100]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_200p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [200, 1]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_200p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [200, 25]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        "C1C1_WW_200p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [200, 50]",                      "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_WW_200p0_75p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [200, 75]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        
        "C1C1_WW_225p0_100p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [225, 100]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_225p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [225, 1]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_225p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [225, 25]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        "C1C1_WW_225p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [225, 50]",                      "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_WW_225p0_75p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [225, 75]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        
        "C1C1_WW_250p0_100p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [250, 100]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_250p0_150p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [250, 150]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_250p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [250, 1]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        "C1C1_WW_250p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [250, 25]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_250p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [250, 50]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_250p0_75p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [250, 75]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        
        "C1C1_WW_275p0_100p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [275, 100]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_275p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [275, 1]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_275p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [275, 25",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        "C1C1_WW_275p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [275, 50]",                      "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },
        
        "C1C1_WW_300p0_100p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [300, 100]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_300p0_125p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [300, 125]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_300p0_150p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [300, 150]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        "C1C1_WW_300p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [300, 1]",                      "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_WW_300p0_200p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [300, 200]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_300p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [300, 250]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_300p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [300, 50]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_300p0_75p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [300, 75]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        
        "C1C1_WW_325p0_100p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [325, 100]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_325p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [325, 1]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_325p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [325, 25]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        "C1C1_WW_325p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [325, 50]",                      "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },
        
        "C1C1_WW_350p0_100p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [350, 100]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_350p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [350, 1]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_350p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [350, 25]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        "C1C1_WW_350p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [350, 50]",                      "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },
        "C1C1_WW_350p0_75p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [350, 75]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        
        "C1C1_WW_375p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [375, 1]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_375p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [375, 25]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_375p0_75p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [375, 75]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        
        "C1C1_WW_400p0_100p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [400, 100]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_400p0_150p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [400, 150]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        "C1C1_WW_400p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [400, 1]",                      "fill_color":kGreen,       "line_color":kGreen,       "line_style":4   },
        "C1C1_WW_400p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [400, 50]",                      "fill_color":kMagenta+2,       "line_color":kMagenta+2,       "line_style":4   },
        
        "C1C1_WW_425p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [425, 1]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_425p0_25p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [425, 25]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        
        "C1C1_WW_450p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [450, 1]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_450p0_50p0"           : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [450, 50]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        
        "C1C1_WW_475p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [475, 1]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        
        "C1C1_WW_500p0_100p0"          : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [500, 100]",                      "fill_color":kRed,       "line_color":kRed,       "line_style":4   },
        "C1C1_WW_500p0_1p0"            : {"type":"signal", "leg":"#tilde{#font[12]{CC->WW}} [500, 1]",                      "fill_color":kCyan-1,       "line_color":kCyan-1,       "line_style":4   },
        
        #SlepSlep_direct

        "SlepSlep_direct_90p0_1p0"     : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [90, 1]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_90p0_30p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [90, 30]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },

        "SlepSlep_direct_100p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [100, 1]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_100p0_40p0"   : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [100, 40]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_100p0_50p0"   : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [100, 50]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        #"SlepSlep_direct_100p0_70p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [100, 70]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        
        #"SlepSlep_direct_125p0_105p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [125, 105]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        #"SlepSlep_direct_125p0_115p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [125, 115]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_125p0_75p0"   : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [125, 75]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        #"SlepSlep_direct_125p0_95p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [125, 95]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        
        "SlepSlep_direct_150p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [150, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        #"SlepSlep_direct_150p0_110p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [150, 110]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        #"SlepSlep_direct_150p0_140p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [150, 140]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_150p0_90p0"   : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [150, 90]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        
        #"SlepSlep_direct_175p0_135p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [175, 135]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        #"SlepSlep_direct_175p0_145p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [175, 145]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        #"SlepSlep_direct_175p0_155p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [175, 155]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        #"SlepSlep_direct_175p0_165p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [175, 165]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        
        #"SlepSlep_direct_200p0_100p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [200, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_200p0_140p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [200, 140]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_200p0_150p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [200, 150]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        #"SlepSlep_direct_200p0_170p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [200, 170]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_200p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [200, 1]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        
        "SlepSlep_direct_250p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [250, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_250p0_150p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [250, 150]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_250p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [250, 1]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_250p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [250, 200]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        #"SlepSlep_direct_250p0_240p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [250, 240]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        
        "SlepSlep_direct_300p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [300, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_300p0_150p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [300, 150]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_300p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [300, 1]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_300p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [300, 200]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_300p0_250p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [300, 250]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_300p0_280p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [300, 280]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        #"SlepSlep_direct_300p0_290p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [300, 290]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        
        "SlepSlep_direct_350p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [350, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_350p0_150p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [350, 150]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        #"SlepSlep_direct_350p0_1p0"   : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [350, 1]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_350p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [350, 200]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_350p0_250p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [350, 250]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_350p0_300p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [350, 300]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        "SlepSlep_direct_350p0_330p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [350, 330]",  "fill_color":kTeal+1,    "line_color":kTeal+1,    "line_style":4   },
        
        "SlepSlep_direct_400p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [400, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_400p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [400, 1]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_400p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [400, 200]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_400p0_250p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [400, 250]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_400p0_300p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [400, 300]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_400p0_350p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [400, 350]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        "SlepSlep_direct_400p0_380p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [400, 380]",  "fill_color":kTeal+1,    "line_color":kTeal+1,    "line_style":4   },
        
        "SlepSlep_direct_450p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [450, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_450p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [450, 1]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_450p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [450, 200]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_450p0_250p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [450, 250]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_450p0_300p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [450, 300]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_450p0_350p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [450, 350]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        "SlepSlep_direct_450p0_400p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [450, 400]",  "fill_color":kTeal+1,    "line_color":kTeal+1,    "line_style":4   },
        
        "SlepSlep_direct_500p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [500, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_500p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [500, 1]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_500p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [500, 200]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_500p0_300p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [500, 300]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_500p0_350p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [500, 350]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_500p0_400p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [500, 400]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        "SlepSlep_direct_500p0_450p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [500, 450]",  "fill_color":kTeal+1,    "line_color":kTeal+1,    "line_style":4   },
        
        "SlepSlep_direct_550p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [550, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_550p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [550, 1]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_550p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [550, 200]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_550p0_300p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [550, 300]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_550p0_350p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [550, 350]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_550p0_400p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [550, 400]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        "SlepSlep_direct_550p0_450p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [550, 450]",  "fill_color":kTeal+1,    "line_color":kTeal+1,    "line_style":4   },
        "SlepSlep_direct_550p0_500p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [550, 500]",  "fill_color":kTeal-9,    "line_color":kTeal-9,    "line_style":4   },
        
        "SlepSlep_direct_600p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [600, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_600p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [600, 1]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_600p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [600, 200]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_600p0_300p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [600, 300]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_600p0_400p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [600, 400]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_600p0_450p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [600, 450]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        "SlepSlep_direct_600p0_500p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [600, 500]",  "fill_color":kTeal+1,    "line_color":kTeal+1,    "line_style":4   },
        
        "SlepSlep_direct_650p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [650, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_650p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [650, 1]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_650p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [650, 200]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_650p0_300p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [650, 300]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_650p0_400p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [650, 400]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_650p0_450p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [650, 450]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        "SlepSlep_direct_650p0_500p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [650, 500]",  "fill_color":kTeal+1,    "line_color":kTeal+1,    "line_style":4   },
        "SlepSlep_direct_650p0_550p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [650, 550]",  "fill_color":kTeal-9,    "line_color":kTeal-9,    "line_style":4   },
        
        "SlepSlep_direct_700p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [700, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_700p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [700, 1]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_700p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [700, 200]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_700p0_300p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [700, 300]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_700p0_400p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [700, 400]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_700p0_500p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [700, 500]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        "SlepSlep_direct_700p0_550p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [700, 550]",  "fill_color":kTeal+1,    "line_color":kTeal+1,    "line_style":4   },
        #"SlepSlep_direct_700p0_600p0" : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [700, 600]",  "fill_color":kTeal-9,    "line_color":kTeal-9,    "line_style":4   },
        
        "SlepSlep_direct_800p0_100p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [800, 100]",  "fill_color":kRed,    "line_color":kRed,    "line_style":4   },
        "SlepSlep_direct_800p0_1p0"    : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [800, 1]",  "fill_color":kCyan-1,    "line_color":kCyan-1,    "line_style":4   },
        "SlepSlep_direct_800p0_200p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [800, 200]",  "fill_color":kGreen,    "line_color":kGreen,    "line_style":4   },
        "SlepSlep_direct_800p0_300p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [800, 300]",  "fill_color":kMagenta+2,    "line_color":kMagenta+2,    "line_style":4   },
        "SlepSlep_direct_800p0_400p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [800, 400]",  "fill_color":kMagenta-3,    "line_color":kMagenta-3,    "line_style":4   },
        "SlepSlep_direct_800p0_500p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [800, 500]",  "fill_color":kBlue,    "line_color":kBlue,    "line_style":4   },
        "SlepSlep_direct_800p0_600p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [800, 600]",  "fill_color":kTeal+1,    "line_color":kTeal+1,    "line_style":4   },
        "SlepSlep_direct_800p0_700p0"  : {"type":"signal", "leg":"#tilde{#font[12]{l}} #tilde{#font[12]{#chi}} [800, 700]",  "fill_color":kTeal-9,    "line_color":kTeal-9,    "line_style":4   },

    }


    return d_sample
