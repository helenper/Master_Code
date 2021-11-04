# Program to craate tex files building up figures for master thesis


import argparse

parser = argparse.ArgumentParser(description='Create figures in tex')
parser.add_argument("-f", "--folder", 
                    type=str, 
                    nargs="+",
                    )

parser.add_argument("-fn", "--file_name",
                    type=str, 
                    nargs="+",
                    )

parser.add_argument("-of", "--output_file",
                    type=str, 
                    )

parser.add_argument("-type", "--type_of_figure", 
                    type=str)

parser.add_argument("-var", "--variables",
                    type=str, 
                    nargs="+",
                    )

parser.add_argument("-r", "--region", 
                    type=str, 
                    )

args = parser.parse_args()



folder_list = args.folder
file_list = [x.replace(".pdf", "") for x in args.file_name]
#output_file = args.output_file + ".tex"
type_of_figure = args.type_of_figure
var_list = args.variables
reg = args.region

if not var_list:
    var_list=["1"]

path = "/Users/helenpersson/Documents/Master/created_figures/"




for f in file_list:
    try:
        outputfile = open(path+f+".tex", "a+")
    except:
        outputfile = open(path+f+".tex", "w+")

    
    for var in var_list:    
        outputfile.write("\n")
        outputfile.write("\\begin{figure} \n")
        outputfile.write("\\centering \n")
        
        outputfile.write("\\advance\\leftskip-2cm \n")
        outputfile.write("\\advance\\rightskip-2cm \n")

        if type_of_figure == "4x4_significance":
            i = 0
            for folder in folder_list:
                outputfile.write("\\begin{subfigure}[b]{0.6\\textwidth} \n")
                outputfile.write("        \\includegraphics[width=\\textwidth]{../results/" + folder + "/"  + f +".pdf} \n")
                outputfile.write("        \\caption{Significance iso " + str(i)  + " } \n")
                outputfile.write("        \\label{fig:significance_iso_" + str(i) + "_" + f + "} \n")
                outputfile.write("\\end{subfigure} \n")
                #print i
                #outputfile.write("\\hfill \n")
                if i == 1:
                    #outputfile.write("\\hfill \n")
                    outputfile.write("\\\\ \n")
        
                i += 1

            name = f.replace("_", "\_")
            #print name
            outputfile.write("\\caption{Significance plot for " + name +"} \n")
            outputfile.write("\\label{fig:significance_" + f +"} \n")
            outputfile.write("\\end{figure} \n")
            outputfile.write("\n")
            outputfile.write("\n")
            
            

        if type_of_figure == "4x4_distribution":
            i = 0
            for folder in folder_list:
           
                outputfile.write("\\begin{subfigure}[b]{0.3\\textwidth} \n")
                outputfile.write("        \\includegraphics[width=\\textwidth]{../results/" + folder + "/Variables_separate/" + reg + "_" +var + "_" + f +".pdf} \n")
                outputfile.write("        \\caption{" + var + " iso " + str(i)  + " } \n")
                outputfile.write("        \\label{fig:" + var +"_iso_" + str(i) + "_" + f + "} \n")
                outputfile.write("\\end{subfigure} \n")
                #print i
                outputfile.write("\\hfill \n")
                if i == 1:
                    #outputfile.write("\\hfill \n")
                    outputfile.write("\\\\ \n")
        
                i += 1
            name = f.replace("ap_plot_bkg_data_sign_", "").replace("_", "\_")
            #print name
            outputfile.write("\\caption{" + var + " plot for " + name +"} \n")
            outputfile.write("\\label{fig:"+ var  + f +"} \n")
            outputfile.write("\\end{figure} \n")
            outputfile.write("\n")
            outputfile.write("\n")



           

        

        



"""
prompt$ python create_result_figures.py -f 2020-04-21_13-14-40 2020-04-21_13-16-57 2020-04-21_13-19-01 2020-04-21_13-20-22 -fn ap_plot_bkg_data_sign_SlepSlep_direct_90p0_1p0_SlepSlep_direct_90p0_30p0_SlepSlep_direct_100p0_50p0.pdf -of ../text/variables_figures -type 4x4_distribution -var leppt mll -r SR-SF-0J
"""
