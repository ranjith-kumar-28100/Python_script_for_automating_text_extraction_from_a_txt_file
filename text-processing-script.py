import re
file = open("data.txt")
file_data = file.readlines()
data=[]
min =[]
sec=[]
for line in file_data:
    if not line.startswith("\n") and not line.startswith("Duration: "):
        data.append(line.replace("\n",''))
    elif line.startswith("Duration: "):
        res = re.findall(r'\d+', line) 
        min.append(int(res[0]))
        if len(res)==2:
            sec.append(int(res[1]))
        else:
            sec.append(0)
list_data =[]
for i,j,k in zip(data,min,sec):
    list_data.append({"Topic":i,"Minutes":j,"Seconds":k})
import pandas as pd
pd.DataFrame(list_data).to_csv("results.csv",index=False)
df = pd.read_csv("results.csv")
print("Total: "+str(round(df["Minutes"].sum()+df["Seconds"].sum()/60,2))+" minutes")