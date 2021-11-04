

def customSortX(list_l):
    """
    Function for sorting the list used to determin the placement of hedings in the result table.
    """

    l_old = list_l
    l_new = []
    order = ['diboson', 
             'higgs', 
             'lowMassDY',
             'singleTop', 
             'topOther', 
             'triboson', 
             'ttbar', 
             'Vgamma', 
             'Wjets', 
             'Zjets', 
             'TotalMC', 
             '% decrease', 
             'data15-16' ]
    
    for elm in order:
        if elm in l_old:
            l_new.append(elm)
            l_old.remove(elm)
        if elm == "TotalMC" or elm == "% decrease":
            l_new.append(elm)
    
    if len(l_old)>0:
        for elm in l_old:
            l_new.append(elm)

    print l_new
            
    return l_new
        

def makeTable(dir_input, cut_string, path_name, background, data, signal):
    """
    Function that creates table out of cutlfow.
    """

    d = dir_input
    hx = d.keys() 
    header_x = customSortX(hx)
    header_y = ["Preselection", "Flavor", "Sign", "nJet", "mll", "met_Et", "met_EtSign"]

    pre = []
    flavor = []
    sign = []
    jet = []
    mll = []
    met_Et = []
    met_EtSign = []
            
    for elm in header_x:
        if elm in ['diboson', 'higgs', 'lowMassDY','singleTop', 'topOther', 'triboson', 'ttbar', 'Vgamma', 'Wjets', 'Zjets', 'data15-16']:
            if len(d[elm].keys()) == 7:
                for e in d[elm].keys():
                    if e == "preselection":
                        pre.append(float(d[elm][e]))
                        
                    elif e == "flavor":
                        flavor.append(float(d[elm][e]))
                        
                    elif e == "sign": 
                        sign.append(float(d[elm][e]))
                                      
                    elif e == "nJet":
                        jet.append(float(d[elm][e]))
                        
                    elif e == "mll":
                        mll.append(float(d[elm][e]))
                        
                    elif e == "met_Et":
                        met_Et.append(float(d[elm][e]))
                        
                    elif e == "met_EtSign":
                        met_EtSign.append(float(d[elm][e]))

            else:
                for e in header_y:
                    if e == "preselection":
                        pre.append("-")
                        
                    elif  e == "flavor":
                        flavor.append("-")
                        
                    elif  e == "sign": 
                        sign.append("-")
                        
                    elif e == "nJet":
                        jet.append("-")
                        
                    elif e == "mll":
                        mll.append("-")
                            
                    elif e == "met_Et":
                        met_Et.append("-")
                        
                    elif e == "met_EtSign":
                        met_EtSign.append("-")

        elif elm == "TotalMC":
            pre.append(sum(pre))
            flavor.append(sum(flavor))
            sign.append(sum(sign))
            jet.append(sum(jet))
            mll.append(sum(mll))
            met_Et.append(sum(met_Et))
            met_EtSign.append(sum(met_EtSign))

        elif elm == "% decrease":
            continue


        else:
            print "tesT"
            

    percent =[None]*7
    idx = header_x.index("TotalMC")

    if cut_string != "Preselection":
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


    # Print to terminal
    #"""
    x_format_h = "{:15}" + (len(header_x))* "{:^16}"
    x_format = "{:15}" + (len(header_x))* "{:>16}"
    border = "-" *(len(header_x)+1)*16

    print " "

    print x_format.format(cut_string, *header_x)
    print border
    print x_format.format(header_y[0], *pre)
    print x_format.format(header_y[1], *flavor)
    print x_format.format(header_y[2], *sign)
    print x_format.format(header_y[3], *jet)
    print x_format.format(header_y[4], *mll)
    print x_format.format(header_y[5], *met_Et)
    print x_format.format(header_y[6], *met_EtSign)
    #"""      

    
    #Write to file
    table_file = open(path_name + "/table.txt", "w+")
    str1 = x_format.format(cut_string, *header_x) + "\n"
    str2 = border + "\n"
    str3 = x_format.format(header_y[0], *pre)+ "\n"
    str4 = x_format.format(header_y[1], *flavor)+ "\n"
    str5 = x_format.format(header_y[2], *sign)+ "\n"
    str6 = x_format.format(header_y[3], *jet)+ "\n"
    str7 = x_format.format(header_y[4], *mll)+ "\n"
    str7 = x_format.format(header_y[5], *met_Et)+ "\n"
    str8 = x_format.format(header_y[6], *met_EtSign)+ "\n"

    table_file.write(str1)
    table_file.write(str2)
    table_file.write(str3)
    table_file.write(str4)
    table_file.write(str5)
    table_file.write(str6)
    table_file.write(str7)
    table_file.write(str8)

    table_file.close()

    return None 
