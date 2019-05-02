import numpy as np
import math


def coord(debut,fin, df):
    cord=[]
    for debut in range(fin):
        cord.append(df.iloc[debut,1,2])
    return cord

#fonction pour matrice euclidienne
def matrice_euclide(dataframe1,dataframe2, len_lig, len_col):
    #leng_lig= dataframe1.shape[0]
    #leng_col= dataframe2.shape[0]
    i=0
    j=0
    #len_mat=200
    euc_mat=np.empty((len_lig,len_col))
    for i in range(len_lig):
        for j in range(len_col):
            Xpow = pow((dataframe1.iloc[i,3]) - (dataframe2.iloc[j,3]),2)
            Ypow = pow((dataframe1.iloc[i,4]) - (dataframe2.iloc[j,4]),2)
            racine = math.sqrt(Xpow+Ypow)
            euc_mat[i,j] = racine
    return euc_mat

def MatriceFrechet(euclideMatrice, len_lig, len_col):
    # initialisation de la matrice
    fre_mat = np.zeros((len_lig, len_col))
    fre_mat[0,0] = euclideMatrice[0,0]
    # remplir la première ligne
    for i in range(1, len_col):
        fre_mat[0, i] = max(euclideMatrice[0, i], fre_mat[0, i-1])
    # remplir la première colomne
    for j in range(1, len_lig):
        fre_mat[j,0] = max(euclideMatrice[j,0], fre_mat[j-1, 0])
    # remplir le reste de la matrice
    for x in range(1, len_lig):
        for y in range(1, len_col):
            fre_mat[x,y] = max(min(fre_mat[x,y-1], fre_mat[x-1,y-1], fre_mat[x-1,y]), euclideMatrice[x,y])
    return fre_mat


#fonction pour distance de frechet
def distance_frechet(fre_mat, len_lig, len_col):
    i=len_lig -1
    j=len_col -1
    listdesmin=[]
    listdesmin.append((fre_mat[i,j], i, j))
    while (i>0 and j>0):
        h=i-1
        hgb=j-1
        lvoisinF=[fre_mat[h,j],fre_mat[h,hgb],fre_mat[i,hgb]]
        coord=[(h,j),(h,hgb),(i,hgb)]
        lvoisinE=[fre_mat[h,j],fre_mat[h,hgb],fre_mat[i,hgb]]
        indices = [i for i, x in enumerate(lvoisinF) if x ==min(lvoisinF)]
        if(len(indices)==1):
            #acceder au coordonnées dans coord
            i=coord[indices[0]][0]
            j=coord[indices[0]][1]
        if(len(indices)==2):
            minE=min(lvoisinE[indices[0]],lvoisinE[indices[1]])
            coordE=[i for i, x in enumerate(lvoisinF) if x == minE]
            i=coord[coordE[0]][0]
            j=coord[coordE[0]][1]
        if(len(indices)==3):
            minE = min(lvoisinE[indices[0]], lvoisinE[indices[1]],lvoisinE[indices[2]])
            coordE = [i for i, x in enumerate(lvoisinF) if x == minE]
            i = coord[coordE[0]][0]
            j = coord[coordE[0]][1]
            #indices = [i for i, x in enumerate(lvoisinF) if x == min(lvoisinF)]
        listdesmin.append((min(lvoisinF),i,j))

    return listdesmin
