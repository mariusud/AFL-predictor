#!/usr/bin/Rscript
library(dplyr)
library(elo)
library(lubridate)
library(fitzRoy)

results <- get_match_results()
fixtures <- get_fixture()
stats <- get_afltables_stats() #start_date = "2018-01-01", end_date = "2020-06-01")
tips <- get_squiggle_data("tips")

odds <- get_footywire_betting_odds()
ladder <- return_ladder()
#dat <- update_footywire_stats()
write.csv(results, "/home/marius/Development/AFL-predictor/datasets/results.csv")
write.csv(fixtures, "/home/marius/Development/AFL-predictor/datasets/fixtures.csv")
write.csv(stats, "/home/marius/Development/AFL-predictor/datasets/stats.csv")
write.csv(tips, "/home/marius/Development/AFL-predictor/datasets/tips.csv")
write.csv(odds, "/home/marius/Development/AFL-predictor/datasets/odds.csv")
write.csv(ladder, "/home/marius/Development/AFL-predictor/datasets/ladder.csv")



