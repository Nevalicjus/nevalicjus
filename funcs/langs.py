from bs4 import BeautifulSoup
import requests

url = "https://github-readme-stats.vercel.app/api/top-langs/?username=Nevalicjus&hide=html"
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

gdp_table = soup.find("svg", attrs={})
gdp_table_data = gdp_table.find_all("g")

langs = []
for g in gdp_table_data[2].find_all("g"):
    for textfield in g.find_all("text"):
        langs.append(f"{textfield.text}")

langs_fin = ""

for x in range(0, 10):
    try:
        langs_fin += f"{langs[x]}"
        if langs[x].endswith("%"):
            langs_fin += f", "
        else:
            langs_fin += " "
    except IndexError:
        pass

print(langs_fin[:-2])
f = open("funcs/temp-langs.txt", "w")
f.write(langs_fin[:-2])
f.close()
