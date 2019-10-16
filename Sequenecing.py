seq = []
filename = input("Please tell me your PDB file name.\n")
pdb = open(filename, "r")
for i in pdb:
    line = i.split()
    if line[0] == "ATOM" and line[2] == "CA":
        seq.append(line[3])

print(seq)
pdb.close()
newfilename = input("Please tell me your NEW PDB file name.\n")
newfile = open(newfilename, "w")
newfile.write("\n".join(seq))