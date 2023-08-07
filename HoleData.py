import FilePath as fp
import numpy as np
import os
import pickle
import Sortimi as st
import export
i=0
word="NAME=BG"
Gjersia_tables = []
Gjatsia_tables = []
Trashesia_tables =[]
side_Hole = []
CRN_Hole = []
numri_vrimav = []
Lista_programev , Numri_Pllakave = fp.ListaProgramev()
Emri_programit =[]
numri_vrimav1 = 0
prev=0
nn=0
def data(Gjersia_tables1 , Gjatsia_tables1 , Trashesia_tables1 , X_Hole1 , Y_Hole1 , Dia_Hole1 , Deep_Hole1, Emri_programit1 , numri_vrimav1):
    return Gjersia_tables , Gjatsia_tables , Trashesia_tables , X_Hole , Y_Hole , Dia_Hole , Deep_Hole, Emri_programit , numri_vrimav   

def exportdata():
    return Gjersia_tables , Gjatsia_tables , Trashesia_tables , X_Hole , Y_Hole , Dia_Hole , Deep_Hole, Emri_programit , numri_vrimav , Lexo_programin   


while(i<Numri_Pllakave):
    nn=0
    X_Hole = []
    Y_Hole = []
    Dia_Hole = []
    TTP_Hole = []
    Deep_Hole = []
    Gjersia_tables = []
    Gjatsia_tables = []
    Trashesia_tables =[]
    x1=0
    Lexo_programin = " "
    Lexo_programin_export = " "
    Lexo_programin_vrima = " "
    lx = " "
    count1 = 0
    #print(count1) 
    Emri_programit.append(Lista_programev[i])
    Programi ="Programet_cix/"+Lista_programev[i]
    Hape_Programin = open(Programi, 'r' ) 
    Hape_Programin_vrimav = open(Programi, 'r' )  
    
    while(Lexo_programin):
        Lexo_programin = Hape_Programin.readline()
        Ndaje_programin = Lexo_programin.split()
        count1+=1
        if count1==6:
            Gjattsia_t=Lexo_programin[5:]
            Gjatsia_t1=Gjattsia_t.rstrip()
            Gjatsia_tables.append(Gjatsia_t1)
            
        if count1==7:
            Gjerrsia_t=Lexo_programin[5:]
            Gjersia_t1=Gjerrsia_t.rstrip()
            Gjersia_tables.append(Gjersia_t1)
        if count1==8:
            trashhsia_t=Lexo_programin[5:]
            Trashesia_t1=trashhsia_t.rstrip()
            Trashesia_tables.append(Trashesia_t1)
        
        numri_vrimav1 = 0
        prev=0
        count = 0
        while(Lexo_programin_vrima):
            Lexo_programin_vrima = Hape_Programin_vrimav.readline()
            Ndaje_programin_vrimav = Lexo_programin_vrima.split()
            if word in Ndaje_programin_vrimav:
                
                numri_vrimav1 +=1
                
                x1=count
            count2 = 0
            count3 = 0
            count4 = 0
            count5 = 0
            count6 = 0
            count7 = 0
            count8 = 0
            
            
            if count == x1+5:
                for c in Lexo_programin_vrima:
                    if count2==20:
                     diaa=Lexo_programin_vrima[22:]
                     dia=diaa.rstrip()
                     Dia_Hole.append(dia)
                    count2+=1
            
            if count == x1+3:
                for c in Lexo_programin_vrima:
                    if count3==20:
                     c_x=Lexo_programin_vrima[20:]
                     c_x1=c_x.rstrip()
                     X_Hole.append(c_x1)
                    count3+=1
    
            if count == x1+4:
                for c in Lexo_programin_vrima:
                    if count4==20:
                     c_y=Lexo_programin_vrima[20:]
                     c_y1=c_y.rstrip()
                     Y_Hole.append(c_y1)
                    count4+=1
            
            if count == x1+7:
                for c in Lexo_programin_vrima:
                    if count5==20:
                     thellsia=Lexo_programin_vrima[21:]
                     thellsia1=thellsia.rstrip()
                     Deep_Hole.append(thellsia1)
                    count5+=1
            count+=1
            if numri_vrimav1>prev:
                prev=numri_vrimav1
                if numri_vrimav1 != 0:
                    nn = numri_vrimav1
    if nn>0:
        Gjersia_tables2 , Gjatsia_tables2 , Trashesia_tables2 , X_Hole2 , Y_Hole2 , Dia_Hole2 , Deep_Hole2, Emri_programit2 , numri_vrimav2=st.getdata(Gjersia_tables , Gjatsia_tables , Trashesia_tables , X_Hole , Y_Hole , Dia_Hole , Deep_Hole, Emri_programit , nn) 
        export.exporti(Gjersia_tables2 , Gjatsia_tables2 , Trashesia_tables2 , X_Hole2 , Y_Hole2 , Dia_Hole2 , Deep_Hole2, Emri_programit2[i] , nn , i)
    if nn<1:
        export.exporti(Gjersia_tables , Gjatsia_tables , Trashesia_tables , X_Hole , Y_Hole , Dia_Hole , Deep_Hole, Emri_programit[i] , nn , i)
        
    numri_vrimav.append(nn)
    i+=1
        
    
    
    
            
    
        

        
    
