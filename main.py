import discord
import os
import requests
import json
import random
from replit import db
from keepalive import keep_alive

client = discord.Client()

randomHappyResponses = ["glad today was good!", "keep it up", "slayyyy"]
toDoList = []
helplines = ["Samaritans of Singapore: 1-767", "IMH: 6389 2222"]

def update_homework(work):
  if "homework" in db.keys():
    homework = db["homework"]
    homework.append(work)
    db["homework"] = homework
  else:
    db["homework"] = [work]

def delete_homework(index):
  homework = db["homework"]
  if len(homework) > index:
    del homework[index]
    db["homework"] = homework

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    werk = toDoList
    if "homework" in db.keys():
      werk = werk + list(db["homework"])

    if message.content.startswith('$hello'):
        await message.channel.send('hello :)))')

    if message.content.startswith('$encourage'):
      await message.channel.send(random.choice(randomHappyResponses))

    if message.content.startswith("$helpme"):
        await message.channel.send(random.choice(helplines))

    if msg.startswith("$list"):
      await message.channel.send(werk)
    
    if msg.startswith("$new"):
      work = msg.split("$new ",1)[1]
      update_homework(work)
      await message.channel.send("New work added.")

    if msg.startswith("$del"):
       homework = []
       if "homework" in db.keys():
         index = int(msg.split("$del",1)[1])
         delete_homework(index)
         homework = db["homework"]
       await message.channel.send(random.choice(randomHappyResponses))
    
keep_alive()
client.run('ODgzNTE4OTA1MDU2OTExNDAw.YTLHGQ.yzgZX4vlHg4nkzdnXuCmAj8OBFs')
