import csv
from datetime import datetime
import numpy
np=(numpy)

path="G:\sample.csv"
path1="G:\outputlunch.csv"
path2="G:\outputdinner.csv"

types=set()
filteredLines=[]
filteredLines2=[]
with open(path, encoding='utf-8') as f:
    lines=f.readlines()
    for line in lines:
        row=line.split(",")
        if(len(row)<14):
            continue
        types.add(row[1])
        tt = row[-5][-8:-3]  #e.g. 07:41
        if tt >=str('10:59') and tt <=str('13:00'):# for lunch begining time 11 am and ending time 2pm
            filteredLines.append(row)

        if tt >=str('16:59') and tt <=str('19:00'):# for lunch begining time 11 am and ending time 2pm
            filteredLines2.append(row)
#sort filteredLines by lunch time
filteredLines=np.array(filteredLines)
filteredLines2=np.array(filteredLines2)
newFilterLines=filteredLines[filteredLines[:,-5].argsort()]
newFilterLines2=filteredLines2[filteredLines2[:,-5].argsort()]
print(newFilterLines)
print(newFilterLines2)
#output
with open(path1,"w", encoding='utf-8') as fw:
    for row in newFilterLines:
        fw.write(",".join(row))

with open(path2,"w", encoding='utf-8') as fw:
    for row in newFilterLines2:
        fw.write(",".join(row))
