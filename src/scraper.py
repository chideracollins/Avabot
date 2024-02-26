from bs4 import BeautifulSoup
import requests
import schedule

url = "https://www.jumia.com.ng/"
source = requests.get(url)
soup = BeautifulSoup(source.text, "html5lib")
links = soup.find_all("a")

for link in links:
    print(link, "\n")