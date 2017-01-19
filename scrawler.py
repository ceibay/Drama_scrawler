#!/usr/local/bin/python3.5
# -*- coding: UTF-8 -*-

from requests import session
from bs4 import BeautifulSoup
import os

file_drama_history = "drama_history.txt"
file_drama_list = "new_drama_list.txt"

# Clear the file contents
f = open(file_drama_list, "w")
f.close()

s = session()

r = s.get("http://kanmeiju.net/detail/2272.html")
bs = BeautifulSoup(r.text, "lxml")
urls = bs.select("body > div.wrap > div > div > div > ul > a")

for url in urls:
    url_text = url.get('href')

    # Find if the drama has already been watched
    count = 0
    with open(file_drama_history, "r") as f:
        for old_url in f.readlines():
            li = old_url.find(url_text)
            if li != -1:
                count += 1
                break
    f.close()

    if count == 0:
        with open(file_drama_history, "a") as f:
            f.write(url_text)
            f.write("\n")
        f.close()
        with open(file_drama_list, "a") as f_dl:
            f_dl.write(url_text)
            f_dl.write("\n")
        f_dl.close()

r = s.get("http://kanmeiju.net/detail/2291.html")
bs = BeautifulSoup(r.text, "lxml")
urls = bs.select("body > div.wrap > div > div > div > ul > a")

for url in urls:
    url_text = url.get('href')

    # Find if the drama has already been watched
    count = 0
    with open(file_drama_history, "r") as f:
        for old_url in f.readlines():
            li = old_url.find(url_text)
            if li != -1:
                count += 1
                break
    f.close()

    if count == 0:
        with open(file_drama_history, "a") as f:
            f.write(url_text)
            f.write("\n")
        f.close()
        with open(file_drama_list, "a") as f_dl:
            f_dl.write(url_text)
            f_dl.write("\n")
        f_dl.close()


r = s.get("http://kanmeiju.net/detail/2304.html")
bs = BeautifulSoup(r.text, "lxml")
urls = bs.select("body > div.wrap > div > div > div > ul > a")

for url in urls:
    url_text = url.get('href')

    # Find if the drama has already been watched
    count = 0
    with open(file_drama_history, "r") as f:
        for old_url in f.readlines():
            li = old_url.find(url_text)
            if li != -1:
                count += 1
                break
    f.close()

    if count == 0:
        with open(file_drama_history, "a") as f:
            f.write(url_text)
            f.write("\n")
        f.close()
        with open(file_drama_list, "a") as f_dl:
            f_dl.write(url_text)
            print(url_text + "\n")
            f_dl.write("\n")
        f_dl.close()

s.close()

#os.system("/Applications/TextEdit.app/Contents/MacOS/TextEdit /Users/Jia/Work/Python/Drama_scrawler/new_drama_list.txt")

