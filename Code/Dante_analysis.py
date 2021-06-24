import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import filecmp
import os, os.path
import glob

data = pd.read_csv("Project/CSS_Alien/Pattern_data/OTS_2_Default_2/general_data.csv")

data.columns=["time step", "number of clusters", "number of clusters with tokens", "number of cells", "number of particles", "number of tokens", "total internal energy", "total kinetic energy"]

# plt.plot(data["time step"],data["number of clusters with tokens"])
# plt.show()



def data_from_text(path):
    text = open(path,"r").read()
    numbers =[[int(s) for s in re.findall(r'\b\d+\b', line, re.M)] for line in text.splitlines()]
    numbers = numbers[2:]
    return numbers
    

# data_from_text(path)

path = "Project/CSS_Alien/Pattern_data/OTS_2_Default_2/"
all_data = []
total_data = []
biggest_data = []
sum_data = []
for i in range(15):
    subdata = data_from_text(path+str(i*5)+"/result.txt")
    all_data.append(subdata)
    biggest_data.append(subdata[0][1])
    total_data.append(len(subdata))
    sum = 0
    for values in subdata:
        sum += values[1]
    sum_data.append(sum)

# print(all_data)
# print(total_data)

# plt.plot(total_data)
# plt.ylabel("Number of species")
# plt.show()

# plt.plot(biggest_data)
# plt.ylabel("amount in biggest group")
# plt.show()

# plt.plot(np.array(biggest_data)/np.array(sum_data))
# plt.ylabel("fraction biggest to all")
# plt.show()

path1 = "Project/CSS_Alien/Pattern_data/OTS_2_Default_2/15"
path2 = "Project/CSS_Alien/Pattern_data/OTS_2_Default_2/10"

def compare_cols(path1, path2):
    num_cols1 = len(glob.glob1(path1,"*.col"))
    num_cols2 = len(glob.glob1(path2,"*.col"))
    
    couples = []
    for i in range(1,num_cols1+1):
        file1 = path1+"/cluster"+str(i).zfill(5)+".col"
        for j in range(1,num_cols2+1):
            file2 = path2+"/cluster"+str(j).zfill(5)+".col"
            if os.stat(file1).st_size == os.stat(file2).st_size:
                couples.append([i,j])
            
    # print(couples)
    return couples

# compare_cols(path1, path2)

def delete_double_cols(path):
    num_cols1 = len(glob.glob1(path,"*.col"))
    subdata = data_from_text(path+"/result.txt")
    # print(subdata)
    
    labelled_data = []

    for i in range(0,num_cols1):
        file1 = path+"/cluster"+str(i+1).zfill(5)+".col"
        labelled_data.append([str(os.stat(file1).st_size),subdata[i][1]])

    done = []
    filtered = []
    for i in range(len(labelled_data)):
        if labelled_data[i][0] not in done:
            sum = labelled_data[i][1]
            for j in range(i+1, len(labelled_data)):
                if labelled_data[j][0] not in done:
                    if labelled_data[i][0] == labelled_data[j][0]:
                        sum += labelled_data[j][1]
                        done.append(labelled_data[j][0])

            filtered.append([labelled_data[i][0],sum])
                
    # print(filtered)
    return filtered

# delete_double_cols(path)

def make_table():
    path1 = "Project/CSS_Alien/Pattern_data/OTS_2_Default_2/"
    table = []
    for step in range(0,15):
        path1 = path+str(step*5)
        # path2 = path+str((step+1)*5)
        # mapping = compare_cols(path1, path2)
        filtered = delete_double_cols(path1)
        table.append(filtered)
        # subdata1 = data_from_text(path1+"/result.txt")
        # subdata2 = data_from_text(path2+"/result.txt")
        # print(mapping)
        # print(subdata1)
        # print(subdata2)
        # print("NEXT")
    print(table)

    whole_table = []
    for time in table:
        


    return

make_table()