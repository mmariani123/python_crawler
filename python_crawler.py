#!/usr/bin/env Python3

# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:42:02 2021

@author: Mike_2
"""

#check out https://www.blog.datahut.co/post/how-to-build-a-web-crawler-from-scratch
#for more info, they used the scrapy module so I will use it here as well. 

import scrapy
       
inputPrompt = "Welcome to python crawler v1.0\n" \
    "This program is usefule for web scraping and SQL databasing\n" \
    "enter 'exit' to exit or 'help' for help\n" \
    "enter 'stats test' to review the stats test\n" \
    "enter 'crawler' to use the web crawler\n" \
    "enter your command below \n" \
    + "> "
helpStatement="---HELP---\n press 'enter' to continue\n"
inputIn=""
crawlerMode=False

while(inputIn!="exit"):
    if inputIn=="help":
        print(helpStatement)
        input()
        inputIn=""
        continue
    elif inputIn=="stats test":
        print("Welcome to the stats review test\n" \
              "press enter to move through the questions\n" \
              "type 'exit' and enter at any point to exit the review\n")
        #Question 1
        statsInput=input("What is the definition of p-value?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 2
        statsInput=input("What is the definition of statistical power?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 3
        statsInput=input("What is faster, using a hashed array or iterating "\
                          "over a sorted array?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 4
        statsInput=input("What is a segmentation fault (seg fault)?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 5
        statsInput=input("Is there a faster way to find the median " \
                          "then simple sorting?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 6
        statsInput=input("How would you detetmine if a distribution is " \
                          "normal (e.g. is there a particular bespoke test?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 7
        statsInput=input("How would you compare two distributions to" \
                          "establish if they are identical?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 8
        statsInput=input("How would you determine goodness of fit for " \
                          "a distribution?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 9
        statsInput=input("Why/when do we use multiple test correction?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
        #Question 10
        statsInput=input("What is principle component analysis and "\
                          "when would one use binomial clustering?\n")
        if statsInput=='exit':
            inputIn=""
            continue
        print("The Defintion of p-value is ... \n")
    elif inputIn=="crawler":
        crawlerMode=True
        while(crawlerMode):
            crawlerInput = input("You are now in crawler mode\n " \
                                 "type 'exit' at anytime to return "\
                                 "to the the main menu\n" \
                                 "crawler> ")
            if(crawlerInput=="exit"):
                crawlerMode=False
                inputIn=""
                continue
            else:
                print("Execute crawler command\n")
                class spider1(scrapy.Spider):
                    name = ‘Wikipedia’
                    start_urls = [‘https://en.wikipedia.org/wiki/Battery_(electricity)’]       
                    def parse(self, response):
                        pass
    else:
        inputIn = input(inputPrompt)
        print(inputIn)
else:
    print("thank you for using python crawler v1.0, thank you!\n")
