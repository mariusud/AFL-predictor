import pandas as pd
import numpy as np
import re
pd.set_option('display.max_columns', None)
pd.set_option("display.max_rows", 25)
from cleanDataset import get_cleaned_results

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


#Return whole dataset
def get_features_with_cleaned_results():
    clean_results = get_cleaned_results()
    feature_1 = get_feature_1()
    features = clean_results[['date', 'game', 'home', 'away', 'venue', 'season']].copy()
    feature_df = pd.merge(features, feature_1.drop(columns=['margin']), on=['game', 'home', 'away'])
    feature_df = pd.merge(feature_df, clean_results[['game', 'result']], on='game')
    return feature_df





