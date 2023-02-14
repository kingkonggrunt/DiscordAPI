import reddit
import random
import database
# import main

# test function
def grab_copypasta(Reddit):
  i = random.randint(0, len(Reddit.children()))
  pasta = Reddit.children()[i]['data']['selftext']
  if len(pasta) >= 2000:
    grab_copypasta(Reddit)
  else:
    return pasta

def grab_link_url(Reddit, image_only=False):
  i = random.randint(0, len(Reddit.children()))
  url = Reddit.children()[i]['data']['url_overridden_by_dest']

  if image_only:
    while url.startswith("https://v.redd.it"):
      i = random.randint(0, len(Reddit.children()))
      url = Reddit.children()[i]['data']['url_overridden_by_dest']
  
  return url

def main():
  r = reddit.Reddit("copypasta", "top", 50, timeframe="week")

  print(grab_copypasta(r))

  r = reddit.Reddit("ShitPostCrusaders", "top", 50, timeframe='week')
  
  print(grab_link_url(r, image_only=True))
  
  # print(r.children()[0])
  # print(type(r.children()))
  # print(type(r.children()[0]))
  
  # r = reddit.Reddit("copypasta", "top")
  # i = random.randint(0, len(r.children()))
  # rand_pasta = r.children()[i]['data']['selftext']
  # print(rand_pasta)
  # database.update_list("bruh_responses", 'sup bruh')
  # database.update_list("bruh_responses", 'yeah bruh')
  # database.update_list("bruh_responses", 'bruuh')
  # database.update_list("bruh_responses", 'hey bruh')

  # bruh = database.database("bruh_responses", )
  # print(bruh)


if __name__ == "__main__":
  main()