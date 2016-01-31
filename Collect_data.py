__author__ = 'azad'

from bs4 import BeautifulSoup

from rematch import extract_data



ecj_data = open("asif.html", 'r').read()


soup = BeautifulSoup(ecj_data, "html5lib")



table = soup.find("table",)
rows = table.findAll('tr')
data = [[td.findChildren(text=True) for td in tr.findAll("td")] for tr in rows]

data = [[u"".join(d).strip() for d in l] for l in data]

info_tuple = ('id', 'name', 'verdict', 'language', 'runtime', 'rank', 'date_of_submit')
s = ','.join(info_tuple)

print s
for x in data:

    extract_data(x)


