#Code written by Dr Ben Coulson 2021

import pandas as pd
import os
import glob
import numpy as np
import math
from matplotlib import pyplot as plt

#this locates the current script's folder, then searches that folder for all files ending with .txt
abspath = os.path.abspath("ir_conv.py")
path = os.path.dirname(abspath)
raw_plots = glob.glob(path + "/*.asp")
#the code below removes the lengthly filepath and outputs a list of "file.txt" strings
filenames = [os.path.split(y)[1] for y in raw_plots]

#displays the filenames accessible
print(filenames)
    
   
#this function is complex! let's break it down.
def load_data(i):
    #this line just loads in the .txt file as a dataframe
    raw_input = pd.read_csv(i)
    #this converts the dataframe into a usable list
    data_list = list(raw_input[list(raw_input.columns)[0]])
    #the first 20 entires are metadata - you can access them if needed but we just cut them off for our purposes
  
    trans = data_list[5:]
    num_points = len(trans)
    start = data_list[0]
    end = data_list[1]
    interval = (start-end)/num_points
    wavenumbers = np.arange(start, end, -interval)
    absorbance = [2-(math.log(i, 10)) for i in trans]
    return wavenumbers, trans, absorbance

def output_txt(i, x, y, z):
    print(i)
    with open(str(i[:-4])+".txt", "w") as f:
        f.write("Wavenumber, Transmittance, Absorbance\n")
        for j, k, l in zip(x, y, z):
            f.write(str(j)+", "+str(k)+", "+str(l)+"\n")
    
def plot_data(i):
    x, y, z = load_data(i)
    plt.plot(x, y)
    plt.title("TRANS "+str(i))
    plt.tight_layout()
    plt.savefig("DRAFT_TRANS_"+str(i[:-4])+".png")
    #plt.show()
    plt.close()
    plt.plot(x, z)
    plt.title("ABS "+str(i))
    plt.tight_layout()
    plt.savefig("DRAFT_ABS_"+str(i[:-4])+".png")
    #plt.show()
    plt.close()
    output_txt(i, x, y, z)
      
    
for i in filenames:
    plot_data(i)
    



