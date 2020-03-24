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
fixtures = pd.read_csv("datasets/fixtures.csv")
ladder = pd.read_csv("datasets/ladder.csv")

# %% 
ladder.tail(3)

# %%
odds.tail(3)

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

# %%
def get_home_ladder():
    df = pd.read_csv("datasets/ladder.csv")
    df = ( df
            .drop(columns=['Unnamed: 0','Percentage'])
            .rename(columns={'Season' : 'season', 'Team' : 'home', 'Round.Number' : 'round',
            'Season.Points' : 'feature_points', 'Score.For' : 'feature_scored', 'Score.Against' : 'feature_conceded', 'Ladder.Position' : 'homeLadderPosition'
            })
            )
    return df


def get_away_ladder():
    df = pd.read_csv("datasets/ladder.csv")
    df = ( df
            .drop(columns=['Unnamed: 0','Percentage', 'Season.Points', 'Score.For', 'Score.Against'])
            .rename(columns={'Season' : 'season', 'Team' : 'away', 'Round.Number' : 'round',
            'Ladder.Position' : 'awayLadderPosition'
            })
            )
    return df
# %%%
clean_results = get_cleaned_results()
clean_results.tail(100)
# %%
ladder = get_away_ladder()
ladder.tail(10)
# %%
