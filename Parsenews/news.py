import sys, re, urllib, html2text
from urllib import request
# Импортируем наш интерфейс
from newsform import *
from browser2 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView, QWebEnginePage as QWebPage, \
    QWebEngineSettings as QwebSettings
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import os, subprocess, threading
import sys, html2text, signal, re
from PyQt5.QtWidgets import (QMainWindow, QWidget, QHBoxLayout, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog
import Sites
import pyperclip
import requests
from bs4 import BeautifulSoup
import fake_useragent
from urllib.request import Request, urlopen  # Python 3

user = fake_useragent.UserAgent().random


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.newsurl = []  # Массив в который надо добавлять ссылки
        # self.Parse2()
        # self.Parse()
        self.first()

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.AllNews)
        self.ui.comboBox.currentTextChanged.connect(self.NAGIM)

        # s='https://tanksgoodnews.com'
        # doc=urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
        # doc=doc.replace('\n', '')
        # doc = doc.replace('">', '*')
        # zagolovki=re.findall('<a href="(.+?)</a></h2>', doc1)

    # for x1 in zagolovki:
    # self.newsurl.append(x1.split('" rel="bookmark">')[0]) # Массив в который надо добавлять ссылки
    # self.ui.listWidget.addItem(x1.split('" rel="bookmark">')[1].strip()) #Вывод в список
    # print(x1)

    # self.web.show()

    # def first(self):

    # css_soup = BeautifulSoup(res, '<div class="entry-featured-media"></div>')
    # css_soup.p['class']
    # print(css_soup)
    # block = soup.find('div', id = "page")
    # print(block)
    # for x in zagolovki:
    #    self.newsurl.append(x.split('">')[0])  # Массив в который надо добавлять ссылки
    #   self.ui.listWidget.addItem(x.split('">')[1].strip())  # Вывод в список
    # res = requests.get(s, headers = header)
    # print(res.text)

    def first(self):
        URL = 'https://tanksgoodnews.com'
        header = {'user-agent': user}

        def get_html(url, params=''):
            r = requests.get(url, headers=header, params=params)
            return r

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            items = soup.find_all('h2', class_='g1-alpha g1-alpha-1st entry-title')
            cards = []
            # print(items)
            for item in items:
                cards.append(

                    item.find('a').get('href'),

                )
            return cards

        def get_content2(html2):
            soup = BeautifulSoup(html2, 'html.parser')
            items = soup.find_all('h2', class_='g1-alpha g1-alpha-1st entry-title')
            cards = []
            # print(items)
            for item in items:
                cards.append(

                    item.find('a').get_text()

                )
            return cards

        html = get_html(URL)
        print(get_content(html.text))  # ссылка
        html2 = get_html(URL)
        print(get_content2(html2.text))  # текст

        h = html2text.HTML2Text()
        h.ignore_links = True
        Z = len(get_content(html.text))
        i = 0
        while i != Z:
            B = h.handle(get_content(html.text)[i])
            B = B.replace("https://tanksgoodnews.com", "")
            # print(B)

            self.newsurl.append(B)
            i = i + 1
        Z = len(get_content2(html2.text))
        i = 0
        while i != Z:
            self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
            i = i + 1
        s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
        n = self.ui.listWidget.currentRow()
        # print(self.newsurl[n])
        u = Sites.TheLink[s] + self.newsurl[n]
        print(u)

    def copy(self):
        s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
        n = self.ui.listWidget.currentRow()
        # print(self.newsurl[n])
        u = Sites.TheLink[s] + self.newsurl[n]
        pyperclip.copy(u)

    def NAGIM(self):
        s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
        if s == 0:  # Работаает
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://tanksgoodnews.com'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('h2', class_='g1-alpha g1-alpha-1st entry-title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('h2', class_='g1-alpha g1-alpha-1st entry-title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get_text()

                    )
                return cards

            html = get_html(URL)
            # print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            # print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                B = B.replace("https://tanksgoodnews.com", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            print(u)
        elif s == 1:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://www.goodnewsnetwork.org'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('h3', class_='entry-title td-module-title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('h3', class_='entry-title td-module-title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get_text()

                    )
                return cards

            html = get_html(URL)
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                B = B.replace("https://www.goodnewsnetwork.org/", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            print(u)
        elif s == 2:  # Работает
            self.ui.listWidget.clear()
            self.newsurl.clear()
            s = 'https://www.today.com/news/good-news'
            doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
            doc = doc.replace('\n', '')
            # print(doc)
            doc = doc.replace('<span class="tease-card__headline">', '')
            doc = doc.replace('We&#x27', '')
            doc = doc.replace('&#x27', '')
            doc = doc.replace(';', '')
            doc = doc.replace('re all in this together&#x27', '')
            doc = doc.replace('https://www.today.com', '')
            zagolovki = re.findall(
                '<h2 class="tease-card__headline tease-card__title relative"><a href="(.+?)</span></a><span class=""></span></h2>',
                doc)
            for x in zagolovki:
                self.newsurl.append(x.split('">')[0])  # Массив в который надо добавлять ссылки
                self.ui.listWidget.addItem(x.split('">')[1].strip())  # Вывод в список
        elif s == 3:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://www.msn.com/en-us/news/good-news'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('li', class_='rc rcp')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('li', class_='rc rcp')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('h3').get_text()

                    )
                return cards

            html = get_html(URL)
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                B = B.replace("en-us/news/good-news/", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]

            print(u)
        elif s == 4:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://www.foxnews.com/category/good-news'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('h4', class_='title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('h4', class_='title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get_text()

                    )
                return cards

            html = get_html(URL)
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                B = B.replace("https://video.foxnews.com/v/6197425479001", "")
                # B = B.replace("/category/good-news", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            u = u.replace("/category/good-news", "")
            print(u)

        elif s == 5:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://www.sunnyskyz.com/good-news'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('a', class_='newslist')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.get('href'),

                    )
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('a', class_='newslist')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('p', class_='titlenews').get_text()

                    )
                return cards

            html = get_html(URL)
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                B = B.replace("/good-news", "")
                # B = B.replace("/category/good-news", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            u = u.replace("/category/good-news", "")
            print(u)
        elif s == 6:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://www.positive.news'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('div', class_='card__content')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('div', class_='card__content')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get_text()

                    )
                return cards

            html = get_html(URL)
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                # B = B.replace("/good-news", "")
                B = B.replace("https://www.positive.news/", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            # u = u.replace("https://www.positive.news", "")
            print(u)
        elif s == 7:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://edition.cnn.com/specials/us/the-good-stuff'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('h3', class_='cd__headline')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                del cards[0]
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('h3', class_='cd__headline')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('span', class_='cd__headline-text vid-left-enabled').get_text()

                    )
                del cards[0]
                return cards

            html = get_html(URL)
            del get_content(html.text)[0]
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                # B = B.replace("/good-news", "")
                # B = B.replace("/index.html", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            # u = u.replace("https://www.positive.news", "")
            u = u.replace("/specials/us/the-good-stuff", "")
            print(u)
        elif s == 8:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://abcnews.go.com/alerts/good-news'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('div', class_='ContentRoll__Headline')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                del cards[0]
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('div', class_='ContentRoll__Headline')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get_text()

                    )
                del cards[0]
                return cards

            html = get_html(URL)
            del get_content(html.text)[0]
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                # B = B.replace("/good-news", "")
                # B = B.replace("/index.html", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            # u = u.replace("https://www.positive.news", "")
            u = u.replace("/specials/us/the-good-stuff", "")
            print(u)
        elif s == 9: # НЕ РАБОТАЕТ, ДОДЕЛАТЬ ДРУГИМИ МЕТОДАМИ
            self.ui.listWidget.clear()
            self.newsurl.clear()
            s = 'https://abc7.com/allgoodnews/'
            doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
            doc = doc.replace('\n', '')
            # doc = doc.replace('<h1 class="Component-h1-0-2-117">', '')
            # doc = doc.replace('</h1>', '')
            # doc = doc.replace('">', '*')
            zagolovki = re.findall(
                '<a class="AnchorLink" tabindex="0" target="_self" href="(.+?)"><div class="image dynamic-loaded" data-imgsrc="(.+?)</a>',
                doc)
            print(zagolovki[1])
            for x in zagolovki:
                self.newsurl.append(x.split('">')[0])  # Массив в который надо добавлять ссылки
                self.ui.listWidget.addItem(x.split('">')[1].strip())  # Вывод в список

        elif s == 10:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://www.reddit.com/r/UpliftingNews'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('div', class_='ContentRoll__Headline')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                del cards[0]
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('div', class_='ContentRoll__Headline')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get_text()

                    )
                del cards[0]
                return cards

            html = get_html(URL)
            del get_content(html.text)[0]
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                # B = B.replace("/good-news", "")
                # B = B.replace("/index.html", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            # u = u.replace("https://www.positive.news", "")
            u = u.replace("/specials/us/the-good-stuff", "")
            print(u)
        elif s == 11:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://www.goodnet.org/'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('a', class_='left preview')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.get('href'),

                    )
                #del cards[0]
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('a', class_='left preview')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('img').get('title')

                    )
                #del cards[0]
                return cards

            html = get_html(URL)
            del get_content(html.text)[0]
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                # B = B.replace("/good-news", "")
                # B = B.replace("/index.html", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            # u = u.replace("https://www.positive.news", "")
            u = u.replace("/specials/us/the-good-stuff", "")
            print(u)
        elif s == 12:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://notallnewsisbad.com/'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('a', class_='entry-title-link')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.get('href'),

                    )
                #del cards[0]
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('a', class_='entry-title-link')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.get_text()

                    )
                #del cards[0]
                return cards

            html = get_html(URL)
            del get_content(html.text)[0]
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                # B = B.replace("/good-news", "")
                # B = B.replace("/index.html", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            # u = u.replace("https://www.positive.news", "")
            u = u.replace("/specials/us/the-good-stuff", "")
            print(u)
        elif s == 13:  #
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://squirrel-news.net/news/'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('h3', class_='title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                #del cards[0]
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('h3', class_='title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get_text()

                    )
                #del cards[0]
                return cards

            html = get_html(URL)
            del get_content(html.text)[0]
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                # B = B.replace("/good-news", "")
                # B = B.replace("/index.html", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            print(u)
        elif s == 14:# не работает ( VPN )
            self.ui.listWidget.clear()
            self.newsurl.clear()
            URL = 'https://www.optimistdaily.com'
            header = {'user-agent': user}

            def get_html(url, params=''):
                r = requests.get(url, headers=header, params=params)
                return r

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                items = soup.find_all('h4', class_='entry-title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get('href'),

                    )
                #del cards[0]
                return cards

            def get_content2(html2):
                soup = BeautifulSoup(html2, 'html.parser')
                items = soup.find_all('h3', class_='title')
                cards = []
                # print(items)
                for item in items:
                    cards.append(

                        item.find('a').get_text()

                    )
                #del cards[0]
                return cards

            html = get_html(URL)
            del get_content(html.text)[0]
            print(get_content(html.text))  # ссылка
            html2 = get_html(URL)
            print(get_content2(html2.text))  # текст

            h = html2text.HTML2Text()
            h.ignore_links = True
            Z = len(get_content(html.text))
            i = 0
            while i != Z:
                B = h.handle(get_content(html.text)[i])
                # B = B.replace("/good-news", "")
                # B = B.replace("/index.html", "")
                # print(B)

                self.newsurl.append(B)
                i = i + 1
            Z = len(get_content2(html2.text))
            i = 0
            while i != Z:
                self.ui.listWidget.addItem(get_content2(html2.text)[i].strip())
                i = i + 1
            # Массив в который надо добавлять ссылки
            # Вывод в список
            s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
            n = self.ui.listWidget.currentRow()
            # print(self.newsurl[n])
            u = Sites.TheLink[s] + self.newsurl[n]
            print(u)
        elif s == 29:  # Работает
            self.ui.listWidget.clear()
            self.newsurl.clear()
            s = 'https://apnews.com/hub/one-good-thing'
            doc = urllib.request.urlopen(s).read().decode('utf-8', errors='ignore')
            doc = doc.replace('\n', '')
            doc = doc.replace('<h1 class="Component-h1-0-2-117">', '')
            # doc = doc.replace('</h1>', '')
            # doc = doc.replace('">', '*')
            zagolovki = re.findall(
                '<a class="Component-headline-0-2-116" data-key="card-headline" href="(.+?)</h1></a>',
                doc)
            print(zagolovki)
            for x in zagolovki:
                self.newsurl.append(x.split('">')[0])  # Массив в который надо добавлять ссылки
                self.ui.listWidget.addItem(x.split('">')[1].strip())  # Вывод в список

    def AllNews(self):
        s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
        n = self.ui.listWidget.currentRow()

        u = Sites.TheLink[s] + self.newsurl[n]
        u = u.replace("\n", "")
        u = u.replace("/category/good-news", "")
        print(u)
        header = {'user-agent': user}
        doc1 = urllib.request.Request(u, headers=header)
        doc = urllib.request.urlopen(doc1).read().decode('utf-8', errors='ignore')

        h = html2text.HTML2Text()
        h.ignore_links = True
        h.body_width = False
        h.ignore_images = True
        doc = h.handle(doc)
        mas = doc.split('\n')

        stroka = ''
        for x in mas:
            if (len(x) > 120):
                stroka = stroka + x + '\n\n'
        self.ui.textEdit.setText(stroka)
        Dialog = QtWidgets.QDialog()

        Dialog.setObjectName("Dialog")
        # Dialog.resize(719, 710)
        Dialog.setGeometry(1000, 300, 719, 710)
        label = QtWidgets.QLabel(Dialog)
        label.setGeometry(QtCore.QRect(20, 10, 601, 20))
        label.setObjectName("label")
        verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        verticalLayoutWidget.setGeometry(QtCore.QRect(410, 610, 160, 80))
        verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        verticalLayout = QtWidgets.QVBoxLayout(verticalLayoutWidget)
        verticalLayout.setContentsMargins(0, 0, 0, 0)
        verticalLayout.setObjectName("verticalLayout")
        pushButton_1 = QtWidgets.QPushButton(verticalLayoutWidget)
        pushButton_1.setObjectName("pushButton")
        verticalLayout.addWidget(pushButton_1)
        verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 609, 160, 81))
        verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        verticalLayout_3 = QtWidgets.QVBoxLayout(verticalLayoutWidget_2)
        verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        verticalLayout_3.setObjectName("verticalLayout_3")
        pushButton_2 = QtWidgets.QPushButton(verticalLayoutWidget_2)
        pushButton_2.setObjectName("pushButton_2")
        verticalLayout_3.addWidget(pushButton_2)
        gridLayoutWidget = QtWidgets.QWidget(Dialog)
        gridLayoutWidget.setGeometry(QtCore.QRect(19, 39, 681, 561))
        gridLayoutWidget.setObjectName("gridLayoutWidget")
        gridLayout = QtWidgets.QGridLayout(gridLayoutWidget)
        gridLayout.setContentsMargins(0, 0, 0, 0)
        gridLayout.setObjectName("gridLayout")

        QtCore.QMetaObject.connectSlotsByName(Dialog)

        web = QWebView()

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        label.setText(_translate("Dialog", u))
        pushButton_1.setText(_translate("Dialog", "PushButton"))
        pushButton_2.setText(_translate("Dialog", "Скопировать ссылку"))
        pushButton_2.clicked.connect(self.copy)
        # pushButton_2.clicked(Lcopy)

        # u = 'https://www.goodnewsnetwork.org/retired-brits-wisdom-onepoll/'
        web.load(QUrl(u.replace("\n", "")))

        gridLayout.addWidget(web)
        Dialog.show()
        Dialog.exec_()


# ================================================= Диалоговое окно с браузером


# self.web.show()


# n=self.ui.listWidget.currentRow()
# print(self.newsurl[n])
# u='https://apnews.com'+self.newsurl[n]
# u2 = 'https://apnews.com' + self.newsurl[n]
# app = QApplication(sys.argv)
# web = QWebEngineView()
# web.load(QUrl(u))
# web.show()
# doc=urllib.request.urlopen(u).read().decode('utf-8', errors='ignore')
# h=html2text.HTML2Text()
# h.ignore_links=True
# h.body_width=False
# h.ignore_images=True
# doc=h.handle(doc)
# mas=doc.split('\n')
# stroka=''
# for x in mas:
# if(len(x)>120):
# stroka=stroka+x+'\n\n'
# self.ui.textEdit.setText(stroka)


if __name__ == "__main__":
    app1 = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app1.exec_())
