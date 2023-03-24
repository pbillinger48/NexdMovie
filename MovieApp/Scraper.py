import requests
from bs4 import BeautifulSoup

def get_user_films_dict(username):
    #Dictionary will hold title of each film, and corresponding rating from 1-10 and 0 for unrated films
    filmsDict = {}

    # Use requests to fetch the HTML of the user's profile page
    Profilehtml = requests.get(f"https://letterboxd.com/{username}/films/").text

    # Load the HTML into a BeautifulSoup object, create another object that will be used for other pages of films
    profileSoup = BeautifulSoup(Profilehtml, 'html.parser')
    pageSoup = BeautifulSoup("", 'html.parser')

    #Parse the page number from the document, and then get the value of the last page

    #FIXXXXX ISSSSSUEEEE
    pages = profileSoup.find("div", {"class": "pagination"})
    if pages is not None:
        pages= profileSoup.find("div", {"class": "pagination"}).find_all("li", {"class": "paginate-page"})
        lastPageNumber = int(pages[-1].text)
    else:
        lastPageNumber = 1

    # Use BeautifulSoup to loop through each page and parse the HTML and extract the watched films
    for i in range(1, lastPageNumber + 1):
        Pagehtml = requests.get(f"https://letterboxd.com/{username}/films/page/{i}/").text

        pageSoup = BeautifulSoup(Pagehtml, 'html.parser')
        #Get html value for each film on the page
        watchedFilms = pageSoup.find_all("li", {"class": "poster-container"})

        #Loop through each film and get title and rating
        for film in watchedFilms:
            Title = film.find("div").find("img")["alt"]
            Rating = film.find("span", {"class": "rating"})
            if Rating is None:
                Rating = 99
            else:
                Rating = int(Rating["class"][-1][-1])
            #Check for no rating and assign it as 0, and check for 5 star rating and assign it as 10, otherwise assign it normally
            if Title not in filmsDict:
                if Rating == 99:
                    filmsDict[Title] = 0
                elif Rating == 0:
                    filmsDict[Title] = 10
                else:
                    filmsDict[Title] = Rating

    return filmsDict