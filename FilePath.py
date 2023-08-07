import numpy as np
import os
import pickle
Emri_tableles=[] 


def ListaProgramev():
    Emri_tableles_1 = Emri_tableles
    numri_tablev_1 = numri_tabelav
    return Emri_tableles_1 , numri_tablev_1    
    

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR , "programet_cix")
numri_tabelav=0
for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("cix"):
            path = os.path.join(file)    
            label = os.path.basename(root).replace(" ", "-").lower()
            Emri_tableles.append(path)
            numri_tabelav+=1
               
            #numri_filev=len(path)
            





            
            