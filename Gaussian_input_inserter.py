from periodictable import ptable

inpfilename = input("Enter the input file name.\n")
inp = open(inpfilename, "r")
# Opening file. correct

coordinate = []
connectivity = []
lista = []
listb = []
# Making lists for data. correct

bondorder = ["1.0", "1.5", "2.0", "2.5", "3.0"]

def inpdata():
    a = input("Input 1st data.(before)\n")
    b = input("Input 2nd data.(after)\n")
    lista.append(int(a))
    listb.append(int(b))

iterationnum = input("How many exchanges do you want to?\n")
cnt = 1
while cnt <= int(iterationnum):
    inpdata()
    cnt += 1
# input before & after correct

atomnum = input("How many atoms in your input file?\n")
for i in inp:
    if i == "\n":
        pass
    else:
        line = i.split()
        print(line[0])
        if line[0] in ptable:
            coordinate.append(line)
        elif int(line[0]) <= int(atomnum):
            connectivity.append(line)
        else:
            pass
# Making coordinate list & connectivity list. correct

for j in range(len(lista)):
    indexorigin = lista[j] - 1
    indexalter = listb[j] - 1 
    origin = coordinate[indexorigin]
    coordinate.insert(indexalter, origin)
    coordinate.pop(lista[j])
    #coordinate insertion correct
    origincon = connectivity[indexorigin]
    connectivity.insert(indexalter, origincon)
    connectivity.pop(lista[j])
    for k in range(len(connectivity)):
        index = 0
        for l in connectivity[k]:
            if l in bondorder:
                index += 1
            elif l == str(lista[j]):
                add = str(listb[j])
                print (connectivity[k][index])
                connectivity[k][index] = add
                index += 1
            elif int(l) <= lista[j] - 1 and int(l) >= listb[j]:
                add = str(int(l) + 1)
                connectivity[k][index] = add
                index += 1
            else:
                index += 1
        cnt += 1
    #change is succeeded.

inp.close()
print(coordinate)
print(connectivity)
for m in range(len(connectivity)):
    if type(connectivity[m]) == list:
        connectivity[m] = " ".join(connectivity[m])
        #connectivity
    cnt2 = 0
    for n in coordinate[m]:
        if coordinate[m][cnt2] in ptable:
            coordinate[m][cnt2] = coordinate[m][cnt2].center(3)
            cnt2 += 1
        elif cnt2 == 1:
            coordinate[m][cnt2] = coordinate[m][cnt2].rjust(27)
            cnt2 += 1
        else:
            coordinate[m][cnt2] = coordinate[m][cnt2].rjust(14)
            cnt2 += 1
    coordinate[m] = "".join(coordinate[m])

newfilename = input("Enter the new file name\n")
newfile = open(newfilename, "w")
newcoor = "\n".join(coordinate)
newfile.write(newcoor)
newfile.write("\n\n")
newconn = "\n".join(connectivity)
newfile.write(newconn)
newfile.write("\n\n")
newfile.close()