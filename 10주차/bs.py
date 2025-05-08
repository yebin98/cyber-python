# pip install beautifulsoup4

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 
# http://www.w3school.com/

from bs4 import BeautifulSoup

html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify()) # HTML 문서 예쁘게 출력

print(soup.title) # title 태그 출력
print(soup.title.parent.name) # title 태그의 부모 태그 출력

print(soup.p) # 첫 번째 p 태그 출력

print(soup.a) # 첫 번째 a 태그 출력
for link in soup.find_all('a'):
  print(link.get('href')) # 모든 a 태그의 href 속성 출력