import periodictable as pt
gaussianfilename = input("Please enter the name of gaussian input and output file.\ne.g.) if jobfile name is aaa.gjf, enter the simply 'aaa'\n")
gaussianoutputfilename = gaussianfilename + ".out"
#read files.

atomlist = []
gcoordinate = []
#make lists.
chargeandmultiplicity = []

gaussianoutputfile = open(gaussianoutputfilename, "r")
cnt = 0
cntforatomlist = 0
for j in gaussianoutputfile:
    line2 = j.split()
    if len(line2) == 0:
        pass
    elif line2[0] == "Charge" and line2[3] == "Multiplicity" and cntforatomlist == 0:
        chargeandmultiplicity.append(line2[2])
        chargeandmultiplicity.append(line2[5])
        for k in gaussianoutputfile:
            line3 = k.split()
            if len(line3) == 0:
                break
            elif line3[0] == "Redundant":
                for l in gaussianoutputfile:
                    line4 = l.split(",")
                    line5 = l.split()
                    if line5[0] == "Recover":
                        break
                    else:
                        atomlist.append(line4[0])
                break
            else:
                atomlist.append(line3[0])
                print(line3)
        cntforatomlist += 1
    elif line2[0] == "Input" and line2[1] == "orientation:":
        gcoordinate = []
        for k in gaussianoutputfile:
            line2 = k.split()
            if line2[0] == "---------------------------------------------------------------------":
                cnt += 1
            elif cnt == 2:
                gcoordinate.append([line2[3],line2[4],line2[5]])
            if cnt == 3:
                cnt = 0
                break
    elif line2[0] == "Standard" and line2[1] == "orientation:":
        gcoordinate = []
        for k in gaussianoutputfile:
            line2 = k.split()
            if line2[0] == "---------------------------------------------------------------------":
                cnt += 1
            elif cnt == 2:
                gcoordinate.append([line2[3],line2[4],line2[5]])
            if cnt == 3:
                cnt = 0
                break
#read output file.

gaussianoutputfile.close()

newinputfilename = input("Please enter the filename of new input file.\n")
newinputfile = open(newinputfilename, "w")

newinputfile.write("# MIN/B3LYP/genecp\n\n")
newinputfile.write(chargeandmultiplicity[0])
newinputfile.write(" ")
newinputfile.write(chargeandmultiplicity[1])
newinputfile.write("\n")

print(atomlist)

for j in range(len(atomlist)):
    newinputfile.write(atomlist[j].center(3))
    newinputfile.write(gcoordinate[j][0].rjust(27))
    newinputfile.write(gcoordinate[j][1].rjust(14))
    newinputfile.write(gcoordinate[j][2].rjust(14))
    newinputfile.write("\n")
newinputfile.write("Options\nGauProc=6\nGauMEM=3000\n")
#write new file.
newinputfile.close()

newcshfilename = newinputfilename.strip(".com")
newcshfilename = newcshfilename + ".csh"
newcshfile = open(newcshfilename, "w")

newcshfile.write("""#!/bin/csh -f
#PBS -l select=1:ncpus=6:mpiprocs=1:ompthreads=6:jobtype=core
#PBS -l walltime=167:00:00

if ($?PBS_O_WORKDIR) then
  cd ${{{PBS_O_WORKDIR}}}
endif\n\n""")
name = newinputfilename.strip(".com")
newcshfile.write("set GRRMinp={}\n".format(name))
newcshfile.write("""setenv WORK /work/users/${{{LOGNAME}}}/grrm.$$
if ( ! -d ${{{WORK}}} ) mkdir ${{{WORK}}}
setenv GAUSS_SCRDIR ${{{WORK}}}

setenv LANG C
source /local/apl/lx/g09d01/g09/bsd/g09.login
setenv subgau g09grrm
setenv subchk formchk
setenv subgrr GRRM.out

set path=(/local/apl/lx/GRRM14 $path)
 
GRRMp ${{{GRRMinp}}} -h24\n""")
newcshfile.close()