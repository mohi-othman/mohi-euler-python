from urllib import request
from lxml import etree

def Solve():   
    reader = request.urlopen("http://projecteuler.net/index.php?section=problems&id=13")
    html = reader.read()
    
    parser = etree.HTMLParser()
    tree = etree.fromstring(str(html), parser)
    
    xpath = "//body/div[2]/div[1]/div[2]/div[3]/div[1]/text() "
    lines = tree.xpath(xpath)

    strings = list(map(lambda x:str.replace(x.strip(),"\\n",""),lines))
    numbers = [int(x) for x in strings if len(x)>0]
    
    return((str(sum(numbers)))[:10])

    