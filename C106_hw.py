import csv
import pandas as pd
import plotly.express as px
import numpy as np


def getdatasource():
    coffee=[]
    sleep=[]

    with open('data2.csv') as f:
        file=csv.DictReader(f)

        graphfile=pd.read_csv('data2.csv')
        
        graph =px.scatter(graphfile,x='Coffee in ml',y='sleep in hours')
        graph.show()

        for i in file:
            coffee.append(float(i['Coffee in ml']))
            sleep.append(float(i['sleep in hours']))


    return {'x':coffee,'y':sleep}





def find_correlation(datasource):
    correlation=np.corrcoef(datasource['x'],datasource['y'])

    print('Correlation of Coffe vs sleep : ',correlation[0,1])





def setup():
    datasource = getdatasource()

    find_correlation(datasource)


setup()


#-------------------------------------------------------------------

def getdatasource1():
    days=[]
    marks=[]

    with open('data4.csv') as f1:
        file1=csv.DictReader(f1)

        graphfile1=pd.read_csv('data4.csv')
        
        graph1 =px.scatter(graphfile1,x='Days Present',y='Marks In Percentage')
        graph1.show()

        for i in file1:
            days.append(float(i['Days Present']))
            marks.append(float(i['Marks In Percentage']))


    return {'x':days,'y':marks}





def find_correlation1(datasource1):
    correlation1=np.corrcoef(datasource1['x'],datasource1['y'])

    print('Correlation of Marks vs Days present : ',correlation1[0,1])





def setup1():
    datasource1 = getdatasource1()

    find_correlation1(datasource1)


setup1()