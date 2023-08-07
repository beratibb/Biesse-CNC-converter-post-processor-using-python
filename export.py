import numpy as np
import os
import pickle
programet_l=[]
import drillingbit as db
word="NAME=GEO"
import FilePath as fp
Lista_programev4 , Numri_Pllakave4 = fp.ListaProgramev()
#import HoleData as hd1
#Gjersia_tables2 , Gjatsia_tables2 , Trashesia_tables2 , X_Hole2 , Y_Hole2 , Dia_Hole2 , Deep_Hole2, Emri_programit2 , numri_vrimav2 = hd1.data()
#Dia_Hole1 , X_Hole1,Y_Hole1 , Deep_Hole1 , numri_vrimav1 = tb.exportdata()
def exporti(Gjersia_tables , Gjatsia_tables , Trashesia_tables , X_Hole , Y_Hole , Dia_Hole , Deep_Hole, Emri_programit , numri_vrimav , p):
    Programi ="Programet_cix/"+Lista_programev4[p]
    lexo_programin_gjeometri = " "
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR , "programet_cix")
    zz=0
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("cix") or file.endswith("cix"):
                path = os.path.join(file)    
                label = os.path.basename(root).replace(" ", "-").lower()
                programet_l.append(path)
                #print(path)
                #print("testi : " , path[-4:])
                if path[-4:]==".cix":
                    zz+=1
                numri_filev=len(path)

    #print("numri i z : " , zz)
    #print("numiriii : ", numri_filev)
    numri_1=0
    u=programet_l[numri_1]
    y="Programet_cnc/"+Emri_programit
    fw=open(y, 'a')
    k=0
    j=0
    fw.write("BEGIN ID CID3" + "\n" + "        REL= 5.0" + "\n" + "END ID" + "\n\n" + "BEGIN MAINDATA" )
    gjer=Gjersia_tables[numri_1]
    gjat = Gjatsia_tables[numri_1]
    trash = Trashesia_tables[numri_1]
    fw.write("\n" + "        LPX=" + gjat + "\n" + "        LPY=" + gjer + "\n" + "        LPZ=" + trash + "\n")
    fw.write("        ORLST=\"5\""+"\n")
    fw.write("        TLCHK=0"+"\n")
    fw.write("        TOOLING=\"\""+"\n")
    fw.write("        CUSTSTR=$B$KBsExportToNcRoverNET.XncExtraPanelData$V\"\""+"\n")
    fw.write("        FCN=1.000000"+"\n")
    fw.write("        JIGTH=0"+"\n")
    fw.write("        CKOP=0"+"\n")
    fw.write("        UNIQUE=0"+"\n")
    fw.write("        MATERIAL=\"wood\""+"\n")
    fw.write("        OPPWKRS=0"+"\n")
    fw.write("        UNICLAMP=0"+"\n")
    fw.write("        CHKCOLL=0"+"\n")
    fw.write("        WTPIANI=0"+"\n")
    fw.write("        COLLTOOL=0"+"\n")
    fw.write("        CALCEDTH=0"+"\n")
    fw.write("        ENABLELABEL=0"+"\n")
    fw.write("        LOCKWASTE=0"+"\n")
    fw.write("        LOADEDGEOPT=0"+"\n")
    fw.write("        ITLTYPE=0"+"\n")
    fw.write("        RUNPAV=0"+"\n")
    fw.write("        FLIPEND=0"+"\n")
    fw.write("        XCUT=0"+"\n")
    fw.write("        YCUT=0"+"\n")
    fw.write("END MAINDATA"+"\n\n")
    fw.write("BEGIN VB"+"\n")
    fw.write("        VBLINE=\"\'\""+"\n")
    fw.write("END VB"+"\n\n")
    fw.write("BEGIN MACRO"+"\n")
    fw.write("        NAME=NOPRK"+"\n")
    fw.write("  PARAM,NAME=ABL,VALUE=0"+"\n")
    fw.write("END MACRO"+"\n\n")
    h=0
    nr_vr=numri_vrimav
    if nr_vr>0:
        
        #print("hhh:" , h)
        while h<nr_vr:
            fw.write("BEGIN MACRO"+"\n")
            fw.write("        NAME=BG"+"\n")
            fw.write("        PARAM,NAME=SIDE,VALUE=0"+"\n")
            fw.write("        PARAM,NAME=CRN,VALUE=\"1\""+"\n")
            fw.write("        PARAM,NAME=X,VALUE="+X_Hole[h]+"\n")
            fw.write("        PARAM,NAME=Y,VALUE="+Y_Hole[h]+"\n")
            fw.write("        PARAM,NAME=DIA,VALUE="+Dia_Hole[h]+"\n")
            dia_int=int(Dia_Hole[h])
            fw.write("        PARAM,NAME=TNM,VALUE="+db.drillbit(dia_int)+"\n")
            #print("kqyre drillin :" + tb.drillbit(dia_int))
            fw.write("        PARAM,NAME=TTP,VALUE=0"+"\n")
            fw.write("        PARAM,NAME=DP,VALUE="+Deep_Hole[h]+"\n")
            fw.write("END MACRO"+"\n\n")  
            h+=1
        numri_1+=1
    #print("mmm")
    Hape_Programin = open(Programi, 'r' )
    p=0 
    b=0
    while(lexo_programin_gjeometri):
        lexo_programin_gjeometri = Hape_Programin.readline()
        ndaje_programin = lexo_programin_gjeometri.split()
        if word in ndaje_programin:
            #print("mir")
           p=p+1
           b=1
        if p==1:
            #print("u printu")
            fw.write("BEGIN MACRO" + "\n")
            p=2
        if b==1:    
            fw.write(lexo_programin_gjeometri)
            #print(lexo_programin_gjeometri)
        #print("ppp=" , p)
    #while(nr_vr>0):
     #       print("mirrrrrr")
          
        
#def test():
#    print("testi21")
         
                