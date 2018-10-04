# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 21:06:39 2017

@author: pc
"""
import pandas as pd
import numpy as np

df = pd.read_csv("orders.csv")

# Basic data exploration
df.head()
df.info()
df.describe()

# Type coercion: Get sure the data is read on the right time
df['Customer ID'] = df['Customer ID'].astype(str)
df['Date'] = pd.to_datetime(df['Date'])

# Looking at some columns
df['Subtotal'].hist(bins=20)

# Filtering out by large, outlier-ish values
df[df['Subtotal']<200]['Subtotal'].hist()


########################
### Group operations
########################

# Total per country
df.groupby('Country')['Subtotal'].apply(sum)


# Show the countries with the highest sold
df.groupby('Country')['Subtotal'].apply(sum)
df.groupby('Country')['Subtotal'].apply(lambda x: np.sum(x))

df.groupby('Country')['Subtotal'].apply(lambda x: np.sum(x)).sort_values()

# Default is by ascending order
df.groupby('Country')['Subtotal'].apply(lambda x: np.sum(x)).sort_values(ascending=False)


df2 =df.groupby('Country')['Subtotal'].agg({'Total_per_Country':np.sum})
df3 =df.groupby('Country')['Subtotal'].agg({'Avg_per_Country':np.mean})

# 'Country' gets a special treatment in pandas... it becomes an index column
df2.reset_index(inplace=True)

df.groupby('Country')['Subtotal'].apply(sum).plot.bar()

df[df['Country']!='Canada'].groupby('Country')['Subtotal'].apply(sum).plot.bar()
df[~df['Country'].isin(['Canada','United States'])].groupby('Country')['Subtotal'].apply(sum).plot.bar()


## USEFUL COMPARISON BETWEEN DPLYR AND PANDAS
# https://gist.github.com/conormm/fd8b1980c28dd21cfaf6975c86c74d07


### MORE COMPLICATED EXPERIMENTS: Tableau Superstore
tb = pd.read_csv("superstore.csv", encoding="cp1252")


# Problems with unfitting columns?
pd.set_option('display.max_columns', 500)

tb['Profit'] = tb['Profit'].apply(lambda x:x.replace('$',''))
tb['Profit'] = tb['Profit'].apply(lambda x:x.replace(',',''))
tb['Profit'] = tb['Profit'].astype(float)


# Create new 'Distribution center' column
tb['Distribution Center'] = tb['Order ID'].apply(lambda x: x.split('-')[0])


# Find the least profitable distribution center
tb.groupby('Distribution Center')['Profit'].apply(lambda x: np.sum(x)/1000).sort_values().head()

tb.groupby('Country')['Profit'].apply(lambda x: np.sum(x)/1000).sort_values().tail()
tb.groupby('Country')['Profit'].apply(lambda x: np.sum(x)/1000).sort_values(ascending=False).head()

#####################################################################
### EXERCISE
###################################################################### 
# Find the least profitable category
