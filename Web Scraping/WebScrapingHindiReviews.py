import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from googletrans import Translator

reviews=[]
rating=[]
star=[]
title=[]
names=[]
cus_r=[]

#The URL of the website, Page number should start from 1 or 2
url='https://www.amazon.in/Mi-Earphone-Basic-Ultra-deep/product-reviews/B07QJYB8BC/ref=cm_cr_getr_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1'

#cookies
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/96.0.4664.110 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

translator = Translator()

#Iterates through all the pages for the reviews (Generally upto 500) 
for i in range(499):

    #Gives Updates for how many pages done
    if(i%50 == 0):
        print(i, "pages are done")
        print('No of Reviews: ', len(cus_r))
        print(url)
    
    #Gets raw data from url
    def get_data(url):
        r=requests.get(url,headers=HEADERS)
        return r.text

    #Converts raw data to html format and parses
    def html_code(url):
        data=get_data(url)
        soup1=BeautifulSoup(data,'html.parser')
        return soup1

    soup=html_code(url) #html data

    #Getting customer names from the raw HTML and extracting the text from it and adding it to an array
    def get_names(soup):
        n=""
        prev = " "
        count = 0
        
        for item in soup.find_all("div",class_="a-row a-spacing-mini"):
            if(count > 3):
                if((('\n' + prev + '\n') != n+item.get_text()) and (n+item.get_text() != 'All critical reviews› ') and (n+item.get_text() != 'AMAZON VERIFIED PROFILE')\
                   and ('\n' not in (n+item.get_text())) and (n+item.get_text() !=  'THE') and ('VINE VOICE' not in n+item.get_text()) and (n+item.get_text() !=  'AMAZON OFFICIAL')):
                    n=n+item.get_text()
                    names.append(n)
                prev = n
                n=""
            count = count + 1
        return names
    cus_n=get_names(soup)

    #Getting ratings from the raw HTML and extracting the text from it and adding it to an array
    def get_rating(soup):
        r=""
        count = 0
        s=""
        for item3 in soup.find_all("i",{"data-hook" : "review-star-rating"}):
            s=s+item3.get_text()
            star.append(s)
            if(int(s[:1]) < 2.5):
                s = 0
            else:
                s = 1
            rating.append(s)
            s=""
            count = count + 1
        return rating

    cus_sentiment = get_rating(soup)
    
    #Getting the class of the reviews from the raw HTML and extracting the text from it and adding it to an array
    def get_reviews(soup):
        r=""

        t=""
        for item2 in soup.find_all("a",class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"):
            t=t+item2.get_text()
            title.append(t)
            t=""

        c=0
        for item in soup.find_all("div",class_="a-row a-spacing-small review-data"):
            r=r+title[c]+"\n"
            r=r+item.get_text()
            reviews.append(r)
            r=""
            c=c+1
        title.clear()
        return reviews

    cus_r=get_reviews(soup)
    #print(len(cus_r))

    test_str=url
    #reg=re.compile(r'[0-9]')
    #match=reg.findall(tstr)
    #num=''.join(match[-1: ])
    #pre_str=tstr.replace(num,'')
    #add_val=int(num)+1
    res = re.sub(r'[0-9]+$',
             lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}", 
             test_str)
    url=str(res)
    #print(url)

#Length of cus_n and cus_r should be the same, else there is an issue
#We can fix this by changing the classnames
#Else we can simply ignore the names as it is not required and use the reviews
print('No of Reviews: ', len(cus_r))
print('No of Names: ', len(cus_n))
print('No of Stars: ', len(star))
print('No of Sentiments: ', len(cus_sentiment))

#Extracting only those reviews that are hindi/hinglish
i=0
cus_no = []
cus_re = []
cus_na = []
cus_se = []
cus_st = []
for data in cus_r:
    if(i%500 == 0):
        print(i, "reviews are done")
    result = translator.translate(data, dest="en")
    if(result.src == "hi"):
        cus_no.append(i)
        cus_re.append(data)
        cus_na.append(cus_n[i])
        cus_st.append(star[i])
        cus_se.append(cus_sentiment[i])
    i = i + 1    

#Converying the names and reviews into a CSV file
data = {'Number': cus_no, 'Name': cus_na, 'Review': cus_re, 'Stars': cus_st, 'Sug/Com': cus_se}
df = pd.DataFrame(data)
df.to_csv('Hindi_Dataset.csv')
