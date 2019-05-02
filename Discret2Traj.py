import pandas as pd
import os
import FrechetDiscret
import time

chemin = os.path.abspath('resources/exemple.csv')
#separateur !! mettre en defaut ';'  !!!
df = pd.read_csv(chemin,sep=';')
print(df)

df1 = df.get(["pos_id", "track_id", "path", "x", "y"])

print(df1[df1.track_id==1])

len_lig = df1[df1.track_id==1].shape[0]
len_col = df1[df1.track_id==2].shape[0]

# nombre de ligne
nb_ligne =df.shape[0]
print(nb_ligne)


# Debut du decompte du temps de traitement
start_time = time.time()

# Calcul de la matrice d'euclide
mat_euc=FrechetDiscret.matrice_euclide(df1[df1.track_id==1],df1[df1.track_id==2], len_lig, len_col)

# Calcul de la matrice de frechet
mat_fre=FrechetDiscret.MatriceFrechet(mat_euc, len_lig, len_col)

# Calcul de la trajectoire frechet
dis_f=FrechetDiscret.distance_frechet(mat_fre, len_lig, len_col)

# Fin du traitement
end_time = time.time() - start_time

print("la matrice d'euclide")
print(mat_euc)
print("la matrice de frechet")
print(mat_fre)
print("Trajecorie frechet")
print(dis_f)
print("Distance frechet")
print(max(dis_f))
print("temps d\'execution")
print(end_time)
