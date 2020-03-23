# AFL-player-prediction
Predicting AFL player scores


to run ipynb: (nbx is alias, check my linux-config for deats)
`nbx [--inplace] <notebook> `

To install dependencies: 
`/usr/bin/python3 -m pip install -U -r requirements.txt --user`



The goal of this model is to predict AFL matches. 

Possible features to build the model on includes: (it should be noted that just adding features for the sake of it is inefficient and will make the model worse, since they become noise that makes the model's job harder)
- team ranking (difference in ladder position(points? jackson?), rolling 5 game percentage?)
- form (im thinking we could do a 3-game  win-loss record)
- venues (who wins more at certain venues, more upsets at other venues)
- fatigue (try and let the machine find correlation between how far along the season we are)
- difference between the two teams: contested posession, handballs, tackles etc.. 
- young vs old age group, or just experienced players/Gary abbletts yaknow?



Thanks to:
fitzRoy for amazing data-scraping package
betfair