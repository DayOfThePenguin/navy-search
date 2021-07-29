import pathlib
import requests
import sys

from urllib.parse import urljoin
from bs4 import BeautifulSoup
from selenium import webdriver

pdf_url_root = "https://www.secnav.navy.mil"
url = "https://www.secnav.navy.mil/doni/manuals-secnav.aspx"

profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
driver = webdriver.Firefox(profile)
driver.get(url)
page_content = driver.page_source
driver.quit()


data = []
soup = BeautifulSoup(page_content, "html.parser")
table = soup.find("table", {"id": "onetidDoclibViewTbl0"})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    pdf_url_stub = row.select("a[href$='.pdf']")[0]["href"]
    cols.insert(0, pdf_url_stub)
    data.append([ele for ele in cols if ele])  # Get rid of empty values

print(data[:5])

# print(len(table_div.find("table")))
# for link in soup.select("a[href$='.pdf']"):
#     print(link)
# Name the pdf files using the last portion of each link which are unique in this case
# filename = os.path.join(folder_location, link['href'].split('/')[-1])
# with open(filename, 'wb') as f:
#     f.write(requests.get(urljoin(url, link['href'])).content)
