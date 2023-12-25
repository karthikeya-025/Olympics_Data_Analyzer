import pandas as pd
import streamlit as st
from src.components.data_preprocessor import Preprocessor
from src.components.tallies import Tallies
from src.components.overall_anlysis import OverallAnalysis
from src.components.country_analysis import CountryAnalysis
from src.components.athletes_analysis import AtleteAnalysis


prep = Preprocessor()

df = prep.preprocessor()

tally = Tallies()

medal_tally,years,regions = tally.medal_tally()



user_opt = st.sidebar.radio(
    "Choose an option",
    (
        "Medal Tally",
        "Overall Analysis",
        "Country-Wise Analysis",
        "Athlete-Wise Analysis",
    ),
)

if user_opt == "Medal Tally":
    st.sidebar.header('Medal Tally')
    select_year = st.sidebar.selectbox("Select an year",years)
    select_region = st.sidebar.selectbox("Select an year",regions)
    if select_year == 'Overall' and select_region == 'Overall':
        st.title('Overall Tally')
    elif select_year != 'Overall' and select_region == 'Overall':
        st.title(f'Medal Tally in {select_year} Olympics')
    elif select_year == 'Overall' and select_region != 'Overall':
        st.title(f'Overall Medals of {select_region}')
    elif select_year != 'Overall' and select_region != 'Overall':
        st.title(f'Medals of {select_region} in {select_year} Olympics')
    
    
    x = tally.fect_medal_tally(select_year,select_region)
    
    
    
    st.table(x)
elif user_opt == 'Overall Analysis':
    ova = OverallAnalysis()
    sports,editions,cities,events,athletes,nations = ova.overall_vals()
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('Editions')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('Nations')
        st.title(nations)
    with col2:
        st.header('Events')
        st.title(events)
    with col3:
        st.header('Athletes')
        st.title(athletes)
    fig_1 = ova.plotly_chart('region')
    fig_2 = ova.plotly_chart('Event')
    fig_3 = ova.plotly_chart('Name')
    fig,ax = ova.heatmap()
    st.title('Participating Nations over the years')
    st.plotly_chart(fig_1)
    st.title('Sporting Events over the years')
    st.plotly_chart(fig_2)
    st.title('Athletes over the years')
    st.plotly_chart(fig_3)
    
    st.title('Sports over the years')
    st.pyplot(fig)
    
    
    st.title('Most Succesful Players')
    sport_list = list(ova.sport)
    sport_list.insert(0,'Overall')
    sport_select = st.selectbox('Sports',sport_list)
    
    players = ova.decorated_athletes(sport_select)
    st.table(players)
    
    
elif user_opt == 'Country-Wise Analysis':
    cta = CountryAnalysis()
    

    countryList = cta.countryList
    
    selection = st.sidebar.selectbox('Countries',countryList)
    cdf = cta.countryVal(selection)
    
    fig = cta.plotlyPlot(cdf,'Year','Medal')
    
    st.title(f"{selection} Medals")
    st.plotly_chart(fig)
    
    fig1,ax = cta.country_sport_analysis(selection)
    st.title(f"{selection}'s Performance in various sports")
    st.pyplot(fig1)
    
    players = cta.most_medals_player(selection)
    st.title(f'Top 10 players from {selection}')
    st.table(players)
elif user_opt == 'Athlete-Wise Analysis':
    athletean = AtleteAnalysis()
    figure = athletean.athletes_age_plot()
    st.title('Overall Age distribution of athletes')
    st.plotly_chart(figure)
    figure_2 = athletean.sport_avg_age()
    st.title('Age distribution of Gold medalists in Famous Sports')
    st.plotly_chart(figure_2)
    
    ova = OverallAnalysis()
    sports = list(ova.sport)
    sports.insert(0,'Overall')
    sport_select = st.selectbox('Sports',sports)
    fig_4,ax_4 = athletean.sport_scatter(sport_select)
    st.title(f"{sport_select} Height Vs Weight plot")
    st.pyplot(fig_4)
    
    fig_5 = athletean.men_vs_women()
    st.title('Men vs Women Participation in Olympics')
    st.plotly_chart(fig_5)
    
    