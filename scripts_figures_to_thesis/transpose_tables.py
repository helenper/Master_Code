import argparse

parser = argparse.ArgumentParser(description='Create figures in tex')

parser.add_argument("-f", "--folder", 
                    type=str, 
                    )

parser.add_argument("-fn", "--file", 
                    type=str, 
                    nargs="+",
                    )

parser.add_argument("-i", "--iso",
                    type=str)


args = parser.parse_args()

fold = args.folder
file_list = [x.replace(".tex", "") for x in args.file]
iso = args.iso

inpath = "/Users/Documents/Master/created_tables/"
outpath = "/Users/Documents/Master/created_tables/longtables/"


for f in file_list:
    print f
    try:
        #infile = open(inpath + f + "_iso" +str(iso) + ".tex", "r")
        infile = open(inpath + f +  ".tex", "r")
    except:
        print "Help", inpath
        continue
    outfile = open(outpath + f +  ".tex", "w+")
    outfile.write("\\setlength\\LTleft{-2.5cm}")
    outfile.write("\\begin{longtable}{cccccccc}")
    print outpath, f , "iso", iso

    linecounter = 0
    for line in infile.readlines():
        if 2 <= linecounter <= 3: 
            outfile.write(line + "\\\\")
        if linecounter == 6:
            outfile.write(line + "\\\\")
            outfile.write("&Preselection&Flavor&Sign&nJet&mll&met\\_Et&met\\_EtSign\\\\")
            outfile.write("\\midrule")
            outfile.write("\\midrule")
            outfile.write("\endfirsthead")

            outfile.write("cont.&Preselection&Flavor&Sign&nJet&mll&met\\_Et&met\\_EtSign\\\\") 
            outfile.write("\\midrule")
            outfile.write("\\midrule")
            outfile.write("\\endhead")

            outfile.write("\\bottomrule")
            outfile.write("\\endfoot")

            outfile.write("\\bottomrule")
            outfile.write("\\endlastfoot")

        if linecounter == 7: 
            signal_samples = line.replace("\\", "").split("&")
        if linecounter == 10:
            pre = line.replace("\\", "").split("&")
        if linecounter == 11: 
            flav = line.replace("\\", "").split("&")
        if linecounter == 12: 
            sign = line.replace("\\", "").split("&")
        if linecounter == 13: 
            nJet = line.replace("\\", "").split("&")
        if linecounter == 14: 
            mll = line.replace("\\", "").split("&")
        if linecounter == 15: 
            met = line.replace("\\", "").split("&")
        if linecounter == 16: 
            met_sign = line.replace("\\", "").split("&")
        
        if linecounter == 17: 
            for i in range(len(pre)):
                print len(signal_samples), len(pre), len(flav), len(sign), len(nJet), len(mll), len(met), len(met_sign)
                print f
                outfile.write(signal_samples[i].replace("_","\\_")+ "&"+ pre[i]+"&"+flav[i]+"&"+sign[i]+"&"+nJet[i]+"&"+mll[i]+"&"+met[i].replace("_","\\_")+"&"+met_sign[i].replace("_","\\_")+"\\\\ \n")
                #outfile.write("\\n
            outfile.write(line)

        if linecounter > 17:
            #outfile.write(line)
            outfile.write("\\end{longtable}")
        linecounter += 1

    infile.close()
    outfile.close()
