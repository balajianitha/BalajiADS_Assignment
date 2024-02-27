# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 01:56:27 2024

@author: 
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def cleaning_data(df):
    """
    Funtion to drop unnecessary columns, transpose the data,
    rename few columns and set the index to year

    """
    #dropping unecessary data
    df = df.drop(['Country Name','Country Code','Series Code'],axis = 1)
    # Transpose the dataframe
    df_jobs_T = df.T
    df_jobs_T.columns = df_jobs_T.iloc[0]
    df_jobs_T = df_jobs_T.iloc[1:]
    #renaming the columns
    df_jobs_T = df_jobs_T.rename(columns=
     {'School enrollment, tertiary (% gross)': 
                     'Tertiary School Enrollment %',
      'School enrollment, secondary (% gross)':
                     'Secondary School Enrollment %',
      'Employment in industry (% of total employment) (modeled ILO estimate)':
                     'Industry Employment %',
      'Employment in agriculture (% of total employment) (modeled ILO estimate)'
                    :'Agriculture Employment %',
      'Employment in services (% of total employment) (modeled ILO estimate)':
                     'Services Employment %',
      'GDP per capita (constant 2005 US$)':'GDP per capita',
      'Population growth (annual %)':'Population Growth %'})

    # Set index name to year and removing unwanted data in years column
    df_jobs_T.index.name = 'Year'
    df_jobs_T.index = df_jobs_T.index.str[:4]
    df_jobs_T.index = pd.to_numeric(df_jobs_T.index)
    df_jobs_T.columns.name = ''
    return df_jobs_T

def  plot_line_graph(df):
    """
    Function to create a Line plot to observe the relation between Teritiary 
    and Secondary school enrollment
    """
    
    plt.figure(dpi =100)
    
    #plotting the data
    plt.plot( df.index,df['Tertiary School Enrollment %'],
                 label = 'Tertiary School Enrollment %')
    
    plt.plot( df.index,df['Secondary School Enrollment %'],
                 label = 'Secondary School Enrollment %')
    
    #Set title, x-axis label, y-axis label, and display legend
    plt.title('School Enrollment over Years')
    plt.xlabel('Years')
    plt.ylabel('Population Percentage')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.xlim(1995,2020)
    plt.legend()
    
    # Saving the plot
    plt.savefig('lineplot.png') 
    plt.show()
    return

def plot_pie_chart(df,year):
    """
    Function to create a pie chart of employment sectors in the year
    """
    
    #Array to have employment sector values 
    Employment = [df['Industry Employment %'][year],
                  df['Agriculture Employment %'][year],
                  df['Services Employment %'][year]]
    #variable for storing label names
    labels = ['Industry Employment %',
              'Agriculture Employment %',
              'Services Employment %']
    
    plt.figure(dpi=100)
    #plotting a pie chart
    plt.pie(Employment,labels=labels, autopct='%1.1f%%')
    
    #setting title
    plt.title( 'Employment Sectors')
    plt.axis('Equal')
    # Saving the plot
    plt.savefig('piechart.png')
    plt.show()
    return

def plot_heatmap(df):
    """
    Function to plot the Heatmap which describes the 
    correlation between the columns 
    """
    # Array for masking the similar data. 
    mask = np.triu(np.ones_like(df.corr()))
    
    plt.figure(dpi=100)
    # plotting the heatmap
    sns.heatmap(df.corr(),annot=True, mask=mask, cmap='Greens', linewidths=.5)
    plt.title('Correlation between various factors effecting jobs')
    # Saving the plot
    plt.savefig('Heatmap.png') 
    plt.show()
    return


#dataframes to store the data from csv files 
df_jobs= pd.read_csv('jobs_data.csv')

#cleaning the data
df_jobs =  cleaning_data (df_jobs)


print('Statistics of the factors', end='\n')
print(df_jobs.describe() , end='\n\n')

print('Skewness of the factors', end='\n')
print(df_jobs.skew() , end='\n\n')

print('Kurtosis of the factors', end='\n')
print(df_jobs.kurtosis() , end='\n\n')

print('Correlation of the factors', end='\n')
print(df_jobs.corr() , end='\n\n')

#plot the line graph

plot_line_graph(df_jobs)

#plot the pie chart

plot_pie_chart(df_jobs,1997)

#plot the heatmap

plot_heatmap(df_jobs)