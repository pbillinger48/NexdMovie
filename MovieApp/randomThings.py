import json
from Scraper import get_user_films_dict, get_user_films_dict_optimized
from EZReccomender import get_reccomendations, getRecInfo


userFilms = get_user_films_dict_optimized('pbillinger48')


for key, value in userFilms.items():
    print(f"{key}: {value}")
'''

    
   
userRecs = get_reccomendations(userFilms)
for key, value in userRecs.items():
    print(f"{key}: {value}")

emptyRecs = []
recInfo = getRecInfo(userRecs,emptyRecs)

for key, value in recInfo.items():
    print(f"{key}: {value}")

recInfo = getRecInfo(userRecs, recInfo)
for key, value in recInfo.items():
    print(f"{key}: {value}")
    
recInfo = getRecInfo(userRecs, recInfo)
for key, value in recInfo.items():
    print(f"{key}: {value}")
'''
