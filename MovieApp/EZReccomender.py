import requests
import json

#Used for API Calls
api_key = 'a497a7718fd66875ff47bd0a20cd4b24'

#Used to get recommendations for individual movies
def get_movie_recommendations(movie_title):   
    # Use the movie ID to get a recommendation
    url = f'https://api.themoviedb.org/3/movie/{get_movie_id(movie_title)}/recommendations?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        recommendations = [result["title"] for result in data["results"]]
        return recommendations


# Gets the id of a specific movie by searching by title  
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
            
#Gets main dictionary of all recommended movies and weighted and ordered based on letterboxd ratings
def get_reccomendations(movieDict):
    movieDict = dict(sorted(movieDict.items(), key=lambda x: x[1], reverse=True))
    recommendations = {}   
    #Loops through movies in dictionary
    for movie_title in movieDict:
        #Gets recommendation for a specific movie
        movie_reccs = get_movie_recommendations(movie_title)
        if movie_reccs is not None:
            #Loops through each recommendation and adds it to recommendation if not yet added or adds the rating weight if already added
            for recommendation_title in movie_reccs:
                #Checks to make sure title has not already been watched
                if recommendation_title not in movieDict:
                    #Checks to make sure its not added
                    if recommendation_title not in recommendations:
                        recommendations[recommendation_title] = 0
                    #Adds the rating of the movie that inspired the recommendation to the total to get an overall recommendation score in the end.
                    recommendations[recommendation_title] += movieDict[movie_title]
    recommendations = dict(sorted(recommendations.items(), key=lambda x: x[1], reverse=True))
    return recommendations

            

#Takes top 5 recommendations and gets info such as movie poster and id
#Uses curList to get updated results when user presses show more button on app
def getRecInfo(RecDict, curList):
    top_recommendations = {}
    counter = 0
    #Loops through recommendation dictionary
    for recommendation_title in RecDict:
        #Checks to make sure it is not already in the info list
        if recommendation_title not in curList:
            #If it is its added to the top_recommendations and counter is added 
            top_recommendations[recommendation_title] = RecDict[recommendation_title]
            counter += 1
        #Once 5 movies are added the loop stops
        if counter == 5:
            break
    #Loops through the added movies
    for title, rating in top_recommendations.items():
        #Gets the movie data for the movie
        response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}") 
        #If movie is found      
        if response.status_code == 200:
            data = response.json()
            if data['total_results'] > 0:
                #Gets the poster of the most relevant movie
                poster_path = data['results'][0]['poster_path']
                #Gets the id of the same movie
                id = data['results'][0]['id']
                #adds the info to the curList
                curList[title] = {"id": id, "poster": poster_path}                                       
    return curList

