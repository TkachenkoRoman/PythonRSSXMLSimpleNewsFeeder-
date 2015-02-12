import xml.etree.ElementTree as ET
from conf import getUrlPath, getInfoList
import urllib.request
import re

class myXMLParser:

    def __init__(self, path):
        tree = ET.parse(path)
        self.root = tree.getroot()

    def getDirectChildrenTagText(self, tagName): #returns list of root children tag texts
        res = []
        for tag in self.root.findall(tagName):
            res.append((tag.text, tag.get("name")))
        return res

    def findWholeWord(self, w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

    def searchForInfo(self, content, info): #finds info in content
        for word in info:
            if (self.findWholeWord(word)(content)):
                print(word)
                return True
        return False

    def parseRss(self, text):
        try:
            rss = ET.fromstring(text)
            i = 0
            for item in rss.iter('item'):
                for child in item:
                    content = str(child.text)
                    if (child.tag == "title" or child.tag == "description"):
                        if (self.searchForInfo(content, getInfoList())): #search for Ukrainian city
                            print("title: " + item.find("title").text)
                            print("description: " + item.find("description").text)
                            print("link: " + item.find("link").text)
        except Exception:
            print("some error occured")


xmlParser = myXMLParser(getUrlPath())
urlList = xmlParser.getDirectChildrenTagText("url")
print(urlList)
for url in urlList:
    file = urllib.request.urlopen(url[0])
    text = file.read()
    print("\n")
    print("read", len(text), "bytes in " + url[1])
    if (text):
        xmlParser.parseRss(text)