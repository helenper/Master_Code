# plotfunctions.py
# Functions used in HistogramMaking.py for ploting histograms
# Helen Persson 


# Python imports
import operator   # Used to sort the backgrounds after size
import os

# Personal imports
import plotglobals as pg # Import to get access to cross file dicts, lists etc

# ROOT imports
from ROOT import gROOT, gPad, gStyle
from ROOT import TCanvas, TFile, THStack, TLegend, TChain, TH1F, TH2, TAxis, TPad, TRatioPlot 
from ROOT import kGreen, kYellow, kRed, kBlue, kOrange, kMagenta, kBlack, kFullCircle 
from ROOT.TAxis import kCenterLabels 
from ROOT import RooFit, RooStats
from ROOT import TH2D

#==================================================
#
# Functions
#
#==================================================

def setup_canvas(arg="plot", ratio_plot=False):
    """
    Function to set up canvas dependent on what user want to plot.

    Input variables:
    - ratio_plot  : bool used to determin if to create pad for  ratio plot data/MC

    Output variable:
    - canvas      : canvas to draw histograms on 
    - leg         : legend for histograms
    - pad1/pad2   : if ratio_plot == True, create two pads on canvas
    """
    
    global canvas, leg, pad1, pad2

    if ratio_plot == False:

        canvas = TCanvas( arg, arg, 1)
        gStyle.SetLegendBorderSize(0); # Remove (default) border around legend 
        gStyle.SetOptStat(0)
        leg = TLegend(0.65, 0.60, 0.9, 0.85) #Creating legend at given coordinates
       
        return canvas, leg

    else:

        canvas = TCanvas(arg, arg, 1)
        gStyle.SetLegendBorderSize(0); # Remove (default) border around legend 
        gStyle.SetOptStat(0)
        leg = TLegend(0.65, 0.60, 0.9, 0.85) #Creating legend at given coordinates
       

        pad1= TPad("pad1_fk","pad1_fk",0.0,0.3,1.0,1.0,21)
        pad1.Draw();
        pad1.SetRightMargin(0.03);
        pad1.SetFillColor(0);
        pad1.SetBottomMargin(0.01);
        
        pad2 = TPad("pad2_mc","pad2_mc",0.0,0.0,1.0,0.3,22)
        pad2.Draw();
        pad2.SetRightMargin(0.03);
        pad2.SetFillColor(0);
        pad2.SetTopMargin(0.05);
        pad2.SetBottomMargin(0.4);
        pad2.SetGridy()

        return canvas, leg, pad1, pad2



def readROOTfiles(ROOT_path, region, variables, signal_names, signal_to_plot, ngroup, plot_MC, plot_data, plot_signal):
    """
    Function that reads root files and put histograms into a dictionary.

    Input variables: 
    - ROOT_path     : path to the ROOT files
    - region        : region to plot hisograms for
    - variables     : list of variables to read in histograms from
    - signal_names  : list of signals to read root files for
    - ngroup        : int giving number for rebinning of histograms 
    - plot_MC       : bool used to determin if to make table for MC
    - plot_data     : bool used to determin if to make table for data
    - plot_signal   : bool used to determin if to make table for signal(s)

    Output variables: 
    - None
    """

    print " "
    print "Reading ROOT files"
    print " "

    # Read MC
    if plot_MC == True:
        nEntries = {}
        for samp in pg.l_sample_bkg:
            

            if os.path.isfile(ROOT_path + samp + ".root"):
                myFile = TFile.Open(ROOT_path + samp + ".root", "r")
                pg.d_hist[samp] = {}
                pg.d_basesignal[samp] = {}
            else:
                print "No file for: ", samp
                continue

            for var in variables:
                if not var in pg.d_MC.keys():
                    pg.d_MC[var] = THStack()
               
                try:
                    if var not in ["nJetB", "nJetLight", "nLepSignal", "nLepBase", "baseVSsignal"]:
                        pg.d_hist[samp][var] = myFile.Get("hist_" + var + "_" + region)
                    else:
                        if var not in ["baseVSsignal"]:
                            pg.d_hist[samp][var] = myFile.Get("hist_" + var)
                        else:
                            pg.d_basesignal[samp][var]= myFile.Get("hist_" + var)

                except:
                    print "did not find histogram of: ", region, samp, var
                    continue 

                if var not in ["baseVSsignal"]:
                    pg.d_hist[samp][var].SetDirectory(0)
                    pg.d_hist[samp][var].SetFillColor(pg.d_sample[samp]["fill_color"])
                    pg.d_hist[samp][var].SetLineColor(pg.d_sample[samp]["line_color"])
                    
                if var == variables[0]:    # Used for sorting the ploting sequence of MC
                    nEntries[samp] =  pg.d_hist[samp][var].GetEntries()

            myFile.Close()

        nEntries_sorted = sorted(nEntries.items(), key=operator.itemgetter(1))
    
        for item in nEntries_sorted:
            if item[0] in pg.l_sample_bkg:
                for var in variables:
                    if var not in ["nJetB", "nJetLight", "nLepSignal", "nLepBase", "baseVSsignal"]:
                        pg.d_MC[var].Add(pg.d_hist[item[0]][var].Rebin(ngroup))
                    else:
                         if var not in ["baseVSsignal"]:
                            pg.d_MC[var].Add(pg.d_hist[item[0]][var].Rebin(1))
                    if not item[0] in pg.l_leg:
                        pg.l_leg.append(item[0])
                        leg.AddEntry(pg.d_hist[item[0]][var],pg.d_sample[item[0]]["leg"], "f")


    # Read data
    if plot_data == True:
        
        for samp in pg.l_sample_data:
        
            if os.path.isfile(ROOT_path + samp + ".root"):
                myFile = TFile.Open(ROOT_path + samp + ".root", "r")
                pg.d_hist[samp] = {}
                pg.d_basesignal[samp] = {}
            
            else:
                print "No file for: ", samp
                continue

            for var in variables:

                if not var in pg.d_data.keys():
                    pg.d_data[var] = THStack()
                
                try:
                    if var not in ["nJetB", "nJetLight", "nLepSignal", "nLepBase","baseVSsignal"]:
                        pg.d_hist[samp][var] = myFile.Get("hist_" + var + "_" + region)
                    else:
                        if var not in ["baseVSsignal"]:
                            pg.d_hist[samp][var] = myFile.Get("hist_" + var)
                        else:
                            pg.d_basesignal[samp][var]= myFile.Get("hist_" + var)

                except:
                    print "did not find histogram of: ", region,  samp, var
                    continue  
  
                if var not in ["baseVSsignal"]:
                    pg.d_hist[samp][var].SetDirectory(0)
                    pg.d_hist[samp][var].SetFillColor(pg.d_sample[samp]["fill_color"])
                    pg.d_hist[samp][var].SetLineColor(pg.d_sample[samp]["line_color"])
                    pg.d_hist[samp][var].SetMarkerStyle(pg.d_sample[samp]["marker_style"])

                    
                if not samp in pg.l_leg:
                    pg.l_leg.append(samp)
                    leg.AddEntry(pg.d_hist[samp][var], pg.d_sample[samp]["leg"], "lp")

                if var not in ["nJetB", "nJetLight", "nLepSignal", "nLepBase", "baseVSsignal"]:
                    pg.d_data[var].Add(pg.d_hist[samp][var].Rebin(ngroup))
                else:
                    if var not in ["baseVSsignal"]:
                        pg.d_data[var].Add(pg.d_hist[samp][var].Rebin(1))

            try:
                myFile.Close()
            except:
                continue

    # Read signal
    if plot_signal == True:

        for samp in signal_names: 
            if os.path.isfile(ROOT_path + samp + ".root"):
                myFile = TFile.Open(ROOT_path + samp + ".root", "r")
                pg.d_hist[samp] = {}
                pg.d_signal[samp] = {}
                pg.d_basesignal[samp] = {}
            else:
                print "No file for: ", samp
                continue

            for var in variables:

                if not var in pg.d_signal.keys():
                    pg.d_signal[samp][var] = THStack()
                
                try:
                    if var not in ["nJetB", "nJetLight", "nLepSignal", "nLepBase", "baseVSsignal"]:
                        pg.d_hist[samp][var] = myFile.Get("hist_" + var + "_" + region)
                    else:
                        if var not in ["baseVSsignal"]:
                            pg.d_hist[samp][var] = myFile.Get("hist_" + var)
                        else:
                            pg.d_basesignal[samp][var]= myFile.Get("hist_" + var)

                    
                except:
                    print "did not find histogram of: ", region, samp, var
                    continue    
                if var not in ["baseVSsignal"]:
                    pg.d_hist[samp][var].SetDirectory(0)
                    pg.d_hist[samp][var].SetFillColorAlpha(pg.d_sample[samp]["fill_color"], 0)
                    pg.d_hist[samp][var].SetLineColor(pg.d_sample[samp]["line_color"])
                    pg.d_hist[samp][var].SetLineStyle(pg.d_sample[samp]["line_style"])
                                
                if not samp in pg.l_leg and samp in signal_to_plot:
                    pg.l_leg.append(samp)
                    leg.AddEntry(pg.d_hist[samp][var], pg.d_sample[samp]["leg"], "l")

                if var not in ["nJetB", "nJetLight", "nLepSignal", "nLepBase", "baseVSsignal"]:
                    pg.d_signal[samp][var].Add(pg.d_hist[samp][var].Rebin(ngroup))
                else:
                    if var not in ["baseVSsignal"]:
                        pg.d_signal[samp][var].Add(pg.d_hist[samp][var].Rebin(1))

            myFile.Close()


    return None


def draw_histograms(PDF_path, region, folder_name, file_name, signal_names, plot_MC, plot_data, plot_signal):
    """
    Function to plot histograms.

    Input variables: 
    - PDF_path      : path to where the pdf files are saved
    - region        : region to draw histogram for
    - folder_name   : name of the folder where to save, format yyyy-mm-dd_hh-mm-ss
    - file_name     : name to spesify more about the file used in final filename when saved
    - signal_names  : list of signals to draw in histogram 
    - plot_MC       : bool used to determin if to make table for MC
    - plot_data     : bool used to determin if to make table for data
    - plot_signal   : bool used to determin if to make table for signal(s)

    Output variables: 
    - 
    """

    print " " 
    print "Drawing histograms"
    print " "

    canvas.Print(PDF_path + folder_name + "_" + region + "_" + file_name + "_histograms.pdf[")

    # Plot only MC
    if plot_MC == True and plot_data == False and plot_signal == False:

        for item in pg.d_MC:
            canvas.cd()
            
            gPad.SetLogy(); # Set log y-axis
            pg.d_MC[item].Draw("hist")
            leg.Draw()
            pg.d_MC[item].GetXaxis().SetTitle(pg.d_xaxis[item])
            pg.d_MC[item].GetXaxis().SetTitleOffset(1.3)
            #pg.d_MC[item].GetXaxis().SetTickLength()      #Set size of ticks along xaxis
            #pg.d_MC[item].GetXaxis().SetLabelOffset(999)  #Removes numbers on xaxis
            
            pg.d_MC[item].GetYaxis().SetTitle("# events")
            pg.d_MC[item].GetYaxis().SetTitleOffset(0.7)
            pg.d_MC[item].GetYaxis().SetTitleSize(0.05)
            
            canvas.Print(PDF_path + folder_name + "_" + region + "_" + file_name+ "_histograms.pdf")


    # Plot only data: 
    if plot_MC == False and plot_data == True and plot_signal == False:
    
        for item in pg.d_data:
            canvas.cd()
            print item
            
            gPad.SetLogy(); # Set log y-axis
            pg.d_data[item].Draw("hist")
            leg.Draw()
            pg.d_data[item].GetXaxis().SetTitle(pg.d_xaxis[item])
            pg.d_data[item].GetXaxis().SetTitleOffset(1.3)
            #pg.d_data[item].GetXaxis().SetTickLength()
            pg.d_data[item].GetXaxis().SetLabelOffset(999)
            
            pg.d_data[item].GetYaxis().SetTitle("# events")
            pg.d_data[item].GetYaxis().SetTitleOffset(0.7)
            pg.d_data[item].GetYaxis().SetTitleSize(0.05)
    
            canvas.Print(PDF_path + folder_name + "_" + file_name + "_histograms.pdf")


    # Plot only signal:
    if plot_MC == False and plot_data == False and plot_signal == True:   

        print " " 
        print "NOT IMPLEMENTED"
        print " "
        
        #canvas.Print(PDF_path + folder_name + "_" + file_name +"_histograms.pdf")

    # Plot MC and data:
    if plot_MC == True and plot_data == True and plot_signal == False:

        
        for item in pg.d_MC:
            canvas.cd()
            pad1.cd()
            
            gPad.SetLogy(); # Set log y-axis
            pg.d_MC[item].Draw("hist")
            leg.Draw()
            pg.d_MC[item].GetXaxis().SetTitle(" ")
            pg.d_MC[item].GetXaxis().SetTitleOffset(1.3)
            #pg.d_MC[item].GetXaxis().SetTickLength()
            pg.d_MC[item].GetXaxis().SetLabelOffset(999)
            
            pg.d_MC[item].GetYaxis().SetTitle("# events")
            pg.d_MC[item].GetYaxis().SetTitleOffset(0.7)
            pg.d_MC[item].GetYaxis().SetTitleSize(0.05)
            
            pg.d_data[item].Draw("same e")
            
            pad2.cd()
            
            hsumMC = (pg.d_MC[item].GetStack().Last()).Clone("mcsum")
            hsumData = (pg.d_data[item].GetStack().Last()).Clone("datasum")
            
            stack_resid = hsumMC.Clone("hist_ratio")
            stack_resid.Divide(hsumData, hsumMC)
        
            stack_resid.SetTitle("")
            #stack_resid.SetMarkerStyle(7)
            stack_resid.SetMarkerColor(kBlack)
            stack_resid.SetLineColor(kBlack)
            
            stack_resid.GetYaxis().SetRangeUser(0,3)
            stack_resid.Draw("pe0");
            stack_resid.GetXaxis().SetTitleOffset(1.2)#(0.9)
            stack_resid.GetXaxis().SetTitle(pg.d_xaxis[item])
            stack_resid.GetXaxis().SetLabelSize(0.09)
            stack_resid.GetXaxis().SetTitleSize(0.12)
            
            stack_resid.GetYaxis().SetTitle("Data/MC")
            stack_resid.GetYaxis().SetTitleOffset(0.35)
            stack_resid.GetYaxis().SetTitleSize(0.12)
            stack_resid.GetYaxis().SetLabelSize(0.09)
            #stack_resid_UP.Draw("hist][ same")
            #stack_resid_DOWN.Draw("hist][ same")
            stack_resid.Draw("pe0 same")
            stack_resid.Draw("axis same")
            stack_resid.Draw("axiG same")

            canvas.Print(PDF_path + folder_name +"_" + region + "_"  + file_name + "_histograms.pdf")


    # Plot Mc and signal:
    if plot_MC == True and plot_data == False and plot_signal == True:
        for item in pg.d_MC:
            canvas.cd()
            
            gPad.SetLogy(); # Set log y-axis
            pg.d_MC[item].Draw("hist")
            leg.Draw()
            pg.d_MC[item].GetXaxis().SetTitle(pg.d_xaxis[item])
            pg.d_MC[item].GetXaxis().SetTitleOffset(1.3)
            #pg.d_MC[item].GetXaxis().SetTickLength()
            #pg.d_MC[item].GetXaxis().SetLabelOffset(999)
            
            pg.d_MC[item].GetYaxis().SetTitle("# events")
            pg.d_MC[item].GetYaxis().SetTitleOffset(0.7)
            pg.d_MC[item].GetYaxis().SetTitleSize(0.05)
            
            for elm in signal_names:
                pg.d_signal[elm][item].Draw("same hist")

        
    
            canvas.Print(PDF_path + folder_name + "_" + region + "_" + file_name +"_histograms.pdf")


    # Plot MC, data and signal:
    if plot_MC == True and plot_data == True and plot_signal == True:       
        
        for item in pg.d_MC:
            canvas.cd()
            pad1.cd()
        
            gPad.SetLogy(); # Set log y-axis
            pg.d_MC[item].Draw("hist")
            leg.Draw()
            pg.d_MC[item].GetXaxis().SetTitle(" ")
            pg.d_MC[item].GetXaxis().SetTitleOffset(1.3)
            #pg.d_MC[item].GetXaxis().SetTickLength()
            pg.d_MC[item].GetXaxis().SetLabelOffset(999)
            
            pg.d_MC[item].GetYaxis().SetTitle("# events")
            pg.d_MC[item].GetYaxis().SetTitleOffset(0.7)
            pg.d_MC[item].GetYaxis().SetTitleSize(0.05)
            
            pg.d_data[item].Draw("same e")
            
            for elm in signal_names:
                pg.d_signal[elm][item].Draw("same hist")


            pad2.cd()
        
            hsumMC = (pg.d_MC[item].GetStack().Last()).Clone("mcsum")
            hsumData = (pg.d_data[item].GetStack().Last()).Clone("datasum")
            
            stack_resid = hsumMC.Clone("hist_ratio")
            stack_resid.Divide(hsumData, hsumMC)
            
            stack_resid.SetTitle("")
            #stack_resid.SetMarkerStyle(7)
            stack_resid.SetMarkerColor(kBlack)
            stack_resid.SetLineColor(kBlack)
            
            stack_resid.GetYaxis().SetRangeUser(0,3)
            stack_resid.Draw("pe0");
            stack_resid.GetXaxis().SetTitleOffset(1.2)#(0.9)
            stack_resid.GetXaxis().SetTitle(pg.d_xaxis[item])
            stack_resid.GetXaxis().SetLabelSize(0.09)
            stack_resid.GetXaxis().SetTitleSize(0.12)
            
            stack_resid.GetYaxis().SetTitle("Data/MC")
            stack_resid.GetYaxis().SetTitleOffset(0.35)
            stack_resid.GetYaxis().SetTitleSize(0.12)
            stack_resid.GetYaxis().SetLabelSize(0.09)
            #stack_resid_UP.Draw("hist][ same")
            #stack_resid_DOWN.Draw("hist][ same")
            stack_resid.Draw("pe0 same")
            stack_resid.Draw("axis same")
            stack_resid.Draw("axiG same")

            canvas.Update()
            canvas.Print(PDF_path + folder_name + "_" + region + "_"  + file_name +"_histograms.pdf")


    canvas.Print(PDF_path + folder_name + "_" + region + "_"  + file_name + "_histograms.pdf]")
    
    return None




def plot_significanse(region, PDF_path, folder_name):
    # Only interested in significance for MT2 variable
          
    if region not in pg.d_zExp.keys():
        pg.d_zExp[region] = {}

    try: 
        x = (pg.d_MC["mT2"].GetStack().Last()).Clone("mcsum")
    except:
        print ""
        print " No mT2 variable from the read ROOT files"
        print ""


    x1 = x.FindBin(100)
    x2 = x.GetNbinsX() + 1
    
    bExpected = x.Integral(x1,x2)
    
    for s in pg.d_signal:

        if not s in pg.d_zExp.keys():
            pg.d_zExp[region][s] = {}

        sExpected = ((pg.d_signal[s]["mT2"].GetStack().Last()).Clone("signalsum")).Integral(x1,x2)

        relativeBkgUncert = 0.3

        zExp = RooStats.NumberCountingUtils.BinomialExpZ(sExpected, bExpected, relativeBkgUncert); 
    
        pg.d_zExp[region][s] = zExp

        signal_split = s.split("_")
        signal_name = signal_split[0] + "_" + signal_split[1]
        particle_mass = signal_split[2].replace("p0", "") + "_" + signal_split[3].replace("p0", "")
        
        if signal_name not in pg.d_significance.keys():
           pg.d_significance[signal_name] = {}
        
        pg.d_significance[signal_name][particle_mass] = zExp

    
    h_significance = {}
    for item in pg.d_significance: 
        print item
        if item not in h_significance.keys():
            h_significance[item] = {} 

        h_significance[item] = TH2D("histo_significance","histo_significance", 20, 0, 1000, 20, 0, 1000)
        h_significance[item].SetDirectory(0)
        
        can_significance, leg_significance = setup_canvas("sign_"+region, ratio_plot=False) 
        can_significance.cd()

        save_path_significance = PDF_path + folder_name + "_" + region + "_significance_plots_" + item +".pdf"
        can_significance.Print(save_path_significance +"[")

        for mass_split in pg.d_significance[item]:

            m1 = float(mass_split.split("_")[0])
            m2 = float(mass_split.split("_")[1])

            z = float(pg.d_significance[item][mass_split])

            h_significance[item].Fill(m1, m2, z)

            gStyle.SetPaintTextFormat("2.2f")
            h_significance[item].SetTitle("")
            h_significance[item].GetXaxis().SetTitle("mass1") 
            h_significance[item].GetXaxis().SetTitleOffset(1.3)
            h_significance[item].GetYaxis().SetTitle("mass2") 
            h_significance[item].GetYaxis().SetTitleOffset(1.3)
            h_significance[item].GetZaxis().SetTitle("Significance") 
            h_significance[item].GetZaxis().SetTitleOffset(0.6)
            h_significance[item].GetZaxis().SetTitleSize(0.025)

            h_significance[item].Draw("same text colz1")



        can_significance.Print(save_path_significance)

        can_significance.Print(save_path_significance +"]")

        can_significance.Close()



def plot_baseVSsignal(region, PDF_path, folder_name):
    
    BS_canvas, BS_leg = setup_canvas("BS_" + region, ratio_plot=False)
    BS_save_path = PDF_path + folder_name + "_" + region + "_baseVSsignal.pdf" 

    BS_canvas.cd()
    
    BS_canvas.Print(BS_save_path + "[")
    
    #print pg.d_basesignal.keys()
    #print pg.d_basesignal["C1C1_SlepSnu_950p0_50p0"]["baseVSsignal"].keys()
    print pg.d_basesignal
    for item in pg.d_hist:
        #print pg.d_basesignal[item]["baseVSsignal"]
                   
        pg.d_basesignal[item]["baseVSsignal"].Draw()
        BS_canvas.Print(BS_save_path)
        
        
    BS_canvas.Print(BS_save_path + "]")
    
    return None





def plot_histograms(ROOT_path, PDF_path, folder_name, region_list, variables, signal_names, signal_to_plot, ngroup, plot_MC, plot_data, plot_signal):
    """
    Function that takes inn signal names and boolean expressions to determin what to plot. If all boolean expressions are false,
    it prints out a statment where it states there is nothing to plot. Calls on necessary functions to read and create histograms.

    Variables to send in:
    - ROOT_path    : path to where the ROOT files are saved
    - PDF_path     : path to where the file should be saved
    - folder_name  : name of the spesific folder, format yyyy-mm-dd_hh-mm-ss.
    - region_list  : list of all regions to plot histograms for
    - variables    : list of variables to create histograms for
    - sinal_names  : list containing the signals you want to plot together with data/MC.
    - plot_MC      : bool used to determin if to make table for MC
    - plot_data    : bool used to determin if to make table for data
    - plot_signal  : bool used to determin if to make table for signal(s)

    Output variables:
    - None
    """
    
    print " " 
    print "Starting process to plot histograms"
    print " "

    print "Plot MC:     ", plot_MC
    print "Plot data:   ", plot_data
    print "Plot signal: ", plot_signal, "with signals", signal_to_plot
    print " "

    #Creating addition to filename or setting plot_signal = False if no signal is given
    sn = ""
    if len(signal_names)>0:
        for elm in signal_to_plot: 
            sn += elm 
    else:
        sn="NoSignal"
        print "No signal given"
        plot_signal = False
        

    # Creating addition to filename from int to string
    ngr = str(ngroup)


    # Plot noting
    if  plot_MC == False and plot_data == False and plot_signal == False:
        print "Noting to plot"
        sys.exit(1)
        
    # Plot MC
    if plot_MC == True and plot_data == False and plot_signal == False:
        file_name = "MC_Rebin_" + ngr
        #canvas, leg = setup_canvas(ratio_plot=False)
            
    #Plot data
    if plot_MC == False and plot_data == True and plot_signal == False:
        file_name = "data_Rebin_" + ngr
        #canvas, leg = setup_canvas(ratio_plot=False)
    
    #Plot signal
    if plot_MC == False and plot_data == False and plot_signal == True:
        file_name = "signal_" + sn + "Rebin_"+ ngr
        #canvas, leg = setup_canvas(ratio_plot=False)

    # Plot MC and data
    if plot_MC == True and plot_data == True and plot_signal == False:
        file_name = "MC_data_Rebin_"+ ngr
        #canvas, leg, pad1, pad2 = setup_canvas(ratio_plot=True)

    # Plot MC and signal
    if plot_MC == True and plot_data == False and plot_signal == True:
        file_name = "MC_signal_" + sn + "_Rebin_" + ngr
        #canvas, leg = setup_canvas(ratio_plot=False)
    
    # Plot MC, data and signal
    if plot_MC == True and plot_data == True and plot_signal == True:
        file_name = "MC_data_signal_" + sn + "_Rebin_" + ngr
        #canvas, leg, pad1, pad2 = setup_canvas("plot", ratio_plot=True)
    

    # Reading and drawing histograms
    for region in region_list:
        print "----------------------"
        print "Running for: ", region
        print "----------------------"

        if plot_MC == True and plot_data == True:
            canvas, leg, pad1, pad2 = setup_canvas("plot_"+region, ratio_plot=True)
        else: 
            canvas, leg = setup_canvas("plot_"+region, ratio_plot=False)

        readROOTfiles(ROOT_path, region, variables, signal_names, signal_to_plot, ngroup, plot_MC, plot_data, plot_signal)
        #draw_histograms(PDF_path, region,  folder_name, file_name, signal_to_plot, plot_MC, plot_data, plot_signal)
        
        print "----------------------"
        print "Calling significance"
        print "----------------------"
        #if region.split("-")[0] == "SR":
        #    plot_significanse(region, PDF_path, folder_name)

        print "----------------------"
        print "Calling baseline vs signal"
        print "----------------------"   
        plot_baseVSsignal(region, PDF_path, folder_name)    



        pg.d_MC.clear()
        pg.d_data.clear()
        pg.d_signal.clear()
        pg.l_leg = []
        leg.Clear()
        

        canvas.Close()   

    return None



if __name__ == "__main__":
    
    print " "
    print "Error in use:"
    print "This program contains functions used by HistogramMaker.py. Use HistogramMaker.py to access these functions"
    print " "

