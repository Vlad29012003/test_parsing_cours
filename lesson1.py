from bs4 import BeautifulSoup

with open('/home/vlad/parsing_test_2/index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title.text)


page_h1 = soup.find("h1")

print(page_h1)

page_all_h1 = soup.find_all("h1")
print([page_all_h1])

for item in page_all_h1:
    print(item.text)

user_name = soup.find(class_="user__name").find("span").text
print(user_name)

user_name = soup.find("div", {"class": "user__name", "id":"aaa"}).find("span").text
print(user_name)

user_span_info = soup.find(class_="user__info").find_all("span")
print(user_span_info[2].text)

for item in user_span_info:



    social_links= soup.find(class_="social__networks").find("ul").find_all("a")
print(social_links)

for tens in social_links:
    print(tens.text)

socian_network = soup.find_all("a")

for item in socian_network:
    item_text = item.text
    item_url = item.get("href")
    print(f'{item_text}: {item_url}')


post_div = soup.find(class_= "post__text").find_parent("div","user__post")
print(post_div)

post_divs = soup.find(class_="post__text").find_parents("div","user__post")
print(post_divs)

next_el = soup.find(class_="post__title").next_element.next_element.text
print(next_el)


next_el = soup.find(class_="post__text").find_next().text
print(next_el)

find_next_sibling =soup.find(class_="post__title").find_next_sibling().text
print(find_next_sibling)

