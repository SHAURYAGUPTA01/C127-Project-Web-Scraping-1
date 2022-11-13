from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
temp_list = []
star_table = soup.find_all('table')
table_rows = star_table[0].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)
    
star_names = []
distance = []
mass = []
radius = []

for index,s in enumerate(temp_list):
    if index == 1 :
        star_names.append(s.find_all("a")[0].contents[0])
    else :
        try:
            distance.append(temp_list[i][3])
            mass.append(temp_list[i][5])
            radius.append(temp_list[i][6])
        except:
            temp_list.append("")
    
df1 = pd.DataFrame(list(zip(star_names,distance,mass,radius,)),columns = ['star_name','distance','mass','radius'])
print(df1)
df2.csv("Stars.csv")