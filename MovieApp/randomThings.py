from Scraper import get_user_films_dict, get_user_films_dict_optimized
from EZReccomender import get_reccomendations


userFilms = get_user_films_dict_optimized('pbillinger48')
for key, value in userFilms.items():
    print(f"{key}: {value}")
    
   
userRecs = get_reccomendations(userFilms)
for key, value in userRecs.items():
    print(f"{key}: {value}")
