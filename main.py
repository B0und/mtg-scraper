from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup


PAGE_COUNT = 25

firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
)
driver = webdriver.Firefox(options=firefox_options)


result_strings = []

for i in range(1, PAGE_COUNT):
    driver.get(f"http://www.mtg.ru/cards/search.phtml?Type=planeswalker&page={i}")
    page = driver.page_source
    soup = BeautifulSoup(page, features="lxml")

    for item in soup.findAll("h2"):
        print(item.text)
        result_strings.append(item.text)


result_strings = [x.strip() for x in result_strings if x.strip()]
result_strings = list(set(result_strings))
with open("result.txt", "w") as fout:
    print(*result_strings, sep="\n", file=fout)
