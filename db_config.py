# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 13:55:11 2018

@author: Ujjval
@mod: Ashwin
"""

import pymysql
import pandas as pd

# cas databases
def getConnect_cas():
    # cnxn = pymysql.connect("cas-rds-production-environment.cefltkhcgkr1.ap-southeast-1.rds.amazonaws.com:3306", "ashwin.manghat","AM-E!5D52018", "assessment")
    cnxn = pymysql.connect("13.250.228.237", "ashwin.manghat","AM-E!5D52018", "assessment")
    print('<<CONNECTED>>')
    return cnxn

#educat database => DA
def getConnect_educat():
    cnxn = pymysql.connect("122.248.246.221", "ashwin.manghat1","71ZDGL", "educatio_educat")
    print('<<CONNECTED>>')
    return cnxn

#adepts database => mindspark and other stuff
def getConnect_adepts():
    cnxn = pymysql.connect("122.248.246.221", "ashwin.manghat1","71ZDGL", "educatio_adepts")
    print('<<CONNECTED>>')
    return cnxn

#function automatically does the job of identifying which table to pull. Pass in 'educat' as first param if you want educat otw it will connect to adepts
def connect(db, q):
    cxn = getConnect_educat() if db == 'educat' else getConnect_adepts() #da_questions\\n\",\n",
    temp = pd.read_sql(q, con = cxn)
    cxn.close()
    return temp
