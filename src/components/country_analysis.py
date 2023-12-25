from src.components import data_preprocessor
from src.exception import CustomException
import pandas as pd 
import numpy as np
import plotly.express as pe
import seaborn as sns
import matplotlib.pyplot as plt

prep = data_preprocessor.Preprocessor()

df = prep.preprocessor()
class CountryAnalysis:
    def __init__(self):
        self.df = df
        self.countryList = np.unique(self.df['region'].unique().tolist())
    def countryVal(self,country):
        try:
            temp_df = self.df.dropna(subset = ['Medal'])
            temp_df =temp_df.drop_duplicates(subset=['Team','NOC','Games','City','Sport','Event','Medal'])
            new_df = temp_df[temp_df['region']==country]
            country_df = new_df.groupby('Year').count()['Medal'].reset_index()
            country_df['Year'] = country_df['Year'].astype(str)
            return country_df
        except Exception as e:
            raise CustomException(e)
        
    def country_sport_analysis(self,country):
        try:
            temp_df = self.df.dropna(subset = ['Medal'])
            temp_df =temp_df.drop_duplicates(subset=['Team','NOC','Games','City','Sport','Event','Medal'])
            new_df = temp_df[temp_df['region']==country]
            new_df = new_df.pivot_table(index='Sport',columns='Year',values='Medal',aggfunc='count').fillna(0)
            fig,ax = plt.subplots(figsize=(10,20))
            ax = sns.heatmap(new_df,annot=True,cmap='Blues')
            return fig,ax
        except Exception as e:
            raise CustomException(e)
    def plotlyPlot(self,dfs,x,y):
        try:
            fig = pe.line(dfs,x=x,y=y)
            return fig
        except Exception as e:
            
            raise CustomException(e)
    def most_medals_player(self,country):
        try:
            temp_df = self.df.dropna(subset=['Medal'])
            temp_df=temp_df[temp_df['region'] == country]
            x= temp_df['Name'].value_counts().reset_index().head(10)
            x = x.merge(df,left_on='Name',right_on='Name',how='left')
            
            x = x[['Name','count','Sport','region']].drop_duplicates()
            return x
        except Exception as e:
            raise(e)
