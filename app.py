
import requests
from bs4 import BeautifulSoup as bs
import streamlit as st
from urllib.request import urlopen as uReq
import pandas as pd

name=st.text_input("Name")
try:
    flipkart_url = "https://www.flipkart.com/search?q=" +name

    uClient = uReq(flipkart_url)

    flipkartPage = uClient.read()

    uClient.close()

    flipkart_html = bs(flipkartPage, "html.parser")

    bigboxes = flipkart_html.findAll("div", {"class": "_1AtVbE col-12-12"})

    del bigboxes[0:3]

    box = bigboxes[0]

    len(bigboxes)

    productLink = "https://www.flipkart.com" + box.div.div.div.a['href']

    prodRes = requests.get(productLink)
    prodRes.encoding='utf-8'

    prod_html = bs(prodRes.text, "html.parser")
    #print(prod_html)

    commentboxes = prod_html.find_all('div', {'class': "_16PBlm"})

    name=[]
    rating=[]
    custComment=[]
    commentHead=[]

    for i in range(len(commentboxes)-1):
        name1=commentboxes[i].div.find_all('p', {'class': '_2sc7ZR _2V5EHH'})[0].text
        name.append(name1)
        rating1 = commentboxes[i].div.div.div.div.text
        rating.append(rating1)
        commentHead1 = commentboxes[i].div.div.div.p.text
        commentHead.append(commentHead1)
        comtag = commentboxes[i].div.div.find_all('div', {'class': ''})
        custComment1 = comtag[0].div.text
        custComment.append(custComment1)

    mat=[]
    for i in range(len(name)):
        xx=[name[i],rating[i],commentHead[i],custComment[i]]
        mat.append(xx)


    matrix=pd.DataFrame(mat)
except:
    matrix="enter a valid product"

if st.button('Find Review'):
    st.write(matrix)
