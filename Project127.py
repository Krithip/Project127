from bs4 import BeautifulSoup
import requests
import pandas as pd
startUrl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(startUrl)
toop = BeautifulSoup(page.text, 'html.parser')
starTable = toop.find('table')
tempList = []
tableRows = starTable.find_all('tr')
for tr in tableRows:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    tempList.append(row)
starName = []
distance = []
mass = []
radius = []
lum = []
for i in range(1, len(tempList)):
    starName.append(tempList[i][1])
    distance.append(tempList[i][3])
    mass.append(tempList[i][5])
    radius.append(tempList[i][6])
    lum.append(tempList[i][7])
df2 = pd.DataFrame(list(zip(starName, distance, mass, radius, lum)), columns = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity'])
print(df2)
df2.to_csv('bright_star.csv')