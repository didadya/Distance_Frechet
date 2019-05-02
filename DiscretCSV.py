import pandas as pd
import os
import FrechetDiscret
import time

chemin = os.path.abspath('resources/pigeons.csv')
#separateur !! mettre en defaut ';'  !!!
df = pd.read_csv(chemin,sep=';')

df1 = df.get(["pos_id", "track_id", "path", "x", "y"])

# Debut du decompte du temps de traitement
start_time = time.time()
for i in range(1,961):
    # Temps de traitement pour chaque 1 avec 959 trajectoire
    start1_959Traj = time.time()
    for j in range(i+1,961):
        # ici on prend 100 points pour chaque trajectoire juste pour tester (vu la volumétrie des données)
        len_lig = 100 #df1[df1.track_id==i].shape[0]
        len_col = 100 #df1[df1.track_id==j].shape[0]
        # Temps de traitement pour chaque 2 trajectoire
        start2Traj = time.time()
        # Calcul de la matrice d'euclide
        mat_euc=FrechetDiscret.matrice_euclide(df1[df1.track_id==i],df1[df1.track_id==j], len_lig, len_col)
        # Calcul de la matrice de frechet
        mat_fre=FrechetDiscret.MatriceFrechet(mat_euc, len_lig, len_col)
        # Calcul de la trajectoire frechet
        dis_f=FrechetDiscret.distance_frechet(mat_fre, len_lig, len_col)
        # Fin du traitement entre 2 trajectoire
        print("Distance de frechet entre les trajets ", i, " et ", j, " est : ", max(dis_f))
        print(" Temps traitement : ", time.time()-start2Traj, "\n")
    # Fin du traitement pour chaque 1 avec 959 trajectoire
    print("Temps total traitement du trajet ", i, " avec tous les autres trajets est : ", time.time()-start1_959Traj, "\n")
# Fin du traitement
print("Le temps total est :", time.time()-start_time)