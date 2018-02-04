#!/usr/bin/env pytnon3


from bs4 import BeautifulSoup, SoupStrainer
from config_parse import *
import requests
import re
import time

page = list()
foundaddresses = list()
urlall = list()
starttime = time.process_time() 

sitew = '//www.'
url = 'http:' + sitew + site 
response = requests.get(url)

if str(response.status_code) != '200' :
    print ("Продолжение после ошибки")
    print(response.status_code)
         
    time.sleep(TIMEPAUS) 
    url = 'http:' + '//' + site 
    response = requests.get(url)
    if str(response.status_code) != '200' :
        print ("Ошибка, остановка программы")
        print(response.status_code)
        exit(0) 
page.append(url)
soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a'))
urls = [link['href'] for link in soup if link.get('href')]

urlall.append(urls)


mail = r"[a-zA-Z0-9]{1,100}@[a-z]{1,10}\.[a-z]{2,4}"

mailsearch = re.findall(mail,str(response.text))
for i in mailsearch:
    if i and not (i in foundaddresses) :
        foundaddresses.append (i)

print(url)
print("Количество ссылок :  ",end='')
print(len(urls))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++")
j = 0
while j <= maximum:
    print (time.process_time())
    if  time.process_time() - starttime >= TIMEMAX :
        print("Привышено время выполнения программы :",end='')
        print (time.process_time())
        print("Количество страниц :  ",end='')
        print(len(page))
        print('Список адресов')
        print(foundaddresses)
        exit(1)
    urls = urlall[j]
    for link1 in urls :
        if  time.process_time() - starttime >= TIMEMAX :
            print("Привышено время выполнения программы :",end='')
            print (time.process_time())
            print("Количество страниц :  ",end='')
            print(len(page))
            print('Список адресов')
            print(foundaddresses)
            exit(1)
        if len(page) >= MAX :
            break
        if link1 in page:
            continue
        if link1 != '/':     
            if link1[0] == '/' and not link1.startswith('//') :
                url1 = url + link1

            elif link1.startswith((sitew + site)):
                
                url1 = 'http:' + link1

            elif link1.startswith(url) :
                url1 = link1

            elif link1.startswith(('http:' + '//' + site)) :
                url1 = link1
            elif link1.startswith(('https:' + '//' + site)) :
                url1 = link1
            elif link1.startswith(('https:' + sitew + site)) :
                url1 = link1
            else :
                continue

            time.sleep(TIMEPAUS)    
            
            if not (url1 in page) :
                response = requests.get(url1)
                if str(response.status_code) != '200' :
                    print ("Продолжение после ошибки :",end='')
                    print(response.status_code)
                    continue
                page.append(url1)
                

                soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a'))
                urls1 = [link1['href'] for link1 in soup if link1.get('href')]
                urlall.append(urls1)
                mailsearch = re.findall(mail,str(response.text))
                for i in mailsearch:
                    if i != None and not (i in foundaddresses) :
                        foundaddresses.append (i)

    j=j+1
        
print('')
print("Количество страниц :  ",end='')
print(len(page))
print("Время выполнения программы :",end='')
print (time.process_time())
print('')
print('Список адресов')
print(foundaddresses)

