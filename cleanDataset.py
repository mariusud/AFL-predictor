# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np
import re
pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", 25)


# %%
match_results = pd.read_csv("datasets/results.csv")
player_stats = pd.read_csv("datasets/stats.csv")
odds = pd.read_csv("datasets/odds.csv") #delivered by footyWire


# %%
def get_cleaned_results():
    df = pd.read_csv("datasets/results.csv")
    df = ( df
            .drop(columns=['Unnamed: 0','Round.Type', 'Round']) 
            .rename(columns={'Game': 'game', 'Date' : 'date', 'Season' : 'season',
            'Home.Team' : 'home', 'Home.Goals' : 'goals', 'Home.Behinds' : 'behinds', 'Home.Points' : 'points',
            'Away.Team' : 'away', 'Away.Goals' : 'away goals', 'Away.Behinds' : 'away behinds', 'Away.Points' : 'away points',
            'Venue' : 'venue','Margin' : 'margin','Round.Number' : 'round'
            })
            .assign(result=lambda df: df.apply(lambda row: 1 if row['points'] > row['away points'] else 0, axis=1)) 
    )
    return df


clean_results = get_cleaned_results()
clean_results.tail(100)


# %%
form_btwn_teams = clean_results[['game', 'home', 'away', 'margin']].copy()
#Calculates 
form_btwn_teams['feature_MarginPast5'] = (clean_results.groupby(['home', 'away'])['margin']
                                                          .transform(lambda row: row.rolling(5).mean().shift())
                                                          .fillna(0))

form_btwn_teams['feature_WinLossPast5'] = (clean_results.assign(win=lambda df: df.apply(lambda row: 1 if row.margin > 0 else 0, axis='columns'))
              .groupby(['home', 'away'])['win']
              .transform(lambda row: row.rolling(5).mean().shift() * 5)
              .fillna(0))


# %%
features = clean_results[['date', 'game', 'home', 'away', 'venue', 'season']].copy()
feature_df = pd.merge(features, form_btwn_teams.drop(columns=['margin']), on=['game', 'home', 'away'])
feature_df = pd.merge(feature_df, clean_results[['game', 'result']], on='game')
feature_df.tail(5)


