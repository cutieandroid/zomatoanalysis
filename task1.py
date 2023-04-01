import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore", message="pandas only supports SQLAlchemy connectable")
#pd.set_option('mode.chained_assignment', 'raise')
#pd.set_option('mode.chained_assignment', 'warn')

def read_data_from_csv():
    hotels=pd.read_csv('zomato.csv')
    #print(hotels.head())
    return hotels
#print(read_data_from_csv())

def remove_unwanted_columns():
    hotels=read_data_from_csv()
    hotels.drop(['address','phone'],axis=1,inplace=True)
    #hotels.info()
    return hotels
#print(remove_unwanted_columns())

#task2
# rename columns,  only these columns are allowed in the dataset
# 1.	Id
# 2.	Name
# 3.	online_order
# 4.	book_table
# 5.	rating
# 6.	votes
# 7.	location
# 8.	rest_type
# 9.	dish_liked
# 10.	cuisines
# 11.	approx_cost
# 12.	type
def rename_columns():
    hotels = remove_unwanted_columns()
    hotels.rename(columns= {'rate':'rating','approx_cost(for two people)':'approx_cost','listed_in(type)':'type'},inplace=True)
    #hotels.info()
    return hotels
#print(rename_columns())

#task3: handle  null values of each column
def null_value_check():
    hotels=rename_columns()
    #handle  null values of each column
    #print(hotels.isnull().sum())

    #delete null values of name column as name is the primary identifier of the dataset
    hotels.dropna(subset=['name'],inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of online order with NA
    hotels['online_order'].fillna('NA',inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of book_table with NA
    hotels['book_table'].fillna('NA',inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of rating to zero as it is a numerical datatype
    hotels['rating'].fillna(0,inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of votes to zero as it is a numerical datatype
    hotels['votes'].fillna(0,inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of location to NA
    hotels['location'].fillna('NA',inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of rest_type to NA
    hotels['rest_type'].fillna('NA',inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of dishliked to NA
    hotels['dish_liked'].fillna('NA',inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of cuisines to NA
    hotels['cuisines'].fillna('NA',inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of approxcost to 0 as it is a numerical value
    hotels['approx_cost'].fillna(0,inplace=True)
    #print(hotels.isnull().sum())

    #replace null values of type to NA
    hotels['type'].fillna('NA',inplace=True)
    #print(hotels.isnull().sum())


    #hotels.info()
    return hotels
    #return hotels.isnull().sum()
#print(null_value_check())

#task4 #find duplicates in the dataset
def find_duplicates():
    hotels=null_value_check()
    #print(hotels.duplicated())
    #droping the duplicates value keeping the first
    hotels.drop_duplicates(inplace=True,keep='first')
    #print(hotels.duplicated().sum())
    #hotels.info()
    return hotels
#print(find_duplicates())

#task5 removing irrelevant text from all the columns
#we have irrelevant reviews like string(RATED,Rated) in our name,online_order etc columns
#removee these irrelevant text from all the columns
def removing_irrelevant_text():
    hotels= find_duplicates()
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
    return filtered_hotels9
#print(removing_irrelevant_text())

#task6: check for unique values in each column and handle the irrelevant values
def check_for_unique_values():
    filtered_hotels9=removing_irrelevant_text()
    #print(filtered_hotels9['name'].unique())


    #online order table should have only yes and no because it is necessary to have the online order as yes or no only, remove other values
    #print(filtered_hotels9['online_order'].unique())

    filtered_hotels10=filtered_hotels9[filtered_hotels9['online_order'].str.contains('Yes|No')==True]

    #print(filtered_hotels10['online_order'].unique())

    #check for rating table and remove NEW,- values to 0 and remove /5 as rating column should only contain decimal values

    filtered_hotels10['rating'].replace(to_replace='NEW', value=0,inplace=True)
    filtered_hotels10['rating'].replace(to_replace='-', value=0,inplace=True)
    filtered_hotels10['rating'].replace(regex='/5',value='',inplace=True)
    #print(filtered_hotels10['rating'].unique())

    return filtered_hotels10

#print(check_for_unique_values())

#task7: remove the unknown character from the dataset, we have Ã charachter in our names column
def remove_the_unknown_character():
    filtered_hotels10=check_for_unique_values()
    filtered_hotels10['name']=filtered_hotels10['name'].str.replace('[Ãx][^A-Za-z]+','',regex=True)
    return filtered_hotels10
#print(remove_the_unknown_character())

#task8 export_the_cleaned_set()
def export_the_cleaned_set():
    filtered_hotels10=remove_the_unknown_character()
    filtered_hotels10.to_csv('zomatocleaned_v2.csv')
    #print("dataset saved")
    return filtered_hotels10
#print(export_the_cleaned_set())

#task9: Use this final dataset and upload it on the provided database for performing analysis in  MySQL
#To Run this task first Run the appliation for Terminal to create table named 'Zomato' and then run test.
def task_runner():
    dataframe = remove_the_unknown_character()
    dataframe.to_csv('zomatocleaned_v2.csv')
    #print(dataframe)


task_runner()
