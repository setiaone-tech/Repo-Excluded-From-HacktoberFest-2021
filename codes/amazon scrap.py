import requests
from bs4 import BeautifulSoup as bs
import time

# url = "https://www.amazon.in/CERTIFIED-REFURBISHED-Ultimate-Wonderboom-Bluetooth/dp/B078HSFRGF/"
url = "https://www.amazon.in/CERTIFIED-REFURBISHED-Logitech-920-007596-Multi-Device/dp/B07C3KHQHC/"
url1 = url[:url.find("dp")]+"product-reviews"+url[url.find("dp")+2:]

print(url1)
res = requests.get(url1)

soup = bs(res.content, "lxml")
result = soup.find(id="filter-info-section")

result = result.text.strip()
# print(result)
total = result[result.find("|")+2:result.find("global reviews")-1]
total = int(total)
print(total)
li = []

url2 = url[:url.find("dp")]+"product-reviews"+url[url.find("dp")+2:]
url2 += "ref=cm_cr_arp_d_paging_btm_next_2?pageNumber="
i = 1
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
while(len(li) < total):
    # time.sleep(1)
    newUrl = url2+str(i)
    # print(newUrl)
    i += 1
    res = requests.get(newUrl, headers=headers)
    soup = bs(res.content, "lxml")
    results = soup.findAll("span", class_="review-text-content")
    # print(results)
    for result in results:
        # print(result.text)
        li.append(result.text.strip())

count = 1
for i in li:
    print(str(count)+"-> "+i)
    count += 1
