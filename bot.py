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
import numpy as np
from datetime import datetime
from time import mktime
import time
import csv
from itertools import groupby
from pymongo import MongoClient
from datetime import date
import calendar
from datetime import timedelta

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

@client.command(name='invite', help='Get an invite link for the bot')
async def invite(ctx):
    await ctx.send('https://discord.com/api/oauth2/authorize?client_id=905146683720097913&permissions=380305984577&scope=bot')



cluster=MongoClient("mydb")

accs=cluster["discord"]["accounts"]

@client.command(name='create', pass_context= True, help='create/update account')
async def create(ctx,classs: int,section: str):
    checker=accs.find_one({"id" : ctx.message.author.id})
    if checker is None:
        newuser={"id":ctx.message.author.id,"class":classs,"section":section}
        accs.insert_one(newuser)
        await ctx.message.add_reaction('👍')
    else:
        accs.update_one({"id":ctx.message.author.id},{"$set":{"class":classs}})
        accs.update_one({"id":ctx.message.author.id},{"$set":{"section":section}})
        await ctx.message.add_reaction('👍')



df2=pd.read_csv('data.csv')


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



l=['Monday','Tuesday','Wednesday','Thursday','Friday','Mon','Tue','Wed','Thurs','Fri']
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



l=['Monday','Tuesday','Wednesday','Thursday','Friday','Mon','Tue','Wed','Thurs','Fri']
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



l=['Monday','Tuesday','Wednesday','Thursday','Friday','Mon','Tue','Wed','Thurs','Fri']
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
timedict={6:lmao2,7:lmao2,8:lmao,9:lmao,10:o,11:o,12:o}
datadict={6:data4,7:data4,8:data3,9:data3,10:data2,11:data2,12:data2}

def get_lcs(s, t, n, m):
    dp_cur = dp_prev = [0 for i in range(m+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp_cur[j] = dp_prev[j-1] + 1
            else:
                dp_cur[j] = max(dp_cur[j-1], dp_prev[j])
        dp_prev = dp_cur.copy()
    return dp_cur[m]

def day_of_week(s):
    s = s.lower()
    best = ''; mx = 0
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    for d in days:
        l = get_lcs(s, d, len(s), len(d))
        if l >= mx:
            mx = l
            best = d
    if mx == 0:
        # return default (today)
        pass
    return best

@client.command(name='get',pass_context=True,help='fetch your timetable `type tt format for the format`')
async def get(ctx,day=None):
    try:
        tnmy=14
        tk=datetime.now().strftime("%H")
        if day == None:
            if int(tk)>tnmy:
                issoke=datetime.now()
                issoke += timedelta(days=1)
                day=str(issoke.strftime("%A"))
            else:
                day=calendar.day_name[date.today().weekday()]
        if day=='Saturday' or day=='Sunday':
            day='Monday'
        global accs
        checker=accs.find_one({"id" : ctx.message.author.id})
        Class=checker['class']
        section=checker['section']
        day=day.lower()
        day = day_of_week(day)
        day=day.lower()
        days={'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4}
        rets={6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',11:'XI',12:'XII'}
        teemp=Class
        Class=rets[Class]
        classes={'VI':1,'VII':0,'VIII':1,'IX':0,'X': 2, 'XI':1,'XII':0}
        j=[]
        section=section.upper()
        zez=timedict[teemp]
        string=Class+'-'+section
        for i in datadict[teemp]:
            if string in i:
                j.append(i)
        k=j[days[day]]
        lop=zez[days[day]]

        fin=[list(g) for k, g in groupby(k, lambda x: x != '') if k]
        fin2=[list(g) for lop, g in groupby(lop, lambda x: x != '') if lop]


        file21 = pd.read_csv('num.csv')
        out21=file21['num'][0]
        embed = discord.Embed(title=f"__**Your Timetable (#{out21}):**__", color=0x03f8fc)
        fin=fin[classes[Class]]
        fin2=fin2[classes[Class]]
        embed.add_field(name=f'**Day**', value=f'> {day.title()}\n',inline=False)
        del fin[0]
        del fin2[0]
        ranger=min((len(fin2)),(len(fin)))
        for i in range(ranger):
            embed.add_field(name=f'**{fin2[i]}**', value=f'> {fin[i]}\n',inline=False)
        await ctx.reply(embed=embed)
    except Exception as e: 
        print(e)
        await ctx.reply('Create an account or check `tt format` if you have already made an account :smile:')

@client.command(name='format',pass_context=True,help='returns the format for the get command')
async def formatt(ctx):
    embed2 = discord.Embed(title=f"__**Format:**__", color=0x03f8fc)
    embed2.add_field(name=f'**Creating an Account**', value=f'> tt create [space] [Class] [space] [Section]\n',inline=False)
    embed2.add_field(name=f'**Getting your Timetable**', value=f'> tt [space] get [space] [Day of the week (Optional - By default current day)]\n',inline=False)
    await ctx.send(embed=embed2)


@tasks.loop(seconds=3660)
async def check():
    try:
        df2=pd.read_csv('data.csv')
        mystr=str(df2['time'][0])
        mystr=mystr.partition('.')[0]
        my_time = time.strptime(mystr, '%Y-%m-%d %H:%M:%S')
        dt = datetime.fromtimestamp(mktime(my_time))
        dif=datetime.now()-dt
        minutes = dif.total_seconds() / 60
        if minutes>60:
            file2 = pd.read_csv('num.csv')
            out2=file2['num'][0]
            now = datetime.now()
            df2['time'][0]=now
            df2.to_csv('data.csv',index=False)
            URL = "https://dpsrkp.net/session-2021-2022-schedule-{}/".format((str(int(out2)+1)).strip())
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
            file2['num'][0]=out2+1
            file2.to_csv('num.csv',index=False)
            os.execv(sys.executable, ['python'] + sys.argv)
    except: # work on python 3.x
        pass


client.run('shh') 