from PIL import Image
import operator
import os

def isWhite(input):
    s = 0
    for i in input:
        s+= i
    if s>180:
        return True
    else :
        return False

def findborder(x,y):
    if x[0][0] <1000 :
        x0 = x[0][0]
        i = 0
        while x[i][0]<1000 :
            i+=1
        x1 = x[i][0]

    else :
        x1 = x[0][0]
        i = 0
        while x[i][0] >1000:
            i+=1
        x0 = x[i][0]

    if y[0][0]<1000:
        y0 = y[0][0]
        i = 0
        while y[i][0]<1000:
            i+=1
        y1 = y[i][0]
    else:
        y1 = y[0][0]
        i = 0
        while y[i][0]>1000:
            i+=1
        y0 = y[i][0]
    return x0,y0,x1,y1

allimg = os.listdir("edit")

for imgnum in range(133,134):
    print(imgnum,end="->")
    im = Image.open('edit/'+allimg[imgnum]) # Can be many different formats.
    pix = im.load()

    count = {}
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if isWhite(pix[i,j]):
                pix[i,j] = (255,255,255)
            else:
                pix[i,j] = (0,0,0)

            if not isWhite(pix[i,j]):
              if i in count :
                  count[i] +=1
              else :
                  count [i] = 1

    x = sorted(count.items(), key=operator.itemgetter(1),reverse=True)
    count ={}
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            if not isWhite(pix[i,j]):
              if j in count :
                  count[j] +=1
              else :
                  count [j] = 1

    y = sorted(count.items(), key=operator.itemgetter(1),reverse=True)
    x0,y0,x1,y1 = findborder(x,y)
    print (x0,y0,x1,y1)
    im = im.crop((x0,y0,x1,y1))
    im.save('withoutborder/'+allimg[imgnum])
    im.close()