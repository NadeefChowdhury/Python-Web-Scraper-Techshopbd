# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 12:21:45 2023

@author: User 2
"""
import PySimpleGUI as pg

from bs4 import BeautifulSoup
import requests
pg.theme("SandyBeach")
pg.set_options(font=('Courier 14'))
column = [
    [pg.Text("", size=(100, 13), key='OUTPUT1')],
    [pg.Text("", size=(100, 13), key='OUTPUT2')],
    [pg.Text("", size=(100, 13), key='OUTPUT3')],
    ]
layout = [
    [pg.Text("Search Product", font=('Helvetica', 14),size=(40,1)),
     pg.InputText()
    ],
    [pg.Button("ok", font=('Helvetica', 14),button_color=('white', 'brown'), size=(4,0), border_width=0,), pg.Button("cancel", font=('Helvetica', 14),button_color = 'Purple', border_width=0)],
    [pg.Column(column, scrollable=True,  vertical_scroll_only=True)],
    
   ]
window = pg.Window("Web Scrapper for Techshop", layout, size=(850,700))
while True:
    event, values = window.read()
    print(event)
    if event == "cancel" or event == pg.WIN_CLOSED:
        break
    elif event == "ok":
        a = values[0]
        b = a.lower()
        c = b.replace(' ','%20')
        html_text = requests.get('https://techshopbd.com/browse/search?term='+c).text

        soup = BeautifulSoup(html_text, 'lxml')

        if len(soup.find_all('a', class_='ml-5')) > 9:
            for i in range(10):
                print(soup.find_all('a', class_='ml-5')[i].text.replace(' ',''))
                print('https://techshopbd.com' + soup.find_all('a', class_='ml-5')[i]['href'])
                print("----------------------------------")
            window['OUTPUT1'].update(value=soup.find_all('a', class_='ml-5')[0].text + 'https://techshopbd.com' + soup.find_all('a', class_='ml-5')[0]['href']+'\n--------------------------------')
            window['OUTPUT2'].update(value=soup.find_all('a', class_='ml-5')[1].text + 'https://techshopbd.com' + soup.find_all('a', class_='ml-5')[1]['href']+'\n--------------------------------')
            window['OUTPUT3'].update(value=soup.find_all('a', class_='ml-5')[2].text + 'https://techshopbd.com' + soup.find_all('a', class_='ml-5')[2]['href']+'\n--------------------------------')
        else:
            for i in range(len(soup.find_all('a', class_='ml-5'))):
                print(soup.find_all('a', class_='ml-5')[i].text.replace(' ',''))
                print('https://techshopbd.com' + soup.find_all('a', class_='ml-5')[i]['href'])
                print("----------------------------------")
            window['OUTPUT1'].update(value=soup.find_all('a', class_='ml-5')[0].text + 'https://techshopbd.com' + soup.find_all('a', class_='ml-5')[0]['href']+'\n--------------------------------')
            
window.close()
