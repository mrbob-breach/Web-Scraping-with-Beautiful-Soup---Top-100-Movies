from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, "html.parser")

with open("movies.txt", mode="w", encoding="utf-8") as file:
    all_movies = soup.find_all("h3", class_="title")
    movies_list = [movie.getText() for movie in all_movies]
    for movie in movies_list[::-1]:
        file.write(f"{str(movie)}\n")

