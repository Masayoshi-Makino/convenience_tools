pdbfilename = input("Please enter the file name you want to analyse.\n")
inpfile = open(pdbfilename, "r")
seq = []
oneseq = []
wat = 18.02
status = []
cnt = 0
charge = 0
mw = 0
for i in inpfile:
    line = i.split()
    if line[0] == "ATOM" and line[3] == "GLY" and line[2] == "CA":
        mw = mw + 75.07 - wat
        seq.append("GLY")
        oneseq.append("G")
    elif line[0] == "ATOM" and line[3] == "ALA" and line[2] == "CA":
        mw = mw + 89.09 - wat
        seq.append("ALA")
        oneseq.append("A")
    elif line[0] == "ATOM" and line[3] == "VAL" and line[2] == "CA":
        mw = mw + 117.15 - wat
        seq.append("VAL")
        oneseq.append("V")
    elif line[0] == "ATOM" and line[3] == "LEU" and line[2] == "CA":
        mw = mw + 131.16 - wat
        seq.append("LEU")
        oneseq.append("L")
    elif line[0] == "ATOM" and line[3] == "ILE" and line[2] == "CA":
        mw = mw + 131.16 - wat
        seq.append("ILE")
        oneseq.append("I")
    elif line[0] == "ATOM" and line[3] == "PHE" and line[2] == "CA":
        mw = mw + 165.19 - wat
        seq.append("PHE")
        oneseq.append("F")
    elif line[0] == "ATOM" and line[3] == "TRP" and line[2] == "CA":
        mw = mw + 204.21 - wat
        seq.append("TRP")
        oneseq.append("W")
    elif line[0] == "ATOM" and line[3] == "PRO" and line[2] == "CA":
        mw = mw + 115.13 - wat
        seq.append("PRO")
        oneseq.append("P")
    elif line[0] == "ATOM" and line[3] == "MET" and line[2] == "CA":
        mw = mw + 149.21 - wat
        seq.append("MET")
        oneseq.append("M")
    elif line[0] == "ATOM" and line[3] == "CYS" and line[2] == "CA":
        mw = mw + 121.16 - wat
        seq.append("CYS")
        oneseq.append("C")
    elif line[0] == "ATOM" and line[3] == "GLN" and line[2] == "CA":
        mw = mw + 146.15 - wat
        seq.append("GLN")
        oneseq.append("Q")
    elif line[0] == "ATOM" and line[3] == "ASN" and line[2] == "CA":
        mw = mw + 132.12 - wat
        seq.append("ASN")
        oneseq.append("N")
    elif line[0] == "ATOM" and line[3] == "SER" and line[2] == "CA":
        mw = mw + 105.09 - wat
        seq.append("SER")
        oneseq.append("S")
    elif line[0] == "ATOM" and line[3] == "THR" and line[2] == "CA":
        mw = mw + 119.12 - wat
        seq.append("THR")
        oneseq.append("T")
    elif line[0] == "ATOM" and line[3] == "TYR" and line[2] == "CA":
        mw = mw + 181.19 - wat
        seq.append("TYR")
        oneseq.append("Y")
    elif line[0] == "ATOM" and line[3] == "GLU" and line[2] == "CA":
        mw = mw + 147.13 - wat
        charge -= 1
        seq.append("GLU")
        oneseq.append("E")
    elif line[0] == "ATOM" and line[3] == "ASP" and line[2] == "CA":
        mw = mw + 133.10 - wat
        charge -= 1
        seq.append("ASP")
        oneseq.append("D")
    elif line[0] == "ATOM" and line[3] == "HIS" and line[2] == "CA":
        mw = mw + 155.16 - wat
        seq.append("HIS")
        oneseq.append("H")
    elif line[0] == "ATOM" and line[3] == "LYS" and line[2] == "CA":
        mw = mw + 146.19 - wat
        charge += 1
        seq.append("LYS")
        oneseq.append("K")
    elif line[0] == "ATOM" and line[3] == "ARG" and line[2] == "CA":
        mw = mw + 174.21 - wat
        charge += 1
        seq.append("ARG")
        oneseq.append("R")
    elif line[0] == "ATOM" and line[3] == "HIP" and line[2] == "CA":
        mw = mw + 156.16 - wat
        charge += 1
        seq.append("HIS")
        oneseq.append("H")
    elif line[0] == "ATOM" and line[3] == "CA" and line[2] == "CA":
        charge += 2
    if line[0] == "END":
        mw = mw + wat
        status.append(charge)
        status.append(mw)
        print("Total charge of this protein is {}\n".format(status[0]))
        print("Moleculer weight of this protein is {}\n".format(status[1]))

inpfile.close()
outfilename = input("Please enter output file name\n")
outfile = open(outfilename, "w")
outfile.write("Total charge of this protein is {}\n".format(status[0]))
outfile.write("Moleculer weight of this protein is {}\n".format(status[1]))
outfile.write("Sequene (Three letters)\n")
outfile.write("\n".join(seq))
outfile.write("Sequence (One letter)\n" + "\n")
outfile.write("".join(oneseq))
print("Total charge of this protein is {}\n".format(charge))
print("Moleculer weight of this protein is {}\n".format(mw))
outfile.close()