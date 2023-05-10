"""
This entire file is not currently used. In a version of the project where movie objects are needed these could possibly 
be used as helper methods to transfer scraped data into movie objects with more movie information.
"""
import requests

TMDB_API_KEY = 'a497a7718fd66875ff47bd0a20cd4b24'
#Used to get movie info such as id, genre, overview, etc
def get_movie_info(movie_title):
    """
    Helper function to get the movie info from TMDB API for a given movie title.
    """
    url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['total_results'] > 0:
            # Return the first result
            return data['results'][0]
    return None
#Used to get cast and crew
def get_movie_credits(movie_id):
    """
    Helper function to get the movie credits from TMDB API for a given movie id.
    Only the top 12 cast members and key crew members are included.
    """
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Get the top 12 cast members
        cast = data['cast'][:12]
        # Get the crew members we're interested in
        crew = [member for member in data['crew'] if member['job'] in ['Director', 'Producer','Editor', 'Cinematography', 'Screenplay',
                                                                        'Art Direction', 'Casting', 'Composer', 'Executive Producer', 'Score', 'Original Music Composer']]
        return cast, crew
    return [], []

#Combines movie info and cast and crew into a list of movies
def gather_credits_and_info(movie_ratings):

    movies_with_ratings_and_credits = []

    for movie_title, rating in movie_ratings.items():
        # Get the movie info from TMDB API
        movie_info = get_movie_info(movie_title)
        if movie_info:
            # Get the movie credits from TMDB API
            cast, crew = get_movie_credits(movie_info['id'])
            # Create a new movie object with the additional fields and the rating added
            movie_with_rating_and_credits = {
                'id': movie_info['id'],
                'title': movie_info['title'],
                'release_date': movie_info['release_date'],
                'overview': movie_info['overview'],
                'popularity': movie_info['popularity'],
                'poster_path': movie_info['poster_path'],
                'genre_ids': movie_info['genre_ids'],
                'vote_average': movie_info['vote_average'],
                'rating': rating,
                'cast': cast,
                'crew': crew
            }
            movies_with_ratings_and_credits.append(movie_with_rating_and_credits)
    return movies_with_ratings_and_credits

