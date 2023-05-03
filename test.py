import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.edf.fr"
page = requests.get(url)
# print(page.content)

soup = BeautifulSoup(page.content, "html.parser")

titles_bs = soup.find_all("a", class_="title-xs")
description_bs = soup.find_all("div", class_="text")

titles = []
description = []

for titre in titles_bs:
    titles.append(titre.string)

for desc in description_bs:
    description.append(desc.string)

with open("data.csv", "w") as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    for titre, desc1 in zip(titles, description):
        line = [titre, desc1]
        writer.writerow(line)
