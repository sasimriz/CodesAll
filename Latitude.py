'''

@author: Administrator
'''
#Wudaokou                         116.331657    39.991462
#Tuanjiehu                        116.455574    39.932395
#Liangmaqiao                      116.455611    39.948019
#AgricultureExhibition Centre     116.455582    39.940006
#Jintaixizhao                     116.455527    39.915818
#Dongdaqiao                       116.445489    39.921754


import os
from anaconda_navigator.static.fonts import PATH
from anaconda_navigator.utils.constants import ROOT

t = str(39.921754)

d=str('SDO')

for numl in range(15,31):

    
    ROOT="G:\\C\\A"
    PATH1="G:\\C\\A\\RR-SEP01-30\\"+str(numl)+"\\"+str(numl)+"R.csv"
    PATH2="G:\\C\\A\\RR-SEP01-30\\"+str(numl)+"\\"+str(numl)+"R-R.csv"
    PATH3="G:\\C\\A\\RR-SEP01-30\\"+str(numl)+"\\"+str(numl)+"R-R-R.csv"
    PATH4="G:\\C\\A\\RR-SEP01-30\\"+str(numl)+"\\"+str(numl)+"R-R-R-R.csv"
    PATH5="G:\\C\\A\\RR-SEP01-30\\"+str(numl)+"\\"+str(numl)+"R-R-R-R-R.csv"
    PATH6="G:\\C\\A\\RR-SEP01-30\\"+str(numl)+"\\"+str(numl)+"R-R-R-R-R-R.csv"
    PATH7="G:\\C\\A\\RR-SEP01-30\\"+str(numl)+"\\"+str(numl)+"R-R-R-R-R-R-R.csv"
    PATH8="G:\\C\\A\\RR-SEP01-30\\"+str(numl)+"\\"+str(numl)+"R-R-R-R-R-R-R-R.csv"
    
    PATH_OUTPUT1="G:\\"+d+"\\R\\"+str(numl)+"\\R.csv"
    PATH_OUTPUT2="G:\\"+d+"\\R\\"+str(numl)+"\\RR.csv"
    PATH_OUTPUT3="G:\\"+d+"\\R\\"+str(numl)+"\\RRR.csv"
    PATH_OUTPUT4="G:\\"+d+"\\R\\"+str(numl)+"\\RRRR.csv"
    PATH_OUTPUT5="G:\\"+d+"\\R\\"+str(numl)+"\\RRRRR.csv"
    PATH_OUTPUT6="G:\\"+d+"\\R\\"+str(numl)+"\\RRRRRR.csv"
    PATH_OUTPUT7="G:\\"+d+"\\R\\"+str(numl)+"\\RRRRRRR.csv"
    PATH_OUTPUT8="G:\\"+d+"\\R\\"+str(numl)+"\\RRRRRRRR.csv"
    
    #for ROOT, dirs, files in os.walk(ROOT):  
        #for filename in files:
            #print(ROOT+filename)
    
    types=set()
    
    filteredLines=[]
    with open(PATH1, encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            row=line.split(",")
            if(len(row)<14):
                continue
            types.add(row[1])
            if row[-2]== t:
                filteredLines.append(line)
    
    with open(PATH_OUTPUT1,"w", encoding='utf-8') as fw:
        fw.write("".join(filteredLines))
        
    #BEGINING OF THE CODE FOR RR
    
    filteredLines=[]
    with open(PATH2, encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            row=line.split(",")
            if(len(row)<14):
                continue
            types.add(row[1])
            if row[-2]==t:
                filteredLines.append(line)
    
    with open(PATH_OUTPUT2,"w", encoding='utf-8') as fw:
        fw.write("".join(filteredLines))
    
    #BEGINING OF THE CODE FOR RRR    
    
    filteredLines=[]
    with open(PATH3, encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            row=line.split(",")
            if(len(row)<14):
                continue
            types.add(row[1])
            if row[-2]==t:
                filteredLines.append(line)
    
    with open(PATH_OUTPUT3,"w", encoding='utf-8') as fw:
        fw.write("".join(filteredLines))
    
    #BEGINING OF THE CODE FOR RRRR
    
        filteredLines=[]
    with open(PATH4, encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            row=line.split(",")
            if(len(row)<14):
                continue
            types.add(row[1])
            if row[-2]==t:
                filteredLines.append(line)
    
    with open(PATH_OUTPUT4,"w", encoding='utf-8') as fw:
        fw.write("".join(filteredLines))
    
    #BEGINING OF THE CODE FOR RRRRR
        
        filteredLines=[]
    with open(PATH5, encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            row=line.split(",")
            if(len(row)<14):
                continue
            types.add(row[1])
            if row[-2]==t:
                filteredLines.append(line)
    
    with open(PATH_OUTPUT5,"w", encoding='utf-8') as fw:
        fw.write("".join(filteredLines))
    
    #BEGINING OF THE CODE FOR RRRRRR
        
        filteredLines=[]
    with open(PATH6, encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            row=line.split(",")
            if(len(row)<14):
                continue
            types.add(row[1])
            if row[-2]==t:
                filteredLines.append(line)
    
    with open(PATH_OUTPUT6,"w", encoding='utf-8') as fw:
        fw.write("".join(filteredLines))
    
    #BEGINING OF THE CODE FOR RRRRRRR
        
        filteredLines=[]
    with open(PATH7, encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            row=line.split(",")
            if(len(row)<14):
                continue
            types.add(row[1])
            if row[-2]==t:
                filteredLines.append(line)
    with open(PATH_OUTPUT7,"w", encoding='utf-8') as fw:
        fw.write("".join(filteredLines))
    
    #BEGINING OF THE CODE FOR RRRRRRRR
        
        filteredLines=[]
    with open(PATH8, encoding='utf-8') as f:
        lines=f.readlines()
        for line in lines:
            row=line.split(",")
            if(len(row)<14):
                continue
            types.add(row[1])
            if row[-2]==t:
                filteredLines.append(line)
    
    with open(PATH_OUTPUT8,"w", encoding='utf-8') as fw:
        fw.write("".join(filteredLines))