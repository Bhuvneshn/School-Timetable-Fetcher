import asyncio
import functools
import itertools
import math
import random
import discord
from discord.ext import commands,tasks
from async_timeout import timeout
from random import choices
from random import choice
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
import sys
import os
import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import urllib.request
from urllib.request import urlopen
from html_table_parser.parser import HTMLTableParser
from pprint import pprint
import numpy as np
from datetime import datetime
from time import mktime
import time
import csv
from itertools import groupby

intents = discord.Intents().all()
client = commands.Bot(command_prefix='tt ',intents=intents)

@client.event
async def on_ready():
    check.start()
    await client.change_presence(activity=discord.Game(name="tt help"))
    print('Bot is online!')

@client.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by Bhuv')


file1 = open("num.txt","r+")
out=file1.read()
URL = "https://dpsrkp.net/session-2021-2022-schedule-{}/".format(out)
r = requests.get(URL) 

df2=pd.read_csv('C:\Python Projs\school notice tracker\data.csv')


url=df2['1'][0]
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")
index = 0
for table in tables:
    with open(str(index) + ".csv", "w",encoding='utf8') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC,lineterminator='\n')
        wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
    


with open('0.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)



l=['Monday','Tuesday','Wednesday','Thursday','Friday']
data2=[]
for i in data:
    t=list(filter(lambda x: x not in l,i))
    if 'ClSec' in t:
        del t[0]
    if 'X-' in ''.join(t):
        t.insert(16,'') 
    data2.append(t)

o=[]
for i in data2:
    if 'ClSec' in i:
            o.append(i)



##################################################

url=df2['2'][0]
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")
index = 1
for table in tables:
    with open(str(index) + ".csv", "w",encoding='utf8') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC,lineterminator='\n')
        wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
    


with open('1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)



l=['Monday','Tuesday','Wednesday','Thursday','Friday']
data3=[]
for i in data:
    t=list(filter(lambda x: x not in l,i))
    if 'ClSec' in t:
        del t[0]
    if 'X-' in ''.join(t):
        t.insert(16,'') 
    data3.append(t)

lmao=[]
for i in data3:
    if 'ClSec' in i:
            lmao.append(i)

###################################################

url=df2['3'][0]
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")
index = 2
for table in tables:
    with open(str(index) + ".csv", "w",encoding='utf8') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC,lineterminator='\n')
        wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
    


with open('2.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)



l=['Monday','Tuesday','Wednesday','Thursday','Friday']
data4=[]
for i in data:
    t=list(filter(lambda x: x not in l,i))
    if 'ClSec' in t:
        del t[0]
    if 'X-' in ''.join(t):
        t.insert(16,'') 
    data4.append(t)

lmao2=[]
for i in data4:
    if 'ClSec' in i:
            lmao2.append(i)

datadict={6:data4,7:data4,8:data3,9:data3,10:data2,11:data2,12:data2}
@client.command(name='get',pass_context=True,help='fetch your timetable `type tt format for the format`')
async def get(ctx,Class: int,section: str,day: str):
    day=day.lower()
    days={'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4}
    rets={6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',11:'XI',12:'XII'}
    teemp=Class
    Class=rets[Class]
    classes={'VI':1,'VII':0,'VIII':1,'IX':0,'X': 2, 'XI':1,'XII':0}
    j=[]
    global o
    string=Class+'-'+section
    for i in datadict[teemp]:
        if string in i:
            j.append(i)
    k=j[days[day]]
    lop=o[days[day]]

    fin=[list(g) for k, g in groupby(k, lambda x: x != '') if k]
    fin2=[list(g) for lop, g in groupby(lop, lambda x: x != '') if lop]


    embed = discord.Embed(title=f"__**Your Timetable:**__", color=0x03f8fc,timestamp= ctx.message.created_at)
    fin=fin[classes[Class]]
    fin2=fin2[classes[Class]]
    
    del fin[0]
    del fin2[0]
    ranger=min((len(fin2)),(len(fin)))
    for i in range(ranger):
        embed.add_field(name=f'**{fin2[i]}**', value=f'> {fin[i]}\n',inline=False)
    await ctx.reply(embed=embed)

@client.command(name='format',pass_context=True,help='returns the format for the get command')
async def formatt(ctx):
    await ctx.channel.send('tt get {your class(int)} {your section(capital)} {Day of the week}')


@tasks.loop(seconds=20)
async def check():
    try:
        df2=pd.read_csv('C:\Python Projs\school notice tracker\data.csv')
        mystr=str(df2['time'][0])
        mystr=mystr.partition('.')[0]
        my_time = time.strptime(mystr, '%Y-%m-%d %H:%M:%S')
        dt = datetime.fromtimestamp(mktime(my_time))
        dif=datetime.now()-dt
        minutes = dif.total_seconds() / 60
        if minutes>300:
            file1 = open("num.txt","r+")
            out=file1.read()
            now = datetime.now()
            df2['time'][0]=now
            df2.to_csv('data.csv',index=False)
            URL = "https://dpsrkp.net/session-2021-2022-schedule-{}/".format(str(int(out)+1))
            r = requests.get(URL) 
            soup = BeautifulSoup(r.content, 'html5lib')
            table = soup.findAll('iframe')
            class_10_12=((table[0]['src']).split('gid'))[0]
            class_8_9=((table[1]['src']).split('gid'))[0]
            class_6_7=((table[2]['src']).split('gid'))[0]
            now = datetime.now()
            data = [{'time':now,'1': class_10_12, '2': class_8_9, '3':class_6_7}]
            df = pd.DataFrame(data)
            df.to_csv('data.csv',index=False)
            f.truncate(0)
            f.write(str(int(out)+1))
            f.close()
            os.execv(sys.executable, ['python'] + sys.argv)
    except:
        pass


client.run('shh')