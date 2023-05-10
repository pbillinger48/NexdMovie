import requests
from bs4 import BeautifulSoup, SoupStrainer


#Method that scrapes list of Letterboxd movies
#Currently not used in favor of optimized method
#Kept in case its needed in future
def get_user_films_dict(username):
    #Dictionary will hold title of each film, and corresponding rating from 1-10 and 0 for unrated films
    filmsDict = {}
    # Use requests to fetch the HTML of the user's profile page
    Profilehtml = requests.get(f"https://letterboxd.com/{username}/films/").text
    # Load the HTML into a BeautifulSoup object, create another object that will be used for other pages of films
    profileSoup = BeautifulSoup(Profilehtml, 'html.parser')
    pageSoup = BeautifulSoup("", 'html.parser')
    #Parse the page number from the document, and then get the value of the last page
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
            if Title not in filmsDict:
                if Rating == 99:
                    filmsDict[Title] = 0
                elif Rating == 0:
                    filmsDict[Title] = 10
                else:
                    filmsDict[Title] = Rating

    return filmsDict

#Method that currently is not used. Gets only movies higher than a 5
#Could be possibly used as an alternative way of ignoring poorly rated movies when making reviews
def get_Positive_user_films_dict(username):
    #Dictionary will hold title of each film, and corresponding rating from 1-10 and 0 for unrated films
    filmsDict = {}
    # Use requests to fetch the HTML of the user's profile page
    Profilehtml = requests.get(f"https://letterboxd.com/{username}/films/").text
    # Load the HTML into a BeautifulSoup object, create another object that will be used for other pages of films
    profileSoup = BeautifulSoup(Profilehtml, 'html.parser')
    pageSoup = BeautifulSoup("", 'html.parser')
    #Parse the page number from the document, and then get the value of the last page
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
                elif Rating >= 5:
                    filmsDict[Title] = Rating

    return filmsDict

#Currently used method, is slightly faster way of scraping letterboxd movies
def get_user_films_dict_optimized(username):
    # Dictionary will hold title of each film, and corresponding rating from 1-10 and 0 for unrated films
    filmsDict = {}
    # Use a session object to make HTTP requests
    session = requests.Session()
    # Use SoupStrainer to parse only the parts of the HTML that are necessary
    parse_only = SoupStrainer('li', {'class': 'poster-container'})
    # Use BeautifulSoup to loop through each page and parse the HTML and extract the watched films
    page_num = 1
    last_page_num = 1
    while page_num <= last_page_num:
        url = f"https://letterboxd.com/{username}/films/page/{page_num}/"
        html = session.get(url)
        pageSoup = BeautifulSoup(html.content, 'html.parser', parse_only=parse_only)
        profileSoup = BeautifulSoup(html.content, 'html.parser')
        # Get html value for each film on the page using list comprehension
        watchedFilms = [film for film in pageSoup.find_all("li", {"class": "poster-container"})]
        # Loop through each film and get title and rating using dictionary comprehension
        filmsDict.update({film.find("div").find("img")["alt"]: 10 if (film.find("span", {"class": "rating"}) is not None and int(film.find("span", {"class": "rating"})["class"][-1][-1]) == 0) else (int(film.find("span", {"class": "rating"})["class"][-1][-1]) if film.find("span", {"class": "rating"}) is not None else 0) for film in watchedFilms})
        # Update last page number
        if last_page_num == 1:
            pages = profileSoup.find("div", {"class": "pagination"})
            if pages is not None:
                pages= profileSoup.find("div", {"class": "pagination"}).find_all("li", {"class": "paginate-page"})
                last_page_num = int(pages[-1].text)
        # Increment page number
        page_num += 1
    return filmsDict