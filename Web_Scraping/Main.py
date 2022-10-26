from gazpacho import get, Soup


url = 'https://pypi.org/project/pandas/#history'
html =get(url)
Soup(html)
soup = Soup(html)
soup.find('a', {'card': 'card'})
cards = soup.find("a", {"class": "card"})
print(cards[1])