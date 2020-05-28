import periodictable as pt
import sys

coordinate = []
rootsection = []
options = []
writtendata = []

grrmoutputfilename = input("Please enter name of GRRM output file.\n")
grrmoutputfile = open(grrmoutputfilename, "r")
#open the output file of GRRM.

cnt = 0

for i in grrmoutputfile:
    line = i.split()
    if len(line) == 0:
        pass
    elif line[0] == "#" and line[1] == "ITR.":
        coordinate = []
        for j in grrmoutputfile:
            line2 = j.split()
            if line2[0] == "Item":
                break
            coordinate.append(j)
    elif line[0] == "The" and line[1] == "structure" and line[2] == "is" and "dissociating":
        print("Geometry optimization might be failed\n")
    else:
        pass

grrmoutputfile.close()
#close the GRRM output file.

whetherhaveornot = input("Do you have GRRM input file of calculation resulting log file you presented?\nyes or no\n")
print(whetherhaveornot)

if whetherhaveornot == "Yes" or whetherhaveornot == "yes" or whetherhaveornot == "Y" or whetherhaveornot == "y":
    grrminputfilename = input("Please enter GRRM input file name which you used.\n")
    grrminputfile = open(grrminputfilename, "r")
    for i in grrminputfile:
        line = i.split()
        if len(line) == 0:
            rootsection.append(i)
        elif line[0] in pt.ptable:
            break
        else:
            rootsection.append(i)
    for i in grrminputfile:
        line = i.split()
        if len(line) == 0:
            options.append(i)
        elif line[0] == "Options":
            options.append(i)
            for j in grrminputfile:
                options.append(j)
        else:
            pass
    grrminputfile.close()
elif whetherhaveornot == "No" or whetherhaveornot == "no" or whetherhaveornot == "N" or whetherhaveornot == "n":
    print("I see. I'll write root section and option section simply.\n")
    rootsection.append("# MIN/B3LYP/6-31+G(D)\n\n0 1\n")
    options.append("Options\nGauProc = 4\n\n")
else:
    print("Error! Please use this module again!")
    sys.exit()

newinputfilename = input("Please enter file name of new inputfile.\n")
newinputfile = open(newinputfilename, "w")
for i in rootsection:
    newinputfile.write(i)
for i in coordinate:
    newinputfile.write(i)
for i in options:
    newinputfile.write(i)
newinputfile.close()