#!/bin/bash
#
# Basic web scraping to any website 
#
import requests
import re
import os 
import bs4


def getMails(var):
    try:
        request = requests.get(var)

        if request.status_code == 200:
            print('[*] Searching for emails..')

            regExMail =r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+" # regex for emails
            emails = set(re.findall(regExMail, request.text, re.I))

            if emails:
                with open('emails.txt', 'w') as m:
                    for i in emails:
                        print('\t[*] %s' %i)
                        m.write(i)
                        m.write('\n')
                m.close()
            else:
                print('\t[*] Not emails found in website')
    
    except requests.RequestException:
        print('\t\t[ERROR] Cannot get %s' %var)

    


def downloadImages(var):
    os.makedirs('Images', exist_ok=True)

    try:
        request = requests.get(var)
        
        if request.status_code == 200:
            print('\t[*] Downloading image: %s' %var)
            
            if '?' in var: 
                # delete query string and  fragments from url
                image = open(os.path.join('Images', os.path.basename(var[:var.find('?')])), 'wb')
            else:
                image = open(os.path.join('Images', os.path.basename(var)), 'wb')

            for chunk in request.iter_content(100000):
                image.write(chunk)

            image.close()
    
    except requests.RequestException as e: 
        print('\t\t[ERROR] %s' %e)


def getSrc(var):
    print('[*] Searching for images in website...')
    request = requests.get(var)

    soup = bs4.BeautifulSoup(request.text, "html.parser")

    img = soup.find_all('img')

    if img ==[]:
        print('\t[*] No images found')
    else:
        for i in range(len(img)):
            try:
                src = (img[i].get('src')) # if error occurs analyze source code and change src

                if not src.startswith('http'):
                    src = var+src

                downloadImages(src)

            except:
                print('\t[ERROR] Can not get src %s' %src)


if __name__=="__main__":
    url = input('[*] Website to investigate: ')
    
    getSrc(url)
    getMails(url)

