filename = input("Please enter file name which contain sequence of Protein\n")
inp = open(filename, "r")
out = []
sel = input("Which do you want to do?\nSelect below number.\n1.1 letter to 3 letter    2.3 letter to 1 letter")
if int(sel) == 1:
    print("On going. Please waiting for release!")

elif int(sel) == 2:
    for i in inp:
        threecode = i[:3]
        if threecode == "GLY":
            out.append("G")
        if threecode == "ALA":
            out.append("A")
        if threecode == "VAL":
            out.append("V")
        if threecode == "LEU":
            out.append("L")
        if threecode == "ILE":
            out.append("I")
        if threecode == "PRO":
            out.append("P")
        if threecode == "PHE":
            out.append("F")
        if threecode == "TRP":
            out.append("W")
        if threecode == "CYS":
            out.append("C")
        if threecode == "MET":
            out.append("M")
        if threecode == "SER":
            out.append("S")
        if threecode == "THR":
            out.append("T")
        if threecode == "TYR":
            out.append("Y")
        if threecode == "ASN":
            out.append("N")
        if threecode == "GLN":
            out.append("Q")
        if threecode == "ASP":
            out.append("D")
        if threecode == "GLU":
            out.append("E")
        if threecode == "LYS":
            out.append("K")
        if threecode == "ARG":
            out.append("R")
        if threecode == "HIS" or threecode == "HID" or threecode == "HIE" or threecode == "HIP":
            out.append("H")

else:
    print("Error!\n")

print(out)
newfilename = input("Please enter name of new file.\n")
newfile = open(newfilename, "w")
newfile.write("".join(out))