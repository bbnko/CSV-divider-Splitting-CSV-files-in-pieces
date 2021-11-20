import pandas as pd

chunk_size = 700000
batch_no = 1

for chunk in pd.read_csv('E:\Bogdan\Downloads\Cross_Coding_Details_Report_2399115_16062020_120456.CSV', chunksize=chunk_size):
   chunk.to_csv('Cross_Coding_Details_Report_2399115_16062020_120456' +str(batch_no) +'.csv', index=False)
   batch_no +=1