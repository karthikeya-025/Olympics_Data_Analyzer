import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.express as px


from src.components.data_preprocessor import Preprocessor
from src.exception import CustomException
from src.components.overall_anlysis import OverallAnalysis

ota = OverallAnalysis()
 


prep = Preprocessor()
df = prep.preprocessor()

class AtleteAnalysis:
    def __init__(self):
        self.df = df
        self.sport = ota.sport
    def athletes_age_plot(self):
        try:
            athlete_df = self.df.drop_duplicates(subset=['Name','region'])
            x1 = athlete_df['Age'].dropna()
            x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
            x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
            x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
            fig = ff.create_distplot([x1,x2,x3,x4],['Overall Age','Gold Medalists','Silver Medalists','Bronze Medalists'],show_hist = False,show_rug = False)
            fig.update_layout(autosize=False,width=1000,height=600)
            return fig
        except Exception as e:
            raise CustomException(e)
    def sport_avg_age(self):
        try:
            athlete_df = self.df.drop_duplicates(subset=['Name','region'])
            famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
            x = []
            name = []
            for i in famous_sports:
                temp_df =athlete_df[athlete_df['Sport'] == i]
                x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
                name.append(i)
            
            fig = ff.create_distplot(x,name,show_hist=False,show_rug=False)
            fig.update_layout(autosize=False,width=1000,height=600)
            return fig
            
        except Exception as e:
            raise CustomException(e)
    def sport_scatter(self,sport):
        try:
            athlete_df = df.drop_duplicates(subset=['Name','region'])
            athlete_df['Medal'].fillna('No Medal',inplace=True)
            fig,ax = plt.subplots(figsize=(10,15))
            if sport!='Overall':
                sport_df = athlete_df[athlete_df['Sport']==sport]
                ax = sns.scatterplot(sport_df,x='Weight',y='Height',hue='Medal',style='Sex',s=100)
                return fig,ax
            ax = sns.scatterplot(athlete_df,x='Weight',y='Height',hue='Medal',style='Sex',s=100)
            return fig,ax
        except Exception as e:
            raise CustomException(e)
    def men_vs_women(self):
        try:
            athlete_df = df.drop_duplicates(subset=['Name','region'])
            men = athlete_df[athlete_df['Sex'] == 'M'].groupby("Year").count()['Name'].reset_index()
            women = athlete_df[athlete_df['Sex'] == 'F'].groupby("Year").count()['Name'].reset_index()
            final = men.merge(women,on='Year',how='left').fillna(0)
            final = final.rename(columns={'Name_x':'Men','Name_y':'Women'})
            fig = px.line(final,x='Year',y=['Men','Women'])
            fig.update_layout(autosize=False,width=1000,height=600)
            return fig
        except Exception as e:
            raise CustomException(e)