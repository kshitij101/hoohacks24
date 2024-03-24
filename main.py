import discord

from discord.ext import commands

TOKEN = 'MTIyMTE4MjU4MTk4MzE1NDIwNg.G7oiSx.C6-VDvL-Ok6maAKAJ4zR5fszhgCqZcnwUeHr38'
# API_ENDPOINT = 'http://example.com/post_messages'

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')

all_messages = []

@bot.event
async def on_guild_join(guild):

  print(f'Joined a new guild: {guild.name}')
  print(f'new guild: {guild}')

  for channel in guild.text_channels:
    print("Channel ---> ",channel)
    if channel.name == 'hoohackstest':
      async for message in channel.history(limit=None):  # Fetch all messages
        all_messages.append(message.content)
  print(f'Total Messages Collected: {len(all_messages)}')
  print("Messages:",all_messages)
#   runAdyant(all_messages)



@bot.event
async def on_message(message):
  bot_user = bot.user
  if message.author == bot_user:
    return
  if len(message.mentions) > 0 and message.mentions[0].name == bot_user:
    return generateAnswerAadyant(message.content)


import json
import pandas as pd
import numpy as np

from google.colab import userdata
import google.generativeai as genai

from annoy import AnnoyIndex

import pickle


#receive chat messages in the form of a list
def runAdyant(msgs):
  chat_messages = msgs

  with open("test", "wb") as fp:
    pickle.dump(chat_messages, fp)

  GOOGLE_API_KEY="AIzaSyAZ79qns-mduY7N8dnJ18lsoMSYiZF5TFU"
  genai.configure(api_key=GOOGLE_API_KEY)

  result = genai.embed_content(
      model="models/embedding-001",
      content=chat_messages,
      task_type="retrieval_document",
      title="Embedding of list of paper abstracts")

  embeds = np.array(result['embedding'])

  annoy_model = AnnoyIndex(embeds.shape[1], metric='angular')
  for i, embed in enumerate(embeds):
      annoy_model.add_item(i, embed)
  annoy_model.build(i)

  annoy_model.save('embeds.ann')

bot.run(TOKEN)




def generateAnswerAadyant(question):
    return 'x'