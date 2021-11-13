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
# pushButton_2.clicked(Lcopy)

web.load(QUrl(u))
gridLayout.addWidget(web)
Dialog.show()
Dialog.exec_()


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
        print(items)
        for item in items:
            cards.append(
                {
                    'link': item.find('a').get('href'),
                    'title': item.find('a').get_text(),
                }
            )
        return cards

    html = get_html(URL)
    print(get_content(html.text))





















































































































###########
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
print(get_content(html.text))
html2 = get_html(URL)
print(get_content2(html2.text))





























####################

try:
    s = self.ui.comboBox.currentIndex()  # Получения номера в выдвижном списке
    n = self.ui.listWidget.currentRow()
    # print(self.newsurl[n])
    u = Sites.TheLink[s] + self.newsurl[n]
    # print(u)
    # print(u)
    # u2='https://www.today.com' + self.newsurl[n]

    # u2 = 'https://apnews.com' + self.newsurl[n]
    # app = QApplication(sys.argv)
    # web = QWebEngineView()
    # web.load(QUrl(u))
    # web.show()
    doc = urllib.request.urlopen(u).read().decode('utf-8', errors='ignore')
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.body_width = False
    h.ignore_images = True
    doc = h.handle(doc)
    mas = doc.split('\n')
    ##############################
    # doc=urllib.request.urlopen(u2).read().decode('utf-8', errors='ignore')
    # h=html2text.HTML2Text()
    # h.ignore_links=True
    # h.body_width=False
    # h.ignore_images=True
    # doc=h.handle(doc)
    # mas=doc.split('\n')
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
    # pushButton_2.clicked.connect(self.copy)
    # pushButton_2.clicked(Lcopy)

    web.load(QUrl(u))
    gridLayout.addWidget(web)
    Dialog.show()
    Dialog.exec_()




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