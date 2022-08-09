
from selenium import webdriver
from array import array
import requests
from bs4 import BeautifulSoup

companies = ["UC Berkeley", "The University of Vienna", "Caribou Biosciences"]

def googleSearch(toSearch):
    driver = webdriver.Firefox(executable_path=r'/Users/saranyasingh/Downloads/geckodriver')
    for i in toSearch:
        reqs = requests.get("https://www.google.com/search?q=" + i)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        counter = 1
        for link in soup.find_all('a'):
            thisLink = link.get('href')
            if thisLink.startswith('/url'):
                if "&sa" in thisLink:
                    file = open("crispr" + str(counter) + ".txt", "a")
                    num = thisLink.find('&sa')
                    driver.get(thisLink[7:num])
                    page = requests.get(thisLink[7:num])
                    file.write(thisLink[7:num]+ "\n")
                    file.write(page.text)
                    counter = counter + 1
                    file.close
                else:
                    file = open("crispr" + str(counter) + ".txt", "a")
                    driver.get(thisLink[7:])
                    page = requests.get(thisLink[7:])
                    file.write(thisLink[7:] + "\n")
                    file.write(page.text)
                    counter = counter + 1
                    file.close
            elif thisLink.startswith('https'):
                if "&sa" in thisLink:
                    file = open("crispr" + str(counter) + ".txt", "a")
                    num = thisLink.find('&sa')
                    driver.get(thisLink[:num])
                    page = requests.get(thisLink[:num])
                    file.write(thisLink[:num]+ "\n")
                    file.write(page.text)
                    counter = counter + 1
                    file.close
                else:
                    file = open("crispr" + str(counter) + ".txt", "a")
                    driver.get(thisLink)
                    page = requests.get(thisLink)
                    file.write(thisLink+ "\n")
                    file.write(page.text)
                    counter = counter + 1
                    file.close
    return counter

def keywordSearch(num):
    counter = 1
    files = []
    while counter < num:
        currentFile = open("crispr" + str(counter) + ".txt", "r")
        for line in currentFile:
            if "CRISPR" in line:
                files.append(counter)
                break
        counter = counter + 1
    for number in files:
        thisFile = open("crispr" + str(number) + ".txt", "r")
        print(thisFile.readline())
    
keywordSearch(googleSearch(companies))
 
