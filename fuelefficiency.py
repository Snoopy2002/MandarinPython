# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:33:47 2020

@author: Snoopy
"""

import pandas as pd
#import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt

def makeplot(cardatanew):
    scatterplot=plt.figure()
    ax1=scatterplot.add_subplot(1,1,1)
    ax1.scatter(x=cardatanew['Displacement in CC'], y=cardatanew['City CO2'])
    ax1.set_title("Plot of Engine Displacement vs City CO2 Production")
    ax1.set_xlabel("Engine Displacement in CC")
    ax1.set_ylabel("City CO2 in g/mile")
    scatterplot.show()
    
    
cardata=pd.read_csv('c:\\pythonprograms\\PandasForEveryone\\2018USfuelefficiency2.csv')
#print(cardata.columns)
#print(cardata.dtypes)
cardatanew=cardata[['Model Year', 'Division', 'Carline', 'Displacement in CC', 'City and Highway Mileage', 'Annual Fuel Cost', 'City CO2', 'Hwy CO2']]
#print(cardatanew.columns)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
'''with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(cardatanew)'''
cardatanew.sort_values('Displacement in CC', ascending=True, inplace=True)
model=sm.OLS(cardatanew['City and Highway Mileage'],cardatanew['Displacement in CC'])
model2=sm.OLS(cardatanew['Annual Fuel Cost'],cardatanew['Displacement in CC'])
model3=sm.OLS(cardatanew['City CO2'],cardatanew['Displacement in CC'])
model4=sm.OLS(cardatanew['Hwy CO2'],cardatanew['Displacement in CC'])
model5=sm.OLS(cardatanew['Annual Fuel Cost'],cardatanew['City and Highway Mileage'])
results1=model.fit()
results2=model2.fit()
results3=model3.fit()
results4=model4.fit()
results5=model5.fit()
print(results1.summary(), results2.summary(), results3.summary(), results4.summary(), results5.summary())
makeplot(cardatanew)
