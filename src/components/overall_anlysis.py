from src.exception import CustomException
import pandas as pd
import numpy as np
from src.components.data_preprocessor import Preprocessor
import plotly.express as pe
import seaborn as sns
import matplotlib.pyplot as plt

prep = Preprocessor()
df = prep.preprocessor()

class OverallAnalysis:
    def __init__(self,df=df):
        self.df = df
        self.sport = np.unique(df['Sport'])
    def overall_vals(self):
        try:
            sports = self.df['Sport'].unique().shape[0]
            editions = self.df['Year'].unique().shape[0]
            cities = self.df['City'].unique().shape[0]
            events = self.df['Event'].unique().shape[0]
            athletes = self.df['Name'].unique().shape[0]
            nations = self.df['region'].unique().shape[0]
            return sports,editions,cities,events,athletes,nations
        except Exception as e:
            raise CustomException(e)
    def plotly_chart(self,col):
        try:
            nation_wise_df =self.df.drop_duplicates(["Year",col])['Year'].value_counts().reset_index()
            nation_wise_df = nation_wise_df.rename(columns = {'count':f'{col} Count'})
            nation_wise_df = nation_wise_df.sort_values(by='Year')
            fig = pe.line(nation_wise_df,x='Year',y=f'{col} Count')
            return fig
        except Exception as e:
            raise CustomException(e)
    def heatmap(self):
        try:
            fig,ax = plt.subplots(figsize=(20,20))
            x = self.df.drop_duplicates(['Year','Event','Sport'])
            x = x.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype(int)
            ax = sns.heatmap(x,annot=True,cmap='Blues')
            return fig,ax
        except Exception as e:
            raise CustomException(e)
    
    def decorated_athletes(self,sport):
        try:
            temp_df = self.df.dropna(subset=['Medal'])
            if sport != 'Overall':
                temp_df=temp_df[temp_df['Sport'] == sport]
            x= temp_df['Name'].value_counts().reset_index().head(15)
            x = x.merge(self.df,left_on='Name',right_on='Name',how='left')
            
            x = x[['Name','count','Sport','region']].drop_duplicates()
            return x
        except Exception as e:
            raise CustomException(e)
    