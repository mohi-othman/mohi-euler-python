import urllib.request
import pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

page = urllib.request.urlopen(url)

result = pickle.load(page)
text = ""
for r in result:
    for x in r:
        text+=(x[0]*x[1])
    text+="\n"

print(text)

