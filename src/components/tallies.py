import pandas as pd
import numpy as np
from src.exception import CustomException

from src.components.data_preprocessor import Preprocessor

prep = Preprocessor()

df = prep.preprocessor()
class Tallies:
    def __init__(self,df=df):
        self.df = df

    def medal_tally(self):
        try:
            medal_tally = self.df.drop_duplicates(subset=["Team", "NOC", "Games", "City", "Sport", "Event", "Medal"])
            years = list(np.unique(sorted(medal_tally['Year'])))
            years.insert(0,'Overall')
            regions = list(np.unique(list(medal_tally['region'])))
            regions.insert(0,'Overall')
            
            medal_tally = medal_tally.groupby(["region"]).sum()[["Gold", "Silver", "Bronze"]].sort_values(by="Gold", ascending=False).reset_index()
            

            medal_tally["Total"] = medal_tally["Gold"] + medal_tally["Silver"] + medal_tally["Bronze"]

            return medal_tally,years,regions
        except Exception as e:
            raise CustomException(e)
    def fect_medal_tally(self,year,country,):
        try:
            flag = 0
            if country=='Overall' and year=='Overall':
                temp_df = self.df
                
            if country!='Overall' and year=='Overall':
                flag =1
                temp_df = self.df[self.df['region'] == country]
                
            if country == 'Overall' and year!='Overall':
                temp_df = self.df[self.df['Year'] == year]
                
            if country!='Overall' and year!='Overall':
                temp_df = self.df[(self.df['Year'] == year)&(self.df['region']==country)]
                
            x  = temp_df.drop_duplicates(subset=["Team", "NOC", "Games", "City", "Sport", "Event", "Medal"])
            
            if flag == 1:
                x  = temp_df.groupby(["Year"]).sum()[["Gold", "Silver", "Bronze"]].sort_values(by="Gold", ascending=False).reset_index()
                x = x.sort_values(by='Year',ascending=True)
                x['Year'] = x['Year'].astype(str)
                
            else:
                x  = temp_df.groupby(["region"]).sum()[["Gold", "Silver", "Bronze"]].sort_values(by="Gold", ascending=False).reset_index()

            x["Total"] = x["Gold"] + x["Silver"] + x["Bronze"]
            
            return x
        except Exception as e:
            raise CustomException(e)