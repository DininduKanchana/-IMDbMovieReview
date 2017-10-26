from os import listdir
import pandas as pd
import glob
import os
import time

positiveList =  listdir("../aclImdb/train/pos")
negativeList =  listdir("../aclImdb/train/neg")
cols = ['review', 'sentiment']

frame = pd.DataFrame(columns = cols)
start = time.time()
"""getting positives"""
for filename in positiveList:
    sentiment = (filename.split("_")[1]).split(".")[0]
    file = open("../aclImdb/train/pos/" + filename, "r") 
    text = file.read()
    df = pd.DataFrame([[text, sentiment]], columns = cols)
    frame = pd.concat([frame, df])
    

"""getting negatives"""
for filename in negativeList:
    sentiment = (filename.split("_")[1]).split(".")[0]
    file = open("../aclImdb/train/neg/" + filename, "r") 
    text = file.read()
    df = pd.DataFrame([[text, sentiment]], columns = cols)
    frame = pd.concat([frame, df])
    

print(frame.head())
frame.to_csv('./frame.csv', index=False)

done = time.time()
elapsed = done - start
print("--- %s seconds ---" % elapsed)
