import numpy as np
import os
import pickle


def getdata(Gjersia_tables1 , Gjatsia_tables1 , Trashesia_tables1 , X_Hole1 , Y_Hole1 , Dia_Hole1 , Deep_Hole1, Emri_programit1 , numri_vrimav1):
    #events = [i for i in dir(cv2) if 'EVENT' in  i]
    #print(events)
    Gjersia_tables , Gjatsia_tables , Trashesia_tables , X_Hole , Y_Hole , Dia_Hole , Deep_Hole, Emri_programit , numri_vrimav = Gjersia_tables1 , Gjatsia_tables1 , Trashesia_tables1 , X_Hole1 , Y_Hole1 , Dia_Hole1 , Deep_Hole1, Emri_programit1 , numri_vrimav1
    Testi=[3,5,3,4,5,6,10,8,3,9,5,3,2]
    brisqit = [3,5,8,10,15,35]
    konfigurimi_brisqve=['FRASES_3','FRAES_6','FRAES_8','FRAES_10','FRAES_4']
    brisr_shangjer=len(brisqit)
    dia=len(Dia_Hole)

    #u=int(Dia_Hole[1])
    #print(Dia_Hole)
    #print("The variable, name is of type:", type(u))
    i=0
    h=0
    #print("diametri" , Deep_Hole)
    while i<brisr_shangjer:
        j=0
        #print("j=" , j)
        #if j<dia:
            #print("mir eshte")
        while j<dia:
            #print("sstt")
            dia_int=int(Dia_Hole[j])
            dia_brisqit=int(brisqit[i])
            if dia_int==dia_brisqit:
                ndrro_hole = Dia_Hole[h]
                Dia_Hole[h]=Dia_Hole[j]
                Dia_Hole[j]=ndrro_hole
                ndrro_x=X_Hole[h]
                ndrro_y=Y_Hole[h]
                ndrro_z=Deep_Hole[h]
                Deep_Hole[h]=Deep_Hole[j]
                Deep_Hole[j]=ndrro_z
                X_Hole[h]=X_Hole[j]
                Y_Hole[h]=Y_Hole[j]
                X_Hole[j]=ndrro_x
                Y_Hole[j]=ndrro_y
                
                h+=1
            #   print("h=", h)
            j+=1
        i+=1

    #print("u sortu")
    #print("dia:" , Dia_Hole)
    return Gjersia_tables , Gjatsia_tables , Trashesia_tables , X_Hole , Y_Hole , Dia_Hole , Deep_Hole, Emri_programit , numri_vrimav

    
        

                
                
                