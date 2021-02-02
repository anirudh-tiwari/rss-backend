
import requests
from bs4 import BeautifulSoup
from rss_app.models import Link
# url = "https://codewithharry.com"
url = "https://www.androidcentral.com/rss.xml"
# url = Link.objects.all()
# print(url)

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent,'xml')
# # print(soup.prettify)
titles=soup.find_all("title")
links=soup.find_all("link")
descriptions=soup.find_all("description")

print(titles[0])
# print(links[0])
# print(descriptions[0])
# title=soup.title
# # print(title)

paras = soup.find_all('item')
anu = paras[0]
# print(paras)


# anchors = soup.find_all('a')
# all_links = set()
# Get all the links on the page:
# for link in anchors:
    # if(link.get('href') != '#'): 
        # linkText = "https://codewithharry.com" +link.get('href')
        # all_links.add(link)
        # print(linkText)
# srk = paras.find("content")
# print(srk)

for avi in paras:
      yos = avi.find('description')
      yo = avi.find('link')
      bro= avi.find_all('content:encoded')
#       print("***************")
      # print(yo)
      # print(yos)
      # print(bro)
#       print("description : ",yos)
#       print("***************")

# case_list = []
# for ani in paras:
#     case = {ani.find('title').text  }
#     case_list.append(case)
# print(len(case_list))
# print(case_list)
for ssr in paras:
      he= ssr.find_all("a", class_="norewrite")
      # print(he)



# anchors = soup.find_all('a')
# print(anchors)

# all_links = set()

# for link in anchors:
#     if(link.get('href') != '#'): 
#         linkText = link.get('href')
#         all_links.add(link)
#         print(linkText)

