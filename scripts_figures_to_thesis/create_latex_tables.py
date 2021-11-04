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

parser.add_argument("-i", "--iso", 
                    type=str,
                    )

# parser.add_argument("-of", "--output_file",
#                     type=str, 
#                     )

# parser.add_argument("-type", "--type_of_figure", 
#                     type=str)

# parser.add_argument("-var", "--variables",
#                     type=str, 
#                     nargs="+",
#                     )

# parser.add_argument("-r", "--region", 
#                     type=str, 
#                     )

args = parser.parse_args()

file_list = [x.replace(".txt", "") for x in args.file_name]
folder = args.folder
iso = args.iso

inpath = "/Users/helenpersson/Documents/Master/results/"
outpath  = "/Users/helenpersson/Documents/Master/created_tables/"


for f in file_list:
    type = f.split("_")[2]
    i = 0
    for fold in folder:
        if iso:
            i = iso

        #print i

        infile = open(inpath + fold + "/" + f + ".txt", "r")
        outfile = open(outpath + f + "_iso" + str(i) + ".tex", "w+")

        line_count = 0
        for line in infile.readlines():
            if line_count == 0:
                l = line.replace("% d", "\%d").split()
                #print l
                outfile.write("\\begin{table}[h]"+ "\n")
                outfile.write("\\centering"+ "\n") 
                outfile.write("\\caption{Cutflow for" + l[0] + " " + type + "iso "+str(i) +  ".}"+ "\n")
                outfile.write("\\label{tab:events_" + l[0] + "_" + type +"iso"+str(i) + "}"+ "\n")
                outfile.write("\\renewcommand{\\arraystretch}{1.5}"+ "\n")
                
                num_of_elements_x = len(l)
                c_count = "c" * num_of_elements_x

                outfile.write("\\begin{tabular}{" + c_count + "}"+ "\n")
                outfile.write("    \\toprule"+ "\n")
                
                header = ""
                for elm in range(num_of_elements_x):
                    if elm != (num_of_elements_x -1):
                        header += l[elm].replace("_", "\\_") + "&"
                    else: 
                        header += l[elm].replace("_", "\\_") + "\\\\"

                outfile.write(header+ "\n")
                outfile.write("\\midrule"+ "\n")
                outfile.write("\\midrule"+ "\n")

            if line_count != 0 and line_count != 1:
                
                l = line.split()
                #print l[0]
                num_of_elm = len(l)

                inline = ""

                for k in range(num_of_elm):
                    if k != (num_of_elm - 1):
                        inline += l[k].replace("_", "\\_") + "&"
                    else: 
                        inline += l[k].replace("_", "\\_") + "\\\\"

                #print inline
                outfile.write(inline+ "\n")


                
            if line_count == 8:
                #print "hello"
                #outfile.write("test")
                outfile.write("\\bottomrule"+ "\n")
                outfile.write("\\end{tabular}"+ "\n")
                outfile.write("\\end{table}"+ "\n")
                

            

            line_count +=1
    


        outfile.close()
        infile.close()

        i += 1



"""
python create_latex_tables.py -f 2020-04-21_13-14-40 -fn table_Signal_SlepSlep_SR-DF-0J_ap

"""
