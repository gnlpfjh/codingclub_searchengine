# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 07:31:36 2015

@author: frosch
"""

import urllib2
import numpy as np
#from BeautifulSoup import BeautifulSoup

def getLinkFromIndex(htmlString):
    
    start_link = htmlString.find('<a href=')
    start_quote = htmlString.find('"', start_link)
    end_quote = htmlString.find('"', start_quote+1)
    
    # check if an occurence has been found
    if start_link == -1 or start_quote == -1 or end_quote == -1 :
        return "", -1
        
    url = htmlString[start_quote+1:end_quote]
    
    # check if url is empty
    if not url:
        return url, -1
        
    return url, end_quote
    

def crawlPage(link):
    
    try:
        page = urllib2.urlopen(link).read()
    except urllib2.HTTPError, e:
        print 'A problem occured while loading the page [' + link + ']. Please try again. ' + e
        return
        
    try:
        page
    except:
        page = "empty"
        return
    print page
    
    
    while page:
        new_url, end_quote = getLinkFromIndex(page)
        
        if new_url:
            print new_url
            page = page[end_quote:]
        else:
            page = None
    
    
    return 0


def getLinkToPage():
    
    return "http://schneefisch.ddns.net/"


def main():
    
#    start by asking for a link
    pageLink = getLinkToPage()
    print "got page " + pageLink
 
 #   search this page for links
    links = crawlPage(pageLink)
    
    return 0

if __name__ == '__main__':
	main()
