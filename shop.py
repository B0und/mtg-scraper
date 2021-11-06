from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup


firefox_options = Options()
firefox_options.add_argument("--headless")
firefox_options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
)
driver = webdriver.Firefox(options=firefox_options)

# read cards from file
with open("FINAL_FINAL.txt", "r") as text_file:
    card_list = text_file.read().split("\n")

print(card_list)
# string = "asd"
# res = string.split("//")
# print(res)
# result_strings = []

card_names = [card.split("//")[0].strip() for card in card_list]


for card_name in card_names:
    card_search_string = "+".join(card_name.split(" "))
    print(card_search_string)
    driver.get(f"http://www.mtg.ru/exchange/card.phtml?Title={card_search_string}")
    page = driver.page_source
    soup = BeautifulSoup(page, features="lxml")

    outer_big_cards = soup.findAll(class_="NoteDivWidth U shadow")
    entries_on_page = len(outer_big_cards)

    cities = []
    shop_names = []

    for outer_big_card_counter in range(10, 10 + 2 * entries_on_page - 1, 2):
        city = soup.select_one(
            f"table.NoteDivWidth:nth-child({outer_big_card_counter}) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > center:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > nobr:nth-child(1)"
        )
        cities.append(city.text)

        shop = soup.select_one(
            f"table.NoteDivWidth:nth-child({outer_big_card_counter}) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > center:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > th:nth-child(2)"
        )

        shop_name = shop.text.replace("\xa0\xa0", "")
        shop_names.append(shop_name)

        child_card_count = len(
            soup.select(
                f"table.NoteDivWidth:nth-child({outer_big_card_counter}) .shadow"
            )
        )
        # print(len(child_card_count))

        for count, inner_card_counter in enumerate(
            range(1, 2 * child_card_count + 1, 2)
        ):
            print(f"{inner_card_counter=}")
            # price = soup.select_one(
            #     f"table.NoteDivWidth:nth-child({outer_big_card_counter}) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child({inner_card_counter}) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:last-child"
            # )
            inner_card = soup.select_one(
                f"table.NoteDivWidth:nth-child({outer_big_card_counter})"
            )
            if inner_card:
                print(inner_card)
                # price = inner_card.select_one(".txt15:last-child")
                # if price:
                #     print(price)
                #     print(price.text)
                #     print(list(price.strings))
                #     print(list(price.stripped_strings))
                # else:
                #     print("None")
                print("-----------------")

        print("$$$$$$$$$$$$$$$$$")

    break

    print(cities)
    print(shop_names)


# table.NoteDivWidth:nth-child(12) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1)

# table.NoteDivWidth:nth-child(12) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(3)