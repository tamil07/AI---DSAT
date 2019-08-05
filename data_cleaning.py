import pandas
df=pd.read_csv(r'C:\Users\tamilarasan_j\Documents\Machine Learning\DSAT\Recent-Rawdata.csv', dtype={'event_date':'int64','response_date':'float64','sr_create_date':'int64','sr_close_date':'float64','so_inv_dt':'float64','so_dt':'float64','crt_dts':'object'})
df['event_date'] = pd.to_datetime(df['event_date'], format='%Y%m%d', errors='coerce')
df['C'] = pd.to_datetime(df['response_date'], format='%Y%m%d', errors='coerce')
df['sr_create_date'] = pd.to_datetime(df['sr_create_date'], format='%Y%m%d', errors='coerce')
df['sr_close_date'] = pd.to_datetime(df['sr_close_date'], format='%Y%m%d', errors='coerce')
df['so_inv_dt'] = pd.to_datetime(df['so_inv_dt'], format='%Y%m%d', errors='coerce')
df['so_dt'] = pd.to_datetime(df['so_dt'], format='%Y%m%d', errors='coerce')
df['crt_dts'] = pd.to_datetime(df['crt_dts'], format='%Y%m%d', errors='coerce')
df.to_csv(r'C:\Users\tamilarasan_j\Documents\Machine Learning\DSAT\Testing_Copy1.csv')

#Module to delete Naan
import pandas as pd
data=pd.read_csv(r'C:\Users\tamilarasan_j\Documents\Machine Learning\DSAT\Testing_Copy1.csv')
import sys
dfff=data['unvrsl_ovral_stsfctn_score_nbr'].isna() #Getting the boolean values of the column
dfff.to_csv(r'C:\Users\tamilarasan_j\Documents\Machine Learning\DSAT\isna.csv') #Exporting it to CSV
dfd=pd.read_csv(r'C:\Users\tamilarasan_j\Documents\Machine Learning\DSAT\isna.csv',header=None, names=['Index','unvrsl_ovral_stsfctn_score_nbr']
) #Reading and converting it to pandas Dataframe
print(dfd.index[dfd['unvrsl_ovral_stsfctn_score_nbr'] == True].tolist()) #Converting the index values to a list
print(type(dfd)) #Checking the type of dfd
print(dfd.index[dfd['unvrsl_ovral_stsfctn_score_nbr'] == True].tolist())
list1=dfd.index[dfd['unvrsl_ovral_stsfctn_score_nbr'] == True].tolist() #Saving the list to a variable
type(list1)
print(len(list1)) #Checking the list of the variable. 
for i in list1:
    data=data.drop(i) #Dropping all the columns of Null values.
#dfd.index[dfd['unvrsl_ovral_stsfctn_score_nbr'] == True].tolist() 
data.to_csv(r'C:\Users\tamilarasan_j\Documents\Machine Learning\DSAT\Cleansing.csv') #Exporting it to a file

#Module to delete values 0
import pandas as pd
data=pd.read_csv(r'C:\Users\tamilarasan_j\Documents\Machine Learning\DSAT\Cleansing.csv')
#print(data1.index[data['unvrsl_ovral_stsfctn_score_nbr'] == 0].tolist())
#print(data['unvrsl_ovral_stsfctn_score_nbr'] == )
x1=data[data['unvrsl_ovral_stsfctn_score_nbr'] != 0]
type(x1)
x1.to_csv(r'C:\Users\tamilarasan_j\Documents\Machine Learning\DSAT\Cleansing1.csv')

