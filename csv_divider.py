import pandas as pd

chunk_size = 700000    #how many lines per file you want to have. In this example a large (3 million lines) file will be divided into batches of 700,000 lines
batch_no = 1           #needed to name the files, no need to edit


for chunk in pd.read_csv('E:\Bogdan\Downloads\Cross_Coding_Details_Report_2399115_16062020_120456.CSV', chunksize=chunk_size):     # here provide path to the file that needs to be divided
   chunk.to_csv('Cross_Coding_Details_Report_2399115_16062020_120456' +str(batch_no) +'.csv', index=False)   #splitting into batches and naming them with name + number 1, 2, 3 etc
   batch_no +=1   