
tarjome = open("nasr.txt","w")
with open("tarjome_hafez.txt",'r') as file :
    x = file.read()
    y= x.split("شرح غزل :")
    y = y[1:]
    counter =1
    for ghazal in y :
        i = 1
        beytcounter = 0
        tarjome.write(str(counter)+"غزل شماره " +"\n")
        while str(i) in ghazal :
            q1 = ghazal.find(str(i))
            q2 = ghazal.find(str(i+1))
            beyt = ghazal[q1:q2]
            beyt = beyt.replace("\n"," ")
            beytcounter+=1
            i+=1
            tarjome.write(beyt+"\n")
        counter+=1
tarjome.close()


