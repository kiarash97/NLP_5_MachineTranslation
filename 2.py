nasr = open("nasr.txt",'r').read()
sher = open("sher.txt",'r').read()

def preProcessing(txt):
    txt = txt.replace("1","")
    txt = txt.replace("2", "")
    txt = txt.replace("3", "")
    txt = txt.replace("4", "")
    txt = txt.replace("5", "")
    txt = txt.replace("6", "")
    txt = txt.replace("7", "")
    txt = txt.replace("8", "")
    txt = txt.replace("9", "")
    txt = txt.replace("0", "")
    junkList = [".", "-", "]", "[", "،", "؛", ":", ")", "(", "!", "؟", "»", "«", "ْ"]
    for jnk in junkList:
        if jnk in txt:
            txt=txt.replace(jnk,"")
    txt = txt.strip()
    return txt
ghazals = sher.split("غزل شماره")[1:]
manighazals = nasr.split("غزل شماره")[1:]

lst_sher = []
lst_nasr = []
for i in range(495) :
    ghazals[i] = preProcessing(ghazals[i])
    manighazals[i] = preProcessing(manighazals[i])

    lst_sher.append(len(ghazals[i].split("\n")))
    lst_nasr.append(len(manighazals[i].split("\n")))

f1 = open("f1.txt",'w')
f2 = open("f2.txt",'w')
for i in range(495):
    if lst_nasr[i]!= lst_sher[i] :
        print(i+1)
    f1.write(ghazals[i])
    f1.write("\n")
    f2.write(manighazals[i])
    f2.write("\n")
f1.close()
f2.close()

