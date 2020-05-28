coordinate = []
writtendata = []

inpfilename = input("Please enter name of GRRM output file.\n")
inpfile = open(inpfilename, "r")
#open the output file of GRRM.

cnt = 0

for i in inpfile:
    line = i.split()
    if len(line) == 0:
        pass
    elif line[0] == "Optimized":
        for j in inpfile:
            line2 = j.split()
            if line2[0] == "ENERGY":
                break
            coordinate.append(line2)
    elif line[0] == "The" and line[1] == "structure" and line[2] == "is" and "dissociating":
        print("Geometry optimization might be failed\n")
    else:
        pass

inpfile.close()
#close the GRRM output file.

coorfilename = input("Please enter the name of new file containing coordinate extracted from GRRM output file.\n")
coorfile = open(coorfilename, "w")

coorfile.write("# /B3LYP/6-31+G\n")
coorfile.write("\n")
coorfile.write("Title section\n")
coorfile.write("\n")
coorfile.write("0 1\n")

cnt2 = 0
for i in coordinate:
    print(i)
    coorfile.write(coordinate[cnt2][0].center(3))
    coorfile.write(coordinate[cnt2][1].rjust(27))
    coorfile.write(coordinate[cnt2][2].rjust(19))
    coorfile.write(coordinate[cnt2][3].rjust(19))
    coorfile.write("\n")
    cnt2 += 1

coorfile.write("\n")
coorfile.close()