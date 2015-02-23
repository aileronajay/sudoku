import math
import sys
import fileinput
a = {}
for i in range (1,10):
    for j in range (1,10):
        a[i,j] = range(1,10)

#code to i
#for i in range (1,10):
#    for c in a.keys():
#        if c[0] == i:
#            print c
        

#remove from horizontal and vertical lines
#i,j
def removeHzVz (i,j,number):
    for k in range (1,10):
        #print number
        #print
        if j != k :
            try:
                a[i,k].remove(number)
            except:
                continue
        #a[i,j].remove(number)
    for l in range (1,10):
        if l != i:
            try:
                a[l,j].remove(number)
            except:
                continue
        
#remove from the box
def removeFromGrid (i,j,number):
    xvar = math.ceil(float(i)/float(3))
    yvar = math.ceil(float(j)/float(3))
    h = 3 * (xvar - 1)
    k = 3 * (yvar - 1)
    #print h
    #print k
    for l in range(1,4):
        for g in range(1,4):
            #print l,g
            if h+l == i and k+g == j:
                pass
            else:
                try:
                    #print h+l,k+g
                    a[h+l,k+g].remove(number)
                except:
                    continue
            #print h+l,k+g
#remove all candidates for the site when a certain number is present for the input
def cleanSite (i,j,number):
    a[i,j] = [number]

def main():  
    #removeFromGrid(1,1,2)
    #removeHzVz (1,1,3)
    #for v in range (1,10):
    #    print a[1,v]
    #for l in range(1,4):
    #    for g in range (1,4):
    #        print l,g,a[l,g]
    #print a
    #f = sys.stdin.readline()
    #f.open()
    #for line in f:
    #    print line

    #narrow down on basis of input
    for line in fileinput.input():
        arry = line.split(",")
        #print arry[0],arry[1],arry[2]
        removeHzVz (int(arry[0]),int(arry[1]),int(arry[2]))
        removeFromGrid (int(arry[0]),int(arry[1]),int(arry[2]))
        cleanSite (int(arry[0]),int(arry[1]),int(arry[2]))

    #further narrowing down
    for z in range(1,10):
        for i in range(1,10):
            for j in range (1,10):
                if len(a[i,j]) == 1:
                    removeFromGrid (i,j,a[i,j][0])
                    removeHzVz (i,j,a[i,j][0])
                #print i, j, a[i,j]

    '''for i in range(1,10):
        for j in range (1,10):
            print i ,j , a[i,j]
            pass'''
    #removeFromGrid(9,8,2)
    '''print len(a[9,8])
    print a[9,8]
    removeFromGrid(9,8,a[9,8][0])
    print a[7,8]'''
    for i in range(1,10):
        for j in range (1,10):
            print i,j,a[i,j]
main()
