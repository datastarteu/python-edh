# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


# Read data file
df = pd.read_csv("./data/loan.csv")


# Access the first 5 rows
df.head()

# Basic description of data types
df.info()

# Descriptive statistics
df.describe()

# Columns of the data frame
df.columns
## QUESTION: Is there gender bias
# in loan applications?

# Look at the loan status col
df['Loan_Status'].head()

# Gender
df['Gender'].head()

# Unique values in the data
df['Gender'].unique()

df['Loan_Status'].unique()

male = df[df['Gender']=='Male']
male.head()

female = df[df['Gender']=='Female']
female.head()

male.groupby('Loan_Status')['Loan_ID'].count()
female.groupby('Loan_Status')['Loan_ID'].count()

df.groupby(['Gender', 'Loan_Status'])['Loan_ID'].count()

#####################
### PLOTS
#####################

df.columns
df['ApplicantIncome'].hist()


## Subset and plot

df[df['ApplicantIncome']<15000]['ApplicantIncome'].hist()

# Other plots by default
df['ApplicantIncome'].plot.box()

# Default plot function
df['ApplicantIncome'].plot()


## Pivot table
df.pivot_table()


## Cross tab
pd.crosstab(df['Gender'],
            df['Loan_Status'])


# Combine groups and plots
df.boxplot(column='ApplicantIncome', 
           by='Gender'
           )


		   

