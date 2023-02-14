from replit import db
# db is a key-value pair data structure

def database(database, return_empty=False):
  if database in db.keys():
    return db[database]
  elif return_empty:
    return []
  else:
    return None

def add_database(database, value):
  if not database in db.keys():
    db[database] = value

def update(database, value):
  db[database] = value

def delete(database):
  del db[database]

def update_list(database, value, add_new=False):
  if database in db.keys():
    l = db[database]
    l.append(value)
    db[database] = l
  else:
    if add_new: 
      db[database] = [value]
    else:
      raise KeyError("Cannot add to not existing database")
    

  def delete_list(database, index):
    l = db[database]
    if len(l) > index:
      del l[index]
    db[database] = l
