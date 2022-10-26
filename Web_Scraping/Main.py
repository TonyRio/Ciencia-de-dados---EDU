from gazpacho import get, Soup
import pandas as pd

url = 'https://pypi.org/project/pandas/#history'
html =get(url)
Soup(html)
soup = Soup(html)
soup.find('a', {'card': 'card'})
cards = soup.find("a", {"class": "card"})
#print(cards[0])
#print(type(cards[1]))
d1 = cards[0].find("p", {"class": "release__version"}, partial=False).text
t1 = cards[0].find("time").attrs ["datetime"]

def parse_card (card):
    versao = card.find("p", {"class": "release__version"}, partial=False).text
    timestamp = card.find("time").attrs ["datetime"]
    return {"versão": versao,  'data:' : timestamp}

#print(parse_card(cards[0]))
data = [parse_card(x) for x in cards]
#print(dataframe)
df = pd.DataFrame(data)
print(df)
