Energy = []
Delta = []
filename = input("Please tell me name of file which you want to calculate.\n")
print(filename)
deta1 = open(filename, "r")
for line in deta1:
    E = line.split("\n")
    Energy.append(float(E[0]))

print(Energy)

deta1.close()
for i in range(len(Energy)-1):
    D = Energy[i+1] - Energy[i]
    Delta.append(D)

print(Delta)

path_w = input("Enter the path name where you want to make file.\n")
deta2 = open(path_w, "w")
for j in range(len(Delta)):
    deta2.write(str(Delta[j]))
    deta2.write("\n")

deta2.close()
