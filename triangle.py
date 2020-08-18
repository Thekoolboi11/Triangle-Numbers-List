# 1
# 2 3
# 4 5 6

#1, 3 , 6, 10

def getTriangle(n):

    c = 0
    resultlist=[]
    for x in range (n):
        for y in range (1,x+1):
            c = c + 1
            if(y == x):
                #print(str(c) + ",",end='')
                resultlist.append(c)

    print(resultlist)

getTriangle(5589)
