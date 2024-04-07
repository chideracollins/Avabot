from bs4 import BeautifulSoup
import requests

url = "https://www.jumia.com.ng/"
source = requests.get(url)
soup = BeautifulSoup(source.text, "html5lib")
print(soup.prettify())
# links = soup.find_all("a")

# for link in links:
#     print(link, "\n")