import json, os, logging, time, re, string, os
from datetime import datetime
import math

#file management and updating channel
def checkfiles(guild):
    if os.path.isdir(f'./guildfiles/{guild}.json') == True:
        return
    else:
        joinguild(guild)
        return

def joinguild(guild):
    if os.path.exists(f'./guildfiles/{guild}.json') == True:
        return
    else:
        with open(f'./guildfiles/{guild}.json', 'w') as f:
            f.write(f"{{\"id\": {guild}, \"highscore\": 0, \"channel\": 0, \"currentnum\": 0, \"currentletter\": 0, \"currentuser\": 0, \"date\": \"\"}}")

def updatechannelid(channelid, guild):
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        x.update({"channel": channelid})
        y = json.dumps(x)
    with open(f'./guildfiles/{guild}.json', 'w') as f:
        f.write(y)

def eval_letters(word):
    with open("cipher.json", "r") as f:
        cipher = json.loads(f.read())
    l = list(word.lower())
    i = 0
    num = 0
    ln = [cipher.get(x) for x in l]
    ln.reverse()
    while i < len(ln):
        num = num + ln[i]*(26**i)
        i=i+1
    return num

#load vars
def loadchannel(guild):
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        y = x["channel"]
        return y

def loadnumber(guild):
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        y = x["currentnum"]
        return y

def loadletter(guild):
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        y = x["currentletter"]
        return y

def loaduser(guild):
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        y = x["currentuser"]
        return y

def loaddate(guild):
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        y = x["date"]
    if y == "":
        return "None"
    else:
        pass
    _today = datetime.today()
    hsdate = datetime.strptime(y, '%b-%d-%Y')
    date = datetime.strftime(hsdate, '%b-%d-%Y')
    days = abs(_today-hsdate).days
    if days == 0:
        z = f"Today"
    else:
        z = f"{days} days ago on {date}"
    return z

def loadguild():
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        y = x["id"]
        return y


#update vars
def updatenumber(number, guild):
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        x.update({"currentnum": number})
        y = json.dumps(x)
    with open(f'./guildfiles/{guild}.json', 'w') as f:
        f.write(y)

def updateletter(letter, guild):
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        x.update({"currentletter": letter})
        y = json.dumps(x)
    with open(f'./guildfiles/{guild}.json', 'w') as f:
        f.write(y)

def updateuser(user, guild):
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        x.update({"currentuser": user})
        y = json.dumps(x)
    with open(f'./guildfiles/{guild}.json', 'w') as f:
        f.write(y)

def updatehighscore(score, guild):
    highscoredate(guild)
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        x.update({"highscore": score})
        y = json.dumps(x)
    with open(f'./guildfiles/{guild}.json', 'w') as f:
        f.write(y)

def highscoredate(guild):
    _today = datetime.today()
    _today= datetime.strftime(_today, '%b-%d-%Y')
    with open(f'./guildfiles/{guild}.json', 'r') as f:
        x = json.loads(f.read())
        x.update({"date": f"{_today}"})
        y = json.dumps(x)
    with open(f'./guildfiles/{guild}.json', 'w') as f:
        f.write(y)