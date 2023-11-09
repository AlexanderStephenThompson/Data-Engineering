import bs4
import requests

Page = requests.get('https://www.furaffinity.net/user/rufusbcobber/')
Page.raise_for_status()

soup = bs4.BeautifulSoup(Page.text, 'html.parser')
Username = '#user-profile > div.user-profile-main.table > div.table-cell > div > div.userpage-flex-item.username > h2 > span'
element = soup.select(Username)
print(element[0].text.strip()[1:])
