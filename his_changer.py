original = [] #list for storing original pdb data.
his = [] #list fore storing atoms included by His residues.
hisresnum = [] #list for recording residue number of His derivative.
hissp = [] #list for recording spiecies of His residues.
#preparing lists

pdbname = input("Please enter your pdb file name.\n")
pdb = open(pdbname, "r")
#open the pdb file.

cnt = -1 #set variable for count.
for i in pdb:
    original.append(i)
    line = i.split()
    if line[0] == "ATOM" and line[2] == "N" and line[3] == "HIS":
        hisresnum.append(line[5])
        cnt += 1
        his.append([])
        his[cnt].append(line)
    elif line[0] == "ATOM" and line[3] == "HIS":
        his[cnt].append(line)
    else:
        pass
#making list original & his & hisresnum.

print(his[1][1][1])

for j in range(len(his)):
    if len(his[j]) == 18:
        hissp.append("HIP")
    elif his[j][16][2] == "HD1":
        hissp.append("HID")
    elif his[j][16][2] == "HE2":
        hissp.append("HIE")
#his discriminating.

print(hissp)

hisdict = dict(zip(hisresnum, hissp))
#make dictionary

cnt2 = 0
for k in original:
    line2 = k.split()
    if len(line2) < 6:
        pass
    elif line2[0] == "ATOM" and line2[3] == "HIS":
        rep = hisdict[line2[5]]
        print(rep)
        original[cnt2] = original[cnt2].replace("HIS", rep)
        print(original[cnt2])
    else:
        pass
    cnt2 += 1
#replacing "HIS" into more detail species.

pdb.close()
outfilename = input("Please enter name of output file\n")
outfile = open(outfilename, "w")
outfile.write("".join(original))
outfile.close()