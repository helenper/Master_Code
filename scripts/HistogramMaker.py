# HistogramMaker
# Reads ROOT files, cerate stacked histograms and cutflow tables
# Helen Persson 



#==================================================
#
# Import statements - python 
#
#==================================================
import sys
import argparse

# Import statements - end
#==================================================


#==================================================
#
# Reading command line arguments
#
#==================================================

possible_variables = ["lepPt",
                      "mll", 
                      "met_Et", 
                      "mT2", 
                      "all",
                     ]


possible_signals = ["C1C1_SlepSnu_200p0_50p0",
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

possible_regions = ["Preselection",
                    "SR-SF-0J", 
                    "SR-SF-1J", 
                    "SR-DF-0J",
                    "SR-DF-1J",
                    "SR-SF-0J-ee",
                    "SR-SF-1J-ee",
                    "SR-SF-0J-mumu",
                    "SR-SF-1J-mumu",
                    "VR-WW-0J",
                    "VR-WW-1J",
                    "VR-VZ",
                    "VR-top-low",
                    "VR-top-high",
                    "VR-top-WW",
                    "all",
                   ]


parser = argparse.ArgumentParser(description="Plotting histograms from ROOT-files")

parser.add_argument("-f", "--folder", 
                    type=str, 
                    help="the folder where the ROOT files are stored",
                    metavar="",
                   )

parser.add_argument("-v", "--variable", 
                    type=str, 
                    nargs="+",
                    default=["all"],
                    help="List of name of variables as strings, name same as in TTree",
                    metavar="",
                   )

parser.add_argument("-r", "--regions", 
                    type=str, 
                    nargs="+",
                    default=["all"],
                    choices=possible_regions,
                    help="List of name of regions to plot as strings. Allowed values are: "+", ".join(possible_regions) ,
                    metavar="",
                   )

parser.add_argument("-p_MC", "--plot_MC", 
                    action="store_true", 
                    default=False, 
                    help="Bool to determin if to plot background",
                    )

parser.add_argument("-p_data", "--plot_data", 
                    action="store_true", 
                    default=False, 
                    help="Bool to determin if to plot data",
                    )

parser.add_argument("-p_signal", "--plot_signal", 
                    action="store_true", 
                    default=False, 
                    help="Bool to determin if to plot signal",
                    )

parser.add_argument("-s" , "--signal", 
                    type=str, 
                    nargs="+",
                    default=[],
                    choices=possible_signals,
                    help="Decide what signals to run over for reading inn files and significance plots.  Allowed values are: "+", ".join(possible_signals) ,
                    metavar="",
                   )

parser.add_argument("-s_lp" , "--signal_list_plot", 
                    type=str, 
                    nargs="+",
                    default=[],
                    choices=possible_signals,
                    help="Decide what signals plot in histograms.  Allowed values are: "+", ".join(possible_signals) ,
                    metavar="",
                   )



parser.add_argument("-n" , "--ngroup", 
                    type=int, 
                    default=1,
                    help="Rebin n bins from original histogram into one bin in drawn histogram" ,
                    metavar="",
                   )


parser.add_argument("-p_table", "--plot_table", 
                    action="store_true", 
                    default=False, 
                    help="Bool to determin if to make tables",
                    )


args = parser.parse_args()

if not args.folder:
    print " "
    print "Must provide folder with files to make histograms from"
    print " "
    sys.exit(1)
else:
    folder_name = args.folder

if args.variable[0] == "all":
    possible_variables.remove("all")
    variables = possible_variables
else:
    variables = args.variable

if args.regions[0] == "all":
    possible_regions.remove("all")
    regions = possible_regions
else:
    regions = args.regions


if args.plot_signal == False:
    signal = []
    signal_to_plot = []


"""



    if not args.signal:
        if args.plot_signal == True:
            print ""
            print "Can not read signal files if no signal sample is given as input"
            print ""
            sys.exit(1)
        else:
            signal = []
            
        elif args.signal[0] == "all":
            l_signals = possible_signals
            l_signals.remove("all")
            signal = l_signals
            
        else:
            signal = args.signal



    if not args.signal_list_plot:
        if args.plot_signal == True:
            print ""
            print "Can not plot signals if no signal sample is given as input"
            print ""
            sys.exit(1)
        else:
            signal_to_plot = []
            
        elif args.signal_list_plot[0] == "all":
            l_signals_list = possible_signals
            l_signals_list.remove("all")
            signal_to_plot = l_signals
            
        else:
            signal_to_plot = args.signal_list_plot



"""     

plot_MC = args.plot_MC
plot_data = args.plot_data
plot_signal = args.plot_signal

ngroup = args.ngroup

plot_table = args.plot_table


# Reading command line arguments - end
#==================================================


#==================================================
#
# Defining paths
#
#==================================================

main_path = "/uio/hume/student-u10/helenper/Master/Analyse/Histograms/"
ROOT_path = main_path + folder_name + "/ROOT/"
PDF_path = main_path + folder_name + "/PDF/"
logfile_path = main_path + folder_name

# Defining paths
#==================================================


#==================================================
#
# Import ROOT here via other files not to 
# collide with argparser
#
#==================================================

import plotfunctions as pf
import plotglobals as pg
import tablefunctions as tf


# Import ROOT - end
#==================================================



#==================================================
#
# Main program
#
#==================================================



# Initialize cross program needed list, dict ect
pg.init()

# Ploting function
if plot_MC == False and plot_data == False and plot_signal == False:
    print "--------------------"
    print " "
    print "Nothing sendt to ploting"
    print " " 
    print "--------------------"

if plot_MC == True or plot_data == True or plot_signal == True:
    print "--------------------"
    print " " 
    print "Plotting"
    print " "
    print "--------------------"
    
    variables += ["nJetB", "nJetLight", "nLepSignal", "nLepBase", "baseVSsignal"]
    pf.plot_histograms(ROOT_path, PDF_path, folder_name, regions, variables, signal, signal_to_plot, ngroup, plot_MC, plot_data, plot_signal)


# Making tables holding cutflows
if plot_table == False:
    print "--------------------"
    print " "
    print "Nothing sendt to make tables"
    print " "
    print "--------------------"

else:
    print "--------------------"
    print " "
    print "Tables are beeing made"
    print " "
    print "--------------------"

    tf.make_table(logfile_path)














#==================================================
#
#  Integrate and rebin histograms
#
#==================================================

#Ask user if they whant to continue to integrate and rebin histograms

"""
txt_input = raw_input("Do you want to integrate and rebin historgam? y/n ")

if txt_input != "y":
    sys.exit(0)
"""


# Integrate histogram
"""
canvas_rebind = TCanvas()
gStyle.SetLegendBorderSize(0); # Remove (default) border around legend 
leg_rebind = TLegend(0.65, 0.60, 0.9, 0.85) #Creating legend at given coordinates

d_hs_rebined = THStack()

 
 
x_low = [100, 105, 110, 120, 140, 160, 180, 220, 260]
x_high = [105, 110, 120, 140, 160, 180, 220, 260, 1000]
"""
"""
#for hist in d_hs["mT2"].GetHists() and for hist in d_data["mT2"].GetHists():
for hist in itertools.chain( d_hs["mT2"].GetHists(), d_data["mT2"].GetHists()):
    h1 = TH1F("","", 9, 0, 9)
    i = 1
    h = 0
    for xL,xH in zip(x_low, x_high):
        x = hist.GetXaxis()
        FillColor = hist.GetFillColor()
        LineColor = hist.GetLineColor()
        MarkerStyle = hist.GetMarkerStyle()
        MarkerColor = hist.GetMarkerColor()
        print MarkerColor
        x1 =x.FindBin(xL)
        x2 = x.FindBin(xH)
        h = hist.Integral(x1, x2)
        h1.SetBinContent(i, h)

        if xH == 1000: 
            xlable = "(" + str(xL) + ", \infty )"
        else:
            xlable = "(" + str(xL) + ", "  + str(xH) + ")" 
        h1.GetXaxis().SetBinLabel(i, xlable)
        
        if MarkerStyle == kFullCircle:
            print "marker"
            h1.SetMarkerStyle(MarkerStyle)
            h1.SetMarkerColor(MarkerColor)
        else:
            print "line"
            h1.SetFillColor(FillColor)
            h1.SetLineColor(LineColor)
            
        i += 1
    d_hs_rebined.Add(h1)


canvas_rebind.cd()
gPad.SetLogy(); # Set log y-axis
d_hs_rebined.Draw("histo")
leg.Draw()
canvas_rebind.Print(PFD_save_path + folder_name+ "Histogram_Rebind.pdf")
"""

#  Integrate and rebin histograms - end
#==================================================

