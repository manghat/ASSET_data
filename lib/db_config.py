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

def getConnect_educat_back():
    cnxn = pymysql.connect("122.248.246.221", "shiny.mathew","EIShiny1234", "educatio_educat")
    print('<<CONNECTED>>')
    return cnxn

#adepts database => mindspark and other stuff
def getConnect_adepts():
    cnxn = pymysql.connect("122.248.246.221", "ashwin.manghat1","71ZDGL", "educatio_adepts")
    print('<<CONNECTED>>')
    return cnxn

#function automatically does the job of identifying which table to pull. Pass in 'educat' as first param if you want educat otw it will connect to adepts
def connect(db, q):
    cxn = getConnect_educat_back() if db == 'educat' else getConnect_adepts() #da_questions\\n\",\n",
    temp = pd.read_sql(q, con = cxn)
    cxn.close()
    return temp


def find_rounds(df_in):
    rounds = list(set(x[2] for x in list(set(df_in.papercode.astype(str))))) # all the rounds
    rounds.sort() # sorting
    while not(rounds[0].isalnum()): # moving '#' to the end (if there is)
        rounds.append(rounds.pop(0)) 
    return rounds

# list of classes in the correct order ----
def find_classes(df_in):
    classes = list(set(x[1] for x in list(set(df_in.papercode.astype(str))))) # all the rounds
    classes.sort() # sorting
    return classes

# list of subjects in the correct order
def find_subjects(df_in):
    subjects = list(set(x[0] for x in list(set(df_in.papercode.astype(str))))) # all the rounds
    subjects.sort() # sorting
    return subjects
