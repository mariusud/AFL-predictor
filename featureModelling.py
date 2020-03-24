# %%

import pandas as pd
import numpy as np
import re
pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", 25)
from cleanDataset import get_cleaned_results, get_home_ladder, get_away_ladder

clean_results = get_cleaned_results()
## Feature creation

# Feature 1 : Historical win/loss and total margin between the two teams
def get_feature_1():
    form_btwn_teams = clean_results[['game', 'home', 'away', 'margin']].copy()
    form_btwn_teams['feature_MarginPast5'] = (clean_results.groupby(['home', 'away'])['margin']
                                                              .transform(lambda row: row.rolling(5).mean().shift())
                                                              .fillna(0))
    form_btwn_teams['feature_WinLossPast5'] = (clean_results.assign(win=lambda df: df.apply(lambda row: 1 if row.margin > 0 else 0, axis='columns'))
                  .groupby(['home', 'away'])['win']
                  .transform(lambda row: row.rolling(5).mean().shift() * 5)
                  .fillna(0))

    return form_btwn_teams


# %%
#Return whole dataset
def get_features_with_cleaned_results():
    clean_results = get_cleaned_results()
    feature_1 = get_feature_1()
    home_ladder = get_home_ladder()
    away_ladder = get_away_ladder()

    features = clean_results[['date', 'game', 'home', 'away', 'venue', 'season','round']].copy()
    feature_df = pd.merge(features, feature_1.drop(columns=['margin']), on=['game', 'home', 'away'])
    feature_df = pd.merge(feature_df, clean_results[['game', 'result']], on='game')

    feature_df = feature_df.merge(away_ladder, on=['away','round','season'])
    feature_df = feature_df.merge(home_ladder, on=['home','round','season'])

    feature_df.assign(ladderDiff=lambda feature_df: feature_df.apply(lambda row: row['homeLadderPosition'] - row['awayLadderPosition'], axis=1)) 
    #feature_df['feature_homeTeamLadderPosition'] = feature_df['ladderPosition']
    #feature_df['feature_awayTeamLadderPosition'] = feature_df['ladderPosition']


    #feature_df.drop(columns=['team'])

    #feature_df.assign(hometeamladderposition=lambda df: df.apply(lambda row: ladder['ladderPosition'] if ladder['team'] == feature_df['team'], axis=1))
    return feature_df

featuredf = get_features_with_cleaned_results()
featuredf.tail(30)

# %%
