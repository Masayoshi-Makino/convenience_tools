deltaE = []
energy = []
filename = input("Please tell me the name of Gaussian output file.\n")
logfile = open(filename, "r")
for i in logfile:
    if "SCF Done:" in i:
        line = i.split()
        if line[1] == "Done:":
            energy.append(float(line[4]))

logfile.close()

newfilename = input("Please tell me new file made by this module.\n")
newfile = open(newfilename, "w")
for j in range(len(energy)-1):
    d = energy[j+1] - energy[j]
    deltaE.append(str(d))

print(deltaE)
output = "\n".join(deltaE)
newfile.write(output)
newfile.close()