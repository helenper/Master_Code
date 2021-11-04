# tablefunctions.py
# Functions used by HistogramMaker.py to create tables showing cutflows
# Helen Persson 


#==================================================
#
# Imports
#
#==================================================

import plotconfig as pc
import os 
import sys

# Imports - end
#==================================================




#==================================================
#
# Functions
#
#==================================================

def read_logfile(logfile_path):
    """
    Function that reads the logfile created from MySelector.C. 
    Information is stored in two dictionaries, d_info and d_cutflow. 

    Input variables:
    - logfile_path  : the path to where the logfile is stored

    Output variables:
    - None
    """

    for path in logfile_path:

        logfile = open(path, "r") 

        for line in logfile:
            if "{" in line:
                continue

            l=  line.replace('\n', "").strip().split(":")
            if len(l)>4:
                samp, timeperiod, region, cut, val = l
                #print samp,timeperiod, region, cut, val
                if timeperiod not in pc.d_cutflow.keys():
                    pc.d_cutflow[timeperiod] = {}
                if not samp in pc.d_cutflow[timeperiod].keys():
                    pc.d_cutflow[timeperiod][samp] = {}
                    #print pc.d_cutflow.keys()
                if not region in pc.d_cutflow[timeperiod][samp].keys():
                    pc.d_cutflow[timeperiod][samp][region] = {}
                    #print pc.d_cutflow[samp].keys()
                if not cut in pc.d_cutflow[timeperiod][samp][region].keys():
                    pc.d_cutflow[timeperiod][samp][region][cut] = float(val)

        logfile.close()
  
    return None




def sort_headerx(list_l, list_elm):
    """
    Function for sorting the list used to determin the placement of hedings (xaxis) in the cutflow table.

    Input variables:
    - list_l    : list containing the headers in random order
    - list_elm  : describes the type of files studied. Can be "bkg", "data" or "signal"

    Output variables:
    - list_new  : list holding the headers in correct order
    """

    l_old = list_l
    l_new = []
    order_bkg = ['diboson','higgs', 'lowMassDY', 'singleTop', 'topOther', 'triboson', 'ttbar', 'Vgamma', 'Wjets', 'Zjets', "fakes"]
    order_data = ["data15-16", "data17", "data18", "data15-17", "data15-18", "data"]
    order_signal = pc.l_signals

    if list_elm == "bkg" or list_elm == "background": 
        for elm in order_bkg:
            if elm in l_old:
                l_new.append(elm)
                l_old.remove(elm)

            
        if len(l_old)>0:
            print "list_element not in order_list"
            for elm in l_old:
                l_new.append(elm)


    if list_elm == "data": 
        for elm in order_data:
            if elm in l_old:
                l_new.append(elm)
                l_old.remove(elm)
                
        if len(l_old)>0:
            print "list_element not in order_list"
            for elm in l_old:
                l_new.append(elm)

    if list_elm == "signal":
        for elm in order_signal:
            if elm in l_old:
                l_new.append(elm)
                l_old.remove(elm)
                
        if len(l_old)>0:
            print "list_element not in order_list"
            for elm in l_old:
                l_new.append(elm)

            
    return l_new




def calculate_percent_decrease(header_x):
    """
    Function that calculates the percent decrese between two consecutive cuts for MC, and inserts them in correct place in the list. 

    Input variables: 
    - header_x  : used to find the right index to place percentage

    Output variables:
    - None
    """

    percent =[None]*7
    idx = header_x.index("TotalMC")

    try:
        percent[0] = "-"
        pre.insert(idx + 1, percent[0])
                
    except:
        print "no percentage to be calculated"
        pre.insert(idx + 1, "-")
                
    try:
        percent[1] = ((flavor[idx] - pre[idx])/pre[idx])*100
        flavor.insert(idx + 1, percent[1])
                    
    except:
        print "no percentage to be calculated"
        flavor.insert(idx + 1, "-") 
        
    try:
        percent[2] = ((sign[idx] - flavor[idx])/flavor[idx])*100
        sign.insert(idx + 1, percent[2])
    
    except:
        print "no percentage to be calculated"
        sign.insert(idx + 1, "-")
                    
    try:
        percent[3] = ((jet[idx] - sign[idx])/sign[idx])*100
        jet.insert(idx + 1, percent[3])
                    
    except:
        print "no percentage to be calculated"
        jet.insert(idx + 1, "-")
                    
    try:    
        percent[4] = ((mll[idx] - jet[idx])/jet[idx])*100
        mll.insert(idx + 1, percent[4])
        
    except:
        print "no percentage to be calculated"
        mll.insert(idx + 1, "-")
                                
    try:    
        percent[5] = ((met_Et[idx] - mll[idx])/mll[idx])*100
        met_Et.insert(idx + 1, percent[5])

    except:
        print "no percentage to be calculated"
        met_Et.insert(idx + 1, "-")        
                    
    try:
        percent[6] = ((met_EtSign[idx] - met_Et[idx])/met_Et[idx])*100
        met_EtSign.insert(idx + 1, percent[6])
                    
    except:
        print "no percentage to be calculated"
        met_EtSign.insert(idx + 1, "-")

    return None





def write_table(output_path_tables, period):

    samp = pc.d_cutflow[period].keys()
    reg = pc.d_cutflow[period][samp[0]].keys()

    #print reg, samp

    samp_bkg = [bkg for bkg in samp if bkg in pc.l_bkg]
    samp_data = [d for d in samp if d in pc.l_data]
    samp_signal = [s for s in samp if s in pc.l_signals]

    global pre, flavor, sign, jet, mll, met_Et, met_EtSign, header_x, header_y

    # Determin header along yaxis
    header_y = ["Preselection", "Flavor", "Sign", "nJet", "mll", "met_Et", "met_EtSign"]
    
    pre = []
    flavor = []
    sign = []
    jet = []
    mll = []
    met_Et = []
    met_EtSign = []

  
    #for x in range(len(samp)):
        #if samp[x] in pc.l_bkg
 

    for r in reg:
        
        print " "
        print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
        print " " 
        print "Running on region: ", r
        print " "
        print "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
        print " "

        
        # MC 
        if len(samp_bkg) > 0:
            header =[x for x in samp_bkg]
            header_x = sort_headerx(header, "bkg")
            
            for elm in header_x: 
                pre.append(float(pc.d_cutflow[period][elm][r]["Preselection"]))
                flavor.append(float(pc.d_cutflow[period][elm][r]["Flavor"]))
                sign.append(float(pc.d_cutflow[period][elm][r]["Sign"]))
                jet.append(float(pc.d_cutflow[period][elm][r]["nJet"]))
                mll.append(float(pc.d_cutflow[period][elm][r]["mll"]))
                met_Et.append(float(pc.d_cutflow[period][elm][r]["met_Et"]))
                met_EtSign.append(float(pc.d_cutflow[period][elm][r]["met_EtSign"]))
            
            
            # Adding TotalMC to list
            header_x = header_x + ["TotalMC"]
            pre.append(sum(pre))
            flavor.append(sum(flavor))
            sign.append(sum(sign))
            jet.append(sum(jet))
            mll.append(sum(mll))
            met_Et.append(sum(met_Et))
            met_EtSign.append(sum(met_EtSign))
            
            # Adding percent decrese from each cut
            calculate_percent_decrease(header_x)
            header_x = header_x + ["% decrease"]
            
            
            tableMC = open(output_path_tables + "/table_MC" + "_" + r + "_" + period +".txt", "w+")
            
            x_format_h = "{:15}" + (len(header_x))* "{:^16}"
            x_format = "{:15}" + (len(header_x))* "{:>16}"
            border = "-" *(len(header_x)+1)*16
            
        
            # Print to terminal
        
                
            # print " "
            
            # print x_format.format(r, *header_x)
            # print border
            # print x_format.format(header_y[0], *pre)
            # print x_format.format(header_y[1], *flavor)
            # print x_format.format(header_y[2], *sign)
            # print x_format.format(header_y[3], *jet)
            # print x_format.format(header_y[4], *mll)
            # print x_format.format(header_y[5], *met_Et)
            # print x_format.format(header_y[6], *met_EtSign)
        
            # print " "
        

            # Print to file

            print >> tableMC,  x_format.format(r , *header_x)
            print >> tableMC, border
            print >> tableMC, x_format.format(header_y[0], *pre)
            print >> tableMC, x_format.format(header_y[1], *flavor)
            print >> tableMC, x_format.format(header_y[2], *sign)
            print >> tableMC, x_format.format(header_y[3], *jet)
            print >> tableMC, x_format.format(header_y[4], *mll)
            print >> tableMC, x_format.format(header_y[5], *met_Et)
            print >> tableMC, x_format.format(header_y[6], *met_EtSign)
        
        
            tableMC.close()
            
            pre[:] = []
            flavor[:] = []
            sign[:] = []
            jet[:] = []
            mll[:] = []
            met_Et[:] = []
            met_EtSign[:] = []
            
            header[:] = []
            header_x[:] = []
        #"""

        #Data

        if len(samp_data) > 0:
            #print "Yello"

            header =[x for x in samp_data]
            header_x = sort_headerx(header, "data")
            
            for elm in header_x: 
        
                pre.append(float(pc.d_cutflow[period][elm][r]["Preselection"]))
                flavor.append(float(pc.d_cutflow[period][elm][r]["Flavor"]))
                sign.append(float(pc.d_cutflow[period][elm][r]["Sign"]))
                jet.append(float(pc.d_cutflow[period][elm][r]["nJet"]))
                mll.append(float(pc.d_cutflow[period][elm][r]["mll"]))
                met_Et.append(float(pc.d_cutflow[period][elm][r]["met_Et"]))
                met_EtSign.append(float(pc.d_cutflow[period][elm][r]["met_EtSign"]))

        
            tableData = open(output_path_tables + "/table_Data" + "_" + r + "_" + period +".txt", "w+")
            
            x_format_h = "{:15}" + (len(header_x))* "{:^16}"
            x_format = "{:15}" + (len(header_x))* "{:>16}"
            border = "-" *(len(header_x)+1)*16
            
            
            # Print to terminal
            
            # print " "
        
            # print x_format.format(r, *header_x)
            # print border
            # print x_format.format(header_y[0], *pre)
            # print x_format.format(header_y[1], *flavor)
            # print x_format.format(header_y[2], *sign)
            # print x_format.format(header_y[3], *jet)
            # print x_format.format(header_y[4], *mll)
            # print x_format.format(header_y[5], *met_Et)
            # print x_format.format(header_y[6], *met_EtSign)
            
            # print " "
            #"""
            # Print to file
            
            print >> tableData,  x_format.format(r , *header_x)
            print >> tableData, border
            print >> tableData, x_format.format(header_y[0], *pre)
            print >> tableData, x_format.format(header_y[1], *flavor)
            print >> tableData, x_format.format(header_y[2], *sign)
            print >> tableData, x_format.format(header_y[3], *jet)
            print >> tableData, x_format.format(header_y[4], *mll)
            print >> tableData, x_format.format(header_y[5], *met_Et)
            print >> tableData, x_format.format(header_y[6], *met_EtSign)
        
            
            tableData.close()

            pre[:] = []
            flavor[:] = []
            sign[:] = []
            jet[:] = []
            mll[:] = []
            met_Et[:] = []
            met_EtSign[:] = []
            
            header[:] = []
            header_x[:] = []


        #Signal

        if len(samp_signal) > 0:

            header_C1C1_SlepSnu = [x for x in samp_signal if x[0:12] == "C1C1_SlepSnu"]
            header_C1C1_WW = [x for x in samp_signal if x[0:7] == "C1C1_WW"]
            header_SlepSlep = [x for x in samp_signal if x[0:8] == "SlepSlep"]

            header_x_C1C1_SlepSnu = sort_headerx(header_C1C1_SlepSnu, "signal")
            header_x_C1C1_WW = sort_headerx(header_C1C1_WW, "signal")
            header_x_SlepSlep = sort_headerx(header_SlepSlep, "signal")
            

            # C1C1_SlepSnu
            tableSignal = open(output_path_tables + "/table_Signal_C1C1_SlepSnu" + "_" + r + "_" + period +".txt", "w+")
            for elm in header_x_C1C1_SlepSnu:

                pre.append(float(pc.d_cutflow[period][elm][r]["Preselection"]))
                flavor.append(float(pc.d_cutflow[period][elm][r]["Flavor"]))
                sign.append(float(pc.d_cutflow[period][elm][r]["Sign"]))
                jet.append(float(pc.d_cutflow[period][elm][r]["nJet"]))
                mll.append(float(pc.d_cutflow[period][elm][r]["mll"]))
                met_Et.append(float(pc.d_cutflow[period][elm][r]["met_Et"]))
                met_EtSign.append(float(pc.d_cutflow[period][elm][r]["met_EtSign"]))
            

            x_format_h = "{:15}" + (len(header_x_C1C1_SlepSnu)+1)* "{:^28}"
            x_format = "{:15}" + (len(header_x_C1C1_SlepSnu))* "{:>28}"
            border = "-" *(len(header_x_C1C1_SlepSnu)+1)*28
            
            
            # print " "
            # print x_format.format(r, *header_x)
            # print border
            # print x_format.format(header_y[0], *pre)
            # print x_format.format(header_y[1], *flavor)
            # print x_format.format(header_y[2], *sign)
            # print x_format.format(header_y[3], *jet)
            # print x_format.format(header_y[4], *mll)
            # print x_format.format(header_y[5], *met_Et)
            # print x_format.format(header_y[6], *met_EtSign)
            # print " " 
            
           
            # Print to file
            #"""
            print >> tableSignal,  x_format.format(r , *header_x_C1C1_SlepSnu)
            print >> tableSignal, border
            print >> tableSignal, x_format.format(header_y[0], *pre)
            print >> tableSignal, x_format.format(header_y[1], *flavor)
            print >> tableSignal, x_format.format(header_y[2], *sign)
            print >> tableSignal, x_format.format(header_y[3], *jet)
            print >> tableSignal, x_format.format(header_y[4], *mll)
            print >> tableSignal, x_format.format(header_y[5], *met_Et)
            print >> tableSignal, x_format.format(header_y[6], *met_EtSign)
            #"""

            pre[:] = []
            flavor[:] = []
            sign[:] = []
            jet[:] = []
            mll[:] = []
            met_Et[:] = []
            met_EtSign[:] = []


            tableSignal.close()


            # C1C1_WW
            tableSignal = open(output_path_tables + "/table_Signal_C1C1_WW" + "_" + r + "_" + period +".txt", "w+")
            for elm in header_x_C1C1_WW:

                pre.append(float(pc.d_cutflow[period][elm][r]["Preselection"]))
                flavor.append(float(pc.d_cutflow[period][elm][r]["Flavor"]))
                sign.append(float(pc.d_cutflow[period][elm][r]["Sign"]))
                jet.append(float(pc.d_cutflow[period][elm][r]["nJet"]))
                mll.append(float(pc.d_cutflow[period][elm][r]["mll"]))
                met_Et.append(float(pc.d_cutflow[period][elm][r]["met_Et"]))
                met_EtSign.append(float(pc.d_cutflow[period][elm][r]["met_EtSign"]))
            

            x_format_h = "{:15}" + (len(header_x_C1C1_WW)+1)* "{:^28}"
            x_format = "{:15}" + (len(header_x_C1C1_WW))* "{:>28}"
            border = "-" *(len(header_x_C1C1_WW)+1)*28
            
            
            # print " "
            # print x_format.format(r, *header_x_C1C1_WW)
            # print border
            # print x_format.format(header_y[0], *pre)
            # print x_format.format(header_y[1], *flavor)
            # print x_format.format(header_y[2], *sign)
            # print x_format.format(header_y[3], *jet)
            # print x_format.format(header_y[4], *mll)
            # print x_format.format(header_y[5], *met_Et)
            # print x_format.format(header_y[6], *met_EtSign)
            # print " " 
            
           
            # Print to file
            #"""
            print >> tableSignal,  x_format.format(r , *header_x_C1C1_WW)
            print >> tableSignal, border
            print >> tableSignal, x_format.format(header_y[0], *pre)
            print >> tableSignal, x_format.format(header_y[1], *flavor)
            print >> tableSignal, x_format.format(header_y[2], *sign)
            print >> tableSignal, x_format.format(header_y[3], *jet)
            print >> tableSignal, x_format.format(header_y[4], *mll)
            print >> tableSignal, x_format.format(header_y[5], *met_Et)
            print >> tableSignal, x_format.format(header_y[6], *met_EtSign)
            #"""

            pre[:] = []
            flavor[:] = []
            sign[:] = []
            jet[:] = []
            mll[:] = []
            met_Et[:] = []
            met_EtSign[:] = []
                
            tableSignal.close()


            # SlepSlep
            tableSignal = open(output_path_tables + "/table_Signal_SlepSlep" + "_" + r + "_" + period +".txt", "w+")
            for elm in header_x_SlepSlep:

                pre.append(float(pc.d_cutflow[period][elm][r]["Preselection"]))
                flavor.append(float(pc.d_cutflow[period][elm][r]["Flavor"]))
                sign.append(float(pc.d_cutflow[period][elm][r]["Sign"]))
                jet.append(float(pc.d_cutflow[period][elm][r]["nJet"]))
                mll.append(float(pc.d_cutflow[period][elm][r]["mll"]))
                met_Et.append(float(pc.d_cutflow[period][elm][r]["met_Et"]))
                met_EtSign.append(float(pc.d_cutflow[period][elm][r]["met_EtSign"]))
            

            x_format_h = "{:15}" + (len(header_x_SlepSlep)+1)* "{:^28}"
            x_format = "{:15}" + (len(header_x_SlepSlep))* "{:>28}"
            border = "-" *(len(header_x_SlepSlep)+1)*28
            
            
            # print " "
            # print x_format.format(r, *header_x_SlepSlep)
            # print border
            # print x_format.format(header_y[0], *pre)
            # print x_format.format(header_y[1], *flavor)
            # print x_format.format(header_y[2], *sign)
            # print x_format.format(header_y[3], *jet)
            # print x_format.format(header_y[4], *mll)
            # print x_format.format(header_y[5], *met_Et)
            # print x_format.format(header_y[6], *met_EtSign)
            # print " " 
            
           
            # Print to file
            #"""
            print >> tableSignal,  x_format.format(r , *header_x_SlepSlep)
            print >> tableSignal, border
            print >> tableSignal, x_format.format(header_y[0], *pre)
            print >> tableSignal, x_format.format(header_y[1], *flavor)
            print >> tableSignal, x_format.format(header_y[2], *sign)
            print >> tableSignal, x_format.format(header_y[3], *jet)
            print >> tableSignal, x_format.format(header_y[4], *mll)
            print >> tableSignal, x_format.format(header_y[5], *met_Et)
            print >> tableSignal, x_format.format(header_y[6], *met_EtSign)
            #"""

            pre[:] = []
            flavor[:] = []
            sign[:] = []
            jet[:] = []
            mll[:] = []
            met_Et[:] = []
            met_EtSign[:] = []
                
            tableSignal.close()

                
    
    return None 



def make_table(logfile_path, output_path_tables, ap):
    """
    Function that takes input from HistogramMaker.py and calls upon necessary functions to make tables.

    Input variables:
    - logfile_path  : path to where the logfile can be found and where the tables are saved
    - regoins       : regions to create tables for
    - plot_MC       : bool used to determin if to make table for MC
    - plot_data     : bool used to determin if to make table for data
    - plot_signal   : bool used to determin if to make table for signal(s)

    Output variables: 
    - None
    """

 
    """
    if os.path.exists(save_path_Tables):
        print "The folder Tables already exists"
        user_input = raw_input("Do you want to overwrite existing files in Tables foler? y/n: ")

        if user_input == "y":
            print "Program will continue to run"
            
        if user_input == "n":
            print "Program exit not to overwrite files in folder Tables"
            sys.exit(1)
    
    else:
        try:  
            os.makedirs(save_path_Tables)

        except OSError:  
            print ("Creation of the directory %s failed" % save_path_Tables)
            sys.exit(1)
        else:  
            print ("Successfully created the directory %s" % save_path_Tables)
    """

    # Read in logfile
    read_logfile(logfile_path)

    if ap == True: 
        pc.d_cutflow["ap"] = {}
        for period in pc.d_cutflow.keys():
            if period != "ap":

                for samp in pc.d_cutflow[period].keys():
                    if samp not in pc.d_cutflow["ap"].keys():
                        pc.d_cutflow["ap"][samp] = {}
                    
                    for reg in pc.d_cutflow[period][samp].keys():
                        if reg not in pc.d_cutflow["ap"][samp].keys():
                            pc.d_cutflow["ap"][samp][reg] = {}

                        for var in pc.d_cutflow[period][samp][reg].keys():
                            #print period, samp, reg, var
                            try:
                                pc.d_cutflow["ap"][samp][reg][var] += pc.d_cutflow[period][samp][reg][var]
                            except KeyError:
                                pc.d_cutflow["ap"][samp][reg][var] = pc.d_cutflow[period][samp][reg][var]
                            #print pc.d_cutflow[period][samp][reg][var]

        #print pc.d_cutflow["ap"]['C1C1_SlepSnu_950p0_150p0']['CR-top']
        #print pc.d_cutflow["18"]['C1C1_SlepSnu_950p0_150p0']['CR-top']
        #print pc.d_cutflow["17"]['C1C1_SlepSnu_950p0_150p0']['CR-top']
        #print pc.d_cutflow["15-16"]['C1C1_SlepSnu_950p0_150p0']['CR-top']
        
        write_table(output_path_tables, "ap")
        #print pc.d_cutflow["ap"].keys()

    if ap == False:
        periods = pc.d_cutflow.keys()
        #print periods
        
        # Make table
        for p in periods:
            write_table(output_path_tables, p)
 

    
    
    return None


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
    print "This program contains functions used by HistogramMaker.py to make tables. Use HistogramMaker.py to access these functions"
    print " "

# If run as a main program - end
#==================================================
