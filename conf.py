import os
import re

def getUrlPath():
    dir = os.path.dirname(__file__)
    urlsPath = (os.path.join(dir, 'source/urls.xml')).replace("\\", "/")
    print("path of url file: ", urlsPath)
    return urlsPath

def getInfoPath():
    dir = os.path.dirname(__file__)
    return (os.path.join(dir, 'gns/data.txt')).replace("\\", "/")

def getInfoList():
    with open (getInfoPath(), "r") as infoFile:
        data = infoFile.read()
    return re.findall(r"[\w']+", data)