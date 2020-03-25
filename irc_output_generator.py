import periodictable as pt
elementlist = []
coordinatelist = []
energyabove = []
reactioncoordinate = []
energybelow = []
atomicnumberlist = []
orderedrc = []

logfilename = input("Please enter GRRM log file name.\n")
logfile = open(logfilename, "r")

cnt = 0
for i in logfile:
    line1 = i.split()
    if len(line1) == 0:
        pass
    elif line1[0] == "#" or line1[0] == ("INITIAL"):
        cnt2 = 0
        coordinatelist.append([])
        for j in logfile:
            line2 = j.split()
            coordinatelist[cnt].append([])
            if line2[0] == "ENERGY":
                energyabove.append(str(round(float(line2[2]), 10)))
                break
            coordinatelist[cnt][cnt2].append(str(round(float(line2[1]), 7)).ljust(9, "0"))
            coordinatelist[cnt][cnt2].append(str(round(float(line2[2]), 7)).ljust(9, "0"))
            coordinatelist[cnt][cnt2].append(str(round(float(line2[3]), 7)).ljust(9, "0"))
            if len(elementlist) < len(coordinatelist[cnt]):
                elementlist.append(line2[0])
            cnt2 += 1
        cnt += 1
    elif line1[0] == "Length" and len(reactioncoordinate) == 0:
        for j in logfile:
            line2 = j.split()
            if line2[0] == "Reverse":
                break
            reactioncoordinate.append(line2[0])
            energybelow.append(str(round(float(line2[1]), 10)))

logfile.close()

for i in energyabove:
    orderedrc.append(reactioncoordinate[energybelow.index(i)])

for i in elementlist:
    atomicnumberlist.append(str(pt.ptable.index(i) + 1))

for i in range(len(coordinatelist)):
    for k in range(len(atomicnumberlist)):
        if "-" in coordinatelist[i][k][0]:
            coordinatelist[i][k][0] = coordinatelist[i][k][0].ljust(10, "0")
        else:
            coordinatelist[i][k][0] = coordinatelist[i][k][0].ljust(9, "0")
        if "-" in coordinatelist[i][k][1]:
            coordinatelist[i][k][1] = coordinatelist[i][k][1].ljust(10, "0")
        else:
            coordinatelist[i][k][1] = coordinatelist[i][k][1].ljust(9, "0")
        if "-" in coordinatelist[i][k][2]:
            coordinatelist[i][k][2] = coordinatelist[i][k][2].ljust(10, "0")
        else:
            coordinatelist[i][k][2] = coordinatelist[i][k][2].ljust(9, "0")

print(atomicnumberlist)

goutputname = input("Please enter file name you make.\n")
goutput = open(goutputname, "w")

goutput.write("Entering Link 1\n\nIRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC\n\nIRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC\n")

cnt3 = 0
for i in coordinatelist:
    goutput.write("                          Input orientation:                          \n ---------------------------------------------------------------------\n Center     Atomic      Atomic             Coordinates (Angstroms)\n Number     Number       Type             X           Y           Z\n ---------------------------------------------------------------------\n")
    cnt4 = 0
    for k in range(len(atomicnumberlist)):
        goutput.write(str(cnt4 + 1).rjust(7))
        print(atomicnumberlist[cnt4])
        print(cnt4)
        goutput.write(atomicnumberlist[cnt4].rjust(12))
        goutput.write("0".rjust(13))
        goutput.write(coordinatelist[cnt3][cnt4][0].rjust(17))
        goutput.write(coordinatelist[cnt3][cnt4][1].rjust(13))
        goutput.write(coordinatelist[cnt3][cnt4][2].rjust(13) + "\n")
        cnt4 += 1
    goutput.write("---------------------------------------------------------------------\nSCF Done:  E(scf) =  ")
    goutput.write(energyabove[cnt3])
    goutput.write("\nIRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC\n")
    if cnt3 == 0:
        pass
    else:
        goutput.write("Pt")
        goutput.write(str(cnt3).rjust(3))
        goutput.write(" Step number   1 out of a maximum of  38\n")
        goutput.write("   NET REACTION COORDINATE UP TO THIS POINT =    {}\n\n".format(orderedrc[cnt3]))
    goutput.write("IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC-IRC\n")
    cnt3 += 1

goutput.write("\nNormal termination of Gaussian\n\n")
goutput.close()