import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.detik.com/terpopuler", params={"tag_from" : "wp_cb_mostPopular_more"})
soup = BeautifulSoup(response.text, "html.parser")
popular_area = soup.find(attrs={"class":"grid-row list-content"})
titles = popular_area.findAll(attrs={"class":"media__title"})
images = popular_area.findAll(attrs={"class":"media__image"})

for image in images:
    print(image.find("a").find("img")["title"])