import sys
import ast
import numpy as np
#from pprint import pprint

def m(a, b):
    if a == b :
        return 0
    else :
        return 1
        
def MatrixD(S1, S2):
    N = len(S1)
    M = len(S2)
    D = np.zeros((N+1, M+1 ))
    D[0][0] = 0
    for j in range (1, M+1):
        #print(j)
        D[0][j] = D[0][j-1] + 1
    for i in range (1, N+1):
        D[i] [0] = D[i-1] [0] + 1
    for i in range (1, N+1):
        for j in range (1, M+1):
            D[i][j] = min([D[i-1][j]+1, D[i][j-1]+1, D[i-1][j-1]+m(S1[i-1], S2[j-1])])
    #print(D)
    #print(D[N][M])
    return D[N][M]

def main():
    input = open(sys.argv[1], "r")   # файл с парами файлов
    scores = open(sys.argv[2], "w")  # путь выходного файла
    #print(sys.argv)

    files = []
    for line in input:
        s = line.split()
        files.append(s)
    #print(files)
    input.close()
    
    
    for i in range(len(files)):
        f0 = ast.parse( open(files[i][0], "r").read() )
        f1 = ast.parse( open(files[i][1], "r").read() )
        
        f0 = ast.dump(f0, annotate_fields=False)
        f1 = ast.dump(f1, annotate_fields=False)
        
        D = MatrixD (f0, f1)
        if max([len(f0), len(f1)]) != 0 :
            #D = D / max([len(f0), len(f1)])
            D = 1 - D / max([len(f0), len(f1)])
        else :
            #D = 0
            D = 1
        scores.write(str(D) + "\n")
    scores.close()
    
    #MatrixD("EXPONENTIAL", "POLYNOMIAL")
    '''
    tree1 = ast.parse("print('Hello, world!')")
    tree1 = ast.dump(tree1)
    tree2 = ast.parse("pint('Hello, world!')")
    tree2 = ast.dump(tree2)
    print (tree1)
    print (tree2)
    MatrixD(tree1, tree2)
    '''
main()
