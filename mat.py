

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
def det(m):
    if len(m) <= 0:
        return None
    elif len(m) == 1:
        return m[0][0]
    else:
        s = 0
        for i in range(len(m)):
            n = [[row[a] for a in range(len(m)) if a != i] for row in m[1:]]  
            s += m[0][i] * det(n) * (-1) ** (i % 2)
        return s
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
    dets = float(det(x))
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

    Ax = inv(x)
    print Ax




if __name__ == '__main__':
    test_Mat()
