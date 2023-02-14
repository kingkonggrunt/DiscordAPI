import requests
import json
import os

class JsonHandler:
  def __init__(self):
    self.json = None

  def load_json(self, filename):
    if os.path.exists(filename):
      with open(filename, 'r') as f:
        self.json = json.load(f)
    else:
      print("File not found")

  def save_json(self, filename, json_content):
    with open(filename, 'w') as f:
      json.dump(json_content, f)


class Reddit(JsonHandler):

  header = {'User-agent': 'MedicBruh Bot#5159/1.3.1'}
  
  def __init__(self, subreddit, listing="new", limit=25, timeframe="week"):
    self.json = None
    self._subreddit = subreddit
    self._listing = listing
    self._limit = limit
    self._timeframe = timeframe

  def request_reddit(self, no_cache=False):
    response = requests.get(f"http://www.reddit.com/r/{self._subreddit}/{self._listing}.json?limit={self._limit}&t={self._timeframe}", headers=self.header)

    status_code = response.status_code
    print(status_code)
    print(response.reason)

    if status_code == 200:
      self.json = response.json()
      self.save_json(f"data/{self._subreddit}_{self._listing}.json", self.json)
    else:
      if not no_cache:
        self.load_json(f"data/{self._subreddit}_{self._listing}.json")
        return
      print("No cache used on request fail")

  def json_data(self):
    return self.json

  def children(self):
    # returns list of dictionaries
    return self.json['data']['children']