template = input("Enter the template sentence.\n")
out = []
yorn = input("Do you want to include template sentence in output file?\nyes/no\n")
if yorn == "yes" or yorn == "y":
    out.append(template)
    print("I've added template sentence to output file.\n")
elif yorn == "no" or yorn == "n":
    print("I see. I didn't add template sentence to output file.\n")

iterationnum = input("How many sentence do you want to make? (ex.template sentence)\n")
cnt = 1
while cnt <= int(iterationnum):
    print("Please tell me the word you want to change, and its alternative.\n")
    origin = input("original word\n")
    alt = input("alternative word\n")
    template2 = template.replace(origin, alt)
    print(template2)
    out.append(template2)
    cnt = cnt + 1

newfilename = input("Please enter new file name.\n")
newfile = open(newfilename, "w")
newfile.write("\n".join(out))
newfile.close()