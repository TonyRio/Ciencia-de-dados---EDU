from gazpacho import get, Soup


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
print(d1)
print(t1)