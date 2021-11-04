import os
import sys


from ROOT import gROOT, gPad, gStyle, gSystem, TStyle
from ROOT import TCanvas, TFile, THStack, TH1F, TLegend, TChain, TH1, TH2, TAxis, TPad, TRatioPlot, TImage
from ROOT import kGreen, kYellow, kRed, kBlue, kOrange, kMagenta, kBlack, kFullCircle, kRainBow
from ROOT.TAxis import kCenterLabels 
from ROOT import RooFit, RooStats
from ROOT import TH2D


import operator   # Used to sort the backgrounds after size
import plotconfig as pc

# Set to true to hide canvases drawing when code is running
gROOT.SetBatch(True)
#Same command?
#ROOT.gROOT.SetBatch(1)

def make_canvas(l_signals_to_plot): 

    l_filename = []

    for signals in l_signals_to_plot:
        #print signals
        signal_names = ""
        for k in range(len(signals)):
            if k == 0:
                signal_names +=signals[k]
            else:
                signal_names += "_"
                signal_names += signals[k] 

        filename = "plot_bkg_data_sign_" + signal_names
        l_filename.append(filename)
        
        pc.d_canvas[filename] = TCanvas(filename, filename, 1)
        gStyle.SetLegendBorderSize(0); # Remove (default) border around legend 
        gStyle.SetOptStat(0)

        #pc.d_leg[filename] = TLegend(0.65, 0.60, 0.9, 0.85)
        pc.d_leg[filename] = TLegend(0.50, 0.50, 0.9, 0.9)
        
        
        pc.d_pad1[filename] = TPad("pad1_fk"+filename,"pad1_fk"+filename,0.0,0.3,1.0,1.0,21)
        pc.d_pad1[filename].Draw();
        pc.d_pad1[filename].SetRightMargin(0.03);
        pc.d_pad1[filename].SetFillColor(0);
        pc.d_pad1[filename].SetBottomMargin(0.01);
        

        pc.d_pad2[filename] = TPad("pad2_mc"+filename,"pad2_mc"+filename,0.0,0.0,1.0,0.3,22)
        pc.d_pad2[filename].Draw();
        pc.d_pad2[filename].SetRightMargin(0.03);
        pc.d_pad2[filename].SetFillColor(0);
        pc.d_pad2[filename].SetTopMargin(0.05);
        pc.d_pad2[filename].SetBottomMargin(0.4);
        pc.d_pad2[filename].SetGridy()

    return l_filename



def readROOTfiles(ROOT_path):
    """
    Function that reads root file and sorts histograms into stacks based on type (bkg, data, signal)
    """

    print " "
    print "Reading ROOT files"
    print " "

    file_paths = []

    for path in ROOT_path:
        #print path
        filelist = [file_ for file_ in os.listdir(path) if file_ not in ["Logfile"]]
        
        file_paths += [path + "/" + f for f in filelist]


    for f_path in file_paths:
        flist = f_path.rpartition("/")
        #print flist
        if len(flist[-1].split(".")[0].split("_")) == 2:
            samp, period = flist[-1].split(".")[0].split("_")
        else:
            samp = flist[-1].split(".")[0].rpartition("_")[0]
            period = flist[-1].split(".")[0].rpartition("_")[-1]

        #print samp, period

        if os.path.isfile(f_path):
            myFile = TFile.Open(f_path, "r")
            #print "File opend"

        else: 
            print " "
            print "No such file", f_path
            print " "


        for elm in myFile.GetListOfKeys():
            hist_name = elm.GetName()

            l_name = hist_name.split("_")
            
            if len(l_name) >3:
                var = l_name[1] + "_" + l_name[2]
                region = l_name[3]

            elif len(l_name) == 3:
                var = l_name[1]
                region = l_name[2]
 
            else:
                var = l_name[1]
                region = "noRegion"

            #print hist_name
            #print hist_name, period, region, var
            #print var

            #Create lists to use later for traversing histograms
            if period not in pc.l_period:
                pc.l_period.append(period)

            if region not in pc.l_region:
                pc.l_region.append(region)

            if samp not in pc.l_samp:
                pc.l_samp.append(samp)

            if var not in pc.l_var:
                pc.l_var.append(var)

            #setup pc.d_hist 
            if period not in pc.d_hist.keys(): 
                pc.d_hist[period] = {}

            if region not in pc.d_hist[period].keys():
                pc.d_hist[period][region] = {}
                
            if samp not in pc.d_hist[period][region].keys():
                pc.d_hist[period][region][samp] = {}

            if var not in pc.d_hist[period][region][samp].keys():
                pc.d_hist[period][region][samp][var] = {}

            #setup pc.d_nEntries 
            if period not in pc.d_nEntries.keys(): 
                pc.d_nEntries[period] = {}

            if region not in pc.d_nEntries[period].keys():
                pc.d_nEntries[period][region] = {}

            if samp not in pc.d_nEntries[period][region].keys() and samp in pc.l_bkg or samp in ["fakes"]:
                pc.d_nEntries[period][region][samp] = {}


            # setup pc.d_bkg  
            if period not in pc.d_bkg.keys():
                pc.d_bkg[period] = {}

            if region not in pc.d_bkg[period].keys():
                pc.d_bkg[period][region] = {}

            if var not in pc.d_bkg[period][region].keys():
                pc.d_bkg[period][region][var] = THStack()

            # setup pc.d_data    
            if period not in pc.d_data.keys():
                pc.d_data[period] = {}

            if region not in pc.d_data[period].keys():
                pc.d_data[period][region] = {}

            if var not in pc.d_data[period][region].keys():
                pc.d_data[period][region][var] = TH1F()

            # setup pc.d_signal 
            if period not in pc.d_signal.keys():
                pc.d_signal[period] = {}

            if region not in pc.d_signal[period].keys():
                pc.d_signal[period][region] = {}

            if samp not in pc.d_signal[period][region].keys():
                pc.d_signal[period][region][samp] = {}

            if var not in pc.d_signal[period][region][samp].keys():
                pc.d_signal[period][region][samp][var] = TH1F()


            # Get histograms
            pc.d_hist[period][region][samp][var] = myFile.Get(hist_name)
            #print period, region, samp, var

            # Set ownership of histograms to d_hist so the ROOT file can be closed
            pc.d_hist[period][region][samp][var].SetDirectory(0)


            # Background
            if samp in pc.l_bkg or samp == "fakes":

                pc.d_hist[period][region][samp][var].SetFillColor(pc.d_sample[samp]["fill_color"])
                pc.d_hist[period][region][samp][var].SetLineColor(pc.d_sample[samp]["line_color"])

                pc.d_nEntries[period][region][samp] =  pc.d_hist[period][region][samp][var].GetEntries()
       
            # Data
            if samp in pc.l_data:
                
                pc.d_hist[period][region][samp][var].SetFillColor(pc.d_sample[samp]["fill_color"])
                pc.d_hist[period][region][samp][var].SetLineColor(pc.d_sample[samp]["line_color"])
                pc.d_hist[period][region][samp][var].SetMarkerStyle(pc.d_sample[samp]["marker_style"])

                
            # Signal
            #if samp in l_signals_to_plot: 
            if samp in pc.l_signals:

                pc.d_hist[period][region][samp][var].SetLineColor(pc.d_sample[samp]["line_color"])
                pc.d_hist[period][region][samp][var].SetFillColorAlpha(pc.d_sample[samp]["fill_color"], 0)
                pc.d_hist[period][region][samp][var].SetLineStyle(pc.d_sample[samp]["line_style"])


        myFile.Close()


    return None


d_ap = {}
d_ap_bkg = {}
ap_nEntries = {}
d_ap_leg = {}

def stack_ap(ngroup):
    print "" 
    print "Creating stack of samples for all periods" 
    print "" 

    #period_list = pc.d_hist.keys()
    period_list = pc.l_period
    #reg_list = [x for x in pc.d_hist[period_list[0]].keys() if x != "noRegion"]
    reg_list = [x for x in pc.l_region if x != "noRegion"]
    #samp_list = pc.d_hist[period_list[0]][reg_list[0]].keys()
    samp_list = pc.l_samp
    #var_list = pc.d_hist[period_list[0]][reg_list[0]][samp_list[0]].keys()
    var_list = [x for x in pc.l_var if x not in pc.l_non_kinematic_var]

    #print var_list
    

    for reg in reg_list: #reg not in pc.l_non_kinematic_var:
        #d_ap_leg[filename+reg] = TLegend(0.65, 0.60, 0.9, 0.85)
        if reg not in d_ap.keys():
            d_ap[reg] = {}
        if reg not in ap_nEntries.keys():
            ap_nEntries[reg] = {}
        
        for samp in samp_list:
            if samp not in d_ap[reg].keys():
                d_ap[reg][samp] = {}
            if samp not in ap_nEntries[reg].keys():
                ap_nEntries[reg][samp] = {}
            
            for var in var_list:
                if var not in d_ap[reg][samp].keys():
                    d_ap[reg][samp][var] = TH1F("hist_all_periods_" + reg + "_" + samp + "_" + var, "hist_all_periods_" + reg + "_" + samp + "_" + var, 1000, 0, 1000).Rebin(ngroup)
    
                for per in period_list:
                    d_ap[reg][samp][var].Add(pc.d_hist[per][reg][samp][var].Clone("ap").Rebin(ngroup))


                d_ap[reg][samp][var].SetDirectory(0)
            
                # Background
                if samp in pc.l_bkg or samp == "fakes":
                    d_ap[reg][samp][var].SetFillColor(pc.d_sample[samp]["fill_color"])
                    d_ap[reg][samp][var].SetLineColor(pc.d_sample[samp]["line_color"])
       
                # Data
                if samp in pc.l_data:
                    d_ap[reg][samp][var].SetFillColor(pc.d_sample[samp]["fill_color"])
                    d_ap[reg][samp][var].SetLineColor(pc.d_sample[samp]["line_color"])
                    d_ap[reg][samp][var].SetMarkerStyle(pc.d_sample[samp]["marker_style"])

                
                # Signal
                if samp in pc.l_signals:
                    d_ap[reg][samp][var].SetLineColor(pc.d_sample[samp]["line_color"])
                    #d_ap[reg][samp][var].SetFillColorAlpha(pc.d_sample[samp]["fill_color"], 0)
                    d_ap[reg][samp][var].SetLineStyle(pc.d_sample[samp]["line_style"])



            bin1 = d_ap[reg][samp]["mT2"].FindBin(1)
            bin2 = d_ap[reg][samp]["mT2"].GetNbinsX() + 1
            ap_nEntries[reg][samp] = d_ap[reg][samp]["mT2"].Integral(bin1,bin2) 

            
    sorted_samp_list = {}
    for reg in reg_list:
        if reg not in d_ap_bkg.keys():
            d_ap_bkg[reg] = {}
        if reg not in sorted_samp_list.keys():
            sorted_samp_list[reg] = []            

        ap_nEntries_sorted = sorted(ap_nEntries[reg].items(), key=operator.itemgetter(1))
        
        for item in ap_nEntries_sorted:
            samp = item[0]
            val = item[1]
        
            for var in var_list:
                if var not in d_ap_bkg[reg].keys():
                    d_ap_bkg[reg][var] = THStack()
            
                if samp in pc.l_bkg or samp == "fakes":
                    #d_ap_bkg[reg][var].Add((d_ap[reg][samp][var].GetStack().Last().Clone("ap_bkg")))
                    d_ap_bkg[reg][var].Add(d_ap[reg][samp][var])

                    if samp not in sorted_samp_list[reg]:
                        sorted_samp_list[reg].append(samp) 


    return sorted_samp_list


def add_legend(sorted_samp_list, reg, signals):

    #reg_list = [x for x in pc.l_region if x != "noRegion"]
    var_list = [x for x in pc.l_var if x not in pc.l_non_kinematic_var]
    var = var_list[0]

    leg = TLegend(0.65, 0.60, 0.9, 0.85)
    
    #   for reg in reg_list:
    for s in reversed(sorted_samp_list[reg]):
           # print ""
           # print "Adding legend", reg, s 
           # print ""
            leg.AddEntry(d_ap[reg][s][var], pc.d_sample[s]["leg"], "f")

        
    leg.AddEntry(d_ap[reg]["data"][var], pc.d_sample["data"]["leg"], "lp")

    
    for sign in signals:
        if sign != "noSignal":
            leg.AddEntry(d_ap[reg][sign][var], pc.d_sample[sign]["leg"], "l")

    return leg





def make_histograms(output_path, filename, l_signals_to_plot, filled_bkg, filled_data, ngroup, ap=True):

    if ap == False:
        for period in pc.l_period:
        #for period in ["17", "15-16"]:
            for region in pc.l_region:
            #for region in ["SR-SF-0J", "SR-DF-0J"]:
                if region != "noRegion":
                    sort_and_stack_bkg(period, region, filename, ngroup, filled_bkg)
                    stack_data(period, region, filename, ngroup, filled_data)
                    stack_signal(period, region, l_signals_to_plot, ngroup, filename)
                    draw_histograms(output_path, filename, period, region, l_signals_to_plot)

    if ap == True:
        sorted_samp_list = stack_ap()
        
        draw_histograms_ap(output_path, filename, ngroup, sorted_samp_list, l_signals_to_plot)

    return None





def draw_histograms_ap(output_path, filename, ngroup, sorted_samp_list, signals):


    print " "
    print " Draw histograms all periods together" 
    print " "

    period_list = pc.l_period
    #reg_list = [x for x in pc.d_hist[period_list[0]].keys() if x != "noRegion"]
    reg_list = [x for x in pc.l_region if x != "noRegion"]
    #samp_list = pc.d_hist[period_list[0]][reg_list[0]].keys()
    samp_list = pc.l_samp
    #var_list = pc.d_hist[period_list[0]][reg_list[0]][samp_list[0]].keys()
    var_list = pc.l_var + ["mT2_100_280"]


    for reg in reg_list:
        #pc.d_canvas[filename].Print("TEEEST.pdf[")
        pc.d_canvas[filename].Print(output_path +"/"+ reg + "_ap_" + filename + ".pdf[")

        leg = add_legend(sorted_samp_list, reg, signals)
        gStyle.SetLegendTextSize(0.04)
        leg.SetNColumns(2)
        #TStyle.SetLabelSize(0.04, "x")
        #gStyle.SetLegendMarkerSize(0.4)


        for var in var_list:
                if var not in pc.l_non_kinematic_var and var != "mT2_100_280":

                    pc.d_canvas[filename].cd()
                    pc.d_pad1[filename].cd()
                
            
                    gPad.SetLogy(); # Set log y-axis
                

                    d_ap_bkg[reg][var].Draw("hist")
                    #(d_ap[reg]["data"][var].GetStack().Last()).Draw("same e")
                    d_ap[reg]["data"][var].Draw("same e")
                    
                    #pc.d_leg[filename].Draw()
                    #d_ap_leg[filename+reg].Draw()
                    ##gStyle.SetLegendTextSize(0.9)
                    leg.Draw()

                    d_ap_bkg[reg][var].GetXaxis().SetTitle(" ")
                    d_ap_bkg[reg][var].GetXaxis().SetTitleOffset(1.3)
                    #d_ap_bkg[reg][var].GetXaxis().SetTickLength()
                    d_ap_bkg[reg][var].GetXaxis().SetLabelOffset(999)
                    
                    d_ap_bkg[reg][var].GetYaxis().SetLabelSize(0.08)                    

                    d_ap_bkg[reg][var].GetYaxis().SetTitle("# events")
                    d_ap_bkg[reg][var].GetYaxis().SetTitleOffset(0.7)
                    d_ap_bkg[reg][var].GetYaxis().SetTitleSize(0.08)
                    
        
                    for elm in signals:
                        if elm != "noSignal":
                            #(d_ap[reg][elm][var].GetStack().Last()).Draw("same hist")
                            d_ap[reg][elm][var].Draw("same hist") 


                    #"""
                    pc.d_pad2[filename].cd()
                    
                    hsumbkg = (d_ap_bkg[reg][var].GetStack().Last()).Clone("mcsum")
                    hsumData = (d_ap[reg]["data"][var].Clone("datasum"))
                    
                    stack_resid = hsumbkg.Clone("hist_ratio")
                    stack_resid.Divide(hsumData, hsumbkg)
                    
                    stack_resid.SetTitle("")
                    #stack_resid.SetMarkerStyle(7)
                    stack_resid.SetMarkerColor(kBlack)
                    stack_resid.SetLineColor(kBlack)
                    
                    stack_resid.GetYaxis().SetRangeUser(0,3)
                    stack_resid.Draw("pe0");
                    stack_resid.GetXaxis().SetTitleOffset(1.2)#(0.9)
                    stack_resid.GetXaxis().SetTitle(pc.d_xaxis[var])
                    stack_resid.GetXaxis().SetLabelSize(0.16)
                    stack_resid.GetXaxis().SetTitleSize(0.16)
                
                    stack_resid.GetYaxis().SetTitle("Data/MC")
                    stack_resid.GetYaxis().SetTitleOffset(0.35)
                    stack_resid.GetYaxis().SetTitleSize(0.12)
                    stack_resid.GetYaxis().SetLabelSize(0.16)
                    #stack_resid.GetXaxis().SetLabelSize(0.05)
                    #stack_resid_UP.Draw("hist][ same")
                    #stack_resid_DOWN.Draw("hist][ same")
                    stack_resid.Draw("pe0 same")
                    stack_resid.Draw("axis same")
                    stack_resid.Draw("axiG same")
                    #"""
    
                    #pc.d_canvas[filename].Print("TEEEST.pdf")
                    pc.d_canvas[filename].Print(output_path +"/"+ reg + "_ap_" + filename + ".pdf")
    
                if var == "mT2_100_280":
                    pc.d_canvas[filename].cd()
                    pc.d_pad1[filename].cd()
                
                    x = (d_ap_bkg[reg]["mT2"].GetStack().Last()).Clone("mcsum")
                    
                    x1 = x.FindBin(100)
                    #print "background", x.GetBinLowEdge(x1)
                    x2 = x.FindBin(280)
            
                    gPad.SetLogy(); # Set log y-axis

                    d_ap_bkg[reg]["mT2"].Draw("hist")
                    d_ap[reg]["data"]["mT2"].Draw("same e")
                    #pc.d_leg[filename].Draw()
                    leg.Draw()
                    
                    d_ap_bkg[reg]["mT2"].GetXaxis().SetTitle(" ")
                    d_ap_bkg[reg]["mT2"].GetXaxis().SetTitleOffset(1.3)
                    #d_ap_bkg[reg]["mT2"].GetXaxis().SetTickLength()
                    d_ap_bkg[reg]["mT2"].GetXaxis().SetLabelOffset(999)
                    d_ap_bkg[reg]["mT2"].GetXaxis().SetRange(x1,x2)
                    
                    d_ap_bkg[reg]["mT2"].GetYaxis().SetTitle("# events")
                    d_ap_bkg[reg]["mT2"].GetYaxis().SetTitleOffset(0.7)
                    d_ap_bkg[reg]["mT2"].GetYaxis().SetTitleSize(0.08)
                    
        
                    for elm in signals:
                        if elm != "noSignal":
                            d_ap[reg][elm]["mT2"].Draw("same hist")
                        
                    #"""
                    pc.d_pad2[filename].cd()
                    
                    hsumbkg = (d_ap_bkg[reg]["mT2"].GetStack().Last()).Clone("mcsum")
                    hsumData = (d_ap[reg]["data"]["mT2"].Clone("datasum"))
                    
                    stack_resid = hsumbkg.Clone("hist_ratio")
                    stack_resid.Divide(hsumData, hsumbkg)
                    
                    stack_resid.SetTitle("")
                    #stack_resid.SetMarkerStyle(7)
                    stack_resid.SetMarkerColor(kBlack)
                    stack_resid.SetLineColor(kBlack)
                    
                    stack_resid.GetYaxis().SetRangeUser(0,3)
                    stack_resid.Draw("pe0");
                    stack_resid.GetXaxis().SetTitleOffset(1.2)#(0.9)
                    stack_resid.GetXaxis().SetTitle(pc.d_xaxis["mT2"])
                    stack_resid.GetXaxis().SetLabelSize(0.16)
                    stack_resid.GetXaxis().SetTitleSize(0.16)
                    stack_resid.GetXaxis().SetRange(x1,x2)

                    stack_resid.GetYaxis().SetTitle("Data/MC")
                    stack_resid.GetYaxis().SetTitleOffset(0.35)
                    stack_resid.GetYaxis().SetTitleSize(0.12)
                    stack_resid.GetYaxis().SetLabelSize(0.16)
                    #stack_resid_UP.Draw("hist][ same")
                    #stack_resid_DOWN.Draw("hist][ same")
                    stack_resid.Draw("pe0 same")
                    stack_resid.Draw("axis same")
                    stack_resid.Draw("axiG same")
                    #"""
    
                    #pc.d_canvas[filename].Print("TEEEST.pdf")
                    pc.d_canvas[filename].Print(output_path +"/"+ reg + "_ap_" + filename + ".pdf")
                    
                    
        #pc.d_canvas[filename].Print("TEEEST.pdf]")
        pc.d_canvas[filename].Print(output_path +"/" + reg + "_ap_" + filename + ".pdf]")

    leg.Clear()
    return None



def plot_significanse_ap(output_path):
    # Only interested in significance for MT2 variable
    h_significance = {}
    #print pc.l_signals
    for region in pc.l_region:
            if region[0] == "S":
	
		if region not in h_significance.keys():
			h_significance[region] = {}               
                #	print "region added for:", period, region
		print ""
                print "Caclulation significance", region
                print "" 

		#print h_significance

                if region not in pc.d_zExp.keys():
                    pc.d_zExp[region] = {}

                try: 
                    x = (d_ap_bkg[region]["mT2"].GetStack().Last()).Clone("mcsum")

                except:
                    print ""
                    print "No mT2 variable for", region
                    print ""

                    
                x1 = x.FindBin(100)
                #print "background", x.GetBinLowEdge(x1)
                x2 = x.GetNbinsX() + 1
    
                bExpected = x.Integral(x1,x2)
                #print "bexpected = ", bExpected
    
                for s in pc.l_signals: # pc.d_signal[period][region]:
         
                    if not s in pc.d_zExp.keys():
                        pc.d_zExp[region][s] = {}

                    #print s, period, region

                    sExpected = (d_ap[region][s]["mT2"].Clone("signalsum")).Integral(x1,x2)
                    #print "sign" , pc.d_signal[period][region][s]["mT2"].Clone("signalsum").GetBinLowEdge(x1)
                    #print "sexpected %s = %.2f" %(s,sExpected)
                    relativeBkgUncert = 0.3
                    
                    zExp = RooStats.NumberCountingUtils.BinomialExpZ(sExpected, bExpected, relativeBkgUncert); 
    
                    #pc.d_zExp[region][s] = zExp

                    signal_split = s.split("_")
                    signal_name = signal_split[0] + "_" + signal_split[1]
                    particle_mass = signal_split[2].replace("p0", "") + "_" + signal_split[3].replace("p0", "")
       
		    #print signal_name, particle_mass 
		    if region not in pc.d_significance.keys():
			pc.d_significance[region] = {}
                    if signal_name not in pc.d_significance[region].keys():
                        pc.d_significance[region][signal_name] = {}
        
                    pc.d_significance[region][signal_name][particle_mass] = zExp


		#if item.startswith("C1C1_WW"):
		h_significance[region]["C1C1_WW"] = TH2D("histo_significance"+region+"C1C1_WW","histo_significance"+region+"C1C1_WW", 20, 70, 550, 20, 0, 250)
                h_significance[region]["C1C1_WW"].SetDirectory(0)  
  		h_significance[region]["C1C1_WW"].GetXaxis().SetTitle("m(#tilde{#chi}_{1}^{#pm}) [GeV]") 
		h_significance[region]["C1C1_WW"].GetYaxis().SetTitle("m(#tilde{#chi}_{1}^{0}) [GeV]") 
			#print "Hello"
		#if item.startswith("C1C1_SlepSnu"):
                h_significance[region]["C1C1_SlepSnu"] = TH2D("histo_significance"+region+"C1C1_SlepSnu","histo_significance"+region+"C1C1_SlepSnu", 20, 150, 1410, 20, 0, 550)
	        h_significance[region]["C1C1_SlepSnu"].SetDirectory(0)
           	h_significance[region]["C1C1_SlepSnu"].GetXaxis().SetTitle("m(#tilde{#chi}_{1}^{#pm}) [GeV]") 
                h_significance[region]["C1C1_SlepSnu"].GetYaxis().SetTitle("m(#tilde{#chi}_{1}^{0}) [GeV]") 
			#print "Yo"
		#if item.startswith("SlepSlep_direct"):
                h_significance[region]["SlepSlep_direct"] = TH2D("histo_significance"+region+"SlepSlep_direct", "histo_significance"+region+"SlepSlep_direct", 20, 50, 850, 20, 0, 800)
                h_significance[region]["SlepSlep_direct"].SetDirectory(0)
		h_significance[region]["SlepSlep_direct"].GetXaxis().SetTitle("m(#tilde{l})")
		h_significance[region]["SlepSlep_direct"].GetYaxis().SetTitle("m(#tilde{#chi}_{1}^{0}) [GeV]")	
			#print"Salu"
		    

		for item in ["C1C1_WW", "C1C1_SlepSnu", "SlepSlep_direct"]:
                	gStyle.SetPaintTextFormat("2.2f")
                	h_significance[region][item].SetTitle("")
                    #h_significance[region][item].GetXaxis().SetTitle("mass1") 
               		h_significance[region][item].GetXaxis().SetTitleOffset(1.3)
                    #h_significance[region][item].GetYaxis().SetTitle("mass2") 
                	h_significance[region][item].GetYaxis().SetTitleOffset(1.3)
                	h_significance[region][item].GetZaxis().SetTitle("Significance")
                	h_significance[region][item].GetZaxis().SetTitleOffset(1)
                	h_significance[region][item].GetZaxis().SetTitleSize(0.025)
                        gStyle.SetPalette(1)

    #print h_significance
    #sys.exit(1)
    #print "Periode 18, 17, 15-16:", h_significance["18"].keys(), h_significance["17"].keys(), h_significance["15-16"].keys()                 
    #print pc.d_significance[region]["C1C1_SlepSnu"]


    #print h_significance
    #print h_significance["18"].keys()

    
    for reg in pc.d_significance.keys():
	    for sample in pc.d_significance[reg].keys():
		print reg, sample
		#print pc.d_significance[per][reg]

                can_significance = TCanvas("significance_" + reg +sample,"significance_" + reg + sample, 1)
                gStyle.SetLegendBorderSize(0); # Remove (default) border around legend 
                gStyle.SetOptStat(0)
		can_significance.cd() 
		
                save_path_significance = output_path + "/" + "Significance" +"_" + reg + "_" + sample +".pdf"
                #save_path_significance = output_path + "/" + "Significance" +"_" + reg + "_" + sample +".png"
                    
                #can_significance.Print(save_path_significance)

		for mass_split in pc.d_significance[reg][sample].keys():
			#print ""
			#print "Now working on", reg, sample, mass_split
			#print ""
                    
                        m1 = float(mass_split.split("_")[0])
                        m2 = float(mass_split.split("_")[1])

                        z = float(pc.d_significance[reg][sample][mass_split])

                        h_significance[reg][sample].Fill(m1, m2, z)
		    
                        h_significance[reg][sample].SetMarkerSize(1.5)
			h_significance[reg][sample].Draw("same text colz1")
                        
                        #can_significance.Print(save_path_significance)

                    #can_significance.Print(save_path_significance +"]")

                 
		can_significance.Print(save_path_significance)       
                can_significance.Close()

    print "Calculated ap significances done" 	

    return None
