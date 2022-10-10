#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 21:23:57 2022

@author: Serah Elsa Abraham
"""

#%%
# import libraries



import pandas as pd
import matplotlib.pyplot as plt


####### Initializing  ###########

dpi = 300
project_dir = r'/Users/ashithacprasad/Desktop/Data_Science/sem5/Data_Visualization/week5/'
df1_filename = 'Supermarket.csv'
df2_filename = 'insurance.csv'
df3_filename = 'heart.disease.csv'

####### End of Initializing  ###########

######## Visualization 1 - Bar chart ####

df1 = pd.read_csv(project_dir + df1_filename)
columns = list(df1.columns)


country_counts = df1['Country'].value_counts(ascending=False)
country = pd.Series(list(country_counts.index))
country_counts.index = range(len(country_counts))

fig, ax = plt.subplots(figsize=(12,6))

ax.bar(country, country_counts)
ax.set_title('Sales Order by Country')
ax.set_xlabel('Country')
ax.set_xticklabels(country, fontsize=8)
ax.set_ylabel('Sales Count')

plt.tight_layout()

plot1_filename = 'Country.png'
fig.savefig(project_dir + plot1_filename, dpi=dpi)

######## End of Visualization 1 -Bar chart ####

######## Visualization 2 - Scatter plot ####

df2 = pd.read_csv(project_dir + df2_filename)
columns = list(df2.columns)
fig, ax = plt.subplots(figsize=(12,8))

bmi = df2.iloc[:,2]
charges = df2.iloc[:,6]


ax.scatter(bmi, charges, alpha=.5)
ax.set_title('BMI and Insurance charges')
ax.set_xlabel('Bmi')
ax.set_ylabel('Charges')



plt.tight_layout()

plot2_filename = 'bmi.png'
fig.savefig(project_dir + plot2_filename, dpi=dpi)

######## End of Visualization 2 - Scatter plot ####

######## Visualization 3 -Line chart ####

df3 = pd.read_csv(project_dir + df3_filename)

df3.sex.replace(0,'Female',inplace=True)
df3.sex.replace(1,'Male',inplace=True)
ax.set_title('Number of heart disease and Survival rate - Female vs Male')
ax.set_xlabel('Number of heart disease')
ax.set_ylabel('Age')
fig, ax = plt.subplots(figsize=(15,7))

df3.groupby(['num','sex']).count()['age'].unstack().plot(ax=ax)

plt.tight_layout()
plot3_filename = 'heart.png'
fig.savefig(project_dir + plot3_filename, dpi=dpi)


######## End of Visualization 3 -Line chart ####
