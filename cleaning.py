import pandas as pd
import numpy as np

hotels=pd.read_csv('zomato.csv')

print(hotels.head())

#task1: remove unwanted columns
hotels.drop(['address','phone'],axis=1,inplace=True)

hotels.info()

#rename columns,  only the below renamed columns are allowed in the dataset

hotels.rename(columns= {'rate':'rating','approx_cost(for two people)':'approx_cost','listed_in(type)':'type'},inplace=True)
hotels.info()

#handle  null values of each column
print(hotels.isnull().sum())

#deleting null values of name column
hotels.dropna(subset=['name'],inplace=True)
print(hotels.isnull().sum())

#handling null values of online_order
hotels['online_order'].fillna('NA',inplace=True)
print(hotels.isnull().sum())

#changing null values of book_table
hotels['book_table'].fillna('NA',inplace=True)
print(hotels.isnull().sum())

#changing null values of rating to zero as it is a numerical datatype
hotels['rating'].fillna(0,inplace=True)
print(hotels.isnull().sum())

#changing null values of votes to zero as it is a numerical datatype
hotels['votes'].fillna(0,inplace=True)
print(hotels.isnull().sum())

#changing null values of location to NA
hotels['location'].fillna('NA',inplace=True)
print(hotels.isnull().sum())

#changing null values of rest_type to NA
hotels['rest_type'].fillna('NA',inplace=True)
print(hotels.isnull().sum())

#changing null values of dishliked to NA
hotels['dish_liked'].fillna('NA',inplace=True)
print(hotels.isnull().sum())

#changing null values of cuisines to NA
hotels['cuisines'].fillna('NA',inplace=True)
print(hotels.isnull().sum())

#changing null values of approxcost to 0 as it is a numerical value
hotels['approx_cost'].fillna(0,inplace=True)
print(hotels.isnull().sum())

#changing null values of type to NA
hotels['type'].fillna('NA',inplace=True)
print(hotels.isnull().sum())


hotels.info()

#find duplicates in the dataset
print(hotels.duplicated())
#droping the duplicates value keeping the first
hotels.drop_duplicates(inplace=True,keep='first')
print(hotels.duplicated().sum())

hotels.info()

#we have irrelevant reviews like string(RATED,Rated) in our name,online_order etc columns
#removing irrelevant text from all the columns
'''
filtered_hotels=hotels[hotels['name'].str.contains('RATED|Rated')==False]
filtered_hotels1=filtered_hotels[filtered_hotels['type'].str.contains('RATED|Rated')==False]
filtered_hotels2=filtered_hotels1[filtered_hotels1['approx_cost'].str.contains('RATED|Rated')==False]
filtered_hotels3=filtered_hotels2[filtered_hotels2['cuisines'].str.contains('RATED|Rated')==False]
filtered_hotels4=filtered_hotels3[filtered_hotels3['dish_liked'].str.contains('RATED|Rated')==False]
filtered_hotels5=filtered_hotels4[filtered_hotels4['rest_type'].str.contains('RATED|Rated')==False]
filtered_hotels6=filtered_hotels5[filtered_hotels5['location'].str.contains('RATED|Rated')==False]
filtered_hotels7=filtered_hotels6[filtered_hotels6['votes'].str.contains('RATED|Rated')==False]
filtered_hotels8=filtered_hotels7[filtered_hotels7['rating'].str.contains('RATED|Rated')==False]
filtered_hotels9=filtered_hotels8[filtered_hotels8['book_table'].str.contains('RATED|Rated')==False]




#check for unique values in each column and handle the irrelevant values

print(filtered_hotels9['name'].unique())


#online order table should have only yes and no, remove other values
print(filtered_hotels9['online_order'].unique())

filtered_hotels10=filtered_hotels9[filtered_hotels9['online_order'].str.contains('Yes|No')==True]

print(filtered_hotels10['online_order'].unique())

#check for rating table and remove NEW,- values to 0 and remove /5

filtered_hotels10['rating'].replace(to_replace='NEW', value=0,inplace=True)
filtered_hotels10['rating'].replace(to_replace='-', value=0,inplace=True)
filtered_hotels10['rating'].replace(regex='/5',value='',inplace=True)
print(filtered_hotels10['rating'].unique())


#remove unkwon charachter from names column

filtered_hotels10['name']=filtered_hotels10['name'].str.replace('[Ãx][^A-Za-z]+','',regex=True)


filtered_hotels10.to_csv('zomatocleaned_v1.csv')




'''











