from subprocess import *

# Signal not made in correct ntuple form

# Demo call from folder Master/Analyse
# call(["python", "scripts/RunSelector.py", "-b" "background wanted", "-p" "data period wanted", "-c" "cut wanted", "-s" "signals wanted"])


# data15-16

#call(["python", "scripts/RunSelector.py", "-b" "mc16a", "-p" "data15-16", "-c" "SR_SF_0J"]) #, "-s" "all"])
#call(["python", "scripts/RunSelector.py", "-b" "mc16a", "-p" "data15-16", "-c" "SR_SF_1J"]) #, "-s" "all"])
#call(["python", "scripts/RunSelector.py", "-b" "mc16a", "-p" "data15-16", "-c" "SR_DF_0J"]) #, "-s" "all"])
#call(["python", "scripts/RunSelector.py", "-b" "mc16a", "-p" "data15-16", "-c" "SR_DF_1J"]) #, "-s" "all"])

#call(["python", "scripts/RunSelector.py", "-b" "mc16a", "-p" "data15-16", "-c" "SR_SF_0J_ee"]) #,   "-s" "all"])
#call(["python", "scripts/RunSelector.py", "-b" "mc16a", "-p" "data15-16", "-c" "SR_SF_1J_ee"]) #,   "-s" "all"])
#call(["python", "scripts/RunSelector.py", "-b" "mc16a", "-p" "data15-16", "-c" "SR_SF_0J_mumu"]) #, "-s" "all"])
#call(["python", "scripts/RunSelector.py", "-b" "mc16a", "-p" "data15-16", "-c" "SR_SF_1J_mumu"]) #, "-s" "all"])


# data17

#call(["python", "scripts/RunSelector.py", "-b" "mc16cd", "-p" "data17", "-c" "SR_SF_0J"]) #, "-s" "all"])
#call(["python", "scripts/RunSelector.py", "-b" "mc16cd", "-p" "data17", "-c" "SR_SF_1J"]) #, "-s" "all"])


# data18

#call(["python", "scripts/RunSelector.py", "-b" "mc16e", "-p" "data18", "-c" "SR_SF_0J"]) #, "-s" "all"])
#call(["python", "scripts/RunSelector.py", "-b" "mc16e", "-p" "data18", "-c" "SR_SF_1J"]) #, "-s" "all"])





# Run bkg, data, signal
#call(["python", "scripts/RunSelector.py", "-iso", "0", "-p", "all", "-b", "-d", "-s"])
#call(["python", "scripts/RunSelector.py", "-iso", "1", "-p", "all", "-b", "-d", "-s"])
#call(["python", "scripts/RunSelector.py", "-iso", "2", "-p", "all", "-b", "-d", "-s"])
#call(["python", "scripts/RunSelector.py", "-iso", "3", "-p", "all", "-b", "-d", "-s"])

# Run fakes
call(["python", "scripts/RunSelector.py", "-iso", "0", "-p", "all", "-f"])
call(["python", "scripts/RunSelector.py", "-iso", "1", "-p", "all", "-f"])
call(["python", "scripts/RunSelector.py", "-iso", "2", "-p", "all", "-f"])
call(["python", "scripts/RunSelector.py", "-iso", "3", "-p", "all", "-f"])
