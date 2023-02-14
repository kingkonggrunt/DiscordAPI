import discord
import os
from reddit import Reddit
import random
import database
import web_server


TOKEN = os.environ['TOKEN']

# database.add_database("bruh_responses", [])
# bruh_responses = [
#   'sup bruh',
#   'yeah bruh',
#   'bruuh',
#   'hey bruh',
# ]
# bruh_responses += database.database("bruh_responses", return_empty=True)

client = discord.Client()



def grab_copypasta(Reddit):
  # i = random.randint(0, len(Reddit.children()))
  # pasta = Reddit.children()[i]['data']['selftext']
  # if len(pasta) >= 2000:
  #   grab_copypasta(Reddit)
  # else:
  #   return pasta
  pasta = ""
  length = 2001

  while length >= 2000:
    i = random.randint(0, len(Reddit.children()))
    pasta = f"""
    \n
    {Reddit.children()[i]['data']['selftext']}
    """
    length = len(pasta)

  return pasta

def grab_link_url(Reddit, image_only=False):
  i = random.randint(0, len(Reddit.children()))
  url = Reddit.children()[i]['data']['url_overridden_by_dest']

  if image_only:
    while url.startswith("https://v.redd.it"):
      i = random.randint(0, len(Reddit.children()))
      url = Reddit.children()[i]['data']['url_overridden_by_dest']
  
  return url

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    content = message.content

    if content.startswith('b!hello'):
        await message.channel.send('Hello!')
    
    if content.startswith('BRUH'):
      await message.channel.send('B')
      await message.channel.send('R')
      await message.channel.send('U')
      await message.channel.send('H')

    if content.startswith("b!PASTA"):
      reddit = Reddit("copypasta", "top", limit=50, timeframe="week")
      reddit.request_reddit()
      rand_pasta = grab_copypasta(reddit)
      await message.channel.send(f"{rand_pasta}")

    if ('bruh' in content) and not (content.startswith("b!add_db")):
      await message.channel.send(random.choice(database.database("bruh_responses", return_empty=False)))

    if content.startswith("b!add_db"):
      command = content.split(" ", 1)[1]
      db = command.split(" ", 1)[0]
      content = command.split(" ", 1)[1]
      database.update_list(db, content)
      await message.channel.send(f"Added Content to Database: {db}")

    if content.startswith("b!SPC"):
      reddit = Reddit("ShitPostCrusaders", "top", 50, "week")
      reddit.request_reddit()
      await message.channel.send(grab_link_url(reddit, image_only=True))

    if content.startswith("b!MC"):
      reddit = Reddit("Minecraft", "top", 50, "week")
      reddit.request_reddit()
      await message.channel.send(grab_link_url(reddit, image_only=False))

    if content.startswith("b!Reddit"):
      subreddit = content.split(" ", 1)[1]
      reddit = Reddit(subreddit, "top", 50, "week")
      reddit.request_reddit()
      await message.channel.send(grab_link_url(reddit, image_only=True))

    if content.startswith("b!AM"):
      reddit = Reddit(None, None, limit=50, timeframe=None) # null class
      reddit.load_json("data/amongus.json")
      

      if content.endswith("C"):
        pasta = reddit.children()[0]['data']['selftext']
      elif content.endswith("F"):
        pasta = reddit.children()[1]['data']['selftext']
      else:
        pasta = reddit.children()[2]['data']['selftext']
      await message.channel.send(f"{pasta}")
      


# @client.event
# async def random_pasta(message):
#   if message.author == client.user:
#     return
#   if content.startswith("PASTA"):
#     reddit = Reddit("copypasta", "top")
#     i = random.randint(0, len(reddit.children()))
#     rand_pasta = reddit.children()[i]['data']['selftext']
#     await message.channel.send(f"{rand_pasta}")

web_server.keep_alive()
client.run(TOKEN)