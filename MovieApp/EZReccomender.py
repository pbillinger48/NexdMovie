import requests
import json
from .Scraper import get_Positive_user_films_dict

api_key = 'a497a7718fd66875ff47bd0a20cd4b24'

def get_movie_recommendations(movie_title):   
    # Use the movie ID to get a recommendation
    url = f'https://api.themoviedb.org/3/movie/{get_movie_id(movie_title)}/recommendations?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        recommendations = [result["title"] for result in data["results"]]
        return recommendations

@staticmethod  
def get_movie_id(movie_title):
    # Get the movie ID for the given movie title
    response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}")
    if response.status_code == 200:
            data = response.json()
            if data['total_results'] > 0:
                # Return the first result
                data = data['results'][0] 
            if 'id' in data:
                movie_id = data['id']
                return movie_id
    
def get_reccomendations(movieDict):
    movieDict = dict(sorted(movieDict.items(), key=lambda x: x[1], reverse=True))
    recommendations = {}
    i = 0     
    for movie_title in movieDict:
        movie_reccs = get_movie_recommendations(movie_title)
        if movie_reccs is not None:
            for recommendation_title in movie_reccs:
                if recommendation_title not in movieDict:
                    if recommendation_title not in recommendations:
                        recommendations[recommendation_title] = 0
                    recommendations[recommendation_title] += movieDict[movie_title]
        #if i == 49:
            #break
        #i += 1
    recommendations = dict(sorted(recommendations.items(), key=lambda x: x[1], reverse=True))
    return recommendations
            

#username = 'Greenellie'
#user_films = get_Positive_user_films_dict(username)
#reccs = get_reccomendations(user_films)
#i=0
#for rec, rating in reccs.items():
    #if i == 5:
        #break
    #print(f"{rec}: {rating}")
    #i += 1