
def t(x):
    tx = [[] for i in x[0]]
    for i in x:
        for j in range(len(i)):
            tx[j].append(i[j])
    return tx
def mulMat(tx,x):#tx [m,n] x[n,p] txx[m,p]
    res = [[0] * len(x[0]) for i in range(len(tx))]
    for i in range(len(tx)):
        for j in range(len(x[0])):
            for k in range(len(x)):
                res[i][j] += tx[i][k] * x[k][j]
    return res
    
def det(x):
    temp = 1
    iteration = 0
    for i in range(len(x)):
        if x[i][i]==0:
            for j in range(i+1,len(x)):
                if x[j][i]!=0:
                    x[i],x[j]=x[j],x[i]
                    
                    iteration+=1
        for k in range(i+1,len(x)):
            yin = -1*x[k][i]/x[i][i]
            for u in range(len(x)):
                x[k][u] = x[k][u]+x[i][u]*yin
    for i in range(len(x)):
        temp = temp*x[i][i]
    if iteration%2==1:
        temp = -temp
    return temp
def delMat(x,r,c):
    Ax = []
    for i in range(len(x)):
        tmp = []
        for j in range(len(x[0])):
            if i!=r and j !=c :
                tmp.append(x[i][j])
        if i!=r:
            Ax.append(tmp)
    return Ax
def A(x):
    tmp = []
    res = []
    for i in range(len(x)):
        tmp = [0 for _ in range(len(x[0]))]
        res.append(tmp)
    for i in range(len(x)):
        for j in range(len(x[0])):
            tmp = x
            tmp = delMat(tmp,i,j)
            res[i][j]=(1 if (i+j)%2==0 else -1)*det(tmp)
    return res
def inv(x):
    res = A(x)
    dets = det(x)
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j]/=dets
    return res
def ConRows(x,y):
    for i in range(len(y)):
        for j in range(len(y[0])):
            x[i].append(y[i][j])
    return x
def ConCols(x,y):
    for i in range(len(y)):
        row = []
        for j in range(len(y[0])):
            row.append(y[i][j])
        x.append(row)
    return x
def test_Mat():
    x = [[2,1,-1],[2,1,0],[1,-1,1]]
    tx = t(x)
    res = mulMat(tx,x)
    Ax = inv(x)
    de = det(x)
    print 'x'
    print x
    print 'tx'
    print tx
    print 'res'
    print res
    print 'Ax'
    print Ax
    print 'de'
    print de


if __name__ == '__main__':
    test_Mat()
