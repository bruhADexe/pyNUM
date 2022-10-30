from operator import index

import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# check panda version

print(pd.__version__)

# Series is like a column in table and hold elements in array like manner

a = [1, 2, 5, 78]

var = pd.Series(a)

print(var)
# lables , i.e. index number
print(var[1])
# with index , can have custom lables that can be used in accessing the elements
a = [1, 7, 2]

myvar = pd.Series(a, index=["x", "y", "z"])

print(myvar)
print(myvar["z"])
# series can store in key value pair just like dictionary
marks = {"ex1": 78, "ex2": 99}
print(marks)

var = pd.Series(marks, index=["ex1"])
print(var)

# DataFrames , Series is like a column while dataframes are whole multidimensional tables

data = {
    "mark": [89, 87, 55],
    "markk": [55, 65, 11]
}

var = pd.DataFrame(data)
print(var)
# locate : Pandas use the loc attribute to return one or more specified row
# in df index arguments can also be used to have index name as per the choice
print("locate")
print(var.loc[1])

# dataframes for reading csv

df = pd.read_csv(r'C:\Users\pandy\PycharmProjects\pythonProject\example.csv')
print(df)
# for selected columns from the csv
dff = pd.DataFrame(df, columns=['period'])
print(dff)
# operations on the loaded csv
sum1 = df['Data_value'].sum()
print(sum1)

# {{{
# mean1 = df['Salary'].mean()
# sum1 = df['Salary'].sum()
# max1 = df['Salary'].max()
# min1 = df['Salary'].min()
# count1 = df['Salary'].count()
# median1 = df['Salary'].median()
# std1 = df['Salary'].std()
# var1 = df['Salary'].var()
#
# # block 2 - group by
# groupby_sum1 = df.groupby(['Country']).sum()
# groupby_count1 = df.groupby(['Country']).count()
#
# # print block 1
# print ('Mean salary: ' + str(mean1))
# print ('Sum of salaries: ' + str(sum1))
# print ('Max salary: ' + str(max1))
# print ('Min salary: ' + str(min1))
# print ('Count of salaries: ' + str(count1))
# print ('Median salary: ' + str(median1))
# print ('Std of salaries: ' + str(std1))
# print ('Var of salaries: ' + str(var1))
#
# # print block 2
# print ('Sum of values, grouped by the Country: ' + str(groupby_sum1))
# print ('Count of values, grouped by the Country: ' + str(groupby_count1))
# }}}

# javascript object notation(JSON)
print("::::json::::")
df = pd.read_json(r'C:\adarsh\example_2.json')
print(df)
# JSON have same formate as directories,
# so if its not in file but in python dir it can be loaded into DataFrames directcly
data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}

df = pd.DataFrame(data)

print(df)

# head() method returns the first specified number of data rows of the frame
# similarly the tail() method return the last specified number of data rows of the frame
print("head and tail method")
df = pd.read_csv(r'c:\adarsh\data.csv')
print(df.head(5))
print(df.tail(2))

# info() method gives us more information related to the data set.
print(df.info())

#            Pandas
# Data cleaning means fixing bad data in your data set.
#
#        Bad data could be:
#
#          Empty cells
#      Data in wrong format
#          Wrong data
#          Duplicates

df = pd.read_csv(r'c:\adarsh\data.csv')

new_df = df.dropna()
print(new_df.to_string())

# by default dropna() returns new DataFrames
# but in order to do changes into the original dataframes dropnaa(inplace = true) is required

# fillna() allows to replace empty cells with the new given value

df.fillna(69, inplace=True)
# df["column name"].fillna(69, inplace = True) for specific column
#
# # Replace empty cells with mean value of the column
# # same thing can be done for median and mode (most frequently appearing entry)
# m = df["Calories"].mean()
# df["Calories"].fillna(m, inplace=True)
# # changing values in date formate
# # df['Date'] = pd.to_datetime(df['Date'])
# # print(df.to_string())
# # removing rows with null values
#
# # df.dropna(subset=['Date'], inplace=True)
# # replacing the data
# df.loc[7, "Duration"] = 45
# # Using for loop
# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#       df.loc[x, "Duration"] = 120
# # Removing rows
# for x in df.index:
#     if df.index[x, "Duration"] > 120:
#       df.drop(x, inplace=True)
#
# print(df.duplicated())
# # Removing duplicates
# df.drop_duplicates(inplace=True)

# corr() method calculates the relations between each column in your dataset
# df = pd.read_csv(r'c:/adarsh/data(1).csv')
# print(df.corr())

# the number will vary from -1 to 1 , anything above or below 0.6 or -0.6 is a good relation ,
# 0.2 is a bad relation because then we won't be able to tell if we increase value of one column ,
#  the other will go up or not

# plotting
import sys
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt

df = pd.read_csv(r'c:/adarsh/data.csv')
df.plot()
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

df.plot(kind= 'scatter', x = 'Duration', y = 'Calories')
plt.show()

df.plot(kind= 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()

df["Duration"].plot(kind = 'hist')
plt.show()

